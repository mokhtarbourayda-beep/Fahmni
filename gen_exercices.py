# -*- coding: utf-8 -*-
"""gen_exercices.py — Générateur DYNAMIQUE d'exercices à la demande.
Chaque appel produit un exercice INÉDIT (paramètres aléatoires) avec une
correction CALCULÉE par le code → toujours exacte.

Usage : generer(code, titre, difficulte) -> dict(enonce, solution, astuce)
"""

import random
from fractions import Fraction as F

# ------------------------------------------------------------- utilitaires --
def fmt(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fr(x, nd=2):
    s = f"{x:.{nd}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def signe(b):
    return "+" if b >= 0 else "-"


def linfmt(a, b):
    return f"{fmt(a)}x {signe(b)} {abs(b)}"


# pools -----------------------------------------------------------------------
TRIGO = {"π/6": ("√3/2", "1/2"), "π/4": ("√2/2", "√2/2"), "π/3": ("1/2", "√3/2"),
         "2π/3": ("−1/2", "√3/2"), "3π/4": ("−√2/2", "√2/2"), "5π/6": ("−√3/2", "1/2"),
         "7π/6": ("−√3/2", "−1/2"), "5π/4": ("−√2/2", "−√2/2"), "4π/3": ("−1/2", "−√3/2"),
         "5π/3": ("1/2", "−√3/2"), "7π/4": ("√2/2", "−√2/2"), "11π/6": ("√3/2", "−1/2")}
COS2 = {"√3/2": ("π/6", "11π/6"), "√2/2": ("π/4", "7π/4"), "1/2": ("π/3", "5π/3"),
        "−1/2": ("2π/3", "4π/3"), "−√2/2": ("3π/4", "5π/4"), "−√3/2": ("5π/6", "7π/6")}
SIN2 = {"1/2": ("π/6", "5π/6"), "√2/2": ("π/4", "3π/4"), "√3/2": ("π/3", "2π/3"),
        "−1/2": ("7π/6", "11π/6"), "−√2/2": ("5π/4", "7π/4"), "−√3/2": ("4π/3", "5π/3")}
TRIPLES2 = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25), (20, 21, 29)]
TRIPLES3 = [(2, 3, 6, 7), (1, 2, 2, 3), (4, 4, 7, 9), (2, 6, 9, 11), (6, 6, 7, 11), (1, 4, 8, 9)]
ATOMES = [(1, "H", "hydrogène"), (12, "C", "carbone"), (14, "N", "azote"), (16, "O", "oxygène"),
          (23, "Na", "sodium"), (24, "Mg", "magnésium"), (27, "Al", "aluminium"),
          (32, "S", "soufre"), (35, "Cl", "chlore"), (39, "K", "potassium"),
          (40, "Ca", "calcium"), (56, "Fe", "fer"), (63, "Cu", "cuivre"), (65, "Zn", "zinc")]
MOLES = [("C6H12O6", 180), ("C12H22O11", 342), ("CO(NH2)2", 60), ("C2H6O", 46),
         ("CuSO4", 159.5), ("NaCl", 58.5), ("C6H8O6", 176), ("NaHCO3", 84)]


def config_electronique(n):
    couches, rest = [], n
    for i, capa in enumerate((2, 8, 18)):
        if rest <= 0:
            break
        p = min(rest, capa)
        couches.append(f"({'KLM'[i]}){p}")
        rest -= p
    return " ".join(couches)


# ==================================================================== MATH ===
GEN = {}


def reg(code, titre, difs):
    def deco(fn):
        for d in (difs if isinstance(difs, tuple) else (difs,)):
            GEN.setdefault(code, {}).setdefault(titre, {}).setdefault(d, []).append(fn)
        return fn
    return deco


# --- Arithmétique
@reg("MATH", "Arithmétique dans ℕ", (1, 2))
def _arith_diviseurs():
    n = random.randint(12, 90)
    divs = [d for d in range(1, n + 1) if n % d == 0]
    return (f"Dresser la liste de tous les diviseurs de {n}. Combien en compte-t-on ?",
            f"Diviseurs de {n} : {' ; '.join(map(str, divs))}\nIl y en a {len(divs)}.",
            "Tester de 1 à √n : chaque diviseur d donne aussi n/d.")


@reg("MATH", "Arithmétique dans ℕ", 1)
def _arith_divisibilite():
    n = random.randint(100, 9999)
    k = random.choice((2, 3, 4, 5, 9, 11))
    ok = n % k == 0
    regles = {2: "le dernier chiffre est pair", 3: "la somme des chiffres est divisible par 3",
              4: "le nombre formé par les 2 derniers chiffres est un multiple de 4",
              5: "il se termine par 0 ou 5", 9: "la somme des chiffres est divisible par 9",
              11: "la différence alternée des chiffres est divisible par 11"}
    s = sum(int(c) for c in str(n))
    detail = f" (somme des chiffres = {s})" if k in (3, 9) else ""
    return (f"Le nombre {n} est-il divisible par {k} ? Justifier par la règle de divisibilité.",
            f"{n} / {k} → {'quotient exact' if ok else 'reste ≠ 0'} : {'OUI' if ok else 'NON'}\n"
            f"Règle : {regles[k]}{detail}.",
            f"Règle du {k} : la connaître par cœur.")


@reg("MATH", "Arithmétique dans ℕ", (2, 3))
def _arith_pgcd():
    a = random.randint(12, 120)
    b = random.randint(12, 120)
    g = __import__("math").gcd(a, b)
    l = a * b // g
    return (f"Calculer PGCD({a} ; {b}) puis PPCM({a} ; {b}).",
            f"PGCD = {g} (décompositions ou algorithme d'Euclide)\n"
            f"PPCM = a×b/PGCD = {a}×{b}/{g} = {l}",
            "PGCD : plus petits exposants ; PPCM : plus grands.")


@reg("MATH", "Arithmétique dans ℕ", 2)
def _arith_premiers():
    n = random.choice([i for i in range(40, 200) if i % 2 == 1])
    d = next((d for d in (3, 5, 7, 11, 13) if n % d == 0), None)
    if d:
        rep = f"{n} = {d} × {n // d} → NON PREMIER (divisible par {d})."
    else:
        rep = f"Aucun premier ≤ √{n} ≈ {fr(__import__('math').sqrt(n), 1)} ne divise {n} → PREMIER."
    return (f"Le nombre {n} est-il premier ? Justifier.",
            rep, "Tester 2, 3, 5, 7, 11, 13… jusqu'à √n.")


@reg("MATH", "Arithmétique dans ℕ", 3)
def _arith_rencontre():
    a = random.choice((6, 8, 9, 10, 12, 15))
    b = random.choice((4, 12, 14, 18, 20))
    g = __import__("math").gcd(a, b)
    l = a * b // g
    return (f"Deux bus partent ensemble d'une gare : le premier repasse toutes les {a} min, "
            f"le second toutes les {b} min. Après combien de minutes repartiront-ils ENSEMBLE ?",
            f"On cherche le PPCM({a} ; {b}).\nPGCD = {g} → PPCM = {a}×{b}/{g} = {l}\n"
            f"Ils repartiront ensemble après {l} minutes.",
            "Retrouvailles simultanées = PPCM des deux durées.")


# --- Ensembles
@reg("MATH", "Les ensembles de nombres", 1)
def _ens_classer():
    n, d = random.randint(1, 12), random.choice((2, 3, 4, 5, 6, 8, 9))
    f = F(n, d)
    dec = f"{float(f):.4f}".rstrip("0").rstrip(".")
    if d in (2, 4, 5, 8):
        rep, expl = "𝔻 (et ℚ)", "virgule FINIE"
    else:
        rep, expl = "ℚ (mais PAS 𝔻)", "périodique infinie"
    return (f"Placer {fmt(f)} dans le plus petit ensemble qui le contient (ℕ, ℤ, 𝔻, ℚ, ℝ).",
            f"{fmt(f)} = {dec.replace('.', ',')} → écriture décimale {expl}.\n"
            f"Donc {fmt(f)} ∈ {rep}.",
            "Fraction : diviser ; virgule finie → 𝔻, périodique → ℚ seulement.")


@reg("MATH", "Les ensembles de nombres", 2)
def _ens_racine():
    n = random.choice([i for i in range(2, 200) if int(__import__("math").isqrt(i)) ** 2 != i])
    r = __import__("math").sqrt(n)
    d = random.choice((1, 2))
    p = 10 ** d
    lo = __import__("math").floor(r * p) / p
    hi = (lo * p + 1) / p
    SUP = {1: "10⁻¹", 2: "10⁻²"}
    return (f"Encadrer √{n} par deux décimaux à {SUP[d]} près (défaut puis excès).",
            f"√{n} ≈ {fr(r, d + 2)}\nPar défaut : {fr(lo, d)} ; par excès : {fr(hi, d)}\n"
            f"→ {fr(lo, d)} ≤ √{n} < {fr(hi, d)}",
            f"Couper au {d + 1}ᵉ chiffre : garder en dessous (défaut), monter d'une unité (excès).")


@reg("MATH", "Les ensembles de nombres", 3)
def _ens_periodique():
    p = random.randint(10, 99)
    f = F(p, 99)
    return (f"Écrire 0,{p}{p}{p}… (= 0,<{p}> période infinie) sous forme de fraction "
            "irréductible.",
            f"x = 0,{p}{p}{p}…\n100x = {p},{p}{p}{p}… → 100x − x = {p}\n99x = {p} → x = {p}/99\n"
            f"Simplification : x = {fmt(f)} (PGCD({p} ; 99) = "
            f"{__import__('math').gcd(p, 99)}).",
            "Période de 2 chiffres → multiplier par 100 ; puis soustraire x.")


# --- Ordre
@reg("MATH", "L'ordre dans ℝ", 1)
def _ordre_encadrer():
    a = random.randint(-3, 2)
    b = a + random.randint(1, 5)
    k = random.randint(2, 6)
    c = random.randint(-5, 5)
    return (f"Sachant {a} ≤ x ≤ {b}, encadrer f(x) = {k}x {'+' if c >= 0 else '-'} {abs(c)}.",
            f"{k}×{a} ≤ {k}x ≤ {k}×{b}\n{k * a} ≤ {k}x ≤ {k * b}\n"
            f"{k * a + c} ≤ {k}x {'+' if c >= 0 else '-'} {abs(c)} ≤ {k * b + c}\n"
            f"Donc f(x) ∈ [{k * a + c} ; {k * b + c}]",
            "Opérer sur les TROIS membres, dans le même sens (k > 0).")


@reg("MATH", "L'ordre dans ℝ", 2)
def _ordre_negatif():
    a = random.randint(-3, 2)
    b = a + random.randint(1, 5)
    k = random.randint(2, 6)
    return (f"Sachant {a} ≤ x ≤ {b}, encadrer g(x) = −{k}x.",
            f"Multiplier par −{k} → les inégalités CHANGENT de sens :\n"
            f"−{k}×{a} ≥ −{k}x ≥ −{k}×{b}\n{fmt(-k * b)} ≤ −{k}x ≤ {fmt(-k * a)}",
            "×(nombre négatif) : RENVERSER les inégalités !")


@reg("MATH", "L'ordre dans ℝ", 2)
def _ordre_comparer_fractions():
    n1, d1 = random.randint(2, 12), random.randint(3, 13)
    n2, d2 = random.randint(2, 12), random.randint(3, 13)
    g1, g2 = n1 * d2, n2 * d1
    rep = "<" if g1 < g2 else (">" if g1 > g2 else "=")
    return (f"Comparer {fmt(F(n1, d1))} et {fmt(F(n2, d2))} (sans calculatrice).",
            f"Produits en croix (dénominateurs positifs) :\n{n1}×{d2} = {g1} et {n2}×{d1} = {g2}\n"
            f"{g1} {rep} {g2} → {fmt(F(n1, d1))} {rep} {fmt(F(n2, d2))}",
            "a/b ⋚ c/d ⟺ a×d ⋚ c×b.")


@reg("MATH", "L'ordre dans ℝ", 3)
def _ordre_inverse():
    a = random.randint(1, 3)
    b = a + random.randint(2, 6)
    return (f"Sachant {a} ≤ x ≤ {b} (x strictement positif), encadrer 1/x.",
            f"La fonction inverse est DÉCROISSANTE sur (0 ; +∞) → les bornes s'ÉCHANGENT :\n"
            f"1/{b} ≤ 1/x ≤ 1/{a}\n(1/{b} = {fmt(F(1, b))} ; 1/{a} = {fmt(F(1, a))})",
            "L'inverse réduit l'encadrement et échange les bornes.")


# --- Polynômes
@reg("MATH", "Les polynômes", 1)
def _poly_doubledistrib():
    a, b, c, d = (random.randint(1, 5), random.randint(-6, 6), random.randint(1, 5),
                  random.randint(-6, 6))
    return (f"Développer et réduire ({fmt(a)}x {signe(b)} {abs(b)})({fmt(c)}x {signe(d)} {abs(d)}).",
            f"= {fmt(a * c)}x² {signe(a * d + b * c)} {abs(a * d + b * c)}x {signe(b * d)} {abs(b * d)}",
            "(ax+b)(cx+d) = acx² + (ad+bc)x + bd.")


@reg("MATH", "Les polynômes", 1)
def _poly_carre():
    a, b = random.randint(1, 5), random.randint(1, 9)
    return (f"Développer ({fmt(a)}x {signe(b)} {abs(b)})².",
            f"= ({a}x)² {signe(-2 * a * b)} {abs(2 * a * b)}x {'+' if b * b >= 0 else '-'} {b * b}\n"
            f"= {fmt(a * a)}x² {signe(-2 * a * b)} {abs(2 * a * b)}x + {b * b}",
            "(a±b)² = a² ± 2ab + b² : ne pas oublier le DOUBLE PRODUIT.")


@reg("MATH", "Les polynômes", 1)
def _poly_diffcarrés():
    r = random.randint(2, 12)
    k = r * r
    return (f"Factoriser x² − {k}.",
            f"x² − {k} = x² − {r}² = (x − {r})(x + {r})",
            "a² − b² = (a − b)(a + b) : repérer le carré parfait.")


@reg("MATH", "Les polynômes", 2)
def _poly_commun():
    g = random.randint(2, 9)
    a = random.randint(1, 6)
    b = random.randint(1, 9)
    n = random.randint(2, 3)
    puiss = f"^{n}" if n > 1 else ""
    puiss_m1 = f"^{n - 1}" if n - 1 > 1 else ""
    return (f"Factoriser {g * a}x{puiss} {'+' if g * b >= 0 else '-'} {abs(g * b)}x{puiss_m1}.",
            f"Facteur commun : {g}x{puiss_m1}\n= {g}x{puiss_m1}({fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)})",
            "PGCD des coefficients + la plus petite puissance.")


@reg("MATH", "Les polynômes", 2)
def _poly_racine_evidente():
    r = random.choice((-3, -2, -1, 1, 2, 3, 4, 5))
    s = random.choice([-4, -2, -1, 2, 3, 4, 6])
    while s == r:
        s = random.choice([-4, -2, -1, 2, 3, 4, 6])
    S, P = r + s, r * s
    term_S = "x" if abs(S) == 1 else f"{abs(S)}x"
    return (f"On donne P(x) = x² {'-' if S >= 0 else '+'} {term_S} {'+' if P >= 0 else '-'} {abs(P)}. "
            f"Vérifier que {r} est racine de P puis factoriser P.",
            f"P({r}) = {r * r} {'-' if S >= 0 else '+'} {abs(S)}×{r} {'+' if P >= 0 else '-'} {abs(P)} "
            f"= {r * r - S * r + P} = 0 ✓\n(r) est racine → P(x) = (x {'-' if r >= 0 else '+'} {abs(r)})"
            f"(x {'-' if s >= 0 else '+'} {abs(s)})\n"
            f"Vérification par développement : x² {'-' if S >= 0 else '+'} {term_S} "
            f"{'+' if P >= 0 else '-'} {abs(P)} ✓",
            "P(a) = 0 ⟺ (x − a) est un facteur ; l'autre racine vient de la somme (S) ou du produit.")


@reg("MATH", "Les polynômes", 3)
def _poly_bicarree():
    k = random.choice((4, 9, 16, 25, 36, 49))
    r = int(__import__("math").isqrt(k))
    return (f"Résoudre : x⁴ − {k + 4}x² + {4 * k} = 0.",
            f"On pose X = x² : X² − {k + 4}X + {4 * k} = 0\n"
            f"Racines évidentes : X = {k} et X = 4 (somme {k + 4} ✓ produit {4 * k} ✓)\n"
            f"X = {k} → x = ±{r} ; X = 4 → x = ±2\nS = {{-{r} ; −2 ; 2 ; {r}}}",
            "Bicarrée : X = x², résoudre en X, puis revenir (x = ±√X).")


@reg("MATH", "Les polynômes", 3)
def _poly_diff_carrés_composée():
    a = random.randint(1, 6)
    b = random.choice((3, 4, 5, 6, 7, 9))
    return (f"Factoriser (x − {a})² − {b * b}.",
            f"A = (x − {a})² − {b}² (différence de carrés)\n"
            f"A = (x − {a} − {b})(x − {a} + {b}) = (x − {a + b})(x + {b - a})"
            if b - a >= 0 else
            f"A = (x − {a} − {b})(x − {a} + {b}) = (x − {a + b})(x − {a - b})",
            "A² − B² avec A = (x − a) et B = {b}.")


# --- Équations / inéquations
@reg("MATH", "Équations, inéquations et systèmes", 1)
def _eq_premier_degre():
    a, b, c = random.randint(2, 9), random.randint(-9, 9), 0
    x = random.randint(-8, 8)
    c = a * x + b
    return (f"Résoudre : {linfmt(a, b)} = {c}.",
            f"{a}x = {c} {'-' if b >= 0 else '+'} {abs(b)} = {c - b}\nx = {fmt(F(c - b, a))}\n"
            f"S = {{{fmt(F(c - b, a))}}}",
            "Isoler ax puis diviser par a.")


@reg("MATH", "Équations, inéquations et systèmes", 2)
def _eq_inequation():
    a = random.choice((2, 3, 4, 5, -3, -4, -6))
    b = random.randint(-9, 9)
    x0 = random.randint(-6, 6)
    c = a * x0 + b
    sym = "≥" if random.random() < 0.5 else "<"
    if a > 0:
        sol = f"x {sym} {fmt(F(x0))}" if sym == "≥" else f"x < {fmt(F(x0))}"
        ens = f"[{fmt(F(x0))} ; +∞[" if sym == "≥" else f"]-∞ ; {fmt(F(x0))}["
    else:
        inv = "≤" if sym == "≥" else ">"
        sol = f"x {inv} {fmt(F(x0))}"
        ens = f"]-∞ ; {fmt(F(x0))}]" if inv == "≤" else f"]{fmt(F(x0))} ; +∞["
    return (f"Résoudre l'inéquation : {linfmt(a, b)} {sym} {c} (S en intervalle).",
            f"{a}x {sym} {c - b}\nDivision par {a} ({'positif : sens conservé' if a > 0 else 'négatif : SENS INVERSÉ'})\n"
            f"{sol}\nS = {ens}",
            "Diviser par un négatif → retourner le symbole.")


@reg("MATH", "Équations, inéquations et systèmes", (2, 3))
def _eq_systeme():
    x0, y0 = random.randint(-5, 6), random.randint(-5, 6)
    a1, b1 = random.randint(1, 3), random.randint(-3, 3)
    a2, b2 = random.randint(2, 5), random.choice((-2, -1, 1, 2))
    while a1 * b2 - a2 * b1 == 0:
        b2 = random.choice((-2, 1, 2))
    c1, c2 = a1 * x0 + b1 * y0, a2 * x0 + b2 * y0
    return (f"Résoudre le système : {{ {a1}x {'+' if b1 >= 0 else '-'} {abs(b1)}y = {c1} ; "
            f"{a2}x {'+' if b2 >= 0 else '-'} {abs(b2)}y = {c2} }}",
            f"Par combinaison (éliminer y) : {a2}×L1 − {a1}×L2 :\n"
            f"({a2 * b1 - a1 * b2})y = {a2 * c1 - a1 * c2} → y = {y0}\n"
            f"Puis dans L1 : {a1}x {'+' if b1 >= 0 else '-'} {abs(b1)}×({y0}) = {c1} → x = {x0}\n"
            f"S = {{({x0} ; {y0})}}",
            "Combinaison linéaire pour une inconnue, substitution pour l'autre.")


@reg("MATH", "Équations, inéquations et systèmes", 3)
def _eq_probleme():
    px = random.randint(5, 15)
    py = random.randint(2, 9)
    n1, n2 = random.randint(2, 5), random.randint(2, 5)
    while n1 == n2:
        n2 = random.randint(2, 5)
    s1 = n1 * px + py
    s2 = px + py
    return (f"Mise en équation : {n1} cahiers et 1 stylo coûtent {s1} DH ; 1 cahier et 1 stylo "
            f"coûtent {s2} DH. Trouver le prix de chaque article.",
            f"Système : {{ {n1}x + y = {s1} ; x + y = {s2} }}\n"
            f"L1 − L2 : ({n1} − 1)x = {s1 - s2} → x = {px}\n"
            f"y = {s2} − {px} = {py}\nCahier : {px} DH ; stylo : {py} DH",
            "Poser les inconnues, traduire CHAQUE phrase, puis combinaison.")


@reg("MATH", "Équations, inéquations et systèmes", 3)
def _eq_tableau_signes():
    r1, r2 = random.randint(-6, -1), random.randint(1, 7)
    S, P = r1 + r2, r1 * r2
    sym = random.choice(("≤", "<"))
    bornes = "[" if sym == "≤" else "]"
    return (f"Résoudre avec un tableau de signes : (x {'+' if -r1 >= 0 else '-'} {abs(r1)})"
            f"(x {'+' if -r2 >= 0 else '-'} {abs(r2)}) {sym} 0.",
            f"Racines : x = {r1} et x = {r2}\nSigne du produit : négatif ENTRE les racines "
            "(a = 1 > 0 à l'extérieur)\nS = {bornes}{min(r1, r2)} ; {max(r1, r2)}{bornes}",
            "Racines ordonnées, signe de a à l'extérieur, bornes selon ≤ ou <.")


# --- Vecteurs
@reg("MATH", "Calcul vectoriel dans le plan", 1)
def _vec_ab():
    (vx, vy, n) = random.choice(TRIPLES2)
    ax, ay = random.randint(-4, 4), random.randint(-4, 4)
    bx, by = ax + vx, ay + vy
    return (f"A({ax} ; {ay}) et B({bx} ; {by}) : coordonnées de AB puis distance AB.",
            f"AB({bx}−({ax}) ; {by}−({ay})) = AB({vx} ; {vy})\n"
            f"AB = √({vx}² + {vy}²) = √{vx * vx + vy * vy} = {n}",
            "AB = B − A ; norme = racine des carrés.")


@reg("MATH", "Calcul vectoriel dans le plan", 1)
def _vec_milieu():
    ax, ay, bx, by = (random.randint(-6, 6) for _ in range(4))
    if (ax + bx) % 2 or (ay + by) % 2:
        bx += 1
    mx, my = F(ax + bx, 2), F(ay + by, 2)
    return (f"Calculer le milieu I de [AB] avec A({ax} ; {ay}) et B({bx} ; {by}).",
            f"I(({ax}+{bx})/2 ; ({ay}+{by})/2) = I({fmt(mx)} ; {fmt(my)})",
            "Milieu = moyennes des coordonnées.")


@reg("MATH", "Calcul vectoriel dans le plan", 2)
def _vec_alignes():
    ax, ay = random.randint(-4, 4), random.randint(-4, 4)
    vx, vy = random.randint(-3, 3), random.randint(-3, 3)
    while vx == 0 and vy == 0:
        vx, vy = random.randint(-3, 3), random.randint(-3, 3)
    k = random.randint(2, 4)
    aligner = random.random() < 0.6
    bx, by = ax + vx, ay + vy
    cx, cy = (ax + k * vx, ay + k * vy) if aligner else (ax + vy * 2, ay + vx * 3)
    if not aligner and (cx - ax) * (by - ay) - (bx - ax) * (cy - ay) == 0:
        cx += 1
    det = (bx - ax) * (cy - ay) - (cx - ax) * (by - ay)
    return (f"A({ax} ; {ay}), B({bx} ; {by}), C({cx} ; {cy}) : sont-ils alignés ?",
            f"AB({bx - ax} ; {by - ay}) ; AC({cx - ax} ; {cy - ay})\n"
            f"Colinéarité : ({bx - ax})×({cy - ay}) − ({cx - ax})×({by - ay}) = {det}\n"
            + (f"= 0 → colinéaires → ALIGNÉS" if det == 0 else f"≠ 0 → NON alignés"),
            "xy′ − x′y = 0 ⟺ colinéaires (avec A commun → alignés).")


@reg("MATH", "Calcul vectoriel dans le plan", 3)
def _vec_parallelogramme():
    ax, ay = random.randint(-4, 4), random.randint(-4, 4)
    vx, vy, wx, wy = (random.randint(-4, 4) for _ in range(4))
    bx, by = ax + vx, ay + vy
    dx, dy = ax + wx, ay + wy
    cx, cy = bx + dx - ax, by + dy - ay
    return (f"ABCD est un parallélogramme avec A({ax} ; {ay}), B({bx} ; {by}), D({dx} ; {dy}). "
            "Déterminer C.",
            f"ABCD parallélogramme ⟺ AB = DC ⟺ C = B + D − A\n"
            f"C({bx}+({dx})−({ax}) ; {by}+({dy})−({ay})) = C({cx} ; {cy})",
            "Relation clé : AB = DC ⟺ C = B + D − A.")


# --- Droite
@reg("MATH", "La droite dans le plan", 1)
def _dr_deux_points():
    m = random.choice((-3, -2, -1, 1, 2, 3, 4))
    ax = random.randint(-4, 4)
    ay = random.randint(-5, 5)
    bx = ax + random.choice((1, 2))
    by = ay + m * (bx - ax)
    p = ay - m * ax
    return (f"Déterminer l'équation de la droite passant par A({ax} ; {ay}) et B({bx} ; {by}).",
            f"m = ({by} − ({ay}))/({bx} − ({ax})) = {fmt(F(m))}\n"
            f"y = {fmt(F(m))}x + p avec A : {ay} = {fmt(F(m))}×{ax} + p → p = {p}\n"
            f"d : y = {fmt(F(m))}x {'+' if p >= 0 else '-'} {abs(p)}  (vérification B ✓)",
            "m = Δy/Δx, puis p avec un point.")


@reg("MATH", "La droite dans le plan", 2)
def _dr_intersection():
    x0 = random.randint(-4, 4)
    y0 = random.randint(-5, 6)
    m1, m2 = random.choice((1, 2, 3, -2)), random.choice((-1, 1, 2, -3))
    while m1 == m2:
        m2 = random.choice((-1, 2, -3, 4))
    p1, p2 = y0 - m1 * x0, y0 - m2 * x0
    xi = F(p2 - p1, m1 - m2)
    yi = m1 * xi + p1
    return (f"Trouver le point d'intersection de d₁ : y = {fmt(F(m1))}x {'+' if p1 >= 0 else '-'} {abs(p1)} "
            f"et d₂ : y = {fmt(F(m2))}x {'+' if p2 >= 0 else '-'} {abs(p2)}.",
            f"Égaliser : {fmt(F(m1))}x {'+' if p1 >= 0 else '-'} {abs(p1)} = {fmt(F(m2))}x {'+' if p2 >= 0 else '-'} {abs(p2)}\n"
            f"({fmt(F(m1 - m2))})x = {p2 - p1} → x = {fmt(xi)}\ny = {fmt(yi)}\nI({fmt(xi)} ; {fmt(yi)})",
            "Intersection : une seule équation en x après égalisation.")


@reg("MATH", "La droite dans le plan", 3)
def _dr_perpendiculaire_projet():
    m1 = random.choice((1, 2, -2, 3))
    m2 = F(-1, m1)
    p1 = random.randint(-4, 4)
    xa, ya = random.randint(-3, 5), random.randint(-4, 6)
    if ya == m1 * xa + p1:
        ya += 1
    p2 = ya - m2 * xa
    xh = (p2 - p1) / (F(m1) - m2)
    yh = m1 * xh + p1
    return (f"A({xa} ; {ya}) et d : y = {fmt(F(m1))}x {'+' if p1 >= 0 else '-'} {abs(p1)}. "
            "Équation de la perpendiculaire à d passant par A, puis projeté orthogonal H de A sur d.",
            f"m(Δ)×m(d) = −1 → m(Δ) = {fmt(m2)}\n"
            f"Δ : y = {fmt(m2)}x + p ; {ya} = {fmt(m2)}×{xa} + p → p = {fmt(p2)}\n"
            f"H = d ∩ Δ : {fmt(F(m1))}x {'+' if p1 >= 0 else '-'} {abs(p1)} = {fmt(m2)}x {'+' if p2 >= 0 else '-'} {abs(p2)}\n"
            f"x = {fmt(xh)} ; y = {fmt(yh)} → H({fmt(xh)} ; {fmt(yh)})",
            "Perpendiculaire : produit des coefficients = −1 ; H = intersection des deux droites.")


# --- Trigo
@reg("MATH", "Trigonométrie", 1)
def _tr_valeurs():
    ang = random.choice(list(TRIGO))
    c, s = TRIGO[ang]
    return (f"Donner cos({ang}) et sin({ang}) (cercle trigonométrique).",
            f"cos({ang}) = {c} ; sin({ang}) = {s}",
            "Placer l'angle sur le cercle ; utiliser les symétries.")


@reg("MATH", "Trigonométrie", 2)
def _tr_angles_associes():
    c, s = TRIGO[random.choice(list(TRIGO))]
    choix = random.choice(("π − x", "−x", "π + x"))
    if choix == "π − x":
        rep = f"cos(π − x) = −cos x = {'' if c.startswith('−') else '−'}{c}\nsin(π − x) = sin x = {s}"
    elif choix == "−x":
        rep = f"cos(−x) = cos x = {c}\nsin(−x) = −sin x = {'' if s.startswith('−') else '−'}{s}"
    else:
        rep = f"cos(π + x) = −cos x = {'' if c.startswith('−') else '−'}{c}\nsin(π + x) = −sin x = {'' if s.startswith('−') else '−'}{s}"
    return (f"On sait cos x = {c} et sin x = {s}. Donner cos({choix}) et sin({choix}) "
            "(angles associés).",
            rep,
            "π − x : symétrie par (Oy) ; −x : (Ox) ; π + x : point opposé.")


@reg("MATH", "Équations et inéquations trigonométriques", 2)
def _treq_equation():
    table = random.choice((COS2, SIN2))
    fn = "cos" if table is COS2 else "sin"
    val = random.choice(list(table))
    a1, a2 = table[val]
    return (f"Résoudre dans [0 ; 2π] : {fn} x = {val}.",
            f"{val} = {fn}({a1})\nLes DEUX points du cercle : {a1} et {a2}\nS = {{{a1} ; {a2}}}",
            "Valeur remarquable + symétrie ; ne pas oublier la 2ᵉ solution !")


@reg("MATH", "Équations et inéquations trigonométriques", 3)
def _treq_affine():
    table = COS2
    val = random.choice(list(table))
    a1, a2 = table[val]
    k = random.choice((2, 3))
    if val.startswith("−"):
        affiche, op = val[1:], "+"      # k·cos x − (−a) → k·cos x + a
    else:
        affiche, op = val, "−"
    return (f"Résoudre dans [0 ; 2π] : {k}cos x {op} {affiche} = 0.",
            f"Isoler : cos x = {val}\n"
            f"= cos({a1}) → S = {{{a1} ; {a2}}}",
            "Isoler cos x (division par k > 0), puis procédure classique.")


@reg("MATH", "Équations et inéquations trigonométriques", 2)
def _treq_inequation():
    eq, sol, ast = random.choice((
        ("cos x > 1/2", "]0 ; π/3[ ∪ ]5π/3 ; 2π[", "abscisse > 1/2 : arc autour de 0"),
        ("cos x ≤ √2/2", "[π/4 ; 7π/4]", "abscisse ≤ √2/2 : grand arc à gauche"),
        ("sin x ≥ √3/2", "[π/3 ; 2π/3]", "ordonnée ≥ √3/2 : arc en haut"),
        ("sin x < −1/2", "]π ; 7π/6[ ∪ ]11π/6 ; 2π[", "ordonnée < −1/2 : arc en bas")))
    return (f"Résoudre dans [0 ; 2π] : {eq}.", f"S = {sol} (lecture sur le cercle : {ast})",
            "Bornes ouvertes si strict, fermées si large.")


# --- Produit scalaire
@reg("MATH", "Produit scalaire dans le plan", 1)
def _ps_calcul():
    u = (random.randint(-5, 5), random.randint(-5, 5))
    v = (random.randint(-5, 5), random.randint(-5, 5))
    while u == (0, 0) or v == (0, 0):
        v = (random.randint(-5, 5), random.randint(-5, 5))
    ps = u[0] * v[0] + u[1] * v[1]
    nu = __import__("math").sqrt(u[0] ** 2 + u[1] ** 2)
    nv = __import__("math").sqrt(v[0] ** 2 + v[1] ** 2)
    return (f"u({u[0]} ; {u[1]}) et v({v[0]} ; {v[1]}) : calculer u·v, ‖u‖ et ‖v‖.",
            f"u·v = ({u[0]})×({v[0]}) + ({u[1]})×({v[1]}) = {ps}\n"
            f"‖u‖ = √({u[0] ** 2} + {u[1] ** 2}) = {fr(nu)} ; ‖v‖ = √({v[0] ** 2} + {v[1] ** 2}) = {fr(nv)}",
            "u·v = xx′ + yy′ ; ‖u‖ = √(x² + y²).")


@reg("MATH", "Produit scalaire dans le plan", 2)
def _ps_orthogonal():
    u = (random.randint(-6, 6), random.randint(-6, 6))
    while u == (0, 0) or u[1] == 0:
        u = (random.randint(-6, 6), random.randint(-6, 6))
    v = (u[1], -u[0])
    return (f"Montrer que u({u[0]} ; {u[1]}) et v({v[0]} ; {v[1]}) sont orthogonaux.",
            f"u·v = {u[0]}×{v[0]} + ({u[1]})×({v[1]}) = {u[0] * v[0] + u[1] * v[1]} = 0\n→ u ⊥ v",
            "Test : produit scalaire nul ⟺ orthogonaux.")


@reg("MATH", "Produit scalaire dans le plan", 3)
def _ps_trouver_v():
    a, b, n = random.choice(((3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17)))
    u = (a, b)
    vs = [(b, -a), (-b, a), (-b, a), (b, -a)]
    v = random.choice(((b, -a), (-b, a)))
    return (f"Soit u({a} ; {b}). Déterminer le(s) vecteur(s) v tel(s) que v ⊥ u et ‖v‖ = {n}.",
            f"v(x ; y) ⊥ u → {a}x + {b}y = 0 → y = −{a}x/{b}\n"
            f"‖v‖ = {n} → x² + y² = {n * n}\n"
            f"Solution types : v = ({b} ; −{a}) et v = (−{b} ; {a}) — vérif : ‖v‖ = √({b * b} + {a * a}) = {n} ✓",
            "v = (y ; −x) est TOUJOURS orthogonal à u(x ; y) et de même norme.")


# --- Fonctions
@reg("MATH", "Généralités sur les fonctions", 1)
def _fn_domaine_rationnel():
    a, b = random.randint(1, 6), random.randint(-8, 8)
    while b + a == 0:
        b = random.randint(-8, 8)
    rac = F(-b, a)
    return (f"Déterminer le domaine de f(x) = ({linfmt(a, b)})/({a}x + {b + a}).",
            f"Le dénominateur s'annule pour {a}x + {b + a} = 0 → x = {fmt(rac)}\n"
            f"D_f = ℝ \\ {{{fmt(rac)}}} = ]-∞ ; {fmt(rac)}[ ∪ ]{fmt(rac)} ; +∞[",
            "Exclure la valeur qui annule le DÉNOMINATEUR.")


@reg("MATH", "Généralités sur les fonctions", 1)
def _fn_domaine_racine():
    a = random.randint(1, 6)
    x0 = random.randint(-6, 3)
    return (f"Déterminer le domaine de g(x) = √({a}x {'+' if -x0 * a >= 0 else '-'} {abs(x0 * a)}).",
            f"Il faut {a}x {'+' if -x0 * a >= 0 else '-'} {abs(x0 * a)} ≥ 0\n"
            f"x ≥ {fmt(F(-x0 * a, a))} → D_g = [{fmt(F(-x0 * a, a))} ; +∞[",
            "Sous une racine : la quantité doit être ≥ 0.")


@reg("MATH", "Généralités sur les fonctions", 2)
def _fn_parite():
    forme = random.choice(("3x + 7", "x4 - 2x2", "x3 + x", "5/x", "x2 + x", "2x5 - 3x"))
    reps = {"3x + 7": "f(−x) = −3x + 7 : ≠ f(x) et ≠ −f(x) → ni paire ni impaire",
            "x4 - 2x2": "f(−x) = x⁴ − 2x² = f(x) → PAIRE (symétrie / (Oy))",
            "x3 + x": "f(−x) = −x³ − x = −f(x) → IMPAIRE (symétrie / O)",
            "5/x": "f(−x) = −5/x = −f(x) → IMPAIRE",
            "x2 + x": "f(−x) = x² − x : ≠ f(x) et ≠ −f(x) → ni l'un ni l'autre",
            "2x5 - 3x": "f(−x) = −2x⁵ + 3x = −f(x) → IMPAIRE"}
    return (f"Étudier la parité de f(x) = {forme}.", reps[forme],
            "Comparer f(−x) à f(x) puis à −f(x).")


@reg("MATH", "Généralités sur les fonctions", 2)
def _fn_taux():
    a = random.choice((2, 3, 4, 5, -2, -3, -4))
    x1 = random.randint(-4, 2)
    x2 = x1 + random.randint(2, 5)
    f = lambda x: a * x + 3
    return (f"f(x) = {fmt(a)}x + 3. Calculer le taux de variation entre {x1} et {x2} et conclure.",
            f"T = (f({x2}) − f({x1}))/({x2} − {x1}) = ({fmt(f(x2))} − {fmt(f(x1))})/{x2 - x1} = {fmt(F(a))}\n"
            f"Taux constant → f affine, {'croissante' if a > 0 else 'décroissante'} sur ℝ.",
            "Pour une affine, le taux = coefficient directeur.")


@reg("MATH", "Généralités sur les fonctions", 3)
def _fn_antecedent():
    a = random.choice((2, 3, 4, 5))
    b = random.randint(-9, 9)
    c = random.randint(-8, 12)
    x = F(c - b, a)
    return (f"Soit f(x) = {fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)}. Déterminer l'antécédent de "
            f"{c} par f (résoudre f(x) = {c}).",
            f"{fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)} = {c}\n{fmt(a)}x = {c - b}\n"
            f"x = {fmt(F(c - b, a))} → l'antécédent est {fmt(x)}",
            "Antécédent : résoudre f(x) = valeur.")


# --- Statistiques
@reg("MATH", "Statistiques", 1)
def _stat_moyenne():
    n = random.choice((5, 7, 9))
    vals = sorted(random.randint(4, 18) for _ in range(n))
    moy = F(sum(vals), n)
    med = vals[n // 2]
    et = vals[-1] - vals[0]
    return (f"Notes : {' ; '.join(map(str, vals))}. Calculer moyenne, médiane et étendue.",
            f"n = {n} ; somme = {sum(vals)} → moyenne = {fmt(moy)} ≈ {fr(float(moy))}\n"
            f"Données ordonnées → médiane = {med} (valeur centrale) ; étendue = {vals[-1]} − {vals[0]} = {et}",
            "TRIER d'abord ; médiane = valeur du milieu.")


@reg("MATH", "Statistiques", 2)
def _stat_ponderee():
    vals = [random.randint(6, 18) for _ in range(3)]
    coefs = random.choice(((1, 2, 1), (2, 3, 1), (1, 1, 2), (2, 1, 1)))
    tot = sum(c * v for c, v in zip(coefs, vals))
    nc = sum(coefs)
    return (f"Moyenne pondérée de : {' ; '.join(f'{v} (coef {c})' for v, c in zip(vals, coefs))}.",
            f"Σ(nᵢxᵢ) = {' + '.join(f'{c}×{v}' for c, v in zip(coefs, vals))} = {tot}\n"
            f"Total des coefficients = {nc} → moyenne = {fmt(F(tot, nc))} ≈ {fr(tot / nc)}",
            "Moyenne pondérée = Σ(nᵢ·xᵢ)/Σnᵢ.")


@reg("MATH", "Statistiques", 3)
def _stat_ecc():
    b1, b2 = 8, 12
    c0 = random.randint(4, 12)
    c1 = c0 + random.randint(6, 14)
    c2 = c1 + random.randint(6, 12)
    tot = c2 + random.randint(6, 16)
    return (f"Effectifs cumulés croissants d'une classe de {tot} élèves : {c0} élèves ont une note "
            f"< {b1}, {c1} ont < 10, {c2} ont < {b2 + 2}. Combien sont dans [10 ; {b2 + 2}[ ? "
            f"Et combien ont au moins 10 ?",
            f"[10 ; {b2 + 2}[ : {c2} − {c1} = {c2 - c1} élèves\n"
            f"≥ 10 : {tot} − {c1} = {tot - c1} élèves",
            "ECC : différence entre deux valeurs cumulées.")


# --- Transformations
@reg("MATH", "Transformations usuelles dans le plan", 1)
def _tr_translation():
    m = (random.randint(-5, 5), random.randint(-5, 5))
    u = (random.randint(-4, 4), random.randint(-4, 4))
    return (f"M({m[0]} ; {m[1]}) et t la translation de vecteur u({u[0]} ; {u[1]}). "
            "Coordonnées de M' = t(M) ?",
            f"M' = M + u = ({m[0]} + ({u[0]}) ; {m[1]} + ({u[1]})) = M'({m[0] + u[0]} ; {m[1] + u[1]})",
            "Translation : ON ADDITIONNE le vecteur.")


@reg("MATH", "Transformations usuelles dans le plan", 1)
def _tr_symetries():
    m = (random.randint(-6, 6), random.randint(-6, 6))
    return (f"Images de M({m[0]} ; {m[1]}) par : s_O (symétrie centrale O), s_(Ox), s_(Oy).",
            f"s_O(M) = (−{m[0]} ; −{m[1]})\ns_(Ox)(M) = ({m[0]} ; −{m[1]})\n"
            f"s_(Oy)(M) = (−{m[0]} ; {m[1]})",
            "O : les deux signes ; (Ox) : y seul ; (Oy) : x seul.")


@reg("MATH", "Transformations usuelles dans le plan", 2)
def _tr_si():
    i = (random.randint(-4, 4), random.randint(-4, 4))
    m = (random.randint(-6, 6), random.randint(-6, 6))
    si = (2 * i[0] - m[0], 2 * i[1] - m[1])
    return (f"I({i[0]} ; {i[1]}) et M({m[0]} ; {m[1]}). Image de M par la symétrie centrale s_I ?",
            f"s_I(M) = 2I − M = ({2 * i[0]} − {m[0]} ; {2 * i[1]} − {m[1]}) = ({si[0]} ; {si[1]})",
            "Formule : s_I(M) = 2I − M.")


@reg("MATH", "Transformations usuelles dans le plan", 2)
def _tr_homothetie():
    a = random.choice((8, 12, 16, 20, 25, 36))
    k = random.choice((2, 3, F(1, 2), F(1, 4)))
    kk = F(k)
    return (f"Une figure d'aire {a} cm² subit l'homothétie h(O ; {fmt(kk)}). Aire de l'image ? "
            "Les longueurs sont multipliées par quoi ?",
            f"Longueurs ×|k| = ×{fmt(abs(kk))} ; aires ×k² = ×{fmt(kk * kk)}\n"
            f"Aire image = {a} × {fmt(kk * kk)} = {fr(float(a) * float(kk * kk), 4)} cm²",
            "Longueurs ×|k| ; AIRES ×k².")


@reg("MATH", "Transformations usuelles dans le plan", 3)
def _tr_rotation():
    p = (random.randint(-5, 5), random.randint(-5, 5))
    ang = random.choice(("90° (sens direct)", "180°"))
    if ang.startswith("90"):
        im = (-p[1], p[0])
        rep = f"r(O ; 90°) : (x ; y) → (−y ; x) → ({im[0]} ; {im[1]})"
    else:
        im = (-p[0], -p[1])
        rep = f"r(O ; 180°) : (−x ; −y) → ({im[0]} ; {im[1]})"
    return (f"Image de P({p[0]} ; {p[1]}) par la rotation de centre O d'angle {ang} ?", rep,
            "90° direct : (x;y)→(−y;x) ; 180° : les deux signes.")


# --- Projection
@reg("MATH", "La projection dans le plan", 2)
def _proj_hauteur():
    a, b, c = random.choice(TRIPLES2)
    ah = F(a * b, c)
    return (f"ABC rectangle en A avec AB = {a} et AC = {b}. H est le projeté orthogonal de A sur "
            "(BC). Calculer BC puis AH.",
            f"Pythagore : BC = √({a}² + {b}²) = {c}\n"
            f"Double expression de l'aire : AB×AC/2 = BC×AH/2\n{a}×{b}/2 = {a * b // 2} ; "
            f"{c}×AH/2 = {a * b // 2} → AH = {fmt(ah)} ≈ {fr(float(ah))}",
            "L'« aire calculée 2 fois » fait sortir la hauteur.")


@reg("MATH", "La projection dans le plan", 3)
def _proj_carre():
    s = random.choice((4, 6, 8))
    e = s // 2
    return (f"ABCD carré de côté {s}, E milieu de [AB], H projeté orthogonal de E sur la diagonale "
            "(AC). Calculer EH et AH.",
            f"La diagonale fait 45° avec (AB) ; AE = {e} ; AEH rectangle en H, angle A = 45°\n"
            f"EH = AE·sin 45° = {e}×√2/2 = {fmt(F(e) * F(1, 2))}√2 ≈ {fr(e * 0.7071)}\n"
            f"AH = AE·cos 45° = même valeur = {fmt(F(e) * F(1, 2))}√2 (triangle rectangle isocèle)",
            "Angle 45° → triangle rectangle isocèle : EH = AH.")


# --- Espace
@reg("MATH", "Géométrie dans l'espace", 1)
def _es_om():
    x, y, z, n = random.choice(TRIPLES3)
    return (f"Calculer la distance OM pour M({x} ; {y} ; {z}).",
            f"OM = √({x}² + {y}² + {z}²) = √{x * x + y * y + z * z} = {n}",
            "Pythagore 3D : √(x² + y² + z²).")


@reg("MATH", "Géométrie dans l'espace", 2)
def _es_ab_milieu():
    a = tuple(random.randint(-4, 4) for _ in range(3))
    x, y, z, n = random.choice(TRIPLES3)
    b = (a[0] + x, a[1] + y, a[2] + z)
    i = tuple(F(a[k] + b[k], 2) for k in range(3))
    return (f"A{tuple(a)} et B{tuple(b)} : coordonnées de AB, distance AB, milieu de [AB].",
            f"AB({x} ; {y} ; {z})\nAB = √({x * x} + {y * y} + {z * z}) = {n}\n"
            f"I({fmt(i[0])} ; {fmt(i[1])} ; {fmt(i[2])})",
            "AB = B − A ; milieu = moyennes ; Pythagore 3D.")


@reg("MATH", "Géométrie dans l'espace", 3)
def _es_alignes():
    a = tuple(random.randint(-3, 3) for _ in range(3))
    u = random.choice(((1, 1, 1), (1, 2, -1), (2, 1, 3), (1, -2, 2)))
    k = random.randint(2, 3)
    aligner = random.random() < 0.55
    b = tuple(a[i] + u[i] for i in range(3))
    if aligner:
        c = tuple(a[i] + k * u[i] for i in range(3))
        rep = f"AC = {k}·AB (ratios égaux : {k} ; {k} ; {k}) → ALIGNÉS"
    else:
        w = (u[1], u[0], u[2])
        c = tuple(a[i] + w[i] * 2 for i in range(3))
        ratios = []
        rep = "AC n'est pas un multiple de AB (au moins un ratio différent) → NON alignés"
    ab = tuple(b[i] - a[i] for i in range(3))
    ac = tuple(c[i] - a[i] for i in range(3))
    detail = " ; ".join(f"{ac[i]}/{ab[i]}" if ab[i] else "—" for i in range(3))
    return (f"A{tuple(a)}, B{tuple(b)}, C{tuple(c)} : sont-ils alignés ?",
            f"AB({ab[0]} ; {ab[1]} ; {ab[2]}) ; AC({ac[0]} ; {ac[1]} ; {ac[2]})\n"
            f"Ratios AC/AB : {detail}\n{rep if aligner else 'Ratios inégaux → NON alignés'}"
            if aligner else
            f"AB({ab[0]} ; {ab[1]} ; {ab[2]}) ; AC({ac[0]} ; {ac[1]} ; {ac[2]})\n"
            f"Ratios AC/AB : {detail} → inégaux → NON alignés",
            "Le multiple k doit être LE MÊME sur les 3 coordonnées.")


# ====================================================================== PC ===
@reg("PC", "L'atome et la structure de la matière", 1)
def _at_composition():
    a, sym, nom = random.choice(ATOMES)
    z = {1: 1, 12: 6, 14: 7, 16: 8, 23: 11, 24: 12, 27: 13, 32: 16, 35: 17, 39: 19,
         40: 20, 56: 26, 63: 29, 65: 30}[a]
    return (f"L'atome {a}/{z} {sym} ({nom}) : composition (p⁺, n, e⁻) et configuration électronique.",
            f"Protons = Z = {z} ; neutrons = A − Z = {a} − {z} = {a - z} ; électrons = {z}\n"
            f"Configuration : {config_electronique(z)}",
            "K (2), L (8), M (18) ; neutrons = A − Z.")


@reg("PC", "L'atome et la structure de la matière", 2)
def _at_ion():
    z, sym, nom = random.choice(ATOMES)
    charge = random.choice((-3, -2, -1, 1, 2, 3))
    if z + charge <= 0:
        charge = 1
    ion = f"{sym}{'+' if charge < 0 else '-'}{abs(charge) if abs(charge) > 1 else ''}"
    ne = z + charge
    return (f"L'ion {ion} (Z = {z} pour {sym}) : nombre d'électrons et configuration. "
            "Est-il stable (octet/duet) ?",
            f"{'CATION' if charge < 0 else 'ANION'} : {z} {'−' if charge < 0 else '+'} "
            f"{abs(charge)} e⁻ = {ne} électrons\nConfiguration : {config_electronique(ne)}\n"
            + ("Octet/duet atteint → ion MONATOMIQUE STABLE." if config_electronique(ne).endswith((")8", ")2")) or ")18" in config_electronique(ne)
               else "Dernière couche non pleine (ion transitoire)."),
            "Cation : perte d'e⁻ ; anion : gain. Les protons ne changent JAMAIS.")


@reg("PC", "L'atome et la structure de la matière", 3)
def _at_isotopes():
    z = random.choice((17, 29, 35))
    a1 = random.choice((35, 63, 79))
    a2 = a1 + 2
    p = random.randint(20, 80)
    m = (a1 * p + a2 * (100 - p)) / 100
    return (f"Le chlore/cuivre/brome naturel (Z = {z}) est un mélange de {a1}/{z} X ({p} %) et "
            f"{a2}/{z} X ({100 - p} %). Pourquoi s'agit-il d'isotopes ? Calculer M naturelle.",
            f"Même Z = {z} (même élément) mais A ≠ ({a1} et {a2}) → ISOTOPES.\n"
            f"M = ({a1}×{p} + {a2}×{100 - p})/100 = {fr(m)} g/mol",
            "Masse molaire naturelle = moyenne PONDÉRÉE par les abondances.")


@reg("PC", "La mole et les concentrations", 1)
def _mo_n():
    form, m = random.choice(MOLES)
    n = random.choice((0.10, 0.20, 0.25, 0.50))
    masse = round(n * m, 2)
    return (f"Quelle quantité de matière dans {fr(masse)} g de {form} (M = {fr(m)} g/mol) ?",
            f"n = m/M = {fr(masse)}/{fr(m)} = {fr(n)} mol",
            "n = m/M ; ordre de grandeur : m < M → n < 1.")


@reg("PC", "La mole et les concentrations", 2)
def _mo_masse():
    form, m = random.choice(MOLES)
    c = random.choice((0.10, 0.20, 0.25, 0.50))
    v = random.choice((100, 250, 500))
    masse = c * (v / 1000) * m
    return (f"On prépare V = {v} mL de solution de {form} à C = {fr(c)} mol/L. "
            f"Quelle masse peser ? (M = {fr(m)} g/mol)",
            f"n = C×V = {fr(c)} × {v / 1000} = {fr(c * v / 1000)} mol\n"
            f"m = n×M = {fr(c * v / 1000)} × {fr(m)} = {fr(masse)} g",
            "Convertir mL → L AVANT tout calcul.")


@reg("PC", "La mole et les concentrations", 2)
def _mo_dilution():
    c1 = random.choice((0.5, 1.0, 1.5, 2.0, 3.0))
    c2 = random.choice((0.05, 0.1, 0.2, 0.25, 0.5))
    if c2 >= c1:
        c2 = F(c1) / 5
    v2 = random.choice((100, 200, 250, 500))
    v1 = float(c2) * v2 / c1
    return (f"Dilution : solution mère C₁ = {fr(c1)} mol/L. Quel volume prélever pour obtenir "
            f"V₂ = {v2} mL à C₂ = {fr(float(c2))} mol/L ? Facteur de dilution ?",
            f"V₁ = C₂V₂/C₁ = {fr(float(c2))}×{v2}/{fr(c1)} = {fr(v1)} mL\n"
            f"F = C₁/C₂ = {fr(c1 / float(c2))} (= V₂/V₁)",
            "Conservation du soluté : C₁V₁ = C₂V₂.")


@reg("PC", "La mole et les concentrations", 3)
def _mo_protocole():
    c1 = random.choice((0.5, 1.0, 2.0))
    c2 = random.choice((0.05, 0.1, 0.2))
    v2 = random.choice((200, 250, 500))
    v1 = c2 * v2 / c1
    form, m = random.choice(MOLES)
    masse = c2 * v2 / 1000 * m
    return (f"Protocole complet : obtenir V₂ = {v2} mL de solution de {form} à C₂ = {fr(c2)} mol/L "
            f"à partir d'une solution mère C₁ = {fr(c1)} mol/L. Verrerie ? Masse de soluté dans la "
            f"fiole (M = {fr(m)} g/mol) ?",
            f"V₁ = C₂V₂/C₁ = {fr(v1)} mL → pipette jaugée de {fr(v1)} mL\n"
            f"Fiole jaugée de {v2} mL : prélever, compléter au trait de jauge, homogénéiser.\n"
            f"m = C₂×V₂×M = {fr(c2)}×{v2 / 1000}×{fr(m)} = {fr(masse)} g",
            "Pipette jaugée (prélèvement exact) + fiole jaugée (volume exact).")


@reg("PC", "La réaction chimique et le bilan de matière", 1)
def _rc_ajuster():
    eq, verif = random.choice((
        ("H2 + O2 → H2O", "2H₂ + O₂ → 2H₂O (H : 4=4 ; O : 2=2)"),
        ("Al + O2 → Al2O3", "4Al + 3O₂ → 2Al₂O₃ (Al : 4=4 ; O : 6=6)"),
        ("Fe + HCl → FeCl2 + H2", "Fe + 2HCl → FeCl₂ + H₂ (Fe, Cl, H équilibrés)"),
        ("CO + O2 → CO2", "2CO + O₂ → 2CO₂ (C : 2=2 ; O : 4=4)"),
        ("C3H8 + O2 → CO2 + H2O", "C₃H₈ + 5O₂ → 3CO₂ + 4H₂O (C, H, O équilibrés)"),
        ("Zn + HCl → ZnCl2 + H2", "Zn + 2HCl → ZnCl₂ + H₂")))
    return (f"Ajuster et vérifier : {eq}.", verif,
            "Coefficients seulement ; équilibrer C, puis H, puis O.")


@reg("PC", "La réaction chimique et le bilan de matière", 2)
def _rc_proportions():
    n = random.choice((0.2, 0.5, 1.5, 2.0))
    return (f"On brûle n = {fr(n)} mol de méthane : CH₄ + 2O₂ → CO₂ + 2H₂O. "
            "Quantités de O₂ consommé, CO₂ et H₂O formés.",
            f"Coefficients 1 ; 2 ; 1 ; 2 :\nn(O₂) = 2×{fr(n)} = {fr(2 * n)} mol\n"
            f"n(CO₂) = {fr(n)} mol ; n(H₂O) = {fr(2 * n)} mol",
            "Les coefficients = proportions MOLAIRES.")


@reg("PC", "La réaction chimique et le bilan de matière", 3)
def _rc_limitant():
    nz = random.choice((0.05, 0.10, 0.15, 0.20, 0.30))
    nah = random.choice((0.10, 0.15, 0.20, 0.30, 0.40, 0.50))
    xh = nah / 2
    xmax = min(nz, xh)
    lim = "H⁺" if xh < nz else ("Zn" if nz < xh else "les deux (stœchiométrique)")
    restes = f"Zn restant = {fr(nz - xmax)} mol" if nz > xmax else "Zn épuisé"
    return (f"On mélange {fr(nz)} mol de zinc et {fr(nah)} mol d'ions H⁺ "
            "(Zn + 2H⁺ → Zn²⁺ + H₂). Réactif limitant ? Quantité de H₂ formée ?",
            f"xmax(Zn) = {fr(nz)}/1 = {fr(nz)} mol ; xmax(H⁺) = {fr(nah)}/2 = {fr(xh)} mol\n"
            f"xmax = {fr(xmax)} mol → limitant : {lim}\n"
            f"n(H₂) = {fr(xmax)} mol ; {restes}" +
            (f" ; n(Zn²⁺) = {fr(xmax)} mol" if True else ""),
            "Diviser chaque n initial par son coefficient ; le minimum limite.")


@reg("PC", "Les solutions acides et basiques : le pH", 1)
def _ph_vers_conc():
    p = random.randint(1, 6)
    return (f"Une solution a pH = {p}. Calculer [H₃O⁺] et donner son caractère.",
            f"[H₃O⁺] = 10⁻{p} = {fr(10 ** (-p), 10)} mol/L\npH < 7 → solution ACIDE",
            "[H₃O⁺] = 10^-pH.")


@reg("PC", "Les solutions acides et basiques : le pH", 2)
def _ph_depuis_conc():
    p = random.randint(0, 4)
    disp = "1" if p == 0 else ("0," + "0" * (p - 1) + "1")
    return (f"[H₃O⁺] = {disp} mol/L. Calculer le pH.",
            f"pH = −log({disp}) = {p}",
            "10^-p → pH = p : compter les zéros.")


@reg("PC", "Les solutions acides et basiques : le pH", 2)
def _ph_dilution():
    p0 = random.randint(1, 4)
    fact = random.choice((10, 100, 1000))
    n = int(__import__("math").log10(fact))
    return (f"Un acide de pH = {p0} est dilué {fact} fois. Nouveau pH ?",
            f"Dilution ×{fact} = ×10^{n} → pH +{n}\npH_final = {p0} + {n} = {p0 + n}",
            "Diluer un acide : +1 unité de pH par facteur 10 (tend vers 7).")


@reg("PC", "Le circuit électrique : courant et tension", 1)
def _el_ohm_u():
    r = random.choice((12, 47, 68, 100, 220, 330, 470))
    i = random.choice((20, 50, 100, 150, 200, 250))
    return (f"Un résistor R = {r} Ω est parcouru par I = {i} mA. Tension U ?",
            f"I = {i} mA = {fr(i / 1000, 3)} A\nU = R×I = {r} × {fr(i / 1000, 3)} = {fr(r * i / 1000)} V",
            "Convertir mA → A AVANT la loi d'Ohm.")


@reg("PC", "Le circuit électrique : courant et tension", 1)
def _el_ohm_i():
    u = random.choice((4.5, 6, 9, 12, 24))
    r = random.choice((30, 60, 90, 120, 240, 300, 450, 1200))
    return (f"Sous U = {fr(u)} V, un résistor de R = {r} Ω. Calculer I en mA.",
            f"I = U/R = {fr(u)}/{r} = {fr(u / r, 4)} A = {fr(u / r * 1000)} mA",
            "I = U/R ; 1 A = 1000 mA.")


@reg("PC", "Le circuit électrique : courant et tension", 2)
def _el_noeuds():
    i1 = random.choice((1.0, 1.5, 2.0, 2.5, 3.0))
    i2 = random.choice((0.5, 1.0, 1.5, 2.0))
    i3 = random.choice((0.3, 0.5, 0.8, 1.0))
    return (f"Loi des nœuds : I₁ = {fr(i1)} A et I₂ = {fr(i2)} A arrivent ; I₃ = {fr(i3)} A sort. "
            "Calculer l'intensité I₄ sortante.",
            f"I₁ + I₂ = I₃ + I₄\n{fr(i1 + i2)} = {fr(i3)} + I₄\nI₄ = {fr(i1 + i2 - i3)} A",
            "Ce qui ENTRE = ce qui SORT.")


@reg("PC", "Le circuit électrique : courant et tension", 2)
def _el_req():
    r1, r2, rp = random.choice(((30, 60, 20), (20, 30, 12), (60, 120, 40), (100, 150, 60),
                                (40, 60, 24), (75, 150, 50), (90, 180, 60), (200, 300, 120)))
    return (f"R₁ = {r1} Ω et R₂ = {r2} Ω : résistance équivalente en SÉRIE puis en PARALLÈLE.",
            f"Série : R_eq = {r1 + r2} Ω\n"
            f"Parallèle : 1/R_eq = 1/{r1} + 1/{r2} → R_eq = {r1}×{r2}/{r1 + r2} = {rp} Ω\n"
            "(parallèle : PLUS PETITE que chaque résistance ✓)",
            "Parallèle : produit/divisé par la somme (pour 2 résistors).")


@reg("PC", "Le circuit électrique : courant et tension", 3)
def _el_mixte():
    r1, r2, rp = random.choice(((100, 150, 60), (60, 120, 40), (40, 60, 24), (90, 180, 60)))
    u = random.choice((9, 12, 24))
    req = r1 + rp
    i = u / req
    u23 = rp * i
    return (f"Générateur {fr(u)} V alimentant R₁ = {r1} Ω en série avec le parallèle de "
            f"R₂ = {r2} Ω et R₃ = {2 * r2} Ω. Calculer R_eq, I puis U aux bornes du groupe parallèle.",
            f"Parallèle : R₂₃ = {r2}×{2 * r2}/{r2 + 2 * r2} = {rp} Ω\n"
            f"Série : R_eq = {r1} + {rp} = {req} Ω\n"
            f"I = U/R_eq = {fr(u)}/{req} = {fr(i, 3)} A\n"
            f"U₂₃ = R₂₃×I = {rp}×{fr(i, 3)} = {fr(u23)} V",
            "Réduire le parallèle, puis le série ; loi d'Ohm à chaque étape.")


@reg("PC", "Puissance et énergie électriques", 1)
def _en_intensite():
    p = random.choice((60, 100, 750, 1000, 1500, 2000))
    u = random.choice((12, 230))
    return (f"Un appareil « {u} V - {p} W » : intensité absorbée ?",
            f"I = P/U = {p}/{u} = {fr(p / u, 3)} A",
            "I = P/U → détermine le fusible.")


@reg("PC", "Puissance et énergie électriques", 2)
def _en_cout():
    p = random.choice((60, 100, 500, 1000, 1500, 2000, 2500))
    h = random.choice((1, 1.5, 2, 3, 4, 5))
    jours = random.choice((20, 30))
    prix = random.choice((1.1, 1.15, 1.2, 1.25, 1.3))
    e = p / 1000 * h * jours
    cout = e * prix
    return (f"Un appareil de {p} W fonctionne {fr(h)} h/jour pendant {jours} jours. "
            f"Énergie (kWh) puis coût à {fr(prix)} DH/kWh.",
            f"E = P×t = {fr(p / 1000)} kW × {fr(h)} h × {jours} = {fr(e)} kWh\n"
            f"Coût = {fr(e)} × {fr(prix)} = {fr(cout)} DH",
            "P en kW × t en h → kWh ; puis × prix.")


@reg("PC", "Puissance et énergie électriques", 2)
def _en_joules():
    kwh = random.choice((0.5, 0.75, 2.5, 5.5, 12))
    return (f"Convertir {fr(kwh)} kWh en joules.",
            f"E = {fr(kwh)} × 3,6×10⁶ = {fr(kwh * 3.6, 2)} × 10⁶ J",
            "1 kWh = 3,6 × 10⁶ J.")


@reg("PC", "Principe des actions réciproques", 1)
def _me_poids():
    m = random.choice((0.2, 0.43, 0.5, 1.5, 2.5, 75))
    return (f"Calculer le poids d'un objet de masse m = {fr(m)} kg (g = 9,8 N/kg).",
            f"P = m×g = {fr(m)} × 9,8 = {fr(m * 9.8)} N",
            "m en KILOGRAMMES ; P en newtons.")


@reg("PC", "Le principe d'inertie et l'équilibre", 2)
def _me_tension():
    m = random.choice((0.8, 2, 5, 8, 12))
    return (f"Un objet de masse {fr(m)} kg est suspendu immobile à un câble. Tension du câble ? Justifier.",
            f"Immobile → équilibre → forces compensées\nT = P = m×g = {fr(m)} × 9,8 = {fr(m * 9.8)} N "
            "(verticale, vers le haut)",
            "2 forces en équilibre : même norme, sens opposés.")


@reg("PC", "Principe des actions réciproques", 3)
def _me_reciproque():
    m = random.choice((0.15, 0.2, 0.3))
    p = m * 9.8
    return (f"Une pomme ({fr(m)} kg) tombe : la Terre l'attire avec {fr(p)} N. Décrire la force "
            "réciproque et expliquer pourquoi c'est la pomme qui « tombe ».",
            f"Actions réciproques : la pomme attire la Terre avec {fr(p)} N (verticale, vers le haut, "
            "appliquée au centre de la Terre).\nMême intensité, mais a = F/m : a(Terre) ≈ 0 "
            "(masse ~6×10²⁴ kg) ; a(pomme) = 9,8 m/s² → seule la pomme bouge visiblement.",
            "Même FORCE sur les deux corps ; accélérations différentes (F = m·a).")


# ------------------------------------------------------------------ moteur --
def generer(code, titre, difficulte=None):
    """Retourne un exercice inédit : dict(enonce, solution, astuce, chapitre, difficulte)."""
    themes = GEN.get(code)
    if not themes:
        return None
    if titre not in themes:
        titre = random.choice(list(themes))
    par_dif = themes[titre]
    if difficulte in (1, 2, 3, "1", "2", "3"):
        d = int(difficulte)
        fns = par_dif.get(d) or [f for lst in par_dif.values() for f in lst]
    else:
        d = random.choice(list(par_dif))
        fns = par_dif[d]
    en, sol, ast = random.choice(fns)()
    return {"enonce": en, "solution": sol, "astuce": ast, "chapitre": titre,
            "difficulte": d}


def themes_disponibles():
    """{code: [titres]} dans l'ordre du dictionnaire."""
    return {code: list(themes) for code, themes in GEN.items()}


# ---- compléments PC : chapitres manquants du programme ----
MELANGES = {"l'eau distillée": "corps pur composé (H₂O seul, mais 2 éléments liés)",
            "le fer": "corps pur simple (1 seul élément)",
            "le dioxygène O₂": "corps pur simple",
            "le dioxyde de carbone CO₂": "corps pur composé",
            "l'air": "mélange homogène (une seule phase)",
            "l'eau sucrée": "mélange homogène (solution)",
            "l'eau salée": "mélange homogène (solution)",
            "l'eau de mer": "mélange homogène (solution)",
            "l'eau + huile": "mélange hétérogène (2 phases)",
            "le sable + eau": "mélange hétérogène (dépôt visible)"}


@reg("PC", "Les mélanges et la pureté", 1)
def _mel_classer():
    items = random.sample(sorted(MELANGES), 4)
    lignes = "\n".join(f"• {it} → {MELANGES[it]}" for it in items)
    return ("Classer chacun de ces échantillons : corps pur simple, corps pur composé, "
            "mélange homogène ou mélange hétérogène :\n" + "\n".join(f"• {it}" for it in items),
            lignes,
            "1 élément = pur simple ; plusieurs liés = pur composé ; une seule phase = homogène.")


SEPARE = [("une eau trouble contenant du sable", "FILTRATION (solide insoluble retenu)",
           "solide insoluble + liquide"),
          ("de l'eau salée dont on veut récupérer le sel", "ÉVAPORATION ou CRISTALLISATION",
           "le solide est DISSOUS : il passe au filtre !"),
          ("un mélange d'eau et d'huile", "DÉCANTATION (entonnoir / ampoule)",
           "2 liquides NON MISCIBLES"),
          ("un mélange d'alcool et d'eau", "DISTILLATION (fractionnée)",
           "2 liquides MISCIBLES de températures d'ébullition différentes"),
          ("une encre noire à analyser", "CHROMATOGRAPHIE",
           "espèces colorées qui migrent différemment")]


@reg("PC", "Les mélanges et la pureté", 2)
def _mel_separation():
    sit, tech, regle = random.choice(SEPARE)
    return (f"Quelle technique de séparation choisir pour {sit} ? Justifier.",
            f"→ {tech}\nRègle : {regle}.",
            "Solide insoluble → filtre ; dissous → évaporation ; non miscibles → décantation ; "
            "miscibles → distillation ; couleurs → chromatographie.")


@reg("PC", "Les mélanges et la pureté", (2, 3))
def _mel_solubilite():
    m, v = random.choice(((36, 100), (80, 200), (18, 50), (90, 300), (45, 150)))
    s = m * 1000 // v
    return (f"On dissout {m} g de sel dans {v} mL d'eau, jusqu'à saturation exacte. "
            "Calculer la solubilité du sel en g/L.",
            f"V = {v} mL = {fmt(F(v, 1000))} L\n"
            f"S = {m} g ÷ {fmt(F(v, 1000))} = {s} g/L\n"
            "(à cette concentration, la solution est SATURÉE : plus rien ne se dissout)",
            "Convertir mL → L puis diviser ; vérifier l'ordre de grandeur (des centaines de g/L).")


@reg("PC", "Les mélanges et la pureté", 3)
def _mel_chromato():
    enc, t1, t2 = random.choice((("une encre verte", "bleue", "jaune"),
                                 ("une encre noire", "bleue", "rouge"),
                                 ("une encre brune", "rouge", "jaune")))
    return (f"À la chromatographie, {enc} donne 2 taches : {t1} et {t2}. Conclure sur la pureté "
            "de l'encre.",
            f"2 taches → 2 espèces colorées migrées\n"
            f"→ {enc} est un MÉLANGE de 2 pigments (pas un corps pur).\n"
            "Le nombre de taches = le nombre d'espèces.",
            "Corps pur = UNE seule tache.")


INERIES = (("une voiture roule sur l'autoroute en ligne droite à 110 km/h constante",
            "Mouvement rectiligne UNIFORME → principe d'inertie → ΣF = 0\n"
            "Le moteur compense exactement frottements + résistance de l'air."),
           ("un palet de hockey glisse sur une glace horizontale à vitesse constante "
            "(frottements négligeables)",
            "Poids P et réaction R de la glace se compensent (2 forces : même direction, "
            "même norme, sens opposés) → ΣF = 0 → mouvement rectiligne uniforme ✓"),
           ("un ascenseur monte en ligne droite à vitesse constante",
            "Vitesse constante → forces compensées : la tension des câbles compense exactement "
            "le poids de la cabine (T = P)"))


@reg("PC", "Le principe d'inertie et l'équilibre", (1, 2))
def _me_inertie():
    sit, rep = random.choice(INERIES)
    return (f"{sit[0].upper()}{sit[1:]}. Que peut-on affirmer sur la somme des forces ?",
            rep, "Vitesse CONSTANTE (ou immobile) ⟺ forces qui se COMPENSENT (ΣF = 0).")


@reg("PC", "Le principe d'inertie et l'équilibre", 3)
def _me_equilibre3():
    m = random.choice((2, 3, 5, 8))
    p = m * 9.8
    return (f"Un lustre de masse {fr(m)} kg est suspendu par DEUX câbles identiques et verticaux. "
            "Que vaut la tension de chaque câble ? Et si les câbles étaient inclinés ?",
            f"Poids : P = m×g = {fr(m)} × 9,8 = {fr(p)} N\n"
            f"Équilibre → T₁ + T₂ compense P → T₁ = T₂ = P/2 = {fr(p / 2)} N (câbles verticaux)\n"
            "Si les câbles sont INCLINÉS : chaque tension est PLUS GRANDE que P/2 "
            "(seules les composantes verticales portent le lustre).",
            "3 forces en équilibre : triangle des forces fermé.")


@reg("PC", "Principe des actions réciproques", 2)
def _me_dynamometre():
    m = random.choice((0.2, 0.5, 1.0, 2.0))
    p = m * 9.8
    return (f"Un objet de masse {fr(m)} kg est suspendu à un dynamomètre, immobile. "
            "Quelle est la mesure affichée ? Décrire la force mesurée.",
            f"Immobile → équilibre → la tension du ressort compense le poids\n"
            f"T = P = m×g = {fr(m)} × 9,8 = {fr(p)} N\n"
            "Caractéristiques : point d'application = crochet ; direction verticale ; "
            "sens vers le haut ; intensité " + fr(p) + " N",
            "Le dynamomètre mesure la tension qui compense le poids.")


import gen_svt_fr  # noqa: E402  (enregistre les générateurs SVT et Français)


# ---- compléments PC 2026 : gravitation universelle + synthèse chimique ----
PLANETES = {"Terre": 9.8, "Lune": 1.6, "Mars": 3.7, "Jupiter": 24.8}


@reg("PC", "La gravitation universelle", 1)
def _pc_poids_planete():
    astre, g = random.choice(list(PLANETES.items()))
    m = random.choice((2, 5, 10, 25, 60, 80))
    p = m * g
    aff = f"{fmt(F(int(p * 10), 10))} N"
    return (f"Calculer le poids d'un objet de masse m = {m} kg sur {astre} "
            f"(g = {str(g).replace('.', ',')} N/kg).",
            f"P = m×g = {m} × {str(g).replace('.', ',')} = {aff}\n"
            "(sa MASSE reste " + f"{m} kg : elle ne dépend pas de l'astre)",
            "P = m × g ; la masse ne change jamais, le poids oui.")


@reg("PC", "La gravitation universelle", 2)
def _pc_force_grav():
    m1 = random.choice((2, 5, 10))
    m2 = random.choice((10, 20, 50, 100))
    d = random.choice((1, 2, 5))
    num = m1 * m2 / (d * d)
    f = num * 6.67
    aff = f"{f:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " × 10⁻¹⁰ N"
    return (f"Deux sphères de masses m₁ = {m1} kg et m₂ = {m2} kg ont leurs centres "
            f"distants de d = {d} m. Calculer la force d'attraction "
            "(G = 6,67 × 10⁻¹¹ SI).",
            f"F = G × (m₁×m₂)/d² = 6,67×10⁻¹¹ × ({m1}×{m2})/{d}²\n"
            f"= 6,67×10⁻¹¹ × {fmt(F(int(num*100), 100))} ≈ {aff}\n"
            "Les deux corps s'attirent avec la MÊME valeur (actions réciproques).",
            "Masses au numérateur, distance AU CARRÉ au dénominateur.")


@reg("PC", "La gravitation universelle", 3)
def _pc_orbite():
    return ("① Expliquer pourquoi un satellite « flotte » autour de la Terre. "
            "② Si on double la distance entre deux astres, que devient la force "
            "d'attraction ? ③ Un astronaute de 70 kg : sa masse et son poids varient-ils "
            "sur la Lune ?",
            "① Il est en CHUTE LIBRE permanente : la gravitation l'attire, mais sa "
            "vitesse le fait « tomber à côté » de la Terre → orbite (la gravité existe "
            "encore en orbite !).\n"
            "② F est divisée par 4 : d passe au carré (2d)² = 4d² au dénominateur.\n"
            "③ Masse : inchangée (70 kg) ; poids : divisé par 6 (g_Lune ≈ 1,6 N/kg) "
            "≈ 117 N au lieu de 686 N.",
            "Orbite = chute perpétuelle ; F ∝ 1/d² ; masse invariante.")


@reg("PC", "La synthèse des espèces chimiques", 1)
def _pc_rendement_basique():
    m_obt = random.choice((6, 8, 9, 12, 15))
    m_the = random.choice((m_obt * 2, m_obt + m_obt // 2, int(m_obt * 4 / 3)))
    r = F(m_obt * 100, m_the)
    return (f"Lors d'une synthèse, la masse théorique attendue est {m_the} g ; on "
            f"recueille {m_obt} g de produit. Calculer le rendement.",
            f"Rendement = masse obtenue ÷ masse théorique × 100\n"
            f"= {m_obt} ÷ {m_the} × 100 = {fmt(r)} %",
            "Le rendement est toujours ≤ 100 %.")


@reg("PC", "La synthèse des espèces chimiques", (2, 3))
def _pc_synthese_complete():
    M = random.choice((138, 180, 60, 92))
    n_mg = random.choice((25, 50, 75, 100))
    n = F(n_mg, 1000)
    m_the = n * M
    r = random.choice((70, 75, 80, 90))
    m_obt = m_the * r / 100

    def g2(x):
        return f"{float(x):.3f}".rstrip("0").rstrip(".").replace(".", ",")
    return (f"On synthétise une espèce chimique (M = {M} g/mol) à partir de "
            f"{n_mg} mg de réactif limitant. ① Calculer la quantité de matière n. "
            f"② Masse théorique de produit ? ③ Le rendement réel est de {r} % : masse "
            "effectivement obtenue ?",
            f"① n = m/M = {n_mg}×10⁻³ ÷ {M} = {g2(n * 1000)}×10⁻³ mol = "
            f"{g2(n * 1000)} mmol\n"
            f"② m_théorique = n × M = {g2(m_the)} g\n"
            f"③ m_obtenue = {g2(m_the)} × {r}/100 = {g2(m_obt)} g",
            "n = m/M ; rendement = obtenu/théorique × 100.")

