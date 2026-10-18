# -*- coding: utf-8 -*-
"""
tutor_engine.py — Le « Prof Atlas » : moteur du tuteur IA.

Deux moteurs interchangeables :
  • LLMTutor   : API OpenAI-compatible (clé dans config.json) — réponses
                 illimitées, style professeur marocain, multi-méthodes.
  • LocalTutor : mode DÉMO hors-ligne — vrais solveurs pas-à-pas (équations,
                 trigonométrie, dérivées, limites, calculs) + explications
                 multi-méthodes de la base + MÉMOIRE de conversation
                 (« plus simple », « un exemple », « un exercice »).

API publique : answer = tutor.respond(question, db, user_id)
"""
import difflib
import json
import os
import re

CFG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")


# ============================================================ utilitaires ====
def load_config():
    cfg = {}
    if os.path.exists(CFG_PATH):
        try:
            cfg = json.load(open(CFG_PATH, encoding="utf-8"))
        except Exception:
            cfg = {}
    env_key = os.environ.get("GROQ_API_KEY")          # déploiement : clé en variable d'environnement
    if env_key:
        cfg["api_key"] = env_key
    return cfg


def _norm(s):
    """minuscules, sans accents, symboles normalisés."""
    s = s.lower()
    s = (s.replace("²", "^2").replace("³", "^3").replace("×", "*")
           .replace("·", "*").replace("−", "-").replace("–", "-"))
    s = re.sub("[àâä]", "a", s)
    s = re.sub("[éèêë]", "e", s)
    s = re.sub("[îï]", "i", s)
    s = re.sub("[ôö]", "o", s)
    s = re.sub("[ûüù]", "u", s)
    s = s.replace("ç", "c")
    return s


def _N(v):
    """Affiche 5.0 comme 5."""
    v = round(v, 6)
    return int(v) if v == int(v) else v


def fmt_num(v):
    return _N(v)


def _paren(v):
    """'x − 2' ou 'x + 2' selon le signe de v."""
    v = _N(v)
    return f"x − {v}" if v >= 0 else f"x + {_N(abs(v))}"


# ================================================== parseur de polynômes ====
def parse_poly(text):
    """'3x^2 - 2x + 5' -> {2:3.0, 1:-2.0, 0:5.0} (None si pas un polynôme)."""
    text = text.replace(" ", "")
    if not text:
        return None
    coeffs = {}
    terms = re.findall(r"[+-]?[^+-]+", text)
    seen = False
    for t in terms:
        if not t:
            continue
        m = re.fullmatch(r"([+-]?)(\d+(?:\.\d+)?)?\*?x(?:\^(-?\d+))?", t)
        if m:
            sign = -1 if m.group(1) == "-" else 1
            coef = float(m.group(2)) if m.group(2) else 1.0
            if m.group(3) is None:
                deg = 1
            else:
                try:
                    deg = int(m.group(3))
                except ValueError:
                    return None
            coeffs[deg] = coeffs.get(deg, 0.0) + sign * coef
            seen = True
            continue
        m = re.fullmatch(r"([+-]?)(\d+(?:\.\d+)?)", t)
        if m:
            sign = -1 if m.group(1) == "-" else 1
            coeffs[0] = coeffs.get(0, 0.0) + sign * float(m.group(2))
            seen = True
            continue
        return None
    return coeffs if seen else None


def poly_to_str(coeffs):
    """{deg: coef} -> 'x^2 - 5x + 6' (coefficient 1 masqué)."""
    def fmt(c, first):
        c = round(c, 6)
        if c == int(c):
            c = int(c)
        if first:
            return str(c)
        return f"{'+' if c >= 0 else '-'} {abs(c)}"

    def head_str(c, body, first):
        c = round(c, 6)
        if c == int(c):
            c = int(c)
        if first:
            if c == 1:
                return body
            if c == -1:
                return "-" + body
            return f"{c}{body}"
        sign = "+" if c >= 0 else "-"
        mag = abs(c)
        mag_s = "" if mag == 1 else mag
        return f"{sign} {mag_s}{body}"

    parts = []
    for deg in sorted(coeffs, reverse=True):
        c = coeffs[deg]
        if c == 0:
            continue
        if deg == 0:
            parts.append(fmt(c, not parts))
        else:
            parts.append(head_str(c, "x" if deg == 1 else f"x^{deg}", not parts))
    return " ".join(parts) if parts else "0"


def poly_eval(coeffs, x):
    return sum(c * x ** d for d, c in coeffs.items())


# ======================================================== solveurs pas-à-pas ==
def solve_quadratic(a, b, c):
    """Solution rédigée pas-à-pas de a x² + b x + c = 0 (a ≠ 0)."""
    a, b, c = _N(a), _N(b), _N(c)
    L = ["📐 Équation du second degré : " + poly_to_str({2: a, 1: b, 0: c}) + " = 0", ""]
    d = b * b - 4 * a * c
    L.append(f"Étape 1 — Discriminant : Δ = b² − 4ac = ({b})² − 4×({a})×({c}) = {_N(d)}")
    if d > 0:
        r = d ** 0.5
        x1 = (-b - r) / (2 * a)
        x2 = (-b + r) / (2 * a)
        L.append("Δ > 0 → l'équation admet DEUX solutions réelles :")
        L.append(f"Étape 2 — x = (−b ± √Δ) / 2a = ({_N(-b)} ± √{_N(d)}) / {_N(2 * a)}")
        L.append(f"   x₁ = {_N(x1)}")
        L.append(f"   x₂ = {_N(x2)}")
        L.append("Étape 3 — Forme factorisée : a(x − x₁)(x − x₂)")
        L.append(f"S = {{{_N(x1)} ; {_N(x2)}}}")
        L.append("")
        L.append(f"📊 Signe du trinôme : signe de a ({'positif' if a > 0 else 'négatif'}) à "
                 "l'extérieur des racines, signe opposé entre les racines.")
    elif d == 0:
        x0 = _N(-b / (2 * a))
        L.append(f"Δ = 0 → UNE solution double : x₀ = −b/2a = {x0}")
        L.append(f"S = {{{x0}}}")
    else:
        L.append("Δ < 0 → aucune solution RÉELLE (les solutions sont complexes, "
                 "à voir en 2ème Bac).")
        L.append("S = ∅")
    return "\n".join(L)


def solve_derivative(coeffs):
    """Dérivée d'un polynôme, rédigée terme à terme."""
    L = ["📐 Dérivée de : f(x) = " + poly_to_str(coeffs), ""]
    L.append("Règle utilisée : (a·xⁿ)' = a·n·xⁿ⁻¹ et la dérivée d'une constante est 0.")
    L.append("")
    out = {}
    for deg in sorted(coeffs, reverse=True):
        c = coeffs[deg]
        if c == 0:
            continue
        if deg == 0:
            L.append(f"• ({fmt_num(c)})' = 0  (constante)")
        else:
            out[deg - 1] = c * deg
            pw = "x" if deg - 1 == 1 else ("1" if deg - 1 == 0 else f"x^{deg - 1}")
            res = poly_to_str({deg - 1: round(c * deg, 6)})
            L.append(f"• ({poly_to_str({deg: c})})' = {fmt_num(c)}×{deg}·{pw} = {res}")
    L.append("")
    L.append("✅ Donc : f '(x) = " + (poly_to_str(out) if out else "0"))
    return "\n".join(L)


def solve_limit(num, den, a, is_infinity):
    """Quelques limites classiques de quotients de polynômes, rédigées."""
    L = ["📐 Limite calculée :", ""]
    if is_infinity:
        dn, dd = max(num), max(den)
        L.append("Quand x → ∞ : forme ∞/∞ (degrés {} et {}).".format(dn, dd))
        L.append(f"On garde les termes dominants : {fmt_num(num[dn])}x^{dn} / "
                 f"{fmt_num(den[dd])}x^{dd}")
        if dn > dd:
            L.append("Le degré du numérateur domine → la limite est infinie "
                     "(signe du terme dominant à préciser).")
        elif dn < dd:
            L.append("Le degré du dénominateur domine → la limite est 0.")
        else:
            val = num[dn] / den[dd]
            L.append("Même degré → limite = quotient des coefficients dominants = "
                     f"{fmt_num(val)}")
        return "\n".join(L)
    nv, dv = poly_eval(num, a), poly_eval(den, a)
    L.append(f"Étape 1 — On remplace x = {_N(a)} : numérateur = {fmt_num(nv)} ; "
             f"dénominateur = {fmt_num(dv)}")
    if dv != 0:
        L.append(f"Étape 2 — Pas d'indétermination → quotient = {fmt_num(round(nv / dv, 6))}")
        return "\n".join(L)
    if nv != 0:
        L.append("Étape 2 — Forme k/0 : la limite est infinie (à justifier par les "
                 "limites à gauche et à droite).")
        return "\n".join(L)
    L.append("Étape 2 — Forme 0/0 → il faut FACTORISER.")
    if max(num) == 2 and den.get(1):
        b_ = num.get(1, 0)
        other = -b_ - a
        if abs(poly_eval(num, other)) < 1e-9:
            lead_n = num[max(num)]
            slope = den[1]
            L.append(f"Étape 3 — Racine évidente x = {_N(a)} : le numérateur se factorise "
                     f"en ({_paren(a)})({_paren(other)}).")
            L.append(f"Étape 4 — Le dénominateur vaut {_N(slope)}({_paren(a)}) : on "
                     f"simplifie par ({_paren(a)}).")
            val = (a - other) * lead_n / slope
            L.append(f"Étape 5 — Il reste {_N(lead_n)}({_paren(other)}) / {_N(slope)} ; "
                     f"on remplace x = {_N(a)} → limite = {fmt_num(round(val, 6))}")
            return "\n".join(L)
    L.append("Indication : factorise (x − a) au numérateur (racine évidente) puis "
             "simplifie avec le dénominateur.")
    return "\n".join(L)


# ============================================== trigonométrie & calcul =======
_TRIG_VALS = {
    "0": (0.0, "0"),
    "1": (1.0, "1"),
    "1/2": (0.5, "1/2"),
    "sqrt2/2": (0.7071, "√2/2"),
    "sqrt3/2": (0.8660, "√3/2"),
    "-1/2": (-0.5, "−1/2"),
    "-sqrt2/2": (-0.7071, "−√2/2"),
    "-sqrt3/2": (-0.8660, "−√3/2"),
    "-1": (-1.0, "−1"),
}
_TRIG_SOL = {
    ("cos", "0"): "x = π/2 ou x = 3π/2",
    ("cos", "1"): "x = 0 (ou x = 2π)",
    ("cos", "-1"): "x = π",
    ("cos", "1/2"): "x = π/3 ou x = 5π/3",
    ("cos", "sqrt2/2"): "x = π/4 ou x = 7π/4",
    ("cos", "sqrt3/2"): "x = π/6 ou x = 11π/6",
    ("cos", "-1/2"): "x = 2π/3 ou x = 4π/3",
    ("cos", "-sqrt2/2"): "x = 3π/4 ou x = 5π/4",
    ("cos", "-sqrt3/2"): "x = 5π/6 ou x = 7π/6",
    ("sin", "0"): "x = 0 (ou x = π ou x = 2π)",
    ("sin", "1"): "x = π/2",
    ("sin", "-1"): "x = 3π/2",
    ("sin", "1/2"): "x = π/6 ou x = 5π/6",
    ("sin", "sqrt2/2"): "x = π/4 ou x = 3π/4",
    ("sin", "sqrt3/2"): "x = π/3 ou x = 2π/3",
    ("sin", "-1/2"): "x = 7π/6 ou x = 11π/6",
    ("sin", "-sqrt2/2"): "x = 5π/4 ou x = 7π/4",
    ("sin", "-sqrt3/2"): "x = 4π/3 ou x = 5π/3",
}


def solve_trig(q):
    """cos x = k / sin x = k avec k remarquable, sur [0 ; 2π]."""
    m = re.search(r"(cos|sin|sinus|cosinus)\s*\(?\s*x\s*\)?\s*=\s*([√0-9\.\s/\-]+)", q)
    if not m:
        return None
    fn_raw, val_raw = m.group(1), m.group(2).strip().replace(" ", "")
    fn = "sin" if fn_raw.startswith("sin") else "cos"
    key = val_raw.replace("√", "sqrt").replace(",", ".")
    if key not in _TRIG_VALS:
        return None
    pretty = _TRIG_VALS[key][1]
    sols = _TRIG_SOL.get((fn, key))
    if not sols:
        return None
    L = [f"📐 Équation trigonométrique : {fn} x = {pretty}", "",
         "Étape 1 — Sur le cercle trigonométrique, repère l'angle remarquable "
         f"dont {fn} vaut {pretty}."]
    base = {"1/2": ("π/3" if fn == "cos" else "π/6"),
            "sqrt2/2": "π/4",
            "sqrt3/2": ("π/6" if fn == "cos" else "π/3")}.get(key)
    if base:
        L.append(f"   C'est {fn}({base}).")
    L.append("Étape 2 — Le cercle donne DEUX positions avec la même valeur "
             f"de {fn} (symétrie : axe des x pour cos, axe des y pour sin).")
    L.append(f"Étape 3 — Solutions dans [0 ; 2π] : {sols}")
    L.append("")
    L.append("ℹ️ Sur ℝ en général : on ajoute + 2kπ à chaque solution "
             "(le cercle se répète tous les 2π).")
    L.append("")
    L.append("⚠️ Piège classique : oublier la deuxième solution ! "
             "Vérifie toujours avec le cercle.")
    return "\n".join(L)


def solve_arithmetic(q):
    """« Combien font 15 × 7 ? », « calcule (3+5)*2 »..."""
    m = re.search(r"(?:combien font|combien fait|calcule|calculer|combien)\s+"
                  r"([0-9\(\)\.,\+\-\*\/×÷^\s]+?)[\?\.!]?$", q)
    if not m:
        return None
    expr = (m.group(1).replace("×", "*").replace("÷", "/")
              .replace("^", "**").replace(",", ".").strip())
    if not re.fullmatch(r"[0-9\.\(\)\+\-\*\/\s]+", expr) or not re.search(r"\d", expr):
        return None
    try:
        val = eval(expr, {"__builtins__": {}}, {})
    except Exception:
        return None
    val = round(val, 6)
    val_i = int(val) if val == int(val) else val
    expr_pretty = expr.replace("**", "^").replace("*", " × ").replace("/", " ÷ ")
    return (f"💡 Calcul : {expr_pretty} = {val_i}\n\n"
            "Rappel des priorités : parenthèses → puissances → × et ÷ "
            "(de gauche à droite) → + et −.")


# ============================================================== LocalTutor ===
class LocalTutor:
    name = "demo"

    def __init__(self):
        self.mem = {}   # user_id -> contexte de conversation

    INTRO = ("👋 Salam ! Je suis **Prof Atlas**, ton professeur particulier "
             "(programme marocain — TC & 1ère Bac).\n\n"
             "Pose ta question à la voix 🎤 ou au clavier :\n"
             "• « résoudre x^2 - 5x + 6 = 0 »\n"
             "• « résoudre cos x = √3/2 »\n"
             "• « dérivée de 3x^3 - 2x + 5 »\n"
             "• « limite de (x^2-4)/(x-2) quand x tend vers 2 »\n"
             "• « explique-moi la mole » / « les suites » / « la génétique »...\n\n"
             "Après une explication, dis « plus simple », « un exemple » "
             "ou « un exercice » : je m'adapte à toi.")

    def respond(self, question, db, user_id=None):
        q = _norm(question)
        uid = user_id or 0
        mem = self.mem.setdefault(uid, {})

        # 0) politesse / salutations
        if any(w in q for w in ["merci", "shukran", "choukran"]):
            return ("Avec plaisir ! 😊 Continue comme ça — la régularité est la clé. "
                    "Une autre question ?")
        if len(q) < 4 or any(w in q for w in ["bonjour", "salut", "hello", "aide", "help"]):
            return self.INTRO

        # 0ter) l'élève INTERROMPT le prof : clarifier une étape / continuer
        if re.search(r"clarif|precise|redetaille|detaille|repete|pas compris.*(etape|cette)|"
                     r"j'ai pas suivi|etape\s*(\d+)|l'etape\s*(\d+)", q) and mem.get("answer"):
            m_n = re.search(r"etape\s*(\d+)", q)
            return self._clarify(uid, int(m_n.group(1)) if m_n else None)
        if any(w in q for w in ["continue", "la suite", "et apres", "termine",
                                "finis"]) and mem.get("answer"):
            return self._continue(uid)

        # 0bis) relances : le prof se souvient du dernier chapitre expliqué
        if any(w in q for w in ["plus simple", "pas compris", "comprends pas",
                                "autrement", "reexplique", "réexplique", "toujours pas"]):
            if mem.get("frag"):
                return self._lesson_alt(mem["frag"], db, mem)
            return "De quoi veux-tu que je parle ? Dis par exemple : « explique les suites »."
        if "exemple" in q and mem.get("frag") and "par exemple" not in q:
            return self._lesson_example(mem["frag"], db)
        if any(w in q for w in ["exercice", "entrainer", "entraîner", "s'entrainer"]) and mem.get("frag"):
            hit = self._find_chapter(mem["frag"], db)
            if hit:
                exs = db.query("SELECT id, difficulte FROM exercises WHERE chapter_id = ? "
                               "ORDER BY difficulte LIMIT 1", (hit["id"],))
                if exs:
                    return (f"🏋️ Parfait ! Ouvre l'exercice n°{exs[0]['id']} dans la rubrique "
                            f"Exercices ({hit['titre']}). Essaie seul, regarde l'indice si tu "
                            "bloques, puis la correction rédigée. Reviens me voir si ça "
                            "coince encore !")

        # 1) trigonométrie
        sol = solve_trig(q)
        if sol:
            return self._remember(uid, "trig", sol, {})

        # 2) équation polynomiale
        if "=" in q:
            sol = self._try_equation(q)
            if sol:
                return self._remember(uid, "quad", sol, {"q": q})

        # 3) dérivée
        if "derive" in q or "deriver" in q:
            sol = self._try_derivative(q)
            if sol:
                return self._remember(uid, "deriv", sol, {})

        # 4) limite
        if "lim" in q:
            sol = self._try_limit(q)
            if sol:
                return self._remember(uid, "lim", sol, {})

        # 5) calcul arithmétique
        sol = solve_arithmetic(q)
        if sol:
            return sol

        # 6) explication de chapitre (mots-clés puis recherche floue des titres)
        frag = self._match_chapter(q, db)
        if frag:
            mem["frag"] = frag
            mem["mi"] = 0
            return self._remember(uid, "lesson", self._lesson_answer(frag, db), {"frag": frag})

        # 7) secours structuré — jamais une impasse
        return ("🤔 Je n'ai pas encore de réponse précise à cette question en mode démo.\n\n"
                "✅ Ce que je sais faire dès maintenant :\n"
                "• « résoudre x^2 - 5x + 6 = 0 » (second degré)\n"
                "• « résoudre cos x = √3/2 » (trigonométrie)\n"
                "• « dérivée de 3x^3 - 2x + 5 »\n"
                "• « limite de (x^2-4)/(x-2) quand x tend vers 2 »\n"
                "• « combien font 15 × 7 ? »\n"
                "• « explique les suites », « la mole », « la génétique », "
                "« figure de style »... (tout le programme)\n\n"
                "💡 Après une explication, dis « plus simple », « un exemple » "
                "ou « un exercice » — je m'adapte à toi.")

    # ------------------------------------------------ clarification & suite --
    def _remember(self, uid, kind, text, payload):
        """Mémorise la dernière explication pour interruption/clarification."""
        steps = [ln.strip() for ln in text.split("\n")
                 if re.match(r"^\s*(Étape\s*\d|\d+\)|▶️)", ln.strip())]
        mem = self.mem.setdefault(uid, {})
        mem.update({"kind": kind, "answer": text, "steps": steps,
                    "payload": payload, "ptr": 0})
        return text

    def _clarify(self, uid, n=None):
        mem = self.mem.get(uid) or {}
        if not mem.get("answer"):
            return None
        steps = mem.get("steps") or []
        kind = mem.get("kind")
        if n is None:
            n = (mem.get("ptr") or 0) + 1 if steps else 1
        if steps and (n < 1 or n > len(steps)):
            return (f"Ma dernière explication a {len(steps)} étapes. "
                    f"Dis « clarifie l'étape 1 » jusqu'à « {len(steps)} » 😉")
        mem["ptr"] = n - 1 if steps else 0
        step_txt = steps[n - 1] if steps and n <= len(steps) else ""
        head = ["⏸️ Très bien, je m'arrête ! Reprenons calmement.", ""]
        if step_txt:
            step_clean = re.sub(r"^Étape\s*\d+\s*[—-]\s*", "", step_txt)
            head.append(f"📄 L'étape {n} disait : « {step_clean} »")
            head.append("")
        if kind == "quad" and n == 1:
            body = [
                "🧠 Décomposons tranquillement :",
                "1) Dans ax² + bx + c = 0, on IDENTIFIE d'abord 3 nombres : a = coefficient de x², b = coefficient de x, c = le nombre tout seul.",
                "2) Le discriminant Δ n'est PAS une solution : c'est un TEST qui compte combien de solutions existent.",
                "3) La formule : Δ = b² − 4ac. Tu élèves b au carré, tu calcules 4 fois a fois c, puis tu soustrais.",
                "",
                "💡 Analogie : Δ, c'est la fièvre chez le médecin — ça ne soigne pas, mais ça dit si ça va (Δ > 0 : 2 solutions), pas malade (Δ = 0 : 1 seule) ou rien à faire (Δ < 0 : aucune solution réelle).",
                "",
                "❓ Mini-test : dans x² − 5x + 6 = 0, qui sont a, b et c ? Dis-moi ta réponse !",
            ]
        elif kind == "quad" and n == 2:
            body = [
                "🧠 La formule x = (−b ± √Δ) / 2a se lit en 3 gestes :",
                "1) −b : on PREND L'OPPOSÉ de b (attention au signe, erreur n°1 aux examens !).",
                "2) ± √Δ : DEUX cas — une fois avec +√Δ, une fois avec −√Δ (d'où 2 solutions).",
                "3) On divise le tout par 2a (jamais par a ou par 2 tout seul).",
                "",
                "💡 Vérification maline : la somme des 2 racines doit donner −b/a. Si ce n'est pas le cas, recompte !",
                "",
                "❓ Dis-moi : dans l'équation qu'on résout, que vaut 2a ?",
            ]
        elif kind == "quad" and n >= 3:
            body = [
                "🧠 Factoriser, c'est réécrire l'équation sous forme a(x − x₁)(x − x₂) = 0.",
                "Un produit est nul si l'un des facteurs est nul → x = x₁ OU x = x₂.",
                "💡 Pour vérifier : remets x₁ dans l'équation de départ, tu dois trouver 0.",
            ]
        elif kind == "trig" and n == 1:
            body = [
                "🧠 Le cercle trigonométrique : un cercle de rayon 1. On place l'angle x en partant de la droite, dans le sens inverse des aiguilles.",
                "cos x = la hauteur HORIZONTALE du point (l'abscisse). sin x = la hauteur VERTICALE (l'ordonnée).",
                "💡 Astuce mémorisation : « cos » comme « côté couché » (horizontal), « sin » debout (vertical).",
                "",
                "❓ Dis-moi : sur ce cercle, que vaut cos(0) ?",
            ]
        elif kind == "trig" and n == 2:
            body = [
                "🧠 Pourquoi DEUX solutions ? Parce que la droite horizontale (pour cos) ou verticale (pour sin) COUPE le cercle en 2 points.",
                "Deux angles différents donnent la même valeur : ce sont tes 2 solutions.",
                "💡 Pour cos, les 2 points sont symétriques par rapport à l'axe horizontal ; pour sin, par rapport à l'axe vertical.",
            ]
        elif kind == "trig" and n >= 3:
            body = [
                "🧠 Sur [0 ; 2π], on liste les angles des 2 points trouvés.",
                "Sur ℝ tout entier, le cercle se répète tous les 2π : on ajoute + 2kπ (k entier) à chaque solution.",
                "💡 Réflexe examen : relis bien l'intervalle demandé — c'est là que tout se joue.",
            ]
        elif kind in ("lim",) and n == 1:
            body = [
                "🧠 Première règle des limites : ON REMPLACE D'ABORD. Toujours.",
                "Si le dénominateur n'est pas 0 → calcul direct, c'est fini.",
                "Si on obtient 0/0 ou ∞/∞ → c'est une FORME INDÉTERMINÉE : ça ne veut PAS dire 0 ni ∞, ça veut dire « il reste du travail » (factoriser…).",
            ]
        elif kind in ("lim",) and n >= 2:
            body = [
                "🧠 La forme 0/0 se traite par FACTORISATION : on cherche la racine évidente (ici x = la valeur vers laquelle on tend).",
                "On factorise le numérateur par (x − a), on simplifie avec le dénominateur, PUIS on remplace.",
                "💡 On ne simplifie « (x − a) » qu'en précisant x ≠ a — et pour une limite, c'est justement ce qui nous autorise !",
            ]
        elif kind == "deriv":
            body = [
                "🧠 La dérivée terme à terme : pour chaque terme a·xⁿ, le terme dérivé est a·n·xⁿ⁻¹.",
                "1) On garde le coefficient a. 2) On le multiplie par l'ancien exposant n. 3) L'exposant baisse d'un cran.",
                "💡 Le cas particulier : une constante (tout seul, sans x) disparaît car sa dérivée est 0 — sa « pente » est nulle.",
            ]
        else:
            body = [
                "🧠 Reprenons autrement, très simplement :",
                "1) Relis l'étape et dis-toi : « que cherche-t-on exactement à cette ligne ? »",
                "2) Quelle information de l'étape d'avant sert ici ?",
                "3) Quel est le résultat concret de cette ligne ?",
                "",
                "💡 Si tu veux, dis « un exemple » (je refais avec des nombres concrets) ou précise « clarifie l'étape 1 » (ou 2, 3…).",
            ]
        out = head + body
        out.append("")
        out.append("🎤 Interromps-moi quand tu veux : dis « clarifie l'étape X » ou « continue ».")
        return "\n".join(out)

    def _continue(self, uid):
        mem = self.mem.get(uid) or {}
        steps = mem.get("steps") or []
        ptr = mem.get("ptr", 0)
        if steps and ptr + 1 < len(steps):
            mem["ptr"] = ptr + 1
            rest = steps[ptr + 1:]
            return ("▶️ On continue l'explication :\n\n" + "\n\n".join(rest) +
                    "\n\n🎤 Dis « clarifie l'étape X » si un point te bloque.")
        return ("✅ C'était la fin de l'explication ! Tu peux : « un exercice » "
                "(pour t'entraîner), « plus simple » (autre méthode), ou poser "
                "une nouvelle question.")

    # ------------------------------------------------------------- chapitres --
    def _find_chapter(self, frag, db):
        rows = db.query(
            "SELECT c.*, s.code, s.nom as sujet FROM chapters c "
            "JOIN subjects s ON s.id = c.subject_id "
            "WHERE c.titre LIKE ? OR c.resume LIKE ? OR c.lecon LIKE ?",
            (f"%{frag}%", f"%{frag}%", f"%{frag}%"))
        return rows[0] if rows else None

    def _lesson_answer(self, frag, db):
        ch = self._find_chapter(frag, db)
        if not ch:
            return None
        lecon = {}
        if ch["lecon"]:
            try:
                lecon = json.loads(ch["lecon"])
            except Exception:
                lecon = {}
        out = [f"👨‍🏫 **{ch['titre']}** — {ch['sujet']} "
               f"({'Tronc Commun' if ch['niveau'] == 'TC' else '1ère Bac'})", ""]
        if lecon.get("intro"):
            out.append("🧭 L'essentiel : " + lecon["intro"])
        for i, m in enumerate(lecon.get("methodes", [])[:3], 1):
            nom = re.sub(r"^Méthode\s*\d+\s*[—-]\s*", "", m["nom"])
            out.append("")
            out.append(f"▶️ Méthode {i} — {nom}")
            out.append(m["texte"])
        ex = (lecon.get("exemples") or [None])[0]
        if ex:
            out.append("")
            out.append(f"✏️ Exemple corrigé : {ex['question']}")
            for e in ex["etapes"]:
                out.append(f"   {e}")
            out.append(f"   ➜ {ex['reponse']}")
        if lecon.get("pieges"):
            out.append("")
            out.append("⚠️ Pièges à éviter :")
            for p in lecon["pieges"][:2]:
                out.append(f"   • {p}")
        out.append("")
        out.append("💬 Dis « plus simple », « un exemple » ou « un exercice » "
                   "et je m'adapte !")
        return "\n".join(out)

    def _lesson_alt(self, frag, db, mem):
        ch = self._find_chapter(frag, db)
        if not ch:
            return None
        lecon = json.loads(ch["lecon"] or "{}")
        methodes = lecon.get("methodes", [])
        if not methodes:
            return self._lesson_answer(frag)
        mi = (mem.get("mi", 0) + 1) % len(methodes)
        mem["mi"] = mi
        m = methodes[mi]
        nom = re.sub(r"^Méthode\s*\d+\s*[—-]\s*", "", m["nom"])
        return ("🙌 D'accord, on prend une autre approche !\n\n"
                f"▶️ {nom}\n{m['texte']}\n\n"
                "C'est plus clair ? Dis « un exemple » ou « un exercice » pour continuer.")

    def _lesson_example(self, frag, db):
        ch = self._find_chapter(frag, db)
        if not ch:
            return None
        lecon = json.loads(ch["lecon"] or "{}")
        exs = lecon.get("exemples", [])
        if not exs:
            return (f"Je n'ai pas d'exemple prêt pour « {ch['titre']} » — mais ouvre un "
                    "exercice du chapitre : chaque correction est rédigée pas à pas.")
        ex = exs[0]
        out = [f"✏️ Exemple type — {ch['titre']} :", "", f"Énoncé : {ex['question']}", ""]
        for i, e in enumerate(ex["etapes"], 1):
            out.append(f"  {i}) {e}")
        out.append(f"  ➜ {ex['reponse']}")
        out.append("")
        out.append("Dis « un exercice » pour t'entraîner sur le même modèle !")
        return "\n".join(out)

    # ------------------------------------------------------------ solveurs ----
    def _try_equation(self, q):
        m = re.search(r"([0-9x\^\s\.\+\-\*]+)=([0-9x\^\s\.\+\-\*]+)", q)
        if not m:
            return None
        left, right = parse_poly(m.group(1)), parse_poly(m.group(2))
        if left is None or right is None:
            return None
        all_degs = set(left) | set(right)
        coeffs = {d: left.get(d, 0) - right.get(d, 0) for d in all_degs}
        coeffs = {d: c for d, c in coeffs.items() if c != 0}
        if not coeffs:
            return "Toute l'équation se simplifie : 0 = 0 → une infinité de solutions."
        deg = max(coeffs)
        a, b, c = coeffs.get(2, 0), coeffs.get(1, 0), coeffs.get(0, 0)
        if deg == 2 and a != 0:
            return solve_quadratic(a, b, c)
        if deg == 1:
            x = -c / b
            return "\n".join([
                f"📐 Équation du premier degré : {poly_to_str(coeffs)} = 0", "",
                f"{poly_to_str({1: b})} = {fmt_num(-c)}",
                f"x = {fmt_num(-c)} / {fmt_num(b)} = {fmt_num(round(x, 6))}",
                f"S = {{{fmt_num(round(x, 6))}}}"])
        if deg == 0:
            return "L'inconnue x disparaît : équation impossible ou toujours vraie."
        return None

    def _try_derivative(self, q):
        m = re.search(r"(?:de|:)?\s*([0-9x\^\s\.\+\-\*]+)$", q.strip())
        if not m:
            return None
        coeffs = parse_poly(m.group(1))
        if coeffs is None or max(coeffs) < 1:
            return None
        return solve_derivative(coeffs)

    def _try_limit(self, q):
        inf = ("infini" in q or "+oo" in q or "infinie" in q)
        m = re.search(r"\(?([0-9x\^\s\.\+\-\*/]+)\)?\s*/\s*\(?([0-9x\^\s\.\+\-\*/]+)\)?", q)
        if not m:
            return None
        num = parse_poly(m.group(1).strip("() "))
        den = parse_poly(m.group(2).strip("() "))
        if num is None or den is None:
            return None
        if inf:
            return solve_limit(num, den, +1, True)
        ma = re.search(r"(?:vers|tend vers|quand x (?:tend vers )?|=)\s*(-?\d+(?:\.\d+)?)", q)
        if not ma:
            return None
        return solve_limit(num, den, float(ma.group(1)), False)

    def _match_chapter(self, q, db):
        topics = {
            "pgcd": "Arithmétique", "ppcm": "Arithmétique", "premier": "Arithmétique",
            "euclide": "Arithmétique", "arithmetique dans": "Arithmétique",
            "divisibilite": "Arithmétique",
            "mole": "La mole", "concentration": "La mole", "dilution": "La mole",
            "masse molaire": "La mole", "avogadro": "La mole",
            "atome": "L'atome", "isotope": "L'atome", "noyau": "L'atome",
            "electron": "L'atome", "proton": "L'atome",
            "action reciproque": "Principe des actions réciproques",
            "newton": "Newton", "cinematique": "Cinématique", "vitesse": "Cinématique",
            "acceleration": "Cinématique",
            "energie": "Énergie mécanique", "energie cinetique": "Énergie mécanique",
            "chute": "Cinématique",
            "onde": "ondes", "frequence": "ondes", "periode": "ondes",
            "oscillogramme": "ondes", "lumiere": "ondes",
            "titrage": "dosage", "dosage": "dosage", "avancement": "dosage",
            "equivalence": "dosage", "reactif limitant": "dosage",
            "suite": "Suites", "geometrique": "Suites", "recurrence": "Suites",
            "arithmetique de suite": "Suites", "raison": "Suites",
            "limite": "Limites", "continuite": "Limites", "forme indeterminee": "Limites",
            "derive": "Dérivation", "tangente": "Dérivation", "extremum": "Dérivation",
            "denombrement": "Dénombrement", "combinaison": "Dénombrement",
            "arrangement": "Dénombrement", "permutation": "Dénombrement",
            "probabilite": "Probabilités", "urne": "Probabilités",
            "fonction": "Généralités sur les fonctions", "image": "Généralités sur les fonctions",
            "antecedent": "Généralités sur les fonctions", "parite": "Généralités sur les fonctions",
            "trinome": "Équations, inéquations et systèmes", "discriminant": "Équations, inéquations et systèmes",
            "valeur absolue": "Équations, inéquations et systèmes",
            "equation du second degre": "Équations, inéquations et systèmes",
            "vecteur": "Calcul vectoriel dans le plan",
            "colineaire": "Calcul vectoriel dans le plan",
            "equation de droite": "Calcul vectoriel dans le plan",
            "cercle trigonometrique": "Trigonométrie", "cosinus": "Trigonométrie",
            "sinus": "Trigonométrie", "radian": "Trigonométrie",
            "statistique": "Statistiques", "moyenne": "Statistiques", "medianne": "Statistiques",
            "quartile": "Statistiques",
            "cellule": "La cellule", "membrane": "La cellule", "chloroplaste": "La cellule",
            "mitose": "La cellule",
            "classification": "classification", "biodiversite": "classification",
            "cle de determination": "classification",
            "strate": "Origines géologiques", "fossile": "Origines géologiques",
            "geologie": "Origines géologiques",
            "tectonique": "Tectonique", "plaque": "Tectonique", "dorsale": "Tectonique",
            "subduction": "Tectonique", "magma": "Tectonique",
            "genetique": "Génétique", "croisement": "Génétique", "punnett": "Génétique",
            "allele": "Génétique", "allèle": "Génétique", "phenotype": "Génétique",
            "genotype": "Génétique", "heredite": "Génétique", "arbre genealogique": "Génétique",
            "immunite": "Immunologie", "immunologie": "Immunologie",
            "anticorps": "Immunologie", "lymphocyte": "Immunologie", "antigene": "Immunologie",
            "vaccin": "Immunologie",
            "argumentatif": "argumentatif", "thèse": "argumentatif",
            "these": "argumentatif", "connecteur": "argumentatif",
            "essai": "littérature d'idées", "lettre ouverte": "littérature d'idées",
            "figure de style": "figures de style", "metaphore": "figures de style",
            "comparaison": "figures de style", "personnification": "figures de style",
            "hyperbole": "figures de style",
            "resume": "résumé", "commentaire": "commentaire",
            "introduction": "commentaire", "plan detaille": "commentaire",
        }
        for key, frag in topics.items():
            if key in q:
                return frag
        # recherche floue sur les titres de chapitres
        titles = [t["titre"] for t in db.query("SELECT titre FROM chapters")]
        nt = [_norm(t) for t in titles]
        cands = [q] + [w for w in re.split(r"[^a-z0-9]+", q) if len(w) >= 5]
        for c in cands:
            m = difflib.get_close_matches(c, nt, n=1, cutoff=0.65)
            if m:
                return titles[nt.index(m[0])]
        return None


# ================================================================ LLMTutor ===
class LLMTutor:
    name = "llm"

    SYSTEM = (
        "Tu es PROF ATLAS, la star d'anime de l'enseignement marocain : prof de 27 ans, "
        "charismatique, drôle et bienveillant, qui CROIT en chacun de ses élèves "
        "(ta devise : « Je suis ton plus grand fan ! »). Tu enseignes les Maths, la "
        "Physique-Chimie, les SVT et le Français (Tronc Commun et 1ère Bac, programme "
        "marocain) — et tu es aussi une ENCYCLOPÉDIE vivante : si l'élève pose une "
        "question de culture générale, d'orientation, de sport, d'espace, d'Histoire... "
        "réponds avec la même passion pédagogique.\n\n"
        "TES RÈGLES D'OR :\n"
        "1. EXEMPLES DE LA VRAIE VIE de l'élève marocain : football (la trajectoire du "
        "ballon = parabole), tajine et cuisine (transferts de chaleur, mélanges), souk et "
        "devise (pourcentages, proportionnalité), téléphone et batterie (circuits, "
        "chimie), hammam (changements d'état), pluie et inondations (érosion), bus "
        "Casablanca-Rabat (vitesse, distance), médina et architecture (géométrie). "
        "TOUJOURS ancrer la notion dans une situation concrète qu'il VIT.\n"
        "2. EXPÉRIENCE À FAIRE À LA MAISON quand c'est possible : une expérience simple "
        "avec des objets du quotidien (verre d'eau et pièce dans une bassine, ballon de "
        "baudruche, sel/sucre/huile, aimant, lampe de poche) en 3 étapes : matériel → "
        "déroulement → ce que tu observeras = la preuve du cours.\n"
        "3. GRAPHISME ET VISUALISATION : rends la science VISIBLE. Utilise des schémas en "
        "caractères (flèches →, cercles ○, cases | |, courbes ASCII simples), des "
        "tableaux comparatifs (| notion | exemple | analogie |), des étapes numérotées, "
        "des analogies parlantes (l'atome = un immeuble, l'ADN = une recette de tajine). "
        "Une explication SANS image mentale est une explication ratée.\n"
        "4. ADAPTATION À LA PERSONNALITÉ : dedans ta réponse, essaie de deviner le profil "
        "de l'élève d'après ses messages (timide → encourage beaucoup ; pressé → va droit "
        "au but ; passionné → donne un bonus « Pour aller plus loin » ; en difficulté → "
        "repart d'une analogie ultra-simple ; amatour de foot/jeux/arts → utilise SA "
        "passion). Salue-le parfois par son prénom s'il te le donne. Ton chaleureux de "
        "grand frère star, jamais infantilisant.\n"
        "5. MÉTHODES MULTIPLES (2-3 approches : intuitive/graphique, formelle/calcul, "
        "concrète/expérience) et étapes de calcul numérotées et justifiées, conforme au "
        "vocabulaire du Ministère.\n"
        "6. Termine par un PIÈGE à éviter + une MINI-QUESTION d'entraînement avec un "
        "défi sympa (style quête d'anime : « Relever le défi du Prof ? ⚔️ »).\n"
        "7. Réponse structurée (titres courts, puces), maximum 350 mots.\n"
        "8. N'utilise JAMAIS LaTeX ni commande LaTeX : interdits \\frac, \\times, "
        "\\Rightarrow, \\sqrt, \\;, \\[, \\], $$. Écris les maths en notation "
        "lisible : x², x³, √5, 12/3, 3x − 5 = 7, x₁, x₂, ×, ÷, ⇒, ≥, ≤, ≠, ∈ ℝ, π, Δ. "
        "Fraction = barre oblique (12/3).\n"
        "9. Emojis anime avec goût (⚔️ ⭐ 🔥 ✨ 🎯 ⚡ 🌟) : c'est ton style de star, mais "
        "restons lisibles — 3 à 5 par réponse maximum.\n"
        "10. Si la question n'est pas scolaire (vie perso, santé mentale...) : réponds en "
        "grand frère à l'écoute, bienveillant, et redirige vers un adulte de confiance si "
        "nécessaire."
    )

    def __init__(self, cfg):
        self.cfg = cfg

    def respond(self, question, db, user_id=None):
        import urllib.error
        import urllib.request
        base = (self.cfg.get("base_url") or "https://api.openai.com/v1").rstrip("/")

        # contexte élève : prénom, classe + 3 dernières questions (adaptation personnalité)
        profil = ""
        if user_id and db:
            try:
                u = db.query("SELECT prenom, nom FROM users WHERE id = ?", (user_id,), one=True)
                classe = db.query(
                    "SELECT c.nom FROM classes c JOIN users u ON u.classe_id = c.id "
                    "WHERE u.id = ? LIMIT 1", (user_id,), one=True)
                hist = db.query(
                    "SELECT question FROM tutor_logs WHERE user_id = ? "
                    "ORDER BY id DESC LIMIT 3", (user_id,))
                p = (u.get("prenom") or "") if u else ""
                if p or classe or hist:
                    morceaux = []
                    if p: morceaux.append(f"prénom {p}")
                    if classe and classe.get("nom"): morceaux.append(f"classe {classe['nom']}")
                    if hist:
                        qs = " ; ".join((h.get("question") or "")[:60] for h in hist if h.get("question"))
                        if qs: morceaux.append(f"sues questions récentes : {qs}")
                    profil = ("\n\n[ÉLÈVE : " + " · ".join(morceaux) +
                              " — adapte ton ton et tes exemples à SON profil]")
            except Exception:
                profil = ""

        body = {
            "model": self.cfg.get("model", "gpt-4o-mini"),
            "messages": [
                {"role": "system", "content": self.SYSTEM + profil},
                {"role": "user", "content": question},
            ],
            "temperature": 0.7,
        }
        headers = {"Authorization": f"Bearer {self.cfg['api_key']}",
                   "Content-Type": "application/json",
                   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Fahmni/1.0"}
        # les modèles gpt-oss raisonnent vite avec effort "low"
        body2 = dict(body)
        body2["reasoning_effort"] = "low"
        body2["max_completion_tokens"] = 1500   # réponse rapide, jamais coupée
        last_err = None
        for essai in range(2):            # 1 réessai automatique si réseau/timeout
            for payload in (body2, body):  # retombe sans l'option si refusée
                req = urllib.request.Request(f"{base}/chat/completions",
                                             data=json.dumps(payload).encode(),
                                             headers=headers)
                try:
                    with urllib.request.urlopen(req, timeout=120) as r:
                        data = json.loads(r.read())
                    return data["choices"][0]["message"]["content"]
                except urllib.error.HTTPError as e:
                    if e.code in (400, 422) and payload is body2:
                        last_err = e
                        continue
                    raise
                except (urllib.error.URLError, TimeoutError, OSError) as e:
                    last_err = e
                    break                # problème réseau → nouvelle tentative
        raise last_err


# ---------------------------------------------------- singleton du moteur ----
_local_instance = None


def get_tutor():
    """Retourne le meilleur moteur disponible (mémoire conservée entre requêtes)."""
    global _local_instance
    cfg = load_config()
    if cfg.get("api_key"):
        return LLMTutor(cfg), True
    if _local_instance is None:
        _local_instance = LocalTutor()
    return _local_instance, False
