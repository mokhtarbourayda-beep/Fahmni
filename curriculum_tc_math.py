# -*- coding: utf-8 -*-
"""
curriculum_tc_math.py — Programme COMPLET de Mathématiques du Tronc Commun
(conforme au programme officiel marocain), avec leçons multi-méthodes et
banque d'exercices étendue (manuel, contrôles, type examen régional).

Structure : chaque chapitre = (semestre, titre, resume, lecon, [exercices])
Exercice = (difficulte, source, enonce, solution, astuce, variantes)
"""

# ============================================================ S1 : CH1..CH9 ==
EN_SEMBLES = {
    "intro": "Les nombres sont organisés en ensembles emboîtés : ℕ (entiers naturels) ⊂ ℤ "
             "(entiers relatifs) ⊂ 𝔻 (décimaux) ⊂ ℚ (rationnels) ⊂ ℝ (réels). Savoir "
             "classer un nombre et écrire une appartenance est LA base de tout le lycée.",
    "methodes": [
        {"nom": "Méthode 1 — reconnaître l'ensemble d'un nombre",
         "texte": "Pose-toi 3 questions dans l'ordre : ① est-ce un entier (sans virgule, "
                  "pas négatif → ℕ ; entier négatif possible → ℤ) ? ② virgule FINIE "
                  "(ex : 3,14 ; −0,5) → 𝔻. ③ quotient de 2 entiers (fraction, y compris "
                  "virgule infinie périodique ex : 1/3 = 0,333…) → ℚ. Sinon (√2, π) → irrationnel, donc ∈ ℝ\\ℚ."},
        {"nom": "Méthode 2 — symboles d'appartenance",
         "texte": "∈ = « appartient à », ∉ = « n'appartient pas », ⊂ = « est inclus dans ». "
                  "Ex : −3 ∈ ℤ ; −3 ∉ ℕ ; ℕ ⊂ ℚ. Sur la droite graduée, un point plein "
                  "● = valeur incluse, un point vide ○ = exclue."},
        {"nom": "Méthode 3 — valeurs approchées",
         "texte": "Valeur approchée décimale de a à 10⁻ⁿ près : on coupe au (n+1)-ième "
                  "chiffre. Par défaut : on garde en dessous ; par excès : au-dessus. "
                  "Ex : π ≈ 3,1415… → 3,14 (défaut) et 3,15 (excès) à 10⁻² près."},
    ],
    "exemples": [
        {"question": "Classer : 25 ; −7 ; 2,35 ; 5/4 ; √3 ; 0,333… (périodique)",
         "etapes": ["25 ∈ ℕ (entier positif)",
                    "−7 ∈ ℤ (entier négatif) mais −7 ∉ ℕ",
                    "2,35 ∈ 𝔻 (virgule finie)",
                    "5/4 ∈ ℚ (et ∈ 𝔻 car 1,25)",
                    "√3 ∉ ℚ → irrationnel, ∈ ℝ",
                    "0,333… = 1/3 ∈ ℚ (périodique = fraction)"],
         "reponse": "Chaque nombre est placé dans son ensemble, du plus petit au plus grand."},
    ],
    "pieges": [
        "Tout nombre à virgule n'est pas décimal : 0,333… (infini) ne l'est pas !",
        "√4 = 2 est un ENTIER ; ne pas croire que toute racine est irrationnelle.",
        "ℕ n'inclut pas les négatifs : −3 ∉ ℕ.",
    ],
    "formules": ["ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ", "0,999… = 1", "irrationnels célèbres : √2, π, e"],
}

CH_ORDRE = {
    "intro": "Comparer des réels, travailler avec les intervalles et les encadrements : "
             "c'est le langage de l'analyse. Toute étude de fonction en dépendra.",
    "methodes": [
        {"nom": "Méthode 1 — comparer deux réels",
         "texte": "Étudie le signe de la différence a − b : a ≥ b ⟺ a − b ≥ 0. "
                  "Pour les quotients, compare au même dénominateur. Pour les carrés : "
                  "0 ≤ a ≤ b ⟺ a² ≤ b² (pour les positifs)."},
        {"nom": "Méthode 2 — opérations sur les inégalités",
         "texte": "On peut additionner membre à membre des inégalités de même sens. "
                  "MULTIPLIER par un négatif CHANGE le sens : si a < b et c < 0 alors "
                  "ac > bc. C'est LE piège classique des contrôles."},
        {"nom": "Méthode 3 — intervalles et encadrements",
         "texte": "[a ; b] inclut les bornes ; ]a ; b[ les exclut. Encadrer x : "
                  "ajoute/soustrais/multiplie TOUS les membres (en changeant les sens si "
                  "nécessaire). Ex : 2 ≤ x ≤ 3 → 6 ≤ 2x ≤ 6... attention 6 ≤ 2x ≤ 6 est "
                  "faux : on écrit 4 ≤ 2x ≤ 6 puis −2 ≤ −2x ≤ −3 (sens inversé)."},
    ],
    "exemples": [
        {"question": "Sachant 1 ≤ x ≤ 2, encadrer f(x) = 3x − 1 puis g(x) = −x + 5.",
         "etapes": ["3 ≤ 3x ≤ 6 (multiplication par 3, positif)",
                    "2 ≤ 3x − 1 ≤ 5 (soustraction de 1)",
                    "1 ≤ x ≤ 2 → −2 ≤ −x ≤ −1 (multiplication par −1 : sens inversé !)",
                    "3 ≤ −x + 5 ≤ 4 (addition de 5)"],
         "reponse": "f(x) ∈ [2 ; 5] et g(x) ∈ [3 ; 4]"},
    ],
    "pieges": [
        "Multiplier par un négatif sans changer le sens de l'inégalité.",
        "Écrire ]3 ; 1[ au lieu de ]1 ; 3[ (petite borne toujours à gauche).",
        "Confondre ⊂ (inclusion d'ensembles) et ∈ (appartenance d'un élément).",
    ],
    "formules": ["a ≤ b ⟺ a − b ≤ 0", "si c < 0 et a < b alors ac > bc",
                 "[a ; b] = {x ∈ ℝ / a ≤ x ≤ b}"],
}

CH_POLYNOMES = {
    "intro": "Un polynôme s'écrit a_n xⁿ + … + a₁x + a₀. Le chapitre clé : développer "
             "avec les identités remarquables, factoriser, et trouver les racines. "
             "Tout le second degré du lycée repose là-dessus.",
    "methodes": [
        {"nom": "Méthode 1 — les identités remarquables",
         "texte": "À connaître PAR CŒUR : (a+b)² = a² + 2ab + b² ; (a−b)² = a² − 2ab + b² ; "
                  "(a−b)(a+b) = a² − b². Astuce de reconnaissance : x² + 6x + 9 = (x+3)² "
                  "car 9 = 3² et 6 = 2×3×1."},
        {"nom": "Méthode 2 — factoriser (le réflexe du facteur commun)",
         "texte": "Ordre de recherche : ① facteur commun (3x² − x = x(3x − 1)), "
                  "② identité remarquable, ③ racine évidente : si f(a) = 0 alors "
                  "(x − a) est un facteur. Ex : x³ − 2x² − 3x = x(x² − 2x − 3) et "
                  "x = 3 annule x² − 2x − 3 → (x−3)(x+1)."},
        {"nom": "Méthode 3 — racines et équations produit",
         "texte": "Une racine de P est une valeur de x qui annule P. Équation produit : "
                  "A(x)·B(x) = 0 ⟺ A(x) = 0 OU B(x) = 0. C'est TOUTE la puissance de la "
                  "factorisation : une équation compliquée devient 2 équations simples."},
    ],
    "exemples": [
        {"question": "Développer (2x − 3)² puis factoriser x² − 25 et 2x² + 6x.",
         "etapes": ["(2x − 3)² = (2x)² − 2×2x×3 + 3² = 4x² − 12x + 9",
                    "x² − 25 = x² − 5² = (x − 5)(x + 5)  (identité a² − b²)",
                    "2x² + 6x = 2x(x + 3)  (facteur commun 2x)"],
         "reponse": "4x² − 12x + 9 ; (x−5)(x+5) ; 2x(x+3)"},
        {"question": "Résoudre (x − 2)(2x + 1) = 0.",
         "etapes": ["Produit nul ⟺ x − 2 = 0 ou 2x + 1 = 0",
                    "x = 2 ou x = −1/2"],
         "reponse": "S = {−1/2 ; 2}"},
    ],
    "pieges": [
        "(a + b)² ≠ a² + b² : il manque le double produit 2ab !",
        "Oublier de vérifier la factorisation en redéveloppant (30 secondes qui sauvent).",
        "x² = 9 ⟹ x = 3 ET x = −3 (deux racines, pas une !).",
    ],
    "formules": ["(a+b)² = a² + 2ab + b²", "(a−b)² = a² − 2ab + b²",
                 "(a−b)(a+b) = a² − b²", "A·B = 0 ⟺ A = 0 ou B = 0"],
}

CH_PROJECTION = {
    "intro": "Projeter un point sur une droite, c'est lui « faire tomber » une "
             "perpendiculaire (projection orthogonale) ou des parallèles à une direction "
             "donnée (projection oblique). Outil clé pour les longueurs et le produit scalaire.",
    "methodes": [
        {"nom": "Méthode 1 — construire une projection orthogonale",
         "texte": "M' = projeté orthogonal de M sur d ⟺ M' ∈ d et (MM') ⊥ d. "
                  "Construction : équerre sur la droite, trace la perpendiculaire passant "
                  "par M, le pied est M'. Si M ∈ d, alors M' = M."},
        {"nom": "Méthode 2 — propriétés à exploiter",
         "texte": "La projection conserve : l'alignement, le milieu, la symétrie. "
                  "Elle NE conserve PAS les longueurs ni les angles en général. "
                  "Un segment perpendiculaire à la droite de projection se projette en UN POINT."},
        {"nom": "Méthode 3 — projeté d'un segment et calcul",
         "texte": "Le projeté de [AB] est [A'B'] (ou un point si AB ⊥ d). Pour calculer "
                  "une longueur projetée : Pythagore dans le triangle rectangle formé. "
                  "Ex : si MM' = 3 et M'N' = 4 avec (MN) ∥ d... length MN se déduit du triangle."},
    ],
    "exemples": [
        {"question": "ABCD rectangle. Soit H le projeté orthogonal de D sur (AC). "
                     "Que représente H ?",
         "etapes": ["On trace la perpendiculaire à (AC) passant par D.",
                    "Elle coupe (AC) en H.",
                    "DH est la distance de D à la droite (AC)."],
         "reponse": "H est le pied de la hauteur issue de D dans le triangle ADC."},
    ],
    "pieges": [
        "Le projeté orthogonal d'un point APPARTIENT à la droite (vérifier !).",
        "Confondre projection orthogonale (perpendiculaire) et oblique (direction donnée).",
    ],
    "formules": ["M' = proj_d(M) ⟺ M' ∈ d et (MM') ⊥ d", "d(M, d) = MM' (distance)"],
}

CH_DROITE = {
    "intro": "Toute droite du plan s'écrit soit y = mx + p (m = coefficient directeur, "
             "p = ordonnée à l'origine), soit ax + by + c = 0. La géométrie analytique "
             "remplace l'intuition par le calcul.",
    "methodes": [
        {"nom": "Méthode 1 — déterminer le coefficient directeur",
         "texte": "Par 2 points A(x_A ; y_A) et B(x_B ; y_B) : m = (y_B − y_A)/(x_B − x_A) "
                  "avec x_A ≠ x_B. Droite horizontale : m = 0. Droite verticale : x = a "
                  "(PAS de coefficient directeur !)."},
        {"nom": "Méthode 2 — trouver l'équation complète",
         "texte": "① Calcule m. ② Utilise y = mx + p avec UN point connu pour trouver p. "
                  "Ex : droite de pente 2 passant par A(1 ; 3) : 3 = 2×1 + p → p = 1 → "
                  "y = 2x + 1."},
        {"nom": "Méthode 3 — positions relatives",
         "texte": "d₁ : y = m₁x + p₁ et d₂ : y = m₂x + p₂. Parallèles ⟺ m₁ = m₂ (et "
                  "p₁ ≠ p₂). Sécantes ⟺ m₁ ≠ m₂ : le point d'intersection se trouve en "
                  "résolvant m₁x + p₁ = m₂x + p₂. Perpendiculaires (admis) : m₁·m₂ = −1."},
    ],
    "exemples": [
        {"question": "Équation de la droite passant par A(−1 ; 2) et B(3 ; 10).",
         "etapes": ["m = (10 − 2)/(3 − (−1)) = 8/4 = 2",
                    "y = 2x + p avec A : 2 = 2×(−1) + p → p = 4"],
         "reponse": "d : y = 2x + 4  (vérification B : 2×3+4 = 10 ✓)"},
        {"question": "Intersection de d₁ : y = 2x + 4 et d₂ : y = −x + 1.",
         "etapes": ["2x + 4 = −x + 1", "3x = −3 → x = −1", "y = 2(−1) + 4 = 2"],
         "reponse": "d₁ et d₂ se coupent en (−1 ; 2) — c'est le point A de l'exemple 1 !"},
    ],
    "pieges": [
        "Une droite verticale s'écrit x = a : il n'existe aucun y = mx + p pour elle.",
        "Diviser par (x_B − x_A) quand il vaut 0 (points alignés verticalement).",
        "Confondre p (ordonnée à l'origine) avec une coordonnée d'un point de la droite.",
    ],
    "formules": ["m = (y_B − y_A)/(x_B − x_A)", "y = mx + p", "ax + by + c = 0 (a ≠ 0 ou b ≠ 0)",
                 "parallèles : m₁ = m₂"],
}

CH_TRANSFORMATIONS = {
    "intro": "Translation, symétrie, homothétie, rotation : des transformations qui "
             "déplacent les figures tout en conservant certaines propriétés. Comprendre "
             "CE QUE CHAQUE transformation conserve est le cœur du chapitre.",
    "methodes": [
        {"nom": "Méthode 1 — identifier la transformation",
         "texte": "Translation t_u : glissement selon le vecteur u (M' = M + u, même "
                  "direction et sens pour tous les points). Symétrie axiale (d) : pliage "
                  "autour de la droite. Symétrie centrale (O) : demi-tour autour du point. "
                  "Rotation (O ; α) : tournant d'angle α autour de O. Homothétie (O ; k) : "
                  "agrandissement/réduction depuis O, avec OM' = |k|·OM."},
        {"nom": "Méthode 2 — ce qui est conservé",
         "texte": "Translation, symétries, rotation : longueurs, angles, aires, "
                  "alignement, parallélisme, milieux → les figures sont ISOMÉTRIQUES "
                  "(superposables). Homothétie (k ≠ ±1) : angles et parallélisme "
                  "conservés, longueurs et aires MULTIPLIÉES par |k| et k²."},
        {"nom": "Méthode 3 — construire une image",
         "texte": "Symétrie axiale : M' tel que (d) soit la médiatrice de [MM']. "
                  "Rotation : report de l'angle au compas puis de la longueur. "
                  "Homothétie de rapport k : aligner M', M et O avec OM' = |k|·OM du "
                  "même côté que M si k > 0, du côté opposé si k < 0."},
    ],
    "exemples": [
        {"question": "ABC a pour aire 12. A'B'C' est l'image de ABC par l'homothétie "
                     "h(O ; 3). Quelle est l'aire de A'B'C' ? Que dire des angles ?",
         "etapes": ["k = 3 → longueurs ×3, aires ×k² = ×9",
                    "Aire(A'B'C') = 12 × 9 = 108",
                    "L'homothétie conserve les angles : triangles semblables"],
         "reponse": "Aire = 108 ; angles identiques ; périmètre ×3."},
        {"question": "M(2 ; 1), translation de vecteur u(3 ; −2). Coordonnées de M' ?",
         "etapes": ["M' = M + u → x' = 2 + 3 = 5 ; y' = 1 + (−2) = −1"],
         "reponse": "M'(5 ; −1)"},
    ],
    "pieges": [
        "k négatif : l'image est de l'AUTRE côté de O (ne pas l'oublier).",
        "Une rotation se définit par son CENTRE et son ANGLE (et son sens).",
        "Aire ×|k| est faux : c'est ×k² pour une homothétie.",
    ],
    "formules": ["t_u(M) = M' ⟺ MM' = u", "h(O;k) : OM' = |k|·OM",
                 "aire image = k² × aire", "isométries : translation, symétries, rotation"],
}

CH_TRIGO_EQ = {
    "intro": "Résoudre cos x = a, sin x = a et les inéquations associées grâce au cercle "
             "trigonométrique. La méthode est GRAPHIQUE avant d'être formelle.",
    "methodes": [
        {"nom": "Méthode 1 — la procédure en 3 temps",
         "texte": "① Vérifie que |a| ≤ 1 (sinon aucune solution). ② Trace le cercle et "
                  "place la droite x = a (pour cos) ou y = a (pour sin). ③ Lis les deux "
                  "angles solutions, puis écris la famille générale avec + 2kπ."},
        {"nom": "Méthode 2 — les valeurs remarquables",
         "texte": "Mémorise le tableau de cos/sin pour 0, π/6, π/4, π/3, π/2 et leurs "
                  "symétriques. Toute équation d'examen utilise ces valeurs (ou −valeur)."},
        {"nom": "Méthode 3 — inéquations",
         "texte": "cos x ≥ a : arcs du cercle où l'abscisse ≥ a → un arc continu "
                  "autour de 0. sin x ≤ a : arc où l'ordonnée ≤ a → autour de −π/2. "
                  "Écris l'intervalle d'angles correspondant SUR [0 ; 2π] (ou [−π ; π])."},
    ],
    "exemples": [
        {"question": "Résoudre dans [0 ; 2π] : sin x = √2/2, puis sin x > √2/2.",
         "etapes": ["√2/2 = sin(π/4)",
                    "La droite y = √2/2 coupe le cercle en π/4 et 3π/4",
                    "S = {π/4 ; 3π/4}",
                    "sin x > √2/2 : partie AU-DESSUS de la droite → x ∈ ]π/4 ; 3π/4["],
         "reponse": "S = {π/4 ; 3π/4} ; sin x > √2/2 ⟺ x ∈ ]π/4 ; 3π/4["},
    ],
    "pieges": [
        "cos x = 2 n'a AUCUNE solution (|cos| ≤ 1).",
        "Oublier le deuxième point d'intersection avec le cercle.",
        "Donner les solutions sur ℝ alors qu'on demande un intervalle précis.",
    ],
    "formules": ["cos x = cos a ⟺ x = ±a + 2kπ", "sin x = sin a ⟺ x = a + 2kπ ou x = π − a + 2kπ"],
}

CH_PRODUIT_SCALAIRE = {
    "intro": "Le produit scalaire associe un NOMBRE à deux vecteurs. Il mesure "
             "l'« accord » entre leurs directions : nul si perpendiculaires, positif si "
             "« de même sens », négatif sinon. Applications : orthogonalité, angles, calculs.",
    "methodes": [
        {"nom": "Méthode 1 — les 3 expressions",
         "texte": "① u·v = ‖u‖·‖v‖·cos(u,v)  (définition). ② Si u(x ; y) et v(x' ; y') : "
                  "u·v = xx′ + yy′ (la plus utilisée en repère). ③ u·v = ½(‖u+v‖² − ‖u‖² − ‖v‖²)."},
        {"nom": "Méthode 2 — orthogonalité",
         "texte": "u ⊥ v ⟺ u·v = 0 ⟺ xx′ + yy′ = 0. C'est LE test des exercices : "
                  "hauteurs, tangentes, perpendiculaires."},
        {"nom": "Méthode 3 — trouver un angle",
         "texte": "cos(angle) = (u·v)/(‖u‖·‖v‖). Calcule le produit scalaire, les deux "
                  "normales (Pythagore : ‖u‖ = √(x²+y²)), divise, puis lis l'angle "
                  "(valeurs remarquables)."},
    ],
    "exemples": [
        {"question": "u(2 ; 3) et v(−3 ; 2). Calculer u·v. Que conclure ?",
         "etapes": ["u·v = 2×(−3) + 3×2 = −6 + 6 = 0"],
         "reponse": "u·v = 0 → u et v sont orthogonaux."},
        {"question": "u(1 ; 2), v(3 ; 1). Angle entre eux ?",
         "etapes": ["u·v = 3 + 2 = 5", "‖u‖ = √5 ; ‖v‖ = √10",
                    "cos θ = 5/√50 = 5/(5√2) = 1/√2 = √2/2"],
         "reponse": "θ = π/4 (45°)"},
    ],
    "pieges": [
        "u·v est un NOMBRE, jamais un vecteur (ne pas répondre « un vecteur »).",
        "u·v = 0 ne veut PAS dire que l'un des vecteurs est nul uniquement.",
        "‖u‖² = x² + y² (ne pas oublier la racine pour ‖u‖).",
    ],
    "formules": ["u·v = xx′ + yy′", "u·v = ‖u‖‖v‖ cos θ", "u ⊥ v ⟺ u·v = 0",
                 "‖u‖ = √(x² + y²)"],
}

CH_ESPACE = {
    "intro": "Passage du plan (2 axes) à l'espace (3 axes x, y, z). Repérage, vecteurs, "
             "et positions relatives de droites et de plans : le même esprit, une "
             "dimension de plus.",
    "methodes": [
        {"nom": "Méthode 1 — repérage dans l'espace",
         "texte": "Un point M(x ; y ; z). Distance à l'origine : OM = √(x² + y² + z²) "
                  "(Pythagore deux fois). Milieu de [AB] : coordonnées = moyennes des "
                  "coordonnées."},
        {"nom": "Méthode 2 — vecteurs de l'espace",
         "texte": "u(x ; y ; z). Colinéarité de u et v : il existe k tel que v = k·u "
                  "(3 égalités à vérifier). AB = B − A (coordonnées). ‖AB‖ = √(Δx²+Δy²+Δz²)."},
        {"nom": "Méthode 3 — positions relatives",
         "texte": "Deux droites de l'espace : coplanaires (sécantes ou parallèles) OU "
                  "non coplanaires (ni l'un ni l'autre — l'essentiel du nouveau vocabulaire). "
                  "Droite ⊥ plan si elle est perpendiculaire à deux droites sécantes du plan."},
    ],
    "exemples": [
        {"question": "A(1 ; 0 ; 2), B(3 ; 2 ; 4). Coordonnées de AB et ‖AB‖ ?",
         "etapes": ["AB = (3−1 ; 2−0 ; 4−2) = (2 ; 2 ; 2)",
                    "‖AB‖ = √(4+4+4) = √12 = 2√3"],
         "reponse": "AB(2 ; 2 ; 2) ; ‖AB‖ = 2√3"},
    ],
    "pieges": [
        "Oublier la 3ᵉ coordonnée dans la distance.",
        "Deux droites sans point commun ne sont pas forcément parallèles (non coplanaires !).",
    ],
    "formules": ["OM = √(x²+y²+z²)", "AB(x_B−x_A ; y_B−y_A ; z_B−z_A)",
                 "‖u‖ = √(x²+y²+z²)"],
}

# ================================================= exercices (tous types) ====
V = lambda *xs: list(xs)

NEW_CHAPTERS = [
    (1, "Les ensembles de nombres", "ℕ, ℤ, 𝔻, ℚ, ℝ : appartenances, inclusions, "
     "valeurs approchées.", EN_SEMBLES, [
        (1, "Manuel", "Classer les nombres suivants dans le bon ensemble : "
         "12 ; −4 ; 0,8 ; 7/3 ; √5 ; −1,25",
         "12 ∈ ℕ ⊂ ℤ\n−4 ∈ ℤ (mais ∉ ℕ)\n0,8 ∈ 𝔻 (8/10)\n7/3 ∈ ℚ (décimale infinie "
         "périodique 2,333…, donc ∈ 𝔻 ? NON : 7/3 n'est pas décimal car "
         "périodique)\n√5 ∉ ℚ : irrationnel ∈ ℝ\n−1,25 = −5/4 ∈ 𝔻",
         "Virgule finie → 𝔻 ; fraction non décimale → ℚ seulement ; racine non exacte → irrationnel.",
         V({"enonce": "Classer : 0 ; √9 ; 22/7 ; 3,1416 ; π",
            "solution": "0 ∈ ℕ ; √9 = 3 ∈ ℕ ; 22/7 ∈ ℚ ; 3,1416 ∈ 𝔻 (et ∈ ℚ) ; "
                        "π ∈ ℝ\\ℚ (irrationnel — 3,1416 n'est qu'une valeur approchée !)"})),
        (2, "Contrôle", "Vrai ou faux ? Justifier : ① −6 ∈ ℕ ② 0 ∈ ℝ ③ 1/3 ∈ 𝔻 "
         "④ ℕ ⊂ ℚ ⑤ √2 ∈ ℚ",
         "① FAUX : les négatifs n'appartiennent pas à ℕ.\n② VRAI : 0 ∈ ℕ ⊂ ℝ.\n"
         "③ FAUX : 1/3 = 0,333… périodique, virgule non finie → 1/3 ∈ ℚ\\𝔻.\n"
         "④ VRAI : tout entier est un rationnel (n = n/1).\n"
         "⑤ FAUX : √2 est irrationnel (démonstration du cours).",
         "Pour « vrai ou faux », une contre-example ou une définition suffit.",
         V()),
        (2, "Manuel", "Donner la valeur approchée de √50 par défaut et par excès à 10⁻¹ près.",
         "√50 ≈ 7,0710…\nPar défaut à 10⁻¹ : 7,0\nPar excès à 10⁻¹ : 7,1\n"
         "(On dit : 7,0 ≤ √50 < 7,1)",
         "Encadrer entre deux décimaux à 1 chiffre après la virgule.",
         V({"enonce": "Encadrer π entre deux décimaux à 10⁻³ près.",
            "solution": "3,141 ≤ π < 3,142"})),
        (3, "Type Examen Régional", "Montrer que 0,999… = 1 (indication : poser "
         "x = 0,999…, calculer 10x − x).",
         "x = 0,999…\n10x = 9,999…\n10x − x = 9,999… − 0,999… = 9\n9x = 9 → x = 1\n"
         "Donc 0,999… = 1 : ce nombre décimal infini périodique coïncide avec l'entier 1.",
         "Le développement périodique se manipule par multiplication par la puissance de 10 adaptée.",
         V({"enonce": "Écrire 0,333… sous forme de fraction (même méthode).",
            "solution": "x = 0,333… ; 10x = 3,333… ; 10x − x = 3 → 9x = 3 → x = 1/3"})),
    ]),

    (1, "L'ordre dans ℝ", "Comparer des réels, intervalles, encadrements, effets des "
     "opérations sur les inégalités.", CH_ORDRE, [
        (1, "Manuel", "Comparer −3/5 et −4/7.",
         "Dénominateur commun 35 : −3/5 = −21/35 ; −4/7 = −20/35\n−21/35 < −20/35\n"
         "Donc −3/5 < −4/7.",
         "Deux négatifs : le plus petit est celui avec la plus grande valeur absolue.",
         V({"enonce": "Comparer √10 et 3,2.",
            "solution": "√10 ≈ 3,162 < 3,2 (ou : 10 < 3,2² = 10,24 → √10 < 3,2)"})),
        (1, "Manuel", "Représenter et écrire avec les notations : « x appartient à "
         "l'intervalle de −2 inclus à 5 exclu ».",
         "x ∈ [−2 ; 5[\nReprésentation : droite graduée, point plein en −2, point vide en 5.",
         "Inclus → crochet fermé [ et point plein ; exclu → crochet ouvert ] et point vide.",
         V({"enonce": "Traduire x ∈ ]−∞ ; −1] en phrase.",
            "solution": "x est un réel inférieur ou égal à −1."})),
        (2, "Contrôle", "Sachant −1 ≤ x ≤ 3, encadrer : ① 2x + 1 ② −3x ③ 1/x "
         "(x ≠ 0... préciser)",
         "① −2 ≤ 2x ≤ 6 → −1 ≤ 2x + 1 ≤ 7\n"
         "② −3 ≤ −3x ≤ 9  (×(−3) : sens INVERSÉ)\n"
         "③ 1 ≤ x ≤ 3 (partie positive) → 1/3 ≤ 1/x ≤ 1 (fonction inverse décroissante sur (0 ; +∞))",
         "L'inverse RÉDUIT l'encadrement quand tout est positif : les bornes s'échangent.",
         V({"enonce": "Sachant 2 ≤ x ≤ 5, encadrer x² puis √x.",
            "solution": "4 ≤ x² ≤ 25 ; √2 ≤ √x ≤ √5"})),
        (2, "Manuel", "Résoudre l'inéquation : 3 − 2x ≥ 7 et donner l'ensemble de "
         "solutions sous forme d'intervalle.",
         "−2x ≥ 7 − 3 = 4\nx ≤ −2  (division par −2 : sens inversé)\nS = ]−∞ ; −2]",
         "Diviser par un négatif inverse le sens : c'est LA faute à éviter.",
         V({"enonce": "Résoudre : 5(x − 1) < 2x + 8.",
            "solution": "5x − 5 < 2x + 8 → 3x < 13 → x < 13/3 → S = ]−∞ ; 13/3["})),
        (3, "Type Examen Régional", "x et y vérifient 1 ≤ x ≤ 2 et 3 ≤ y ≤ 5. "
         "Encadrer x + y ; x·y ; puis montrer que |x − y| ≤ 4.",
         "x + y : 4 ≤ x + y ≤ 7\n"
         "x·y : min = 1×3 = 3 (tout positif) ; max = 2×5 = 10 → 3 ≤ xy ≤ 10\n"
         "|x − y| ≤ |x| + |y| ≤ 2 + 5 = 7... on affine : y − x ≤ 5 − 1 = 4 et "
         "x − y ≤ 2 − 3 < 0 ≤ 4 → −4 ≤ x − y ≤ 4 → |x − y| ≤ 4",
         "Pour l'encadrement d'un produit, tout tester par les bornes extrêmes.",
         V({"enonce": "Encadrer 2x − 3y sachant 1 ≤ x ≤ 2 et 3 ≤ y ≤ 5.",
            "solution": "2 ≤ 2x ≤ 4 ; −15 ≤ −3y ≤ −9 ; somme : −13 ≤ 2x − 3y ≤ −5"})),
    ]),

    (1, "Les polynômes", "Développement, identités remarquables, factorisation, "
     "racines, équations-produit.", CH_POLYNOMES, [
        (1, "Manuel", "Développer : ① (x + 5)² ② (3x − 1)² ③ (2x − 7)(2x + 7)",
         "① x² + 10x + 25\n② 9x² − 6x + 1\n③ 4x² − 49",
         "Reconnaître a² + 2ab + b², a² − 2ab + b², a² − b².",
         V({"enonce": "Développer (x + 2)(x − 3).",
            "solution": "x² − 3x + 2x − 6 = x² − x − 6"})),
        (1, "Manuel", "Factoriser : ① x² − 81 ② x² + 8x + 16 ③ 5x² − 10x",
         "① x² − 9² = (x − 9)(x + 9)\n② (x + 4)²  (car 16 = 4² et 8x = 2·x·4)\n"
         "③ 5x(x − 2)  (facteur commun 5x)",
         "① différence de carrés ② carré parfait ③ facteur commun.",
         V({"enonce": "Factoriser 4x² − 12x + 9.",
            "solution": "(2x)² − 2·2x·3 + 3² = (2x − 3)²"})),
        (2, "Contrôle", "Factoriser x³ − 9x.",
         "x³ − 9x = x(x² − 9) = x(x − 3)(x + 3)",
         "Toujours chercher le facteur commun AVANT l'identité remarquable.",
         V({"enonce": "Factoriser (x + 1)² − 4.",
            "solution": "(x + 1)² − 2² = (x + 1 − 2)(x + 1 + 2) = (x − 1)(x + 3)"})),
        (2, "Contrôle", "Montrer que 2 est une racine de P(x) = x² − 3x + 2, puis "
         "factoriser P.",
         "P(2) = 4 − 6 + 2 = 0 → 2 est racine → (x − 2) facteur\n"
         "P(x) = (x − 2)(x − a) ; développons : x² − (a+2)x + 2a = x² − 3x + 2\n"
         "→ a + 2 = 3 → a = 1 ; vérif : 2a = 2 ✓\nP(x) = (x − 2)(x − 1)",
         "Si P(a) = 0, factoriser par (x − a) et identifier les coefficients.",
         V({"enonce": "Montrer que −1 est racine de x³ + 1 et factoriser.",
            "solution": "(−1)³ + 1 = 0 ; x³ + 1 = (x + 1)(x² − x + 1)"})),
        (2, "Manuel", "Résoudre : (3x + 2)(x − 5) = 0",
         "3x + 2 = 0 ou x − 5 = 0\nx = −2/3 ou x = 5\nS = {−2/3 ; 5}",
         "Équation-produit : chaque facteur annule l'équation.",
         V({"enonce": "Résoudre x(4 − x) = 0.",
            "solution": "x = 0 ou x = 4 ; S = {0 ; 4}"})),
        (3, "Type Examen Régional", "Résoudre x⁴ − 5x² + 4 = 0 (indication : poser "
         "X = x²).",
         "X = x² → X² − 5X + 4 = 0\nX = 1 ou X = 4 (1 + 4 = 5, 1×4 = 4)\n"
         "X = 1 → x² = 1 → x = ±1\nX = 4 → x² = 4 → x = ±2\nS = {−2 ; −1 ; 1 ; 2}",
         "Équation bicarrée : changement d'inconnue X = x², puis retour à x.",
         V({"enonce": "Résoudre x − 6√x + 8 = 0 (poser X = √x).",
            "solution": "X² − 6X + 8 = 0 → X = 2 ou 4 → x = 4 ou 16 (X ≥ 0) → S = {4 ; 16}"})),
    ]),

    (1, "La projection dans le plan", "Projeté orthogonal et oblique d'un point/d'un "
     "segment, propriétés de conservation, distance à une droite.", CH_PROJECTION, [
        (1, "Manuel", "ABC triangle rectangle en A, AB = 6, AC = 8. H projeté "
         "orthogonal de A sur (BC). Justifier que H ∈ [BC].",
         "Le triangle est rectangle en A → les angles en B et C sont aigus.\n"
         "La perpendiculaire à (BC) passant par A coupe donc le segment [BC] en H.\n"
         "De plus BC = √(36+64) = 10 (Pythagore).",
         "Dans un triangle rectangle, le pied de la hauteur issue de l'angle droit est sur l'hypoténuse.",
         V()),
        (2, "Contrôle", "Dans le même triangle : calculer l'aire de ABC de deux façons "
         "pour en déduire AH.",
         "Aire = AB×AC/2 = 6×8/2 = 24\nAire = BC×AH/2 = 10×AH/2 = 5AH\n"
         "5AH = 24 → AH = 4,8",
         "« Double expression de l'aire » : la technique reine pour les hauteurs.",
         V({"enonce": "Que vaut la distance de A à la droite (BC) ?",
            "solution": "C'est AH = 4,8."})),
        (2, "Manuel", "MNP rectangle en M. Que devient l'image du segment [NP] par la "
         "projection orthogonale sur la droite (MN) ?",
         "Le projeté de N est N (N ∈ (MN)).\nLe projeté de P est le pied P' de la "
         "perpendiculaire à (MN) passant par P.\nComme (MP) ⊥ (MN), P' = M.\n"
         "[NP] se projette sur [NM].",
         "Un segment perpendiculaire à la droite de projection se projette en un point ; ici P → M.",
         V()),
        (3, "Type Examen Régional", "ABCD est un carré de côté 4, E le milieu de [AB]. "
         "H est le projeté orthogonal de E sur la diagonale (AC). Montrer que EH = √2.",
         "La diagonale (AC) fait un angle de 45° avec (AB), donc EAH = 45°.\n"
         "AE = AB/2 = 2. Le triangle AEH est rectangle en H (H projeté orthogonal).\n"
         "EH = AE × sin(45°) = 2 × √2/2 = √2. ∎",
         "Projeté orthogonal + angle 45° : trigonométrie dans le triangle rectangle AEH.",
         V()),
    ]),

    (1, "La droite dans le plan", "Coefficient directeur, équations de droites, "
     "positions relatives, intersection.", CH_DROITE, [
        (1, "Manuel", "Déterminer le coefficient directeur de la droite passant par "
         "A(2 ; −1) et B(6 ; 7).",
         "m = (7 − (−1))/(6 − 2) = 8/4 = 2",
         "m = (y_B − y_A)/(x_B − x_A).",
         V({"enonce": "Droite passant par A(−2 ; 3) et B(1 ; 3). Coefficient ? Nature ?",
            "solution": "m = 0 → droite horizontale d'équation y = 3."})),
        (1, "Manuel", "Équation de la droite de coefficient directeur −3 passant par "
         "P(2 ; 5).",
         "y = −3x + p ; 5 = −3×2 + p → p = 11\nd : y = −3x + 11",
         "Remplacer les coordonnées du point pour trouver p.",
         V({"enonce": "Équation de la droite passant par O(0 ; 0) et A(4 ; −6).",
            "solution": "m = −6/4 = −3/2 ; droite passe par O → p = 0 ; y = −3x/2"})),
        (2, "Contrôle", "La droite d₁ : y = 3x − 2 est-elle parallèle à d₂ : "
         "6x − 2y = 5 ? Justifier.",
         "d₂ : 6x − 2y = 5 → −2y = −6x + 5 → y = 3x − 5/2\nm₁ = 3 = m₂ et p₁ = −2 ≠ −5/2\n"
         "→ d₁ ∥ d₂ (strictement parallèles)",
         "Mettre les deux équations sous la forme y = mx + p avant de comparer.",
         V({"enonce": "d₁ : y = 2x + 1 et d₂ : y = −x/2 + 3. Que dire ?",
            "solution": "m₁·m₂ = 2×(−1/2) = −1 → d₁ ⊥ d₂ (perpendiculaires)."})),
        (2, "Manuel", "Trouver le point d'intersection de d₁ : y = x + 1 et d₂ : "
         "y = −2x + 7.",
         "x + 1 = −2x + 7 → 3x = 6 → x = 2 ; y = 3\nI(2 ; 3)",
         "Égaler les deux expressions de y, résoudre, puis reporter.",
         V({"enonce": "d₁ : 2x + y = 3 et d₂ : x − y = 6. Intersection ?",
            "solution": "Addition : 3x = 9 → x = 3 ; y = 3 − 6 = −3 ; I(3 ; −3)"})),
        (3, "Type Examen Régional", "Soit A(1 ; 2) et d : y = 2x + 3. Déterminer "
         "l'équation de la droite Δ perpendiculaire à d passant par A, puis le projeté "
         "orthogonal H de A sur d.",
         "m(Δ)·m(d) = −1 → m(Δ) = −1/2\nΔ : y = −x/2 + p ; 2 = −1/2 + p → p = 5/2\n"
         "Δ : y = −x/2 + 5/2\nH = d ∩ Δ : 2x + 3 = −x/2 + 5/2 → (5/2)x = −1/2 → x = −1/5\n"
         "y = 2(−1/5) + 3 = 13/5",
         "Perpendiculaire : produit des coefficients = −1 ; H = intersection des 2 droites.",
         V()),
    ]),

    (2, "Transformations usuelles dans le plan", "Translation, symétries, homothétie, "
     "rotation : constructions, propriétés de conservation.", CH_TRANSFORMATIONS, [
        (1, "Manuel", "A(1 ; 2), B(4 ; −1). t est la translation de vecteur u(2 ; 3). "
         "Donner les coordonnées de A' = t(A) et B' = t(B). Que peut-on dire de [A'B'] ?",
         "A'(1+2 ; 2+3) = A'(3 ; 5)\nB'(4+2 ; −1+3) = B'(6 ; 2)\n"
         "La translation conserve les longueurs : A'B' = AB = √(9+9) = 3√2, et (A'B') ∥ (AB).",
         "Translation : on ajoute le vecteur aux deux coordonnées.",
         V()),
        (2, "Contrôle", "Que devient le point M(−2 ; 3) par la symétrie centrale de "
         "centre O(0 ; 0) ? Et par la symétrie d'axe (Ox) ?",
         "Symétrie centrale de centre O : s_O(M) = −M → M'(2 ; −3)\n"
         "Symétrie d'axe (Ox) : l'ordonnée change de signe → M''(−2 ; −3)",
         "Symétrie centrale : (x ; y) → (−x ; −y). Axe (Ox) : (x ; y) → (x ; −y).",
         V({"enonce": "Symétrie d'axe (Oy) du point N(5 ; −7) ?",
            "solution": "N'(−5 ; −7) (l'abscisse change de signe)."})),
        (2, "Manuel", "Un carré de côté 5, d'aire 25, subit une homothétie de rapport "
         "k = 1/2. Donner côté, périmètre et aire de l'image.",
         "Côté : 5 × 1/2 = 2,5\nPérimètre : 20 × 1/2 = 10\nAire : 25 × (1/2)² = 25/4 = 6,25",
         "Longueurs ×|k| ; aires ×k².",
         V({"enonce": "Et si k = −2 (même figure de départ) ?",
            "solution": "Côté 10, périmètre 40, aire 100 ; image de l'autre côté du centre O "
                        "(k < 0) et symétrique (rotation de 180° incorporée)."})),
        (2, "Manuel", "ABC est un triangle. Construire (description) l'image A'B'C' de "
         "ABC par la rotation de centre A et d'angle 90° dans le sens direct.",
         "A' = A (centre invariant).\nB' : on place, à partir de A, l'angle 90° avec [AB] "
         "(sens inverse des aiguilles) et on reporte AB : A'B' = AB.\nIdem pour C : "
         "A'C' = AC avec angle 90°.\nLe triangle A'B'C' est l'image : superposable à ABC.",
         "Rotation : centre invariant, longueurs conservées, on reporte angle puis longueur.",
         V()),
        (3, "Type Examen Régional", "Soit I le milieu de [AB] avec A(1 ; 1), B(5 ; 3). "
         "Montrer que s_I(A) = B (la symétrie centrale échange A et B), puis donner les "
         "coordonnées de I et de s_I(O) où O est l'origine.",
         "I((1+5)/2 ; (1+3)/2) = I(3 ; 2)\ns_I(A) = 2I − A = (6−1 ; 4−1) = (5 ; 3) = B ✓\n"
         "s_I(O) = 2I − O = (6 ; 4)",
         "Formule clé : s_I(M) = 2I − M (coordonnées).",
         V()),
    ]),

    (2, "Équations et inéquations trigonométriques", "Résolution avec le cercle "
     "trigonométrique : équations et inéquations en cos x et sin x.", CH_TRIGO_EQ, [
        (1, "Manuel", "Résoudre dans [0 ; 2π] : cos x = 1/2.",
         "1/2 = cos(π/3)\nLa droite verticale x = 1/2 coupe le cercle en π/3 et −π/3 "
         "(= 5π/3)\nS = {π/3 ; 5π/3}",
         "Repérer l'angle remarquable, puis le second point par symétrie.",
         V({"enonce": "Résoudre dans [0 ; 2π] : sin x = −1/2.",
            "solution": "S = {7π/6 ; 11π/6}"})),
        (2, "Contrôle", "Résoudre dans [0 ; 2π] : cos x = −√2/2.",
         "−√2/2 = cos(3π/4)\nSymétrie par rapport à l'axe (Oy) : l'autre solution est "
         "5π/4\nS = {3π/4 ; 5π/4}",
         "Pour une valeur négative de cos : solutions dans les cadrants 2 et 3.",
         V({"enonce": "Résoudre dans [0 ; 2π] : sin x = √3/2.",
            "solution": "S = {π/3 ; 2π/3}"})),
        (2, "Manuel", "Résoudre dans [−π ; π] : cos x = √3/2.",
         "√3/2 = cos(π/6)\nSur [−π ; π] : x = π/6 ou x = −π/6\nS = {−π/6 ; π/6}",
         "Attention à l'intervalle demandé : ici les solutions sont symétriques autour de 0.",
         V()),
        (2, "Contrôle", "Résoudre dans [0 ; 2π] l'inéquation : cos x > 1/2.",
         "La partie du cercle où l'abscisse > 1/2 est l'arc entre −π/3 et π/3\n"
         "Sur [0 ; 2π] : x ∈ [0 ; π/3[ ∪ ]5π/3 ; 2π]",
         "Inéquation : on REGARDE le cercle et on lit l'arc, bornes ouvertes (>) ou fermées (≥).",
         V({"enonce": "Résoudre dans [−π ; π] : sin x ≤ 0.",
            "solution": "Ordonnée négative : moitié basse du cercle → x ∈ [−π ; 0]"})),
        (3, "Type Examen Régional", "Résoudre dans [0 ; 2π] : 2cos x − √3 = 0.",
         "cos x = √3/2\n√3/2 = cos(π/6)\nS = {π/6 ; 11π/6}",
         "Isoler d'abord cos x, l'équation devient classique.",
         V({"enonce": "Résoudre dans [0 ; 2π] : √2 sin x + 1 = 0.",
            "solution": "sin x = −√2/2 → S = {5π/4 ; 7π/4}"})),
    ]),

    (2, "Produit scalaire dans le plan", "Expressions du produit scalaire, "
     "orthogonalité, calculs d'angles et de longueurs.", CH_PRODUIT_SCALAIRE, [
        (1, "Manuel", "u(3 ; −2) et v(1 ; 4). Calculer u·v, ‖u‖, ‖v‖.",
         "u·v = 3×1 + (−2)×4 = 3 − 8 = −5\n‖u‖ = √(9+4) = √13\n‖v‖ = √(1+16) = √17",
         "u·v = xx′ + yy′ ; norme = racine de la somme des carrés.",
         V({"enonce": "u(−1 ; 5) et v(2 ; −10) : u·v ? Conclusion ?",
            "solution": "−2 − 50 = −52 ≠ 0 ; les vecteurs sont colinéaires (v = −2u) "
                        "mais pas orthogonaux ; u·v = ‖u‖‖v‖cos(π) = −‖u‖‖v‖ < 0."})),
        (2, "Contrôle", "Montrer que le triangle ABC avec A(1 ; 1), B(4 ; 2), C(2 ; −2) "
         "est rectangle en A.",
         "AB(4−1 ; 2−1) = AB(3 ; 1)\nAC(2−1 ; −2−1) = AC(1 ; −3)\n"
         "AB·AC = 3×1 + 1×(−3) = 0\nAB·AC = 0 → (AB) ⊥ (AC) : triangle rectangle en A. ∎\n"
         "Bonus : AB = AC = √10 → rectangle ISOCÈLE en A.",
         "Le produit scalaire nul teste l'orthogonalité : LE réflexe du chapitre.",
         V({"enonce": "Vérifier que le triangle n'est pas rectangle en B.",
            "solution": "BA(−3 ; −1) et BC(−2 ; −4) : BA·BC = 6 + 4 = 10 ≠ 0 → non."})),
        (2, "Manuel", "Calculer l'angle entre u(1 ; 1) et v(0 ; 2).",
         "u·v = 0 + 2 = 2 ; ‖u‖ = √2 ; ‖v‖ = 2\ncos θ = 2/(2√2) = 1/√2 = √2/2\nθ = π/4",
         "cos θ = u·v/(‖u‖‖v‖), reconnaître une valeur remarquable.",
         V({"enonce": "Angle entre u(2 ; 0) et v(−2 ; 2) ?",
            "solution": "u·v = −4 ; ‖u‖ = 2 ; ‖v‖ = 2√2 ; cos θ = −4/(4√2) = −√2/2 → θ = 3π/4"})),
        (2, "Contrôle", "ABCD est un carré de côté a. Calculer AB·AC.",
         "L'angle entre AB et AC vaut 45°, et ‖AC‖ = a√2\nAB·AC = a × a√2 × cos 45° "
         "= a²√2 × √2/2 = a²",
         "Formule trigonométrique : ‖u‖‖v‖cos(angle).",
         V({"enonce": "Même carré : AB·AD ?",
            "solution": "AB ⊥ AD → AB·AD = 0."})),
        (3, "Type Examen Régional", "Soit u(4 ; 3). Déterminer les coordonnées de "
         "v(x ; y) tel que v ⊥ u et ‖v‖ = 5 (v d'abscisse positive).",
         "v ⊥ u : 4x + 3y = 0 → y = −4x/3\n‖v‖² = x² + y² = 25\n"
         "x² + 16x²/9 = 25 → 25x²/9 = 25 → x² = 9 → x = 3 (positif) ; y = −4",
         "Système : orthogonalité + norme ; résoudre par substitution.",
         V()),
    ]),

    (2, "Géométrie dans l'espace", "Repérage dans l'espace, vecteurs, distances, "
     "positions relatives.", CH_ESPACE, [
        (1, "Manuel", "A(1 ; 2 ; 0), B(4 ; 6 ; 4). Calculer AB et le milieu I de [AB].",
         "AB(3 ; 4 ; 4) → ‖AB‖ = √(9+16+16) = √41\nI((1+4)/2 ; (2+6)/2 ; (0+4)/2) = I(2,5 ; 4 ; 2)",
         "Coordonnées du vecteur = arrivée − départ ; milieu = moyennes.",
         V()),
        (2, "Contrôle", "Les points A(0 ; 1 ; 2), B(1 ; 3 ; 0), C(2 ; 5 ; −2) sont-ils "
         "alignés ?",
         "AB(1 ; 2 ; −2) ; AC(2 ; 4 ; −4)\nAC = 2·AB → colinéaires, et A commun\n"
         "→ A, B, C sont alignés.",
         "Alignés ⟺ vecteurs colinéaires (l'un multiple de l'autre).",
         V({"enonce": "Même question avec A(0;0;0), B(1;1;1), C(2;3;1).",
            "solution": "AB(1;1;1), AC(2;3;1) : AC ≠ k·AB (2/1 ≠ 3/1) → non alignés."})),
        (2, "Manuel", "Calculer la distance du point M(2 ; 3 ; 6) à l'origine O.",
         "OM = √(4 + 9 + 36) = √49 = 7",
         "Pythagore généralisé : OM = √(x²+y²+z²).",
         V({"enonce": "Distance OM pour M(1 ; 2 ; 2) ?",
            "solution": "√(1+4+4) = 3"})),
        (3, "Type Examen Régional", "ABC est un tétraèdre avec A(0 ; 0 ; 0), "
         "B(2 ; 0 ; 0), C(0 ; 2 ; 0), D(0 ; 0 ; 2). Montrer que la droite (AD) est "
         "perpendiculaire au plan (ABC).",
         "(ABC) est le plan z = 0 (trois points de cote 0).\n(AD) a pour vecteur "
         "directeur AD(0 ; 0 ; 2), porté par l'axe (Oz).\nL'axe (Oz) est perpendiculaire "
         "au plan (ABC) (il est perpendiculaire à AB et à AC, deux droites sécantes du plan).\n"
         "→ (AD) ⊥ (ABC).",
         "Perpendiculaire au plan = perpendiculaire à 2 droites sécantes du plan.",
         V()),
    ]),
]

# ---- exercices supplémentaires pour les chapitres TC déjà présents ----
EXTRA_TC = {
    "Arithmétique dans ℕ": [
        (2, "Contrôle", "Montrer que la somme de deux nombres pairs est paire.",
         "n = 2k, m = 2k' (k, k' entiers)\nn + m = 2k + 2k' = 2(k + k') → pair ✓",
         "Écriture générale : pair = 2k, impair = 2k+1.",
         V({"enonce": "Montrer que le produit d'un entier par 2 nombres consécutifs est pair.",
            "solution": "k(k+1) : deux entiers consécutifs, l'un est forcément pair → produit pair."})),
        (2, "Manuel", "Décomposer 360 en produit de facteurs premiers.",
         "360 = 36 × 10 = (6×6) × 10 = (2×3)² × (2×5)\n= 2³ × 3² × 5",
         "Diviser successivement par 2, 3, 5, 7…",
         V({"enonce": "En déduire le nombre de diviseurs de 360.",
            "solution": "(3+1)(2+1)(1+1) = 4×3×2 = 24 diviseurs."})),
        (3, "Type Examen Régional", "n est un entier. Montrer que si n² est pair, "
         "alors n est pair.",
         "Par contraposée : si n est impair, n = 2k+1 → n² = 4k² + 4k + 1 = 2(2k²+2k) + 1 "
         "→ impair.\nDonc si n² est pair, n ne peut pas être impair : n est pair. ∎",
         "Raisonnement par contraposée : « A ⟹ B » équivaut à « non B ⟹ non A ».",
         V()),
    ],
    "Équations et inéquations dans ℝ": [
        (1, "Manuel", "Résoudre le système : { x + y = 10 ; x − y = 4 }",
         "Addition : 2x = 14 → x = 7 ; y = 10 − 7 = 3\nS = {(7 ; 3)}",
         "Méthode par combinaison (addition) ou substitution.",
         V({"enonce": "Résoudre : { 2x + y = 8 ; x = 3 }",
            "solution": "x = 3 → 6 + y = 8 → y = 2 ; S = {(3 ; 2)} (substitution)."})),
        (2, "Contrôle", "Résoudre : { 2x + 3y = 12 ; 3x − 3y = 3 }",
         "Addition membre à membre : 5x = 15 → x = 3\n2(3) + 3y = 12 → 3y = 6 → y = 2\n"
         "S = {(3 ; 2)}",
         "Les y s'éliminent par addition : c'est voulu, cherche la combinaison astucieuse.",
         V({"enonce": "Un objet et un stylo coûtent 15 DH ; 2 objets et 3 stylos 36 DH. "
                      "Prix de chaque ?",
            "solution": "{ o + s = 15 ; 2o + 3s = 36 } → o = 9, s = 6 : objet 9 DH, stylo 6 DH."})),
        (3, "Type Examen Régional", "Résoudre l'inéquation : (x − 1)(x + 2) ≤ 0 "
         "(tableau de signes).",
         "Racines : x = 1 et x = −2\nSigne de (x−1)(x+2) : négatif entre les racines\n"
         "S = [−2 ; 1]",
         "Tableau de signes : racines ordonnées, signe de a à l'extérieur.",
         V({"enonce": "Résoudre : (2x + 1)(3 − x) > 0.",
            "solution": "Racines −1/2 et 3 ; produit > 0 entre les racines → S = ]−1/2 ; 3["})),
    ],
    "Configurations du plan et vecteurs": [
        (1, "Manuel", "A(1 ; 2), B(4 ; 6), C(7 ; 10). A, B, C sont-ils alignés ?",
         "AB(3 ; 4) ; AC(6 ; 8) = 2·AB → colinéaires → alignés ✓",
         "Coordonnées puis colinéarité xy′ − yx′ = 0 (ici 24 − 24 = 0).",
         V()),
        (2, "Contrôle", "Le quadrilatère ABCD avec A(0;0), B(3;1), C(4;4), D(1;3) : "
         "quelle est sa nature ?",
         "AB(3 ; 1) ; DC(3 ; 1) → AB = DC : ABCD est un parallélogramme\n"
         "AB·AD avec AD(1 ; 3) : 3×1 + 1×3 = 6 ≠ 0 (pas rectangle)\n"
         "AB = AD ? ‖AB‖ = √10 ; ‖AD‖ = √10 → losange !\nABCD est un losange (non carré).",
         "Parallélogramme : côtés opposés égaux-vecteurs ; losange : 2 côtés consécutifs de même longueur.",
         V()),
        (3, "Type Examen Régional", "Soit A(2 ; 3) et B(−1 ; 5). Déterminer les "
         "coordonnées de M tel que AM = 2AB.",
         "AB(−3 ; 2) → 2AB(−6 ; 4)\nM(x ; y) : AM = M − A = (x−2 ; y−3) = (−6 ; 4)\n"
         "→ x = −4 ; y = 7",
         "Traduire vectoriellement : AM = 2AB ⟺ M − A = 2(B − A).",
         V()),
    ],
    "Trigonométrie": [
        (1, "Manuel", "Placer sur le cercle trigonométrique les angles : π/6, 2π/3, "
         "7π/4, −π/2. Donner cos et sin de chacun.",
         "π/6 : cos = √3/2, sin = 1/2\n2π/3 : cos = −1/2, sin = √3/2\n"
         "7π/4 : cos = √2/2, sin = −√2/2\n−π/2 : cos = 0, sin = −1",
         "Le cercle d'abord : sens direct (anti-horaire), valeurs remarquables.",
         V()),
        (2, "Contrôle", "Montrer que cos(π/2 − x) = sin x (à l'aide du cercle).",
         "Le point associé à π/2 − x est le symétrique du point associé à x par rapport "
         "à la première bissectrice (y = x).\nCette symétrie échange abscisse et ordonnée "
         "→ cos(π/2 − x) = sin x ✓",
         "La symétrie par rapport à la bissectrice échange cos et sin.",
         V({"enonce": "En déduire sin(π/2 − x).",
            "solution": "sin(π/2 − x) = cos x."})),
        (2, "Manuel", "Simplifier : cos²x + sin²(π − x).",
         "sin(π − x) = sin x\ndonc cos²x + sin²x = 1",
         "Angles associés : sin(π − x) = sin x ; puis relation fondamentale.",
         V()),
    ],
    "Généralités sur les fonctions": [
        (1, "Manuel", "f(x) = (x − 2)/(x + 1). Déterminer le domaine de définition de f.",
         "x + 1 ≠ 0 → x ≠ −1\nD_f = ℝ \\ {−1} = ]−∞ ; −1[ ∪ ]−1 ; +∞[",
         "Exclure les valeurs qui annulent le dénominateur.",
         V({"enonce": "Domaine de g(x) = √(x − 3).",
            "solution": "x − 3 ≥ 0 → x ≥ 3 → D_g = [3 ; +∞["})),
        (2, "Contrôle", "f définie par f(x) = 2x + 3. Calculer le taux de variation "
         "entre x₁ = 1 et x₂ = 4. Que conclut-on ?",
         "T = (f(4) − f(1))/(4 − 1) = (11 − 5)/3 = 2\nLe taux est constant = 2 : f est "
         "affine de coefficient 2 → croissante sur ℝ.",
         "Taux constant = fonction affine, le taux EST le coefficient directeur.",
         V()),
        (2, "Manuel", "Montrer que f(x) = x² + 1 est paire, et g(x) = x³ est impaire. "
         "Interprétation graphique ?",
         "f(−x) = (−x)² + 1 = x² + 1 = f(x) → paire : symétrie par rapport à (Oy)\n"
         "g(−x) = (−x)³ = −x³ = −g(x) → impaire : symétrie par rapport à O",
         "Parité : comparer f(−x) à f(x) et −f(x).",
         V({"enonce": "h(x) = x² + 2x : paire, impaire, ni l'un ni l'autre ?",
            "solution": "h(−x) = x² − 2x ≠ h(x) et ≠ −h(x) → ni l'un ni l'autre."})),
        (3, "Type Examen Régional", "Soit f(x) = 3x − 1. Montrer que f est croissante "
         "sur ℝ à l'aide du taux de variation (a < b arbitraires).",
         "T = (f(b) − f(a))/(b − a) = (3b − 1 − 3a + 1)/(b − a) = 3(b − a)/(b − a) = 3 > 0\n"
         "Taux positif pour tous a < b → f croissante sur ℝ.",
         "Lettres génériques a < b, calculer T, conclure par son signe.",
         V()),
    ],
    "Statistiques": [
        (1, "Manuel", "Notes sur 20 : 8 ; 10 ; 12 ; 12 ; 14 ; 15 ; 15 ; 15 ; 18. "
         "Déterminer la moyenne et la médiane.",
         "Effectif n = 9 ; somme = 119\nMoyenne = 119/9 ≈ 13,2\n"
         "Données ordonnées → médiane = 5ᵉ valeur = 12\n"
         "Lecture : la moitié de la classe a une note ≤ 12.",
         "Trier les données ; médiane = valeur centrale quand n est impair.",
         V({"enonce": "Ajouter un élève noté 19 (n = 10). Nouvelle médiane ?",
            "solution": "Ordonnées : 8;10;12;12;14;15;15;15;18;19 → médiane = (14+15)/2 = 14,5"})),
        (2, "Contrôle", "Un élève a : 12 (coef 1), 15 (coef 2), 9 (coef 1). Moyenne "
         "pondérée ?",
         "(12×1 + 15×2 + 9×1)/(1+2+1) = (12 + 30 + 9)/4 = 51/4 = 12,75",
         "Moyenne pondérée = Σ(n_i·x_i)/Σn_i.",
         V({"enonce": "Ajouter un 18 (coef 2). Nouvelle moyenne ?",
            "solution": "(51 + 36)/6 = 87/6 = 14,5"})),
        (2, "Manuel", "Série : 5 ; 7 ; 7 ; 8 ; 20. Comparer moyenne et médiane. "
         "Laquelle résume le mieux ?",
         "Moyenne = 47/5 = 9,4 ; médiane = 7\nLa valeur extrême 20 « tire » la moyenne "
         "vers le haut.\nLa médiane (7) résume mieux le centre de la série ici.",
         "Valeur aberrante → la médiane est plus robuste que la moyenne.",
         V()),
        (3, "Type Examen Régional", "Dans une classe de 40 élèves, l'effectif cumulé "
         "croissant atteint 10 pour la note 10 et 30 pour la note 14. Combien "
         "d'élèves ont une note dans ]10 ; 14] ? Combien ont ≤ 14 ?",
         "]10 ; 14] : 30 − 10 = 20 élèves\n≤ 14 : 30 élèves",
         "Lire un effectif CUMULÉ : différence entre deux valeurs cumulées.",
         V()),
    ],
}


def sync(db):
    """Ajoute les chapitres manquants + les exercices additionnels (non destructif)."""
    import json as _json

    def ensure_semestre_column():
        cols = [r["name"] for r in db.query("PRAGMA table_info(chapters)")]
        if "semestre" not in cols:
            db.execute("ALTER TABLE chapters ADD COLUMN semestre INTEGER DEFAULT 1")

    ensure_semestre_column()
    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    n_ch = n_ex = 0

    # 1) nouveaux chapitres TC maths
    for semestre, titre, resume, lecon, exos in NEW_CHAPTERS:
        exists = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                          "AND titre = ?", (subjects["MATH"], titre), one=True)
        if not exists:
            cid = db.execute(
                "INSERT INTO chapters(subject_id, niveau, semestre, titre, resume, lecon) "
                "VALUES (?,?,?,?,?,?)",
                (subjects["MATH"], "TC", semestre, titre, resume,
                 _json.dumps(lecon, ensure_ascii=False)))
            n_ch += 1
        else:
            cid = exists["id"]
        # exercices du nouveau chapitre (tous absents par construction, on vérifie quand même)
        for diff, source, enonce, solution, astuce, variantes in exos:
            dupe = db.query("SELECT id FROM exercises WHERE chapter_id = ? AND enonce = ?",
                            (cid, enonce), one=True)
            if not dupe:
                db.execute(
                    "INSERT INTO exercises(chapter_id, difficulte, source, enonce, solution, "
                    "astuce, variantes) VALUES (?,?,?,?,?,?,?)",
                    (cid, diff, source, enonce, solution, astuce,
                     _json.dumps(variantes, ensure_ascii=False)))
                n_ex += 1

    # 2) enrichissement des chapitres existants
    for titre, exos in EXTRA_TC.items():
        ch = db.query("SELECT id FROM chapters WHERE titre = ? AND niveau = 'TC' "
                      "AND subject_id = ?", (titre, subjects["MATH"]), one=True)
        if not ch:
            continue
        for diff, source, enonce, solution, astuce, variantes in exos:
            dupe = db.query("SELECT id FROM exercises WHERE chapter_id = ? AND enonce = ?",
                            (ch["id"], enonce), one=True)
            if not dupe:
                db.execute(
                    "INSERT INTO exercises(chapter_id, difficulte, source, enonce, solution, "
                    "astuce, variantes) VALUES (?,?,?,?,?,?,?)",
                    (ch["id"], diff, source, enonce, solution, astuce,
                     _json.dumps(variantes, ensure_ascii=False)))
                n_ex += 1

    # 3) semestres des anciens chapitres TC maths
    SEMESTRES = {"Arithmétique dans ℕ": 1, "Équations et inéquations dans ℝ": 1,
                 "Configurations du plan et vecteurs": 1, "Trigonométrie": 1,
                 "Généralités sur les fonctions": 2, "Statistiques": 2}
    for titre, sem in SEMESTRES.items():
        db.execute("UPDATE chapters SET semestre = ? WHERE titre = ? AND niveau = 'TC' "
                   "AND subject_id = ?", (sem, titre, subjects["MATH"]))

    print(f"[sync TC math] +{n_ch} chapitres, +{n_ex} exercices")
