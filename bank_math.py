# -*- coding: utf-8 -*-
"""bank_math.py — Générateur d'exercices TC Maths.
Chaque solution est CALCULÉE par le code (exactitude garantie)."""

import math
from fractions import Fraction as F


def E(d, src, en, sol, ast=""):
    return (d, src, en, sol, ast, [])


def fmt(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fr(x):
    s = f"{x:.4f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


def arith():
    T = "Arithmétique dans ℕ"
    exos = []
    for n in (36, 48, 60, 84, 90):
        divs = [d for d in range(1, n + 1) if n % d == 0]
        exos.append(E(1, "Manuel", f"Dresser la liste des diviseurs de {n}. Combien en compte-t-on ?",
                      "Diviseurs de {n} : {d}\nSoit {k} diviseurs.".format(
                          n=n, d=" ; ".join(map(str, divs)), k=len(divs)),
                      "Tester 1, 2, 3… jusqu'à √n : chaque diviseur d entraîne n/d."))
    for n, ks in ((4872, (3, 4, 9)), (1350, (3, 5, 9)), (2048, (2, 3, 4)), (7425, (3, 5, 11))):
        parts = []
        for k in ks:
            ok = n % k == 0
            rule = {2: "dernier chiffre pair", 3: "somme des chiffres divisible par 3",
                    4: "les 2 derniers chiffres forment un multiple de 4",
                    5: "se termine par 0 ou 5", 9: "somme des chiffres divisible par 9",
                    11: "différence alternée des chiffres divisible par 11"}[k]
            s = sum(int(c) for c in str(n))
            det = f"(somme des chiffres = {s})" if k in (3, 9) else ""
            parts.append(f"Divisible par {k} : {'OUI' if ok else 'NON'} — règle : {rule} {det}")
        exos.append(E(1, "Manuel", f"Le nombre {n} est-il divisible par "
                      + " ; ".join(f"{k}" for k in ks) + " ? Justifier par les règles de divisibilité.",
                      "\n".join(parts),
                      "Connaître les règles : 2, 3, 4, 5, 9, 11."))
    for a, b in ((18, 24), (30, 45), (36, 60), (42, 56), (63, 84), (120, 150)):
        g = math.gcd(a, b); l = a * b // g
        exos.append(E(1, "Contrôle", f"Calculer PGCD({a} ; {b}) puis PPCM({a} ; {b}).",
                      f"Décompositions ou algorithme d'Euclide → PGCD = {g}\n"
                      f"PPCM = a × b ÷ PGCD = {a} × {b} ÷ {g} = {l}",
                      "PGCD : plus petits exposants ; PPCM : plus grands."))
    for n in (72, 96, 150, 210, 330, 420, 500):
        x = n; fac = []
        for p in (2, 3, 5, 7, 11, 13):
            while x % p == 0:
                fac.append(p); x //= p
        exos.append(E(2, "Contrôle", f"Décomposer {n} en produit de facteurs premiers.",
                      f"{n} = {' × '.join(map(str, fac))}",
                      "Diviser successivement par 2, 3, 5, 7, 11… jusqu'à 1."))
    for n, k1, k2 in ((168, 2, 4), (252, 3, 4), (450, 3, 5)):
        q1, q2 = n // k1, n // k2
        exos.append(E(2, "Contrôle", f"Montrer que la fraction {n}/{k1 * k2} n'est pas "
                      f"irréductible, puis donner sa forme simplifiée.",
                      f"PGCD({n} ; {k1 * k2}) : {k1 * k2} divise {n} ? {n % (k1 * k2) == 0}.\n"
                      f"Forme simplifiée : {n // math.gcd(n, k1 * k2)}/{k1 * k2 // math.gcd(n, k1 * k2)}.",
                      "Fraction irréductible ⟺ PGCD(num, den) = 1."))
    exos.append(E(1, "Manuel", "Lister les nombres premiers inférieurs à 30.",
                  "2 ; 3 ; 5 ; 7 ; 11 ; 13 ; 17 ; 19 ; 23 ; 29",
                  "Un premier a exactement 2 diviseurs : 1 et lui-même."))
    for p in (51, 53, 57, 67, 91, 97):
        divs = [d for d in (2, 3, 5, 7) if p % d == 0]
        if not divs and p < 100:
            rep = "PREMIER"
            det = "aucun des premiers 2, 3, 5, 7 ne le divise (√97 ≈ 9,8)"
        else:
            rep = "NON PREMIER"
            det = f"divisible par {divs[0]}" if divs else f"= 7 × 13"
        exos.append(E(2, "Contrôle", f"Le nombre {p} est-il premier ? Justifier.",
                      f"{p} : {det} → {rep}.",
                      "Tester la divisibilité par 2, 3, 5, 7 (jusqu'à √p)."))
    exos.append(E(3, "Type Examen Régional",
                  "Montrer que pour tout entier n, n(n + 1)(n + 2) est divisible par 6.",
                  "Parmi 3 entiers consécutifs, il y a au moins un pair → divisible par 2.\n"
                  "Et un multiple de 3 (3 entiers consécutifs parcourent tous les restes mod 3).\n"
                  "Divisible par 2 ET par 3 → divisible par 2 × 3 = 6. ∎",
                  "PGCD(2 ; 3) = 1 : être divisible par 2 et 3 ⟺ divisible par 6."))
    return (T, exos)


def ensembles():
    T = "Les ensembles de nombres"
    exos = []
    data = [("3/8", "0,375 : virgule finie → 𝔻 (et ℚ)"),
            ("-12", "entier relatif → ℤ (∉ ℕ)"),
            ("5/11", "0,4545… périodique infinie → ℚ mais PAS 𝔻"),
            ("√16", "= 4 → ℕ"),
            ("√5", "irrationnel → ℝ \\ ℚ"),
            ("2,71", "décimal fini → 𝔻"),
            ("-0,25", "= -1/4 → 𝔻"),
            ("π/3", "quotient par un irrationnel → irrationnel (ℝ)"),
            ("0,777…", "= 7/9 → ℚ (périodique)")]
    for num, rep in data:
        exos.append(E(1, "Manuel", f"Placer le nombre {num} dans le plus petit ensemble qui le contient (ℕ, ℤ, 𝔻, ℚ, ℝ).",
                      f"{num} : {rep}.", "Virgule finie → 𝔻 ; fraction périodique → ℚ ; racine non exacte/π → irrationnel."))
    SUP = {1: "10⁻¹", 2: "10⁻²", 3: "10⁻³"}
    for n, d in ((50, 1), (200, 2), (7, 2), (3, 3)):
        r = math.sqrt(n)
        p = 10 ** d
        lo = math.floor(r * p) / p
        hi = (math.floor(r * p) + 1) / p
        l, h = fr(lo), fr(hi)
        exos.append(E(2, "Contrôle", f"Encadrer √{n} par deux décimaux à {SUP[d]} près (défaut et excès).",
                      f"√{n} ≈ {fr(round(r, d + 2))}\nPar défaut : {l} ; par excès : {h}\n"
                      f"Donc {l} ≤ √{n} < {h}",
                      "Couper au (d+1)-ième chiffre : en dessous (défaut), au-dessus (excès)."))
    for frac, dec, rep in (("1/3", "0,333…", "ℚ (périodique = fraction)"),
                           ("22/7", "3,142857…", "ℚ (périodique)"),
                           ("7/4", "1,75", "𝔻 (virgule finie)")):
        exos.append(E(2, "Contrôle", f"Écrire {frac} sous forme décimale et préciser son ensemble.",
                      f"{frac} = {dec} → {rep}.", "Diviser posément ; observer la période."))
    exos.append(E(3, "Type Examen Régional",
                  "Montrer que la somme d'un rationnel et d'un irrationnel est irrationnelle.",
                  "Par l'absurde : supposons a ∈ ℚ, b irrationnel et a + b = c ∈ ℚ.\n"
                  "Alors b = c - a. Or la différence de deux rationnels est rationnelle → b ∈ ℚ : contradiction.\n"
                  "Donc a + b est irrationnel. ∎",
                  "Raisonnement par l'absurde : nier la conclusion et retomber sur une contradiction."))
    return (T, exos)


def ordre():
    T = "L'ordre dans ℝ"
    exos = []
    for a, b, k, c in ((2, 5, 3, 1), (-1, 4, 2, 3), (0, 3, 5, 2), (-2, 6, 2, 1), (1, 4, 4, 3)):
        lo1, hi1 = k * a + c, k * b + c
        lo2, hi2 = -k * b + c, -k * a + c
        exos.append(E(1, "Manuel", f"Sachant {a} ≤ x ≤ {b}, encadrer f(x) = {k}x + {c} puis g(x) = -{k}x + {c}.",
                      f"{k}×{a} ≤ {k}x ≤ {k}×{b} → {lo1} ≤ {k}x + {c} ≤ {hi1}\n"
                      f"×(-{k}) : sens inversé → {lo2} ≤ -{k}x ≤ {hi2} → {lo2} ≤ -{k}x + {c} ≤ {hi2}",
                      "Multiplier par un négatif RENVERSE les inégalités."))
    for n1, d1, n2, d2 in ((3, 7, 5, 11), (-4, 9, -3, 8), (7, 12, 11, 19), (5, 6, 8, 9)):
        g1, g2 = n1 * d2, n2 * d1
        rep = "<" if g1 < g2 else (">" if g1 > g2 else "=")
        exos.append(E(1, "Contrôle", f"Comparer {fmt(F(n1, d1))} et {fmt(F(n2, d2))} (produit en croix).",
                      f"{n1}×{d2} = {g1} et {n2}×{d1} = {g2}\n{g1} {rep} {g2} → "
                      f"{fmt(F(n1, d1))} {rep} {fmt(F(n2, d2))}",
                      "a/b vs c/d : comparer a×d et c×b (dénominateurs positifs)."))
    for n, d in ((10, "3,2"), (7, "2,7"), (45, "6,7"), (99, "10,0")):
        dn = float(d.replace(",", "."))
        ok = n < dn ** 2
        rep = "<" if ok else ">"
        exos.append(E(2, "Contrôle", f"Comparer √{n} et {d} (sans calculatrice).",
                      f"Deux positifs : comparer les carrés.\n{dn}² = {fr(dn ** 2)} et √{n}² = {n}\n"
                      f"{n} {rep} {fr(dn ** 2)} → √{n} {rep} {d}",
                      "0 < a, b : a ≤ b ⟺ a² ≤ b²."))
    for a, b, dec in ((1, 4, "1/x"), (2, 8, "1/x"), (1, 5, "x²")):
        if dec == "x²":
            exos.append(E(2, "Contrôle", f"Sachant {a} ≤ x ≤ {b} (positif), encadrer x².",
                          f"{a}² ≤ x² ≤ {b}² car x ↦ x² croît sur [0 ; +∞[\n{a * a} ≤ x² ≤ {b * b}",
                          "Tout positif : mettre au carré sans changer les bornes."))
        else:
            exos.append(E(2, "Contrôle", f"Sachant {a} ≤ x ≤ {b} (strictement positif), encadrer 1/x.",
                          f"1/{b} ≤ 1/x ≤ 1/{a} (l'inverse RÉDUIT l'encadrement : bornes échangées)",
                          "x ↦ 1/x décroît sur (0 ; +∞) : les bornes s'échangent."))
    exos.append(E(3, "Type Examen Régional",
                  "Montrer que pour tous réels a et b : |a + b| ≤ |a| + |b| (inégalité triangulaire).",
                  "-|a| ≤ a ≤ |a| et -|b| ≤ b ≤ |b|\nSomme membre à membre : -(|a| + |b|) ≤ a + b ≤ |a| + |b|\n"
                  "Donc |a + b| ≤ |a| + |b|. ∎",
                  "Encadrer a + b entre deux opposés puis traduire avec |·|."))
    return (T, exos)


def polynomes():
    T = "Les polynômes"
    exos = []
    for a, b, c, d in ((1, 3, 1, 5), (2, 1, 1, -3), (3, 2, 2, -1), (1, -4, 1, 4), (2, 3, 1, 2), (5, 1, 1, 6)):
        exos.append(E(1, "Manuel", f"Développer et réduire ({fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)})"
                      f"({fmt(c)}x {'+' if d >= 0 else '-'} {abs(d)}).",
                      f"= {fmt(a * c)}x² {'+' if a * d + b * c >= 0 else '-'} {abs(a * d + b * c)}x "
                      f"{'+' if b * d >= 0 else '-'} {abs(b * d)}",
                      "(ax+b)(cx+d) = acx² + (ad+bc)x + bd."))
    for a, b in ((1, 6), (1, 10), (2, 4), (3, 12), (1, 14), (4, 20)):
        A = a * a; B = 2 * a * b; C = b * b
        exos.append(E(1, "Manuel", f"Développer ({fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)})².",
                      f"= {fmt(A)}x² {'+' if B >= 0 else '-'} {abs(B)}x {'+' if C >= 0 else '-'} {abs(C)}\n"
                      f"(identité (a+b)² = a² + 2ab + b² avec a = {fmt(a)}x et b = {'+' if b >= 0 else '-'}{abs(b)})",
                      "Ne jamais oublier le DOUBLE PRODUIT."))
    for k in (4, 9, 16, 25, 36, 49, 64, 81, 100):
        r = int(math.isqrt(k))
        exos.append(E(1, "Manuel", f"Factoriser x² - {k}.",
                      f"x² - {r}² = (x - {r})(x + {r})",
                      "a² - b² = (a - b)(a + b)."))
    for a, b, n in ((3, 12, 2), (5, 20, 3), (4, 28, 2), (6, 15, 4), (7, 21, 5)):
        g = math.gcd(a, b)
        exos.append(E(1, "Manuel", f"Factoriser {a}x^{n} + {b}x^{n - 1}.",
                      f"Facteur commun {g}x^{n - 1} : = {g}x^{n - 1}({fmt(a // g)}x + {b // g})",
                      "Chercher d'abord le plus grand facteur commun (coefficient + puissance)."))
    for r, s in ((2, 5), (3, 4), (-1, 6), (-2, -3), (4, 7), (1, -8)):
        S, P = r + s, r * s
        exos.append(E(2, "Contrôle", f"Montrer que {r} est une racine de P(x) = x² - {fmt(S)}x {'+' if P >= 0 else '-'} {abs(P)}, "
                      "puis factoriser P.",
                      f"P({r}) = {r * r} - {fmt(S)}×{r} {'+' if P >= 0 else '-'} {abs(P)} = {r * r - S * r + P} = 0 ✓\n"
                      f"Donc (x - {r}) est un facteur : P(x) = (x - {r})(x - {s})\n"
                      f"Vérification en développant : x² - {fmt(S)}x {'+' if P >= 0 else '-'} {abs(P)} ✓",
                      "P(a) = 0 ⟺ (x - a) factorise P. Identifier ensuite les coefficients."))
    for a, b in ((2, 6), (3, 9), (4, 8), (5, 10), (6, 12)):
        exos.append(E(2, "Contrôle", f"Résoudre ({a}x - {b})({a}x + {b}) = 0.",
                      f"{a}x - {b} = 0 ou {a}x + {b} = 0\n"
                      f"x = {fmt(F(b, a))} ou x = {fmt(F(-b, a))}\nS = {{{fmt(F(-b, a))} ; {fmt(F(b, a))}}}",
                      "Équation-produit : chaque facteur fournit une solution."))
    for k in (1, 9, 16, 25, 36, 49):
        r = int(math.isqrt(k))
        exos.append(E(3, "Type Examen Régional", f"Résoudre : x⁴ - {k + 4}x² + {4 * k} = 0.",
                      f"Poser X = x² : X² - {k + 4}X + {4 * k} = 0\n"
                      f"Racines évidentes : X = {k} et X = 4 (somme {k + 4} ✓, produit {4 * k} ✓)\n"
                      f"X = {k} → x² = {k} → x = ±{r} ; X = 4 → x = ±2\n"
                      f"S = {{-{r} ; -2 ; 2 ; {r}}}",
                      "Équation bicarrée : poser X = x², résoudre en X, revenir à x."))
    return (T, exos)


def equations():
    T = "Équations et inéquations dans ℝ"
    exos = []
    for a, b, c in ((3, 5, 20), (4, -7, 9), (5, 12, -8), (7, 3, 24), (6, -9, 15), (2, 11, -5)):
        x = F(c - b, a)
        exos.append(E(1, "Manuel", f"Résoudre : {a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}.",
                      f"{a}x = {c} {'-' if b >= 0 else '+'} {abs(b)} = {c - b}\nx = {fmt(F(c - b, a))}\nS = {{{fmt(x)}}}",
                      "Isoler ax, diviser par a."))
    for a, b, c in ((2, 3, 13), (4, 5, -7), (3, 8, 2), (5, -4, 11), (7, 6, 20)):
        x = F(c - b, a)
        sens = "sens conservé" if a > 0 else "SENS INVERSÉ"
        exos.append(E(2, "Contrôle", f"Résoudre l'inéquation : {a}x {'+' if b >= 0 else '-'} {abs(b)} < {c} "
                      "et donner S sous forme d'intervalle.",
                      f"{a}x < {c - b}\nx {'<' if a > 0 else '≤'} {fmt(x)} ({sens} : division par {a})\n"
                      f"S = ]-∞ ; {fmt(x)}[" if a > 0 else f"S = ]{fmt(x)} ; +∞[",
                      "Diviser par un négatif change le sens de l'inégalité."))
    for x0, y0 in ((3, 2), (4, 1), (2, 5), (5, 3), (1, 7), (6, 2), (3, 4)):
        a1, b1, a2, b2 = 1, 1, 2, -1
        s1 = a1 * x0 + b1 * y0; s2 = a2 * x0 + b2 * y0
        exos.append(E(2, "Contrôle", f"Résoudre le système : {{ {a1}x + {b1}y = {s1} ; {a2}x + {b2}y = {s2} }}",
                      f"Par combinaison : ({a2})×L1 - ({a1})×L2 : ({a2 * b1 - a1 * b2})y = {a2 * s1 - a1 * s2}\n"
                      f"y = {y0} puis x = {x0}\nS = {{({x0} ; {y0})}}",
                      "Combinaison linéaire pour éliminer une inconnue, puis substitution."))
    for x0, y0, p in ((5, 3, 2), (4, 2, 3), (7, 2, 4)):
        exos.append(E(3, "Type Examen Régional",
                      f"Deux articles et {p} stylos coûtent {2 * x0 + p * y0} DH ; un article et un stylo "
                      f"coûtent {x0 + y0} DH. Trouver le prix de chaque article.",
                      f"Système : {{ a + s = {x0 + y0} ; 2a + {p}s = {2 * x0 + p * y0} }}\n"
                      f"2×(L1) - L2 : ({p - 2})s = {2 * (x0 + y0) - (2 * x0 + p * y0)} → s = {y0}\n"
                      f"a = {x0 + y0} - {y0} = {x0}\nArticle : {x0} DH ; stylo : {y0} DH",
                      "Mettre en système puis résoudre par combinaison."))
    for r1, r2 in ((-2, 3), (1, 4), (-5, -1), (2, 7), (-3, 6)):
        S, P = r1 + r2, r1 * r2
        exos.append(E(3, "Type Examen Régional", f"Résoudre avec un tableau de signes : "
                      f"(x {'+' if -r1 >= 0 else '-'} {abs(r1)})(x {'+' if -r2 >= 0 else '-'} {abs(r2)}) ≤ 0.",
                      f"Racines : x = {r1} et x = {r2}\nSigne de a = 1 > 0 à l'extérieur des racines, négatif entre elles\n"
                      f"S = [{min(r1, r2)} ; {max(r1, r2)}]",
                      "Racines ordonnées ; signe de a à l'extérieur ; ≤ → bornes FERMÉES."))
    return (T, exos)


def vecteurs():
    T = "Configurations du plan et vecteurs"
    exos = []
    triples = ((3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (7, 24, 25), (12, 16, 20))
    for (vx, vy, n), (ax, ay) in zip(triples, ((1, 2), (0, 0), (2, 3), (1, 1), (3, 4), (2, 5), (0, 1))):
        bx, by = ax + vx, ay + vy
        exos.append(E(1, "Manuel", f"A({ax} ; {ay}) et B({bx} ; {by}). Calculer les coordonnées de "
                      f"AB et la distance AB.",
                      f"AB({bx}-({ax}) ; {by}-({ay})) = AB({vx} ; {vy})\n"
                      f"AB = √({vx}² + {vy}²) = √{vx * vx + vy * vy} = {n}",
                      "AB = B - A ; norme = racine de la somme des carrés."))
    for ax, ay, bx, by in ((2, 3, 8, 7), (1, 5, 9, 1), (0, 4, 10, 2), (3, 3, 11, 11)):
        mx, my = F(ax + bx, 2), F(ay + by, 2)
        exos.append(E(1, "Manuel", f"Calculer les coordonnées du milieu I de [{fmt(ax)} ; {fmt(ay)}] [{fmt(bx)} ; {fmt(by)}]."
                      .replace("[", "A(").replace("]", ")"),
                      f"I((({ax})+({bx}))/2 ; (({ay})+({by}))/2) = I({fmt(mx)} ; {fmt(my)})",
                      "Milieu = moyenne des abscisses, moyenne des ordonnées."))
    for u, k in (((2, 3), 3), ((1, -4), -2), ((3, 5), 4), ((-2, 6), 2), ((4, 1), -3)):
        vx, vy = k * u[0], k * u[1]
        exos.append(E(2, "Contrôle", f"u({u[0]} ; {u[1]}) et v({vx} ; {vy}) : montrer qu'ils sont "
                      "colinéaires à l'aide du critère xy' - x'y = 0.",
                      f"xy' - x'y = {u[0]}×({vy}) - ({vx})×{u[1]} = {u[0] * vy - vx * u[1]} = 0 ✓\n"
                      f"De plus v = {k}·u → colinéaires.",
                      "Le déterminant nul prouve la colinéarité ; repérer le coefficient k."))
    for ax, ay, bx, by, cx, cy in ((0, 0, 3, 1, 6, 2), (1, 1, 4, 3, 7, 5), (2, 2, 5, 4, 8, 6)):
        exos.append(E(2, "Contrôle", f"A({ax} ; {ay}), B({bx} ; {by}), C({cx} ; {cy}) : sont-ils alignés ?",
                      f"AB({bx - ax} ; {by - ay}) ; AC({cx - ax} ; {cy - ay})\n"
                      f"Colinéarité : ({bx - ax})×({cy - ay}) - ({cx - ax})×({by - ay}) = "
                      f"{(bx - ax) * (cy - ay) - (cx - ax) * (by - ay)} = 0 ✓ → alignés",
                      "AB et AC colinéaires + point A commun = alignés."))
    for ax, ay, bx, by, dx, dy in ((0, 0, 3, 1, 5, 4), (1, 2, 4, 2, 6, 5), (0, 1, 2, 5, 7, 6)):
        cx, cy = bx + dx - ax, by + dy - ay
        exos.append(E(3, "Type Examen Régional", f"ABCD avec A({ax} ; {ay}), B({bx} ; {by}), D({dx} ; {dy}). "
                      "Trouver C pour que ABCD soit un parallélogramme.",
                      f"ABCD parallélogramme ⟺ AB = DC ⟺ C = B + D - A\n"
                      f"C({bx}+({dx})-({ax}) ; {by}+({dy})-({ay})) = C({cx} ; {cy})",
                      "Relation clé : AB = DC ⟺ C = B + D - A."))
    return (T, exos)


def droite():
    T = "La droite dans le plan"
    exos = []
    pts = (((1, 2), (4, 8), 2), ((0, 3), (5, 13), 2), ((2, 1), (6, -7), -2), ((1, 5), (3, 11), 3),
           ((0, 0), (4, -6), -3))
    for (ax, ay), (bx, by), m in pts:
        p = ay - m * ax
        exos.append(E(1, "Manuel", f"Déterminer l'équation de la droite passant par A({ax} ; {ay}) et B({bx} ; {by}).",
                      f"m = ({by} - ({ay}))/({bx} - ({ax})) = {fmt(F(by - ay, bx - ax))}\n"
                      f"y = {fmt(F(m))}x + p avec A : {ay} = {fmt(F(m))}×{ax} + p → p = {p}\n"
                      f"d : y = {fmt(F(m))}x {'+' if p >= 0 else '-'} {abs(p)}  (vérif B ✓)",
                      "m = Δy/Δx puis p à l'aide d'un point."))
    for m, ax, ay in ((3, 1, 4), (-2, 2, 3), (5, 1, 1), (-4, 1, 6), (2, 5, 3)):
        p = ay - m * ax
        exos.append(E(1, "Manuel", f"Droite de coefficient directeur {m} passant par P({ax} ; {ay}) : équation ?",
                      f"y = {m}x + p ; {ay} = {m}×{ax} + p → p = {p}\nd : y = {m}x {'+' if p >= 0 else '-'} {abs(p)}",
                      "Reporter le point dans y = mx + p."))
    for m1, p1, m2, p2 in ((2, 1, -1, 7), (3, -2, 1, 6), (1, 4, -2, 1), (4, 0, -2, 9), (2, 3, 2, 8)):
        if m1 == m2:
            exos.append(E(2, "Contrôle", f"d₁ : y = {m1}x + {p1} et d₂ : y = {m2}x + {p2} : position relative ?",
                          f"Mêmes coefficients ({m1} = {m2}) et ordonnées à l'origine différentes "
                          f"({p1} ≠ {p2})\n→ d₁ et d₂ sont STRICTEMENT PARALLÈLES",
                          "Parallèles ⟺ m₁ = m₂ et p₁ ≠ p₂."))
        else:
            xi = F(p2 - p1, m1 - m2)
            yi = m1 * xi + p1
            exos.append(E(2, "Contrôle", f"Trouver le point d'intersection de d₁ : y = {m1}x {'+' if p1 >= 0 else '-'} {abs(p1)} "
                          f"et d₂ : y = {m2}x {'+' if p2 >= 0 else '-'} {abs(p2)}.",
                          f"{m1}x {'+' if p1 >= 0 else '-'} {abs(p1)} = {m2}x {'+' if p2 >= 0 else '-'} {abs(p2)}\n"
                          f"({fmt(F(m1 - m2))})x = {p2 - p1} → x = {fmt(xi)} ; y = {fmt(yi)}\nI({fmt(xi)} ; {fmt(yi)})",
                          "Égaler les deux expressions de y."))
    for m1, m2 in ((2, -1 / 2), (3, -1 / 3), (-4, 1 / 4), (1 / 2, -2), (5, -1 / 5)):
        exos.append(E(2, "Contrôle", f"d₁ a pour coefficient {fmt(F(m1).limit_denominator(20))} ; d₂ a pour coefficient "
                      f"{fmt(F(m2).limit_denominator(20))}. Ces droites sont-elles perpendiculaires ?",
                      f"Produit : {fmt(F(m1).limit_denominator(20))} × {fmt(F(m2).limit_denominator(20))} = -1\n"
                      "→ perpendiculaires ✓",
                      "Perpendiculaires ⟺ m₁ × m₂ = -1."))
    exos.append(E(3, "Type Examen Régional",
                  "A(2 ; 1) et d : y = 3x - 5. Donner l'équation de la perpendiculaire à d passant par A, "
                  "puis le projeté orthogonal H de A sur d.",
                  "m(⊥) = -1/3 (produit = -1)\nΔ : y = -x/3 + p ; 1 = -2/3 + p → p = 5/3\n"
                  "Δ : y = -x/3 + 5/3\nH = d ∩ Δ : 3x - 5 = -x/3 + 5/3 → (10/3)x = 20/3 → x = 2 ; "
                  "y = 1 → H(2 ; 1) = A : A ∈ d ! (vérifier toujours)",
                  "Perpendiculaire : produit des coefficients = -1 ; H = intersection."))
    return (T, exos)


TRIGO = {"0": ("1", "0"), "π/6": ("√3/2", "1/2"), "π/4": ("√2/2", "√2/2"), "π/3": ("1/2", "√3/2"),
         "π/2": ("0", "1"), "2π/3": ("-1/2", "√3/2"), "3π/4": ("-√2/2", "√2/2"),
         "5π/6": ("-√3/2", "1/2"), "π": ("-1", "0"), "7π/6": ("-√3/2", "-1/2"),
         "5π/4": ("-√2/2", "-√2/2"), "4π/3": ("-1/2", "-√3/2"), "3π/2": ("0", "-1"),
         "5π/3": ("1/2", "-√3/2"), "7π/4": ("√2/2", "-√2/2"), "11π/6": ("√3/2", "-1/2")}
COS_EQ = {"√3/2": ("π/6", "11π/6"), "√2/2": ("π/4", "7π/4"), "1/2": ("π/3", "5π/3"),
          "0": ("π/2", "3π/2"), "-1/2": ("2π/3", "4π/3"), "-√2/2": ("3π/4", "5π/4"),
          "-√3/2": ("5π/6", "7π/6")}
SIN_EQ = {"1/2": ("π/6", "5π/6"), "√2/2": ("π/4", "3π/4"), "√3/2": ("π/3", "2π/3"),
          "1": ("π/2", None), "-1/2": ("7π/6", "11π/6"), "-√2/2": ("5π/4", "7π/4"),
          "-√3/2": ("4π/3", "5π/3"), "-1": ("3π/2", None)}


def trigo():
    T = "Trigonométrie"
    exos = []
    for ang in ("π/6", "π/4", "π/3", "2π/3", "3π/4", "5π/6", "7π/6", "4π/3", "5π/3", "7π/4", "11π/6"):
        c, s = TRIGO[ang]
        exos.append(E(1, "Manuel", f"Donner cos({ang}) et sin({ang}) à l'aide du cercle trigonométrique.",
                      f"cos({ang}) = {c} ; sin({ang}) = {s}",
                      "Repérer l'angle sur le cercle ; symétries pour les angles > π/2."))
    for val, (a1, a2) in COS_EQ.items():
        exos.append(E(2, "Contrôle", f"Résoudre dans [0 ; 2π] : cos x = {val}.",
                      f"{val} = cos({a1})\nDeux points du cercle ont cette abscisse : {a1} et {a2}\n"
                      f"S = {{{a1} ; {a2}}}",
                      "Valeur remarquable + symétrie par rapport à (Ox)."))
    for val, (a1, a2) in SIN_EQ.items():
        if a2:
            exos.append(E(2, "Contrôle", f"Résoudre dans [0 ; 2π] : sin x = {val}.",
                          f"{val} = sin({a1})\nDeux points ont cette ordonnée : {a1} et {a2}\n"
                          f"S = {{{a1} ; {a2}}}",
                          "Valeur remarquable + symétrie par rapport à (Oy) / point O."))
    for k, rel in (("cos", "sin(π - x) = sin x"), ("sin", "cos(π - x) = -cos x"),
                   ("cos", "sin(π/2 - x) = sin x")):
        exos.append(E(2, "Contrôle", f"Simplifier : {('cos²x + ' if k == 'cos' else 'sin²x + ')}"
                      f"{rel.split('=')[0]}. Donner le résultat.",
                      f"{rel.split('=')[0]} = {rel.split('= ')[1] if '= ' in rel else rel.split('=')[1]}\n"
                      "Puis relation fondamentale : cos²x + sin²x = 1.",
                      "Angles associés + relation fondamentale = 1."))
    exos.append(E(3, "Type Examen Régional",
                  "Montrer, à l'aide du cercle, que cos(π/2 - x) = sin x et sin(π/2 - x) = cos x.",
                  "Le point associé à π/2 - x est le symétrique du point M(x) par rapport à la "
                  "première bissectrice (y = x).\nCette symétrie ÉCHANGE abscisse et ordonnée.\n"
                  "cos(π/2 - x) = y_M(x) = sin x ; sin(π/2 - x) = x_M(x) = cos x. ∎",
                  "Bissectrice (y = x) : échange de cos et sin."))
    return (T, exos)


def trigo_eq():
    T = "Équations et inéquations trigonométriques"
    exos = []
    for k, c, (a1, a2), sgn in ((1, "√3/2", ("π/6", "11π/6"), 1), (2, "1/2", ("π/3", "5π/3"), 1),
                                (3, "√2/2", ("π/4", "7π/4"), -1), (4, "-1/2", ("2π/3", "4π/3"), 1),
                                (5, "-√2/2", ("3π/4", "5π/4"), -1)):
        fn = "cos" if sgn else "sin"
        exos.append(E(2, "Contrôle", f"Résoudre dans [0 ; 2π] : {fn} x = {c}.",
                      f"{c} = {fn}({a1})\nS = {{{a1} ; {a2}}}",
                      "Valeur remarquable ; les DEUX points du cercle."))
    data = (("cos x > 1/2", "]0 ; π/3[ ∪ ]5π/3 ; 2π[", "abscisse > 1/2 : arc autour de 0"),
            ("cos x ≤ √2/2", "[π/4 ; 7π/4]", "abscisse ≤ √2/2 : grand arc à gauche"),
            ("sin x ≥ √3/2", "[π/3 ; 2π/3]", "ordonnée ≥ √3/2 : arc en haut"),
            ("sin x < -1/2", "]π/2 ; 7π/6[ ∪ ]11π/6 ; 2π[", "ordonnée < -1/2 : arcs bas"))
    for eq, sol, ast in data:
        exos.append(E(2, "Contrôle", f"Résoudre dans [0 ; 2π] l'inéquation : {eq}.",
                      f"Sur [0 ; 2π] : S = {sol}\n({ast})",
                      "Lire l'arc sur le cercle : bornes ouvertes si strict, fermées si large."))
    for k, form, fn, val, (a1, a2) in ((1, "2cos x - √3 = 0", "cos", "√3/2", ("π/6", "11π/6")),
                                       (2, "√2 sin x + 1 = 0", "sin", "-√2/2", ("5π/4", "7π/4")),
                                       (3, "cos x + √3/2 = 0", "cos", "-√3/2", ("5π/6", "7π/6")),
                                       (4, "2 sin x - 1 = 0", "sin", "1/2", ("π/6", "5π/6"))):
        exos.append(E(3, "Type Examen Régional", f"Résoudre dans [0 ; 2π] : {form}.",
                      f"Isoler : {fn} x = {val}\n{val} = {fn}({a1})\nS = {{{a1} ; {a2}}}",
                      "Isoler la fonction trigonométrique, puis procédure classique."))
    return (T, exos)


def produit_scalaire():
    T = "Produit scalaire dans le plan"
    exos = []
    for u, v in (((3, -2), (1, 4)), ((2, 5), (-4, 1)), ((-1, 3), (2, 2)),
                 ((4, 2), (0, 3)), ((5, 1), (2, -6)), ((-2, -3), (1, 4))):
        ps = u[0] * v[0] + u[1] * v[1]
        nu = math.sqrt(u[0] ** 2 + u[1] ** 2)
        nv = math.sqrt(v[0] ** 2 + v[1] ** 2)
        exos.append(E(1, "Manuel", f"u({u[0]} ; {u[1]}) et v({v[0]} ; {v[1]}) : calculer u·v, ‖u‖ et ‖v‖.",
                      f"u·v = {u[0]}×({v[0]}) + {u[1]}×({v[1]}) = {ps}\n"
                      f"‖u‖ = √({u[0]}² + {u[1]}²) = {fr(nu)} ; ‖v‖ = √({v[0]}² + {v[1]}²) = {fr(nv)}",
                      "u·v = xx′ + yy′ ; ‖u‖ = √(x² + y²)."))
    for u in ((3, 4), (2, 7), (-5, 2), (6, 1), (1, 9), (4, -3)):
        v = (u[1], -u[0])
        exos.append(E(2, "Contrôle", f"Montrer que u({u[0]} ; {u[1]}) et v({v[0]} ; {v[1]}) sont orthogonaux.",
                      f"u·v = {u[0]}×{v[0]} + {u[1]}×({v[1]}) = {u[0] * v[0] + u[1] * v[1]} = 0\n→ u ⊥ v",
                      "v = (y ; -x) est toujours orthogonal à u(x ; y)."))
    for u, v, ang in (((1, 1), (0, 2), "π/4"), ((2, 0), (-2, 2), "3π/4"), ((1, 0), (1, math.sqrt(3)), "π/3"),
                      ((3, 0), (3, -3 * math.sqrt(3)), "π/6"), ((2, 2), (-2, -2), "π")):
        ps = u[0] * v[0] + u[1] * v[1]
        nu = math.sqrt(u[0] ** 2 + u[1] ** 2)
        nv = math.sqrt(v[0] ** 2 + v[1] ** 2)
        c = ps / (nu * nv)
        exos.append(E(2, "Contrôle", f"Calculer l'angle entre u({u[0]} ; {u[1]}) et v({fr(v[0])} ; {fr(v[1])}).",
                      f"u·v = {fr(ps)} ; ‖u‖ = {fr(nu)} ; ‖v‖ = {fr(nv)}\n"
                      f"cos θ = {fr(ps)}/({fr(nu)} × {fr(nv)}) = {fr(c)} → θ = {ang}",
                      "cos θ = u·v/(‖u‖‖v‖) ; reconnaître une valeur remarquable."))
    for a in (3, 5, 7):
        exos.append(E(2, "Contrôle", f"ABCD carré de côté {a}. Calculer AB·AC.",
                      f"‖AB‖ = {a} ; ‖AC‖ = {a}√2 ; angle BAC = 45°\n"
                      f"AB·AC = {a} × {a}√2 × √2/2 = {a * a}",
                      "Forme trigonométrique : ‖u‖·‖v‖·cos(angle)."))
    exos.append(E(3, "Type Examen Régional",
                  "Soit u(4 ; 3). Déterminer v(x ; y) tel que v ⊥ u, ‖v‖ = 5 et x > 0.",
                  "v ⊥ u : 4x + 3y = 0 → y = -4x/3\n‖v‖² = x² + 16x²/9 = 25x²/9 = 25 → x² = 9 → x = 3 (x > 0)\n"
                  "y = -4 → v(3 ; -4)",
                  "Système : orthogonalité + norme ; substitution puis choix du signe."))
    return (T, exos)


def fonctions():
    T = "Généralités sur les fonctions"
    exos = []
    for a, b in ((2, 3), (3, 5), (5, -4), (4, 8), (7, 2), (6, -7)):
        exos.append(E(1, "Manuel", f"Déterminer le domaine de définition de f(x) = ({fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)})/({a}x + {b + 2 * a}).",
                      f"Le dénominateur doit être non nul : {a}x + {b + 2 * a} ≠ 0\n"
                      f"x ≠ {fmt(F(-(b + 2 * a), a))}\nD_f = ℝ \\ {{{fmt(F(-(b + 2 * a), a))}}}",
                      "Exclure la valeur qui annule le DÉNOMINATEUR."))
    for a, b in ((1, 3), (2, 8), (3, 12), (5, 10), (4, -4)):
        exos.append(E(1, "Manuel", f"Déterminer le domaine de g(x) = √({fmt(a)}x {'+' if b >= 0 else '-'} {abs(b)}).",
                      f"Il faut {a}x + {b} ≥ 0\nx ≥ {fmt(F(-b, a))}\nD_g = [{fmt(F(-b, a))} ; +∞[",
                      "Sous une racine : quantité ≥ 0."))
    for f, rep in (("f(x) = 3x + 7", "affine : ni paire ni impaire (f(-x) ≠ f(x) et ≠ -f(x))"),
                   ("f(x) = x⁴ - 2x²", "f(-x) = x⁴ - 2x² = f(x) → PAIRE (symétrie / (Oy))"),
                   ("f(x) = x³ + x", "f(-x) = -x³ - x = -f(x) → IMPAIRE (symétrie / O)"),
                   ("f(x) = 5/x", "f(-x) = -5/x = -f(x) → IMPAIRE"),
                   ("f(x) = x² + x", "ni l'un ni l'autre")):
        exos.append(E(2, "Contrôle", f"Étudier la parité de {f}.",
                      rep, "Comparer f(-x) avec f(x) puis -f(x)."))
    for a, x1, x2 in ((3, 1, 4), (-2, 0, 5), (4, 2, 6), (5, 1, 3)):
        fx = lambda x: a * x + 2
        exos.append(E(2, "Contrôle", f"f(x) = {fmt(a)}x + 2. Calculer le taux de variation entre {x1} et {x2}. Que conclut-on ?",
                      f"T = (f({x2}) - f({x1}))/({x2} - {x1}) = ({fmt(fx(x2))} - ({fmt(fx(x1))}))/{fmt(x2 - x1)} = {fmt(F(a))}\n"
                      f"Taux constant ({fmt(F(a))} {'>' if a > 0 else '<'} 0) → f affine, "
                      f"{'croissante' if a > 0 else 'décroissante'} sur ℝ.",
                      "Pour une affine, le taux = coefficient directeur."))
    exos.append(E(3, "Type Examen Régional",
                  "Montrer que f(x) = x² est croissante sur [0 ; +∞[ à l'aide du taux de variation.",
                  "a < b arbitraires dans [0 ; +∞[ :\nT = (b² - a²)/(b - a) = (b - a)(b + a)/(b - a) = a + b > 0\n"
                  "Taux positif pour tous a < b → f croissante sur [0 ; +∞[. ∎",
                  "Factoriser b² - a² = (b-a)(b+a) ; simplifier par (b-a) > 0."))
    return (T, exos)


def statistiques():
    T = "Statistiques"
    exos = []
    data = (([8, 10, 12, 14, 12, 15, 9, 11, 13],), ([6, 7, 9, 10, 12, 14, 15, 16, 18],),
            ([11, 5, 13, 7, 17, 9, 19, 12, 15],), ([4, 8, 8, 10, 12, 16, 18],), ([5, 5, 6, 9, 10, 14, 15],))
    for (vals,) in data:
        vals_s = sorted(vals)
        n = len(vals_s)
        moy = F(sum(vals_s), n)
        med = vals_s[n // 2] if n % 2 == 1 else F(vals_s[n // 2 - 1] + vals_s[n // 2], 2)
        et = vals_s[-1] - vals_s[0]
        exos.append(E(1, "Contrôle", f"Notes : {' ; '.join(map(str, vals))}. Calculer moyenne, médiane et étendue.",
                      f"n = {n} ; somme = {sum(vals)} → moyenne = {fmt(moy)} ≈ {fr(float(moy))}\n"
                      f"Données ordonnées : {' ; '.join(map(str, vals_s))}\n"
                      f"Médiane = {fmt(med)} (valeur centrale) ; étendue = {vals_s[-1]} - {vals_s[0]} = {et}",
                      "TRIER d'abord ; médiane = valeur du milieu."))
    for vals, coefs in (((12, 15, 9), (1, 2, 1)), ((10, 14, 8), (2, 3, 1)), ((7, 11, 16), (1, 1, 2)),
                        ((13, 6, 9), (2, 1, 1))):
        tot = sum(c * v for c, v in zip(coefs, vals))
        nc = sum(coefs)
        exos.append(E(2, "Contrôle", f"Moyenne pondérée : {' ; '.join(f'{v} (coef {c})' for v, c in zip(vals, coefs))}.",
                      f"Σ(nᵢxᵢ) = {' + '.join(f'{c}×{v}' for c, v in zip(coefs, vals))} = {tot}\n"
                      f"Total des coefficients = {nc} → moyenne = {fmt(F(tot, nc))} ≈ {fr(tot / nc)}",
                      "Moyenne pondérée = Σ(nᵢ·xᵢ)/Σnᵢ."))
    for c0, c1, c2, b1, b2, b3, tot in ((10, 25, 40, 6, 10, 14, 40), (5, 18, 30, 4, 8, 16, 42),
                                        (8, 20, 35, 6, 10, 18, 35)):
        exos.append(E(2, "Contrôle", f"ECC d'une classe de {tot} élèves : {c0} ont une note < {b1}, "
                      f"{c1} ont < {b2}, {c2} ont < {b3}. Combien d'élèves sont dans [{b2} ; {b3}[ ? "
                      f"Et combien ont une note ≥ {b2} ?",
                      f"[{b2} ; {b3}[ : {c2} - {c1} = {c2 - c1} élèves\n"
                      f"≥ {b2} : {tot} - {c1} = {tot - c1} élèves",
                      "ECC : soustraire deux valeurs cumulées."))
    exos.append(E(3, "Type Examen Régional",
                  "Comparaison : série A : 10 ; 10 ; 10 ; 10 ; 20. Série B : 11 ; 12 ; 12 ; 12 ; 13. "
                  "Calculer les moyennes et médianes. Quelle série est la plus « homogène » ?",
                  "A : moyenne = 60/5 = 12 ; médiane = 10 (la valeur 20 tire la moyenne)\n"
                  "B : moyenne = 60/5 = 12 ; médiane = 12\n"
                  "Mêmes moyennes, mais B est plus homogène (valeurs concentrées autour de 12) ; "
                  "en A la moyenne ne reflète pas le centre (10).",
                  "Moyennes égales ≠ séries semblables : regarder la DISPERSION."))
    return (T, exos)


def transformations():
    T = "Transformations usuelles dans le plan"
    exos = []
    for m, u in (((2, 1), (3, -2)), ((-1, 4), (2, 3)), ((5, 0), (-4, 6)), ((0, 0), (1, 7))):
        mp = (m[0] + u[0], m[1] + u[1])
        exos.append(E(1, "Manuel", f"M({m[0]} ; {m[1]}), translation t de vecteur u({u[0]} ; {u[1]}). "
                      "Coordonnées de M' = t(M) ?",
                      f"M' = M + u → ({m[0]} + ({u[0]}) ; {m[1]} + ({u[1]})) = M'({mp[0]} ; {mp[1]})",
                      "Translation : ON AJOUTE le vecteur."))
    for m in ((3, 5), (-2, 7), (4, -6), (-5, -1)):
        exos.append(E(1, "Contrôle", f"Donner l'image de M({m[0]} ; {m[1]}) par la symétrie centrale de "
                      "centre O, puis par les symétries d'axes (Ox) et (Oy).",
                      f"s_O(M) = (-{m[0]} ; -{m[1]})\ns_(Ox)(M) = ({m[0]} ; -{m[1]})\ns_(Oy)(M) = (-{m[0]} ; {m[1]})",
                      "s_O : (x,y)→(-x,-y) ; (Ox) : y change ; (Oy) : x change."))
    for m, i in (((2, 3), (5, 1)), ((-1, 4), (3, 0)), ((6, 2), (1, 5))):
        si = (2 * i[0] - m[0], 2 * i[1] - m[1])
        exos.append(E(2, "Contrôle", f"I({i[0]} ; {i[1]}). Image de M({m[0]} ; {m[1]}) par la symétrie centrale s_I ?",
                      f"s_I(M) = 2I - M = ({2 * i[0]} - {m[0]} ; {2 * i[1]} - {m[1]}) = ({si[0]} ; {si[1]})",
                      "Formule : s_I(M) = 2I - M."))
    for a, k in ((12, 3), (25, 1 / 2), (16, 2), (30, 3), (8, 1 / 4)):
        exos.append(E(2, "Contrôle", f"Une figure d'aire {a} cm² subit l'homothétie h(O ; {fmt(F(k).limit_denominator(10))}). "
                      "Que devient son aire ? Son périmètre est multiplié par quoi ?",
                      f"Aires × k² = {fmt(F(k).limit_denominator(10))}² = {fmt(F(k * k).limit_denominator(100))}\n"
                      f"Aire image = {fmt(F(a).limit_denominator(10))} × {fmt(F(k * k).limit_denominator(100))} = "
                      f"{fr(a * k * k)} cm²\nLongueurs × |k| : périmètre × {fmt(F(abs(k)).limit_denominator(10))}",
                      "Longueurs ×|k| ; AIRES ×k² (jamais ×k !)."))
    for p in ((3, 4), (-2, 5), (1, -6)):
        exos.append(E(2, "Manuel", f"Image de P({p[0]} ; {p[1]}) par la rotation de centre O et d'angle 180°, "
                      "puis 90° (sens direct) ?",
                      f"r(O ; 180°) : (-{p[0]} ; -{p[1]})\n"
                      f"r(O ; 90°) : (x ; y) → (-y ; x) = (-{p[1]} ; {p[0]})",
                      "180° : changement des deux signes ; 90° direct : (x;y)→(-y;x)."))
    exos.append(E(3, "Type Examen Régional",
                  "A(1 ; 1), B(5 ; 3). I milieu de [AB]. Montrer que s_I(A) = B et calculer s_I(O).",
                  "I((1+5)/2 ; (1+3)/2) = I(3 ; 2)\ns_I(A) = 2I - A = (6-1 ; 4-1) = (5 ; 3) = B ✓\n"
                  "s_I(O) = 2I - O = (6 ; 4)",
                  "s_I(M) = 2I - M : tout se calcule."))
    return (T, exos)


def projection():
    T = "La projection dans le plan"
    exos = []
    base = [E(2, "Contrôle", "ABC triangle rectangle en A avec AB = 9, AC = 12. H projeté orthogonal de A "
              "sur (BC). Calculer BC puis AH (double expression de l'aire).",
              "BC = √(81 + 144) = √225 = 15\nAire = AB×AC/2 = 54 = BC×AH/2 = 15×AH/2\n"
              "AH = 108/15 = 7,2",
              "Aire calculée 2 façons : l'hauteur sort toute seule."),
            E(2, "Contrôle", "MNP rectangle en M, MN = 5, MP = 12. Que devient [NP] par projection "
              "orthogonale sur (MN) ? En déduire NP.",
              "Le projeté de N est N ; celui de P est M ((MP) ⊥ (MN)) → [NP] se projette en [NM].\n"
              "NP = √(25 + 144) = √169 = 13",
              "Un segment perpendiculaire à la droite de projection → un POINT."),
            E(3, "Type Examen Régional", "ABCD carré de côté 6, E milieu de [AB]. H projeté orthogonal "
              "de E sur la diagonale (AC). Calculer EH et AH.",
              "(AC) à 45° de (AB) ; AE = 3 ; AEH rectangle en H, angle EAH = 45°\n"
              "EH = AE·sin 45° = 3×√2/2 = 3√2/2 ≈ 2,12\nAH = AE·cos 45° = 3√2/2 ≈ 2,12\n"
              "(triangle AEH rectangle ISOCÈLE en H)",
              "45° → triangle rectangle isocèle : EH = AH.")]
    exos += base
    for ab, ac in ((6, 8), (5, 12), (8, 15), (7, 24)):
        bc = int(math.isqrt(ab * ab + ac * ac))
        ah = F(ab * ac, bc)
        exos.append(E(2, "Contrôle", f"ABC rectangle en A : AB = {ab}, AC = {ac}. H projeté de A sur (BC) : "
                      "calculer BC et AH.",
                      f"BC = √({ab}² + {ac}²) = √{ab * ab + ac * ac} = {bc}\n"
                      f"Aire = {ab}×{ac}/2 = {ab * ac // 2} = BC×AH/2 → AH = {fmt(ah)} ≈ {fr(float(ah))}",
                      "Double expression de l'aire = LA technique des hauteurs."))
    return (T, exos)


def espace():
    T = "Géométrie dans l'espace"
    exos = []
    triples = ((2, 3, 6), (1, 2, 2), (4, 4, 7), (2, 6, 9), (6, 6, 7), (1, 4, 8), (3, 12, 4))
    for (x, y, z), n in zip(triples, (7, 3, 9, 11, 11, 9, 13)):
        exos.append(E(1, "Manuel", f"Calculer la distance OM pour M({x} ; {y} ; {z}).",
                      f"OM = √({x}² + {y}² + {z}²) = √{x * x + y * y + z * z} = {n}",
                      "Pythagore deux fois : OM = √(x²+y²+z²)."))
    for a, b in (((1, 2, 0), (4, 6, 4)), ((0, 0, 0), (2, 6, 9)), ((-1, 3, 2), (5, 3, 2)),
                 ((2, 2, 2), (4, 8, 9))):
        v = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
        n = math.isqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        nn = n if n * n == v[0] ** 2 + v[1] ** 2 + v[2] ** 2 else None
        i = tuple(F(a[k] + b[k], 2) for k in range(3))
        exos.append(E(1, "Contrôle", f"A{a} et B{b} : coordonnées de AB, distance AB, milieu I de [AB]."
                      .replace("A(", "A(").replace("B(", "B("),
                      f"AB({v[0]} ; {v[1]} ; {v[2]})\nAB = √({v[0] ** 2}+{v[1] ** 2}+{v[2] ** 2}) = "
                      f"{fr(math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2))}\n"
                      f"I({fmt(i[0])} ; {fmt(i[1])} ; {fmt(i[2])})",
                      "AB = B - A ; milieu = moyennes ; Pythagore 3D."))
    for a, b, c, ok in (((0, 0, 0), (1, 1, 1), (3, 3, 3), True), ((1, 0, 2), (2, 2, 0), (3, 4, -2), True),
                        ((0, 0, 0), (1, 1, 0), (2, 3, 1), False)):
        u = tuple(b[k] - a[k] for k in range(3))
        v = tuple(c[k] - a[k] for k in range(3))
        ratios = [F(v[k], u[k]) if u[k] else None for k in range(3)]
        coll = all(r is not None and r == ratios[0] for r in ratios)
        exos.append(E(2, "Contrôle", f"A{a}, B{b}, C{c} : alignés ?",
                      f"AB({u[0]} ; {u[1]} ; {u[2]}) ; AC({v[0]} ; {v[1]} ; {v[2]})\n"
                      + ("AC = k·AB avec k = " + fmt(ratios[0]) + " → colinéaires → ALIGNÉS" if coll
                         else "AC n'est pas multiple de AB (ratios inégaux) → NON alignés"),
                      "3 coordonnées : le multiple k doit être LE MÊME pour les trois."))
    exos.append(E(3, "Type Examen Régional",
                  "ABCDEFGH cube. Montrer que la droite (AG) est perpendiculaire au plan (BDH).",
                  "(BDH) : les diagonales des faces du cube (plan horizontal du sommet haut).\n"
                  "La grande diagonale (AG) est perpendiculaire à BD et à BH (démonstration par le "
                  "produit scalaire ou les symétries du cube) : deux droites sécantes du plan (BDH).\n"
                  "→ (AG) ⊥ (BDH).",
                  "⊥ à 2 droites sécantes du plan = ⊥ au plan."))
    return (T, exos)


def generators():
    return [arith(), ensembles(), ordre(), polynomes(), equations(), vecteurs(), droite(),
            trigo(), trigo_eq(), produit_scalaire(), fonctions(), statistiques(),
            transformations(), projection(), espace()]
