# -*- coding: utf-8 -*-
"""
seed_curriculum.py — Matières, chapitres (TC & 1BAC), leçons multi-méthodes
et banque d'exercices, conformes au programme marocain (Ministère de
l'Éducation Nationale). Les sources "Type Examen National/Régional" désignent
des exercices d'entraînement dans le style des examens officiels.
"""
import json

SUBJECTS = [
    ("MATH", "Mathématiques", "#2563eb", "📐"),
    ("PC", "Physique-Chimie", "#dc2626", "⚗️"),
    ("SVT", "Sciences de la Vie et de la Terre", "#059669", "🧬"),
    ("FR", "Français", "#d97706", "📖"),
]

# --------------------------------------------------------------- LEÇONS ----
# lecon = {"intro", "methodes":[{nom,texte}], "exemples":[{question,etapes,reponse}],
#          "pieges":[...], "formules":[...]}

LECON_LIMITES = {
    "intro": "La limite décrit le comportement d'une fonction quand x se rapproche "
             "d'une valeur (finie ou infinie). C'est LA porte d'entrée de l'analyse "
             "en 1ère Bac : presque tout (continuité, dérivation, suites) s'appuie dessus.",
    "methodes": [
        {"nom": "Méthode 1 — intuitive (la courbe)",
         "texte": "Dessine mentalement la courbe et demande-toi : vers quelle hauteur "
                  "les points s'approchent-ils ? Ex : pour f(x)=1/x quand x→+∞, la courbe "
                  "colle à l'axe des x → la limite est 0. L'intuition graphique évite 80% "
                  "des erreurs de calcul."},
        {"nom": "Méthode 2 — les règles de priorité (calcul formel)",
         "texte": "En ±∞ pour un quotient de polynômes : garde uniquement le terme de "
                  "plus haut degré au numérateur ET au dénominateur, puis simplifie. "
                  "En un point fini : remplace d'abord. Si tu obtiens 0/0 → il faut "
                  "transformer (factoriser, quantité conjuguée…)."},
        {"nom": "Méthode 3 — les formes indéterminées (4 au programme)",
         "texte": "+∞−∞, 0×∞, 0/0, ∞/∞. Ce ne sont PAS des réponses, ce sont des "
                  "signaux : « il reste du travail ». Factorise par le terme dominant, "
                  "utilise les valeurs remarquables (ex : (cos x −1)/x² → −1/2 quand x→0), "
                  "ou le taux d'accroissement."},
    ],
    "exemples": [
        {"question": "Calculer lim (x→+∞) (3x² − 2x + 1)/(x² + 5)",
         "etapes": ["Forme ∞/∞ : indéterminée.",
                    "Terme dominant en haut : 3x² ; en bas : x².",
                    "La limite du quotient = quotient des limites des termes dominants = 3/1."],
         "reponse": "lim = 3"},
        {"question": "Calculer lim (x→2) (x² − 4)/(x − 2)",
         "etapes": ["On remplace : (4−4)/(2−2) = 0/0 → indéterminé.",
                    "On factorise le numérateur : x² − 4 = (x−2)(x+2).",
                    "On simplifie : (x−2)(x+2)/(x−2) = x+2 (valable car x≠2).",
                    "On remplace : 2+2 = 4."],
         "reponse": "lim = 4"},
    ],
    "pieges": [
        "Écrire « lim = 0/0 » : une forme indéterminée n'est jamais un résultat final.",
        "Oublier de justifier par les limites de référence (√x → +∞, cos x borné…).",
        "Confondre « la limite n'existe pas » et « la limite est infinie ».",
    ],
    "formules": [
        "lim (x→+∞) 1/xⁿ = 0 (n ≥ 1)",
        "lim (x→0⁺) 1/x = +∞   ;   lim (x→0⁻) 1/x = −∞",
        "lim (x→0) sin x / x = 1",
    ],
}

LECON_SUITES = {
    "intro": "Une suite est une liste numérotée u₀, u₁, u₂… L'objectif du chapitre : "
             "comprendre sa nature (arithmétique/géométrique), son sens de variation "
             "et sa limite. Le raisonnement par récurrence apparaît ici pour la 1ère fois.",
    "methodes": [
        {"nom": "Méthode 1 — reconnaître la nature",
         "texte": "u_{n+1} − u_n = constante → arithmétique (raison r). "
                  "u_{n+1} / u_n = constante ≠ 0 → géométrique (raison q). "
                  "Si le quotient ou la différence dépend de n → ni l'un ni l'autre : "
                  "étudie la variation par u_{n+1} − u_n."},
        {"nom": "Méthode 2 — formules de cours à connaître par cœur",
         "texte": "Arithmétique : u_n = u₀ + n·r ; somme = (nb de termes)×(1er + dernier)/2. "
                  "Géométrique : u_n = u₀·qⁿ ; somme = u₀·(1−q^{n+1})/(1−q). "
                  "Ce sont les 2 formules qui rapportent le plus de points aux examens."},
        {"nom": "Méthode 3 — le raisonnement par récurrence",
         "texte": "3 étapes obligatoires : ① Initialisation (vrai au rang 0), "
                  "② Hérédité (si vrai au rang n, alors vrai au rang n+1), "
                  "③ Conclusion (vrai pour tout n). Rédige toujours ces 3 titres : "
                  "le correcteur note étape par étape."},
    ],
    "exemples": [
        {"question": "u_n = 3n + 2. Nature, raison, u₁₀ ?",
         "etapes": ["u_{n+1} − u_n = 3(n+1)+2 − (3n+2) = 3 = constante.",
                    "Donc arithmétique de raison r = 3 et u₀ = 2.",
                    "u_n = u₀ + n·r → u₁₀ = 2 + 30 = 32."],
         "reponse": "Arithmétique, r = 3, u₁₀ = 32"},
        {"question": "Somme 1 + 2 + 4 + … + 2¹⁰",
         "etapes": ["Suite géométrique v_n = 2ⁿ (u₀ = 1, q = 2), 11 termes (n = 0…10).",
                    "S = u₀(1 − q¹¹)/(1 − q) = (1 − 2¹¹)/(1 − 2) = 2¹¹ − 1."],
         "reponse": "S = 2047"},
    ],
    "pieges": [
        "Confondre le nombre de termes n+1 avec l'indice n dans les sommes.",
        "Utiliser u_n = u₀ + nr pour une suite NON arithmétique.",
        "En récurrence : oublier l'initialisation = 0 point même si le reste est juste.",
    ],
    "formules": [
        "u_n = u₀ + nr  (arithmétique)",
        "u_n = u₀·qⁿ  (géométrique)",
        "1+2+…+n = n(n+1)/2",
        "1+q+q²+…+qⁿ = (1−q^{n+1})/(1−q), q ≠ 1",
    ],
}

LECON_MOLE = {
    "intro": "La mole est « la paquet géant » des chimistes : 1 mole = 6,02×10²³ entités "
             "(constante d'Avogadro N_A). Tout le calcul chimique du lycée repose sur "
             "n = m/M et C = n/V.",
    "methodes": [
        {"nom": "Méthode 1 — le triangle des unités",
         "texte": "m (g) = n (mol) × M (g/mol) et n = C (mol/L) × V (L). "
                  "Dessine un triangle : masque ce que tu cherches, il apparaît. "
                  "Réflexe : écrire les unités à chaque ligne — c'est noté et ça évite "
                  "les erreurs de facteur 1000 (mL vs L)."},
        {"nom": "Méthode 2 — la masse molaire pas à pas",
         "texte": "M(molécule) = somme des masses atomiques. Ex : M(H₂SO₄) = 2×1 + 32 + "
                  "4×16 = 98 g/mol. Utilise la classification périodique donnée aux examens."},
        {"nom": "Méthode 3 — la dilution en 3 lignes",
         "texte": "Diluer ne change pas la quantité de matière : n₁ = n₂ donc C₁V₁ = C₂V₂. "
                  "Toujours : ① écrire la relation, ② isoler l'inconnue, ③ convertir les "
                  "volumes en L avant de calculer."},
    ],
    "exemples": [
        {"question": "Quantité de matière dans 36 g d'eau ? M(H₂O) = 18 g/mol",
         "etapes": ["n = m/M", "n = 36/18", "n = 2 mol"],
         "reponse": "n = 2 mol (soit 2 × 6,02×10²³ = 1,204×10²⁴ molécules)"},
        {"question": "Concentration de 5,85 g de NaCl (M = 58,5 g/mol) dans 500 mL ?",
         "etapes": ["n = m/M = 5,85/58,5 = 0,1 mol",
                    "V = 500 mL = 0,5 L",
                    "C = n/V = 0,1/0,5 = 0,2 mol/L"],
         "reponse": "C = 0,2 mol/L"},
    ],
    "pieges": [
        "Oublier de convertir mL → L (facteur 1000 !).",
        "Confondre masse molaire atomique et moléculaire.",
        "Diviser par V en mL au lieu de L dans C = n/V.",
    ],
    "formules": ["n = m/M", "n = C×V", "C₁V₁ = C₂V₂ (dilution)", "C_m = m/V (concentration massique)"],
}

LECON_ARGU_FR = {
    "intro": "Le texte argumentatif défend une thèse (un point de vue) à l'aide "
             "d'arguments appuyés par des exemples. Tu le retrouveras partout : essai, "
             "article de presse, lettre ouverte — et au examen régional.",
    "methodes": [
        {"nom": "Méthode 1 — repérer la structure",
         "texte": "Cherche : ① la thèse (souvent en tête ou en conclusion), "
                  "② les connecteurs logiques (d'abord, ensuite, cependant, ainsi, "
                  "par conséquent…) qui organisent les arguments, "
                  "③ les exemples introduits par « par exemple », « ainsi », « comme »."},
        {"nom": "Méthode 2 — le schéma argumentatif",
         "texte": "Chaque paragraphe = 1 argument : Argument (idée générale) → "
                  "Explication (pourquoi c'est vrai) → Exemple (fait concret). "
                  "Pour l'écriture d'un essai, prépare toujours ce trio pour chaque partie."},
        {"nom": "Méthode 3 — prendre position avec nuance",
         "texte": "Un bon devoir reconnaît l'opinion adverse (« Certes… mais », "
                  "« Il est vrai que… cependant ») avant de la réfuter. C'est ce que les "
                  "correcteurs appellent la « nuance » : vis 2 arguments pour, 1 contre nuancé."},
    ],
    "exemples": [
        {"question": "Analyser : « Le portable est utile en classe. En effet, il donne accès "
                     "aux dictionnaires en un clic ; ainsi, les élèves gagnent du temps. »",
         "etapes": ["Thèse : le portable est utile en classe.",
                    "Argument 1 : accès aux dictionnaires (connecteur « En effet »).",
                    "Argument 2 : gain de temps (connecteur « ainsi »)."],
         "reponse": "Structure thèse → argument → conséquence, sans exemple concret ici."},
    ],
    "pieges": [
        "Confondre argument (idée) et exemple (illustration).",
        "Résumer le texte au lieu d'analyser la démarche de l'auteur.",
        "Oublier les connecteurs logiques dans ta propre production.",
    ],
    "formules": ["Thèse + arguments + exemples = texte argumentatif",
                 "Connecteurs d'addition / cause / conséquence / concession"],
}

LECON_GENETIQUE = {
    "intro": "La génétique humaine explique la transmission des caractères (groupe "
             "sanguin, maladies héréditaires…) via les gènes portés par les chromosomes. "
             "Aux examens : croisements et arbres généalogiques.",
    "methodes": [
        {"nom": "Méthode 1 — le croisement simple (tableau de Punnett)",
         "texte": "① Écris les génotypes des parents (ex : Aa × Aa). ② Liste les gamètes "
                  "de chacun (A, a). ③ Remplis le tableau → ¼ AA, ½ Aa, ¼ aa. "
                  "④ Traduis en phénotypes selon la dominance."},
        {"nom": "Méthode 2 — lire un arbre généalogique",
         "texte": "Carré = homme, rond = femme, plein = malade. Si 2 parents sains ont un "
                  "enfant malade → le caractère est récessif et les parents sont "
                  "hétérozygotes. Si la maladie touche surtout les hommes → pense au "
                  "chromosome X (récessif lié à X)."},
    ],
    "exemples": [
        {"question": "Croisement AA × aa : génotypes et phénotypes en F1 ?",
         "etapes": ["Gamètes : A côté de a.", "F1 : 100 % Aa.",
                    "Si A dominant : phénotype [A] pour tous."],
         "reponse": "F1 = 100 % hétérozygotes, phénotype dominant"},
    ],
    "pieges": [
        "Confondre génotype (allèles) et phénotype (caractère observable).",
        "Oublier que 2 parents sains peuvent avoir un enfant malade (récessivité).",
    ],
    "formules": ["F1 de Aa×Aa : 1/4 AA, 1/2 Aa, 1/4 aa → 3/4 dominant"],
}

# Chapitres : (matière, niveau, titre, resume, lecon ou None)
CHAPTERS = [
    # ---------------- MATH TC ----------------
    ("MATH", "TC", "Arithmétique dans ℕ", "Divisibilité, nombres premiers, PGCD & PPCM, "
     "décomposition en facteurs premiers.", {
        "intro": "L'arithmétique étudie les entiers naturels : divisibilité, multiples, "
                 "diviseurs, PGCD. Outils essentiels pour tout le reste du programme.",
        "methodes": [
            {"nom": "Méthode 1 — divisibilité",
             "texte": "b divise a ⟺ a = b·k (k ∈ ℕ). Règles rapides : par 2 (dernier chiffre "
                      "pair), 3 (somme des chiffres multiple de 3), 4, 5, 9, 11 (différence "
                      "alternée des chiffres)."},
            {"nom": "Méthode 2 — PGCD par l'algorithme d'Euclide",
             "texte": "PGCD(a, b) : divise a par b, garde le reste, recommence jusqu'à reste 0. "
                      "Le dernier diviseur non nul est le PGCD. Ex : PGCD(252,198) → "
                      "252=1×198+54 ; 198=3×54+36 ; 54=1×36+18 ; 36=2×18+0 → PGCD=18."},
            {"nom": "Méthode 3 — décomposition en facteurs premiers",
             "texte": "Décompose en 2×3×5×7… puis PGCD = produit des facteurs communs avec "
                      "le plus petit exposant ; PPCM = produit de tous avec le plus grand exposant."},
        ],
        "pieges": ["1 n'est pas premier.", "Confondre PGCD (divise) et PPCM (multiple)."],
    }),
    ("MATH", "TC", "Généralités sur les fonctions", "Domaine de définition, image, antécédent, "
     "parité, sens de variation, taux de variation.",
     {"intro": "Vocabulaire et lecture graphique des fonctions : la base de l'analyse.",
      "methodes": [
          {"nom": "Méthode 1 — domaine de définition",
           "texte": "Exclus : dénominateur nul, radicande négatif. Résous les inéquations/"
                    "équations correspondantes et conclus avec un intervalle."},
          {"nom": "Méthode 2 — taux de variation et variations",
           "texte": "T = (f(b)−f(a))/(b−a). Si T ≥ 0 sur un intervalle → f croissante "
                    "(pour les fonctions usuelles). Parité : f(−x)=f(x) paire (symétrie axe y), "
                    "f(−x)=−f(x) impaire (symétrie origine)."},
      ],
      "pieges": ["Confondre image (calcul direct) et antécédent (résoudre f(x)=k)."]}),
    ("MATH", "TC", "Équations et inéquations dans ℝ", "Équations 1er degré, 2nd degré, "
     "signe du trinôme, équations avec valeur absolue.",
     {"intro": "Résoudre une équation = transformer par des opérations réversibles "
               "jusqu'à isoler x.",
      "methodes": [
          {"nom": "Méthode 1 — 2nd degré par le discriminant",
           "texte": "ax²+bx+c=0 : Δ=b²−4ac. Δ>0 : x=(−b±√Δ)/2a. Δ=0 : x=−b/2a. "
                    "Δ<0 : pas de solution réelle. Signe du trinôme : signe de a à "
                    "l'extérieur des racines, − entre les racines (si Δ>0)."},
          {"nom": "Méthode 2 — valeur absolue",
           "texte": "|X|=k (k≥0) ⟺ X=k ou X=−k. |X|≤k ⟺ −k≤X≤k. |X|≥k ⟺ X≤−k ou X≥k. "
                    "Toujours isoler la valeur absolue d'abord."},
      ],
      "pieges": ["Diviser par x sans discuter x=0.", "Oublier les 2 cas de |X|=k."]}),
    ("MATH", "TC", "Configurations du plan et vecteurs", "Colinéarité, repères, coordonnées, "
     "équations de droites.",
     {"intro": "Le calcul vectoriel traduit la géométrie en calcul : distances, alignement, "
               "parallélisme.",
      "methodes": [
          {"nom": "Méthode 1 — vecteurs et colinéarité",
           "texte": "u(x;y), v(x';y') colinéaires ⟺ x·y′ − y·x′ = 0. Alignement de A,B,C : "
                    "montre AB et AC colinéaires. Parallélisme de droites : vecteurs directeurs colinéaires."},
          {"nom": "Méthode 2 — équations de droites",
           "texte": "y = mx + p (m=pente) ou ax+by+c=0. Pente entre 2 points : "
                    "m=(y_B−y_A)/(x_B−x_A). Droites sécantes : pentes différentes ; "
                    "parallèles : même pente."},
      ],
      "pieges": ["Diviser par une pente nulle (droite horizontale)."]}),
    ("MATH", "TC", "Trigonométrie", "Cercle trigonométrique, cosinus/sinus d'angles remarquables, "
     "équations trigonométriques.",
     {"intro": "Le cercle trigo associe à chaque réel un point : cos = abscisse, sin = ordonnée.",
      "methodes": [
          {"nom": "Méthode 1 — le cercle d'abord",
           "texte": "Place l'angle, lis cos (horizontal) et sin (vertical). Angles remarquables "
                    "à connaître : 0, π/6, π/4, π/3, π/2 et leurs symétriques."},
          {"nom": "Méthode 2 — équations de base",
           "texte": "cos x = cos a ⟺ x = a + 2kπ ou x = −a + 2kπ. "
                    "sin x = sin a ⟺ x = a + 2kπ ou x = π − a + 2kπ. "
                    "Toujours préciser l'intervalle demandé."},
      ],
      "pieges": ["Donner toutes les solutions au lieu de celles de l'intervalle demandé."]}),
    ("MATH", "TC", "Statistiques", "Effectifs, fréquences, moyenne, médiane, quartiles, "
     "diagrammes.",
     {"intro": "Organiser des données et les résumer par des indicateurs.",
      "methodes": [
          {"nom": "Méthode 1 — moyenne et médiane",
           "texte": "Moyenne = Σ(n_i·x_i)/N. Médiane : valeur centrale des données ordonnées "
                    "(effectif cumulé N/2). Quartiles Q1, Q3 : positions N/4 et 3N/4."},
      ],
      "pieges": ["Moyenne pondérée : ne pas diviser par le nombre de valeurs au lieu de N."]}),

    # ---------------- MATH 1BAC ----------------
    ("MATH", "1BAC", "Suites numériques", "Nature (arithmétique/géométrique), variation, "
     "limites, récurrence, sommes célèbres.", LECON_SUITES),
    ("MATH", "1BAC", "Limites et continuité", "Limites de référence, formes indéterminées, "
     "continuité en un point, théorème des valeurs intermédiaires.", LECON_LIMITES),
    ("MATH", "1BAC", "Dérivation", "Nombre dérivé, fonction dérivée, sens de variation, "
     "extremums.",
     {"intro": "La dérivée mesure la vitesse de changement : f'(a) = pente de la tangente en a.",
      "methodes": [
          {"nom": "Méthode 1 — les formules de dérivation",
           "texte": "(xⁿ)' = n·xⁿ⁻¹ ; (u+v)' = u'+v' ; (u·v)' = u'v+uv' ; "
                    "(u/v)' = (u'v−uv')/v² ; (√u)' = u'/(2√u). "
                    "Ex : (3x³)' = 9x²."},
          {"nom": "Méthode 2 — étude complète de fonction",
           "texte": "① Domaine. ② f'(x), signe de f'. ③ Tableau de variations. "
                    "④ Tangentes remarquables, extremums (f' s'annule en changeant de signe). "
                    "⑤ Courbe. Ce plan vaut des points à chaque examen."},
      ],
      "pieges": ["Oublier de factoriser f'(x) avant d'étudier son signe.",
                 "Extremum : f'(x₀)=0 ne suffit pas (voir x³ en 0)."]}),
    ("MATH", "1BAC", "Dénombrement", "Principe additif/multiplicatif, arrangements, "
     "permutations, combinaisons.",
     {"intro": "Compter sans énumérer : arrangements (ordre, sans répétition), "
               "combinaisons (sans ordre).",
      "methodes": [
          {"nom": "Méthode 1 — ordre ou pas ordre ?",
           "texte": "L'ordre compte (classement, code, podium) → arrangements A(n,p)=n!/(n−p)!. "
                    "L'ordre ne compte pas (comité, main de cartes) → combinaisons "
                    "C(n,p)=n!/(p!(n−p)!)."},
          {"nom": "Méthode 2 — binôme et propriétés",
           "texte": "(a+b)ⁿ = Σ C(n,k)·aⁿ⁻ᵏ·bᵏ. Symétrie C(n,p)=C(n,n−p) ; "
                    "Pascal : C(n,p)+C(n,p+1)=C(n+1,p+1)."},
      ],
      "pieges": ["Confondre A et C.", "Oublier les cas « tout » et « aucun »."]}),
    ("MATH", "1BAC", "Probabilités", "Univers, événements, équiprobabilité, probabilités "
     "conditionnelles (introduction).",
     {"intro": "P(A) = cas favorables / cas possibles (équiprobabilité).",
      "methodes": [
          {"nom": "Méthode 1 — dénombrer puis diviser",
           "texte": "① Décris l'univers Ω et compte-le. ② Compte les cas favorables. "
                    "③ Divise. Pour plusieurs tirages : attention remise / sans remise."},
          {"nom": "Méthode 2 — événements composés",
           "texte": "P(A∪B) = P(A)+P(B)−P(A∩B). Contraire : P(Ā) = 1 − P(A). "
                    "Souvent plus rapide de passer par le contraire."},
      ],
      "pieges": ["Additionner des probabilités d'événements non disjoints sans soustraire l'intersection."]}),

    # ---------------- PC TC ----------------
    ("PC", "TC", "L'atome et la structure de la matière", "Modèles atomiques, numéro "
     "atomique Z, nombre de masse A, isotopes, ions.",
     {"intro": "L'atome : noyau (protons + neutrons) et électrons. Z = protons, "
               "A = nucléons. La charge globale est nulle (atome) ou signée (ion).",
      "methodes": [
          {"nom": "Méthode 1 — lire un symbole nucléaire",
           "texte": "^A_Z X : Z = protons = électrons (atome neutre) ; A = protons + neutrons "
                    "→ neutrons = A − Z. Isotopes : même Z, A différent."},
      ],
      "pieges": ["Confondre A (masse) et Z (charge)."]}),
    ("PC", "TC", "La mole et les concentrations", "Quantité de matière, masse molaire, "
     "concentration molaire et massique, dilution.", LECON_MOLE),
    ("PC", "TC", "Les mélanges et la pureté", "Miscibilité, dissolution, extraction, "
     "chromatographie.",
     {"intro": "Un mélange homogène est microscopiquement uniforme ; hétérogène sinon.",
      "methodes": [
          {"nom": "Méthode 1 — séparer un mélange",
           "texte": "Décantation (2 phases non miscibles), filtration (solide/liquide), "
                    "distillation (2 liquides miscibles, différence de température "
                    "d'ébullition), chromatographie (tester la pureté)."},
      ],
      "pieges": ["Confondre soluté (dissous) et solvant (qui dissout)."]}),
    ("PC", "TC", "Principe des actions réciproques", "Forces, interactions, principe des "
     "actions réciproques (3e loi de Newton).",
     {"intro": "Toute force exercée par A sur B est accompagnée d'une force de B sur A, "
               "de même intensité, même droite, sens opposé.",
      "methodes": [
          {"nom": "Méthode 1 — identifier les actions",
           "texte": "Actions de contact (poussée, frottement) et à distance (pesanteur, "
                    "électrique). Schématise : point d'application, droite d'action, sens, intensité."},
          {"nom": "Méthode 2 — tester le principe",
           "texte": "La Terre attire la Lune (poids) ⟺ la Lune attire la Terre : même "
                    "intensité, directions identiques, sens opposés — même si les masses "
                    "sont très différentes !"},
      ],
      "pieges": ["Croire que la Terre « tire plus fort » que la Lune ne tire la Terre."]}),

    # ---------------- PC 1BAC ----------------
    ("PC", "1BAC", "Cinématique et lois de Newton", "Référentiels, vitesse, accélération, "
     "première, deuxième et troisième lois de Newton.",
     {"intro": "La cinématique décrit le mouvement (vitesse, accélération) ; la dynamique "
               "l'explique par les forces (ΣF = m·a).",
      "methodes": [
          {"nom": "Méthode 1 — résoudre un exercice de mécanique",
           "texte": "① Système + référentiel. ② Bilan des forces (schéma !). ③ 2e loi de "
                    "Newton : ΣF = m·a (projection sur les axes). ④ Intégrer pour obtenir "
                    "v(t) puis x(t). ⑤ Application numérique avec unités SI."},
          {"nom": "Méthode 2 — chute libre",
           "texte": "Seul le poids agit : a = g = 9,8 m/s². Chute verticale sans vitesse "
                    "initiale : v = g·t et h = ½g·t², d'où v = √(2gh)."},
      ],
      "pieges": ["Confondre masse (kg, invariante) et poids (N, P = mg).",
                 "Oublier de convertir km/h → m/s (÷3,6)."]}),
    ("PC", "1BAC", "Énergie mécanique", "Travail d'une force, énergies cinétique et "
     "potentielle, conservation, frottements.",
     {"intro": "Ec = ½mv², Ep = mgh (près de la Terre), Em = Ec + Ep. Sans frottement, "
               "Em = constante.",
      "methodes": [
          {"nom": "Méthode 1 — théorème de l'énergie cinétique",
           "texte": "ΔEc = ΣW(forces). Puissant pour trouver une vitesse sans cinématique : "
                    "chute de hauteur h sans frottement → ½mv² = mgh → v = √(2gh)."},
          {"nom": "Méthode 2 — bilan d'énergie",
           "texte": "Si Em diminue, l'énergie perdue = travail des frottements : "
                    "W_f = Em(final) − Em(initial) < 0. Les examens adorent cette question."},
      ],
      "pieges": ["Oublier le travail du poids quand la trajectoire n'est pas horizontale."]}),
    ("PC", "1BAC", "Phénomènes périodiques et ondes", "Période, fréquence, ondes "
     "mécaniques, lumineuses et sonores.",
     {"intro": "Un phénomène périodique se répète après une période T ; f = 1/T (Hz). "
               "Une onde transporte de l'énergie sans transport de matière.",
      "methodes": [
          {"nom": "Méthode 1 — lire un oscillogramme",
           "texte": "Période T = durée d'un motif complet (attention à la sensibilité "
                    "temporelle en ms/div). f = 1/T. Amplitude = valeur maximale."},
          {"nom": "Méthode 2 — spectre et lumière",
           "texte": "Lumière visible : 400 nm (violet) à 800 nm (rouge). Lumière "
                    "monochromatique = une seule fréquence ; polychromatique = plusieurs."},
      ],
      "pieges": ["Confondre période spatiale et temporelle.", "Unités : ms vs μs."]}),
    ("PC", "1BAC", "Suivi d'une transformation et dosage", "Avancement, réactif limitant, "
     "vitesse de réaction, dosage acido-basique.",
     {"intro": "L'avancement x suit la transformation ; à l'équivalence de titrage, les "
               "réactifs sont dans les proportions stœchiométriques.",
      "methodes": [
          {"nom": "Méthode 1 — tableau d'avancement",
           "texte": "① Écris l'équation ajustée. ② Colonnes x=0, x, x_max. ③ n(final) = "
                    "n(initial) ± coef·x. ④ Réactif limitant : celui qui annule x le plus petit."},
          {"nom": "Méthode 2 — titrage",
           "texte": "À l'équivalence : n(acide) = n(base) (pour un couple 1/1), donc "
                    "C_a·V_a = C_b·V_b. Repère l'équivalence par le saut de pH ou le "
                    "changement de couleur de l'indicateur."},
      ],
      "pieges": ["Oublier d'équilibrer l'équation avant le tableau.",
                 "Confondre équivalence et neutralisation quelconque."]}),

    # ---------------- SVT TC ----------------
    ("SVT", "TC", "La cellule, unité de la vie", "Structure cellulaire, organites, "
     "cellule animale vs végétale.",
     {"intro": "Toute cellule possède une membrane, un cytoplasme et de l'ADN ; les "
               "cellules eucaryotes ont un noyau et des organites spécialisés.",
      "methodes": [
          {"nom": "Méthode 1 — comparer animale et végétale",
           "texte": "Végétale UNIQUEMENT : paroi de cellulose, chloroplastes, grande vacuole. "
                    "Communes : membrane, noyau, cytoplasme, mitochondries."},
      ],
      "pieges": ["La paroi n'est pas la membrane !"]}),
    ("SVT", "TC", "Biodiversité et classification", "Critères de classification, clés de "
     "détermination, emboîtements d'embranchement.",
     {"intro": "Classer = regrouper selon des critères scientifiques (pas d'utilité "
               "humaine) : la clé de détermination est l'outil du chapitre.",
      "methodes": [
          {"nom": "Méthode 1 — utiliser une clé de détermination",
           "texte": "Descends les choix 1a/1b… en observant le document : chaque étape "
                    "élimine un groupe jusqu'au nom de l'espèce."},
      ],
      "pieges": ["Classifier selon la taille ou l'« utilité » = critère non scientifique."]}),
    ("SVT", "TC", "Origines géologiques de la vie", "Strates, datation relative, fossiles, "
     "principales étapes de l'histoire de la Terre.",
     {"intro": "Les strates se superposent : la plus basse est la plus ancienne "
               "(principe de superposition) ; les fossiles datent et caractérisent les époques.",
      "methodes": [
          {"nom": "Méthode 1 — dater relativement",
           "texte": "① Superposition : dessous = ancien. ② Continuité : une strate a le même "
                    "âge latéralement. ③ Fossiles caractéristiques : même fossile = même époque."},
      ],
      "pieges": ["Une faille est plus jeune que les strates qu'elle coupe."]}),

    # ---------------- SVT 1BAC ----------------
    ("SVT", "1BAC", "Tectonique des plaques et magmatisme", "Structure du globe, "
     "divergence/convergence, roches magmatiques.",
     {"intro": "La lithosphère est découpée en plaques en mouvement : divergence "
               "(dorsales) et convergence (subduction, collision).",
      "methodes": [
          {"nom": "Méthode 1 — exploiter un document géologique",
           "texte": "① Lis la légende AVANT. ② Identifie la coupe (transect). ③ Repère les "
                    "structures (failles, fosses, dorsales). ④ Relie au contexte "
                    "divergence/convergence et au magmatisme associé."},
      ],
      "pieges": ["Confondre lithosphère (rigide) et asthénosphère (ductile)."]}),
    ("SVT", "1BAC", "Génétique humaine", "Gènes, allèles, croisements, arbres généalogiques, "
     "hérédité liée au sexe.", LECON_GENETIQUE),
    ("SVT", "1BAC", "Immunologie", "SOI et non-SOI, réponse innée et acquise, lymphocytes "
     "B et T, anticorps.",
     {"intro": "Le système immunitaire distingue le SOI du non-SOI : barrières + réponse "
               "innée (rapide, non spécifique) puis réponse acquise (spécifique, avec mémoire).",
      "methodes": [
          {"nom": "Méthode 1 — le scénario immunitaire",
           "texte": "① Brèche → inflammation (innée, phagocytes). ② Présentation de "
                    "l'antigène → activation des LB/LT spécifiques. ③ Anticorps + LTc "
                    "éliminent l'antigène ; mémoire = vaccination."},
      ],
      "pieges": ["Antigène (déclenche) ≠ anticorps (défense produite)."]}),
    ("SVT", "1BAC", "Géologie : ressources et sols", "Formations des sols, ressources "
     "géologiques et gestion durable.",
     {"intro": "Le sol se forme lentement par altération de la roche mère et action du "
               "vivant : ressource fragile à préserver.",
      "methodes": [
          {"nom": "Méthode 1 — profil de sol",
           "texte": "3 horizons : O (litière), A (humus + minéraux), C (roche mère "
                    "altérée). L'érosion et la déforestation détruisent plus vite que la "
                    "pédogenèse ne construit."},
      ],
      "pieges": ["Le sol n'est pas une simple poussière : c'est un écosystème lent."]}),

    # ---------------- FR TC ----------------
    ("FR", "TC", "Le texte argumentatif", "Thèse, arguments, exemples, connecteurs "
     "logiques ; savoir analyser et produire.", LECON_ARGU_FR),
    ("FR", "TC", "Les figures de style", "Comparaison, métaphore, personnification, "
     "hyperbole, antithèse : les reconnaître et les interpréter.",
     {"intro": "Une figure de style joue sur les mots pour créer un effet (image, "
               "émotion, insistance).",
      "methodes": [
          {"nom": "Méthode 1 — le trio à maîtriser",
           "texte": "Comparaison : outil de comparaison présent (comme, tel que). "
                    "Métaphore : outil absent. Personnification : attribuer des traits "
                    "humains. Pour l'interprétation : effet + intention de l'auteur."},
      ],
      "pieges": ["Citer la figure sans expliquer son effet = demi-point."]}),
    ("FR", "TC", "Le résumé de texte", "Réduire un texte en respectant les proportions et "
     "les idées essentielles.",
     {"intro": "Résumer = garder la logique du texte en supprimant exemples, répétitions "
               "et digressions.",
      "methodes": [
          {"nom": "Méthode 1 — la méthode des 4 étapes",
           "texte": "① Lecture globale : idée directrice. ② Découpe en mouvements. "
                    "③ Une phrase par mouvement (proportions respectées). ④ Vérification : "
                    "cohérence et aucun jugement personnel."},
      ],
      "pieges": ["Copier des phrases du texte.", "Ajouter son opinion."]}),

    # ---------------- FR 1BAC ----------------
    ("FR", "1BAC", "La littérature d'idées", "L'essai, la lettre ouverte, le discours : "
     "enjeux et procédés argumentatifs.",
     {"intro": "La littérature d'idées défend des valeurs par l'argumentation directe "
               "(essai) ou indirecte (récit à thèse, lettre ouverte).",
      "methodes": [
          {"nom": "Méthode 1 — argumentation directe vs indirecte",
           "texte": "Directe : thèse explicite, connecteurs, exemples. Indirecte : "
                    "l'auteur fait agir des personnages (ex : conte philosophique). "
                    "À l'examen : identifie le genre, la thèse, les procédés."},
      ],
      "pieges": ["Parler du sujet général au lieu de la thèse précise du texte."]}),
    ("FR", "1BAC", "Le commentaire et l'essai : méthodes de rédaction", "Plan détaillé, "
     "introduction et conclusion, transition.",
     {"intro": "Introduction : amorce → problématique → annonce du plan. "
               "Conclusion : bilan + ouverture.",
      "methodes": [
          {"nom": "Méthode 1 — le plan du parfait devoir",
           "texte": "Intro (5 lignes) ; 2-3 parties = 2-3 arguments, chacune : idée → "
                    "explication → exemple du texte/corpus → mini-conclusion ; conclusion "
                    "(bilan + ouverture). Relis-toi pour les connecteurs."},
      ],
      "pieges": ["Annoncer un plan non tenu.", "Parties déséquilibrées."]}),
]

# Exercices : (matière, niveau, titre chapitre, difficulté, source, énoncé, solution, astuce, variantes)
V = lambda *xs: list(xs)  # variantes rapides

EXERCISES = [
    # ---- MATH TC ----
    ("MATH", "TC", "Équations et inéquations dans ℝ", 1, "Manuel",
     "Résoudre dans ℝ : 3x − 5 = 7",
     "3x = 7 + 5 = 12\nx = 12/3 = 4\nS = {4}",
     "Isoler x : passer les constantes d'un côté, diviser.", V()),
    ("MATH", "TC", "Équations et inéquations dans ℝ", 1, "Manuel",
     "Résoudre dans ℝ : 2(x − 3) = 5x + 4",
     "2x − 6 = 5x + 4\n−6 − 4 = 5x − 2x\n−10 = 3x\nx = −10/3\nS = {−10/3}",
     "Développer d'abord, regrouper les x d'un côté.", V()),
    ("MATH", "TC", "Équations et inéquations dans ℝ", 2, "Contrôle",
     "Résoudre dans ℝ : x² − 5x + 6 = 0",
     "Δ = b² − 4ac = 25 − 24 = 1 > 0\nx₁ = (5 − 1)/2 = 2 ; x₂ = (5 + 1)/2 = 3\nS = {2 ; 3}",
     "Chercher 2 nombres dont la somme = 5 et le produit = 6 (2 et 3) : factorisation directe possible.",
     V({"enonce": "Résoudre dans ℝ : 2x² + x − 3 = 0",
        "solution": "Δ = 1 + 24 = 25 ; x = (−1 ± 5)/4 → x₁ = 1 ; x₂ = −3/2\nS = {−3/2 ; 1}"})),
    ("MATH", "TC", "Équations et inéquations dans ℝ", 2, "Manuel",
     "Résoudre dans ℝ : |2x − 1| = 5",
     "Cas 1 : 2x − 1 = 5 → x = 3\nCas 2 : 2x − 1 = −5 → x = −2\nS = {−2 ; 3}",
     "|X| = k ⟺ X = k ou X = −k (k ≥ 0).", V()),
    ("MATH", "TC", "Équations et inéquations dans ℝ", 3, "Type Examen Régional",
     "Résoudre dans ℝ : x² − 3x + 1 = 0, puis déterminer le signe du trinôme.",
     "Δ = 9 − 4 = 5 > 0\nx₁ = (3 − √5)/2 ≈ 0,38 ; x₂ = (3 + √5)/2 ≈ 2,62\n"
     "Signe : a = 1 > 0 → positif à l'extérieur des racines, négatif entre.\n"
     "S = {(3 ± √5)/2}",
     "Δ non carré parfait → laisser les racines en écriture exacte avec √5.",
     V({"enonce": "Résoudre dans ℝ : −x² + 2x + 3 = 0 et donner le signe du trinôme.",
        "solution": "Δ = 4 + 12 = 16 ; x₁ = −1 ; x₂ = 3. a = −1 < 0 → négatif à l'extérieur, "
                    "positif sur ]−1 ; 3[. S = {−1 ; 3}"})),
    ("MATH", "TC", "Trigonométrie", 2, "Contrôle",
     "Résoudre dans [0 ; 2π] : cos x = √3/2",
     "cos x = √3/2 = cos(π/6)\nx = π/6 + 2kπ ou x = −π/6 + 2kπ\nDans [0 ; 2π] : S = {π/6 ; 11π/6}",
     "Reconnaître l'angle remarquable, puis écrire les solutions générales avant de filtrer.",
     V({"enonce": "Résoudre dans [0 ; 2π] : sin x = 1/2",
        "solution": "sin x = sin(π/6) → x = π/6 + 2kπ ou x = 5π/6 + 2kπ → S = {π/6 ; 5π/6}"})),
    ("MATH", "TC", "Statistiques", 1, "Manuel",
     "Notes d'un élève : 12 ; 14 ; 9 ; 16 ; 14. Calculer la moyenne et la médiane.",
     "Moyenne = (12+14+9+16+14)/5 = 65/5 = 13\n"
     "Ordre : 9 ; 12 ; 14 ; 14 ; 16 → médiane = 3ᵉ valeur = 14",
     "Trier les valeurs AVANT de chercher la médiane.", V()),
    ("MATH", "TC", "Arithmétique dans ℕ", 2, "Manuel",
     "Calculer PGCD(252 ; 198) par l'algorithme d'Euclide, puis rendre la fraction 252/198 irréductible.",
     "252 = 1×198 + 54\n198 = 3×54 + 36\n54 = 1×36 + 18\n36 = 2×18 + 0\nPGCD = 18\n"
     "252/198 = (252÷18)/(198÷18) = 14/11",
     "Le dernier reste non nul est le PGCD.", V()),

    # ---- MATH 1BAC ----
    ("MATH", "1BAC", "Suites numériques", 1, "Manuel",
     "u_n = 3n + 2. Montrer que (u_n) est arithmétique, préciser sa raison et calculer u₁₀.",
     "u_{n+1} − u_n = [3(n+1)+2] − [3n+2] = 3 = constante\n→ arithmétique de raison r = 3, u₀ = 2\n"
     "u_n = u₀ + n·r → u₁₀ = 2 + 3×10 = 32",
     "La différence u_{n+1} − u_n constante est la définition d'une suite arithmétique.", V()),
    ("MATH", "1BAC", "Suites numériques", 2, "Manuel",
     "Soit v_n = 2·3ⁿ. Calculer v₅ puis la somme v₀ + v₁ + … + v₅.",
     "v₅ = 2·3⁵ = 2×243 = 486\nSomme géométrique : S = v₀(1 − q⁶)/(1 − q) = 1×(2⁶... "
     "non : q = 3 → S = 2(3⁶ − 1)/(3 − 1) = 2(729 − 1)/2 = 728",
     "Somme géométrique = 1er terme × (1 − q^(nb termes))/(1 − q).",
     V({"enonce": "Soit v_n = 5·2ⁿ. Calculer v₄ et la somme v₀ + … + v₄.",
        "solution": "v₄ = 5×16 = 80 ; S = 5(2⁵ − 1)/(2 − 1) = 5×31 = 155"})),
    ("MATH", "1BAC", "Limites et continuité", 2, "Contrôle",
     "Calculer lim (x→+∞) (3x² − 2x + 1)/(x² + 5) en justifiant.",
     "Forme ∞/∞ indéterminée.\nTerme de plus haut degré en haut : 3x² ; en bas : x².\n"
     "lim = lim (3x²/x²) = 3",
     "Au numérateur et au dénominateur, seul le terme dominant compte en ±∞.",
     V({"enonce": "Calculer lim (x→−∞) (2x³ + x)/(5x³ − 4)",
        "solution": "Termes dominants 2x³/5x³ → lim = 2/5"})),
    ("MATH", "1BAC", "Limites et continuité", 3, "Type Examen National",
     "Calculer lim (x→2) (x² − 4)/(x − 2).",
     "Substitution → 0/0 (indéterminé).\nx² − 4 = (x − 2)(x + 2)\n"
     "Quotient = x + 2 pour x ≠ 2\nlim (x→2) (x + 2) = 4",
     "0/0 → FACTORISER. Ici identité remarquable a² − b².",
     V({"enonce": "Calculer lim (x→1) (x³ − 1)/(x − 2... plutôt : (x³ − 1)/(x − 1)",
        "solution": "x³ − 1 = (x − 1)(x² + x + 1) → lim = 1² + 1 + 1 = 3"})),
    ("MATH", "1BAC", "Dérivation", 2, "Manuel",
     "Dériver f(x) = 3x³ − 4x² + 5x − 7.",
     "f'(x) = 3×3x² − 4×2x + 5 = 9x² − 8x + 5",
     "Dériver terme à terme : (xⁿ)' = n·xⁿ⁻¹.", V()),
    ("MATH", "1BAC", "Dérivation", 3, "Type Examen Régional",
     "Soit f(x) = x³ − 3x + 2. Étudier les variations de f et préciser ses extremums locaux.",
     "f'(x) = 3x² − 3 = 3(x − 1)(x + 1)\nSigne : f' > 0 si x < −1 ou x > 1 ; f' < 0 sur ]−1 ; 1[\n"
     "f croissante sur ]−∞ ; −1] et [1 ; +∞[, décroissante sur [−1 ; 1]\n"
     "Maximum local : f(−1) = 4 ; minimum local : f(1) = 0",
     "Toujours FACTORISER f' avant d'étudier son signe.", V()),
    ("MATH", "1BAC", "Dénombrement", 2, "Manuel",
     "Un club de 10 membres veut élire un bureau de 3 personnes (sans fonction précise). "
     "Combien de bureaux possibles ?",
     "L'ordre ne compte pas → combinaisons.\nC(10,3) = 10!/(3!·7!) = 120",
     "« Un bureau sans fonction » = combinaison. S'il y avait président/trésorier/secrétaire → arrangement.",
     V({"enonce": "Parmi 10 membres, combien de façon de choisir président, secrétaire et trésorier ?",
        "solution": "L'ordre compte → A(10,3) = 10×9×8 = 720"})),
    ("MATH", "1BAC", "Dénombrement", 1, "Manuel",
     "Combien de codes PIN de 4 chiffres tous distincts peut-on former (0 à 9) ?",
     "L'ordre compte, sans répétition → A(10,4) = 10×9×8×7 = 5040",
     "« Distincts » = sans répétition ; « code » = l'ordre compte.", V()),
    ("MATH", "1BAC", "Probabilités", 2, "Type Examen Régional",
     "Une urne contient 5 boules rouges et 3 bleues. On tire 2 boules sans remise. "
     "Calculer P(deux rouges).",
     "P(R1) = 5/8 ; après un rouge retiré : P(R2|R1) = 4/7\nP = 5/8 × 4/7 = 20/56 = 5/14",
     "Sans remise : le second tirage se fait sur 7 boules dont 4 rouges.", V()),

    # ---- PC TC ----
    ("PC", "TC", "La mole et les concentrations", 1, "Manuel",
     "Quelle quantité de matière représente 36 g d'eau (M(H₂O) = 18 g/mol) ?",
     "n = m/M = 36/18 = 2 mol",
     "Appliquer n = m/M avec les unités.", V()),
    ("PC", "TC", "La mole et les concentrations", 1, "Manuel",
     "Quelle est la masse de 0,25 mol de chlorure de sodium NaCl (M = 58,5 g/mol) ?",
     "m = n×M = 0,25×58,5 = 14,6 g",
     "m = n×M : l'inverse de n = m/M.", V()),
    ("PC", "TC", "La mole et les concentrations", 2, "Contrôle",
     "On dissout 5,85 g de NaCl (M = 58,5 g/mol) dans 500 mL d'eau. Calculer la "
     "concentration molaire de la solution.",
     "n = m/M = 5,85/58,5 = 0,1 mol\nV = 500 mL = 0,5 L\nC = n/V = 0,1/0,5 = 0,2 mol/L",
     "CONVERTIR mL → L avant C = n/V.",
     V({"enonce": "On dissout 11,7 g de NaCl dans 2 L. Calculer C.",
        "solution": "n = 11,7/58,5 = 0,2 mol ; C = 0,2/2 = 0,1 mol/L"})),
    ("PC", "TC", "L'atome et la structure de la matière", 2, "Manuel",
     "Pour l'atome de carbone ¹²C : donner Z, A, le nombre de protons, de neutrons "
     "et d'électrons.",
     "Z = 6 (carbone) ; A = 12\nProtons = 6 ; neutrons = A − Z = 6 ; électrons = 6 (atome neutre)",
     "neutrons = A − Z ; électrons = protons si atome neutre.", V()),
    ("PC", "TC", "La mole et les concentrations", 3, "Type Examen Régional",
     "On veut préparer V₂ = 100 mL d'une solution de sulfate de cuivre de concentration "
     "C₂ = 0,10 mol/L à partir d'une solution mère C₁ = 0,50 mol/L. Décrire le protocole "
     "et calculer le volume prélevé.",
     "Dilution : n constant → C₁V₁ = C₂V₂\nV₁ = C₂V₂/C₁ = (0,10×100)/0,50 = 20 mL\n"
     "Protocole : prélever 20 mL à la pipette jaugée, verser dans une fiole jaugée de "
     "100 mL, compléter au trait de jauge avec de l'eau distillée, homogénéiser.",
     "Le protocole complet (pipette + fiole jaugée + homogénéisation) rapporte des points.",
     V({"enonce": "Quelle dilution (facteur) entre C₁ = 0,50 et C₂ = 0,10 mol/L ?",
        "solution": "F = C₁/C₂ = 5 (dilution 5 fois)"})),
    ("PC", "TC", "Principe des actions réciproques", 2, "Manuel",
     "La Terre de masse M attire la Lune de masse m avec une force d'intensité F. "
     "Quelle est l'intensité de la force exercée par la Lune sur la Terre ? Justifier.",
     "Même intensité F.\nPrincipe des actions réciproques : la force exercée par A sur B "
     "et celle de B sur A ont même intensité, même droite d'action, sens opposés — "
     "indépendamment des masses.",
     "Le principe s'applique quelle que soit la différence de masse.", V()),

    # ---- PC 1BAC ----
    ("PC", "1BAC", "Cinématique et lois de Newton", 1, "Manuel",
     "Un coureur parcourt 150 m en 10 s de façon uniforme. Calculer sa vitesse en m/s puis en km/h.",
     "v = d/t = 150/10 = 15 m/s\n15 × 3,6 = 54 km/h",
     "Conversion m/s → km/h : multiplier par 3,6.", V()),
    ("PC", "1BAC", "Cinématique et lois de Newton", 2, "Contrôle",
     "Un solide de masse m = 2 kg glisse sur un plan horizontal sans frottement sous "
     "l'action d'une force horizontale F = 10 N. Calculer son accélération.",
     "2ᵉ loi de Newton (projection horizontale) : F = m·a\na = F/m = 10/2 = 5 m/s²",
     "Sans frottement, la seule force horizontale est F (le poids est vertical).",
     V({"enonce": "Même solide avec frottement f = 4 N. Calculer a.",
        "solution": "F − f = m·a → a = (10 − 4)/2 = 3 m/s²"})),
    ("PC", "1BAC", "Énergie mécanique", 2, "Manuel",
     "Calculer l'énergie cinétique d'une voiture de masse 1000 kg roulant à 20 m/s. "
     "Même question à 40 m/s. Conclusion ?",
     "Ec = ½mv² = ½×1000×20² = 200 000 J = 200 kJ\nÀ 40 m/s : Ec = ½×1000×40² = 800 kJ\n"
     "Vitesse doublée → Ec multipliée par 4 (relation quadratique).",
     "Le facteur entre v et v² explique les limitations de vitesse.", V()),
    ("PC", "1BAC", "Énergie mécanique", 3, "Type Examen National",
     "Un corps tombe sans vitesse initiale d'une hauteur h = 20 m (g = 10 m/s²). "
     "Calculer sa vitesse d'arrivée au sol et la durée de la chute.",
     "Chute libre : v = √(2gh) = √(2×10×20) = √400 = 20 m/s\nh = ½gt² → t = √(2h/g) = √4 = 2 s",
     "v = √(2gh) et t = √(2h/g) : les 2 formules à connaître par cœur.",
     V({"enonce": "Même question avec h = 45 m (g = 10 m/s²).",
        "solution": "v = √(2×10×45) = 30 m/s ; t = √(2×45/10) = 3 s"})),
    ("PC", "1BAC", "Phénomènes périodiques et ondes", 2, "Contrôle",
     "Un phénomène a une période T = 0,02 s. Calculer sa fréquence.",
     "f = 1/T = 1/0,02 = 50 Hz",
     "f = 1/T avec T en secondes.", V()),
    ("PC", "1BAC", "Suivi d'une transformation et dosage", 3, "Type Examen National",
     "On titre V_a = 20 mL d'acide chlorhydrique (C_a inconnue) par une solution de "
     "soude C_b = 0,10 mol/L. L'équivalence est atteinte pour V_b = 15 mL. Calculer C_a.",
     "Équation : H₃O⁺ + HO⁻ → 2H₂O\nÀ l'équivalence : n(acide) = n(base)\n"
     "C_a·V_a = C_b·V_b → C_a = (0,10×15)/20 = 0,075 mol/L",
     "Écrire l'équation de la réaction de titrage AVANT la relation d'équivalence.", V()),
    ("PC", "1BAC", "Suivi d'une transformation et dosage", 2, "Manuel",
     "Réaction : N₂ + 3H₂ → 2NH₃. On introduit 1 mol de N₂ et 3 mol de H₂. "
     "Déterminer le réactif limitant et x_max.",
     "x_max pour N₂ : 1 − x ≥ 0 → x ≤ 1\nx_max pour H₂ : 3 − 3x ≥ 0 → x ≤ 1\n"
     "Les deux donnent x_max = 1 : mélange stœchiométrique (aucun réactif en excès).",
     "Comparer les x_max calculés pour chaque réactif : le plus petit gagne.", V()),

    # ---- SVT TC ----
    ("SVT", "TC", "La cellule, unité de la vie", 2, "Contrôle",
     "Citer 3 différences entre une cellule végétale et une cellule animale.",
     "Cellule végétale uniquement : ① paroi de cellulose (rigidité), ② chloroplastes "
     "(photosynthèse), ③ grande vacuole centrale (réserve, turgescence).\n"
     "Communes : membrane, cytoplasme, noyau, mitochondries.",
     "3 éléments EXCLUSIFS au végétal : paroi, chloroplaste, vacuole.", V()),
    ("SVT", "TC", "Biodiversité et classification", 2, "Manuel",
     "Pourquoi la taille d'un organisme n'est-elle pas un critère de classification "
     "scientifique ? Citer 2 critères valides.",
     "La taille varie au sein d'un même groupe (ex : grand/petit chien = même espèce) "
     "et ne reflète pas la parenté.\nCritères valides : présence/absence de caractères "
     "anatomiques (colonne vertébrale, plumes, fleurs), nature de la reproduction, "
     "nombre d'états d'un caractère (vertébrés/invertébrés).",
     "Classifier selon des caractères héréditaires structuraux, pas des dimensions.", V()),

    # ---- SVT 1BAC ----
    ("SVT", "1BAC", "Génétique humaine", 2, "Manuel",
     "Croisement entre deux plantes de lignée pure : [Fleurs rouges] × [Fleurs blanches]. "
     "F1 toutes rouges. On croise deux F1 : donner les génotypes et proportions phénotypiques en F2.",
     "Rouge dominant. Lignée pure : RR × rr → F1 : 100 % Rr (rouges).\n"
     "F1 × F1 : Rr × Rr → gamètes R, r\nF2 : 1/4 RR + 1/2 Rr → 3/4 [rouge] ; 1/4 rr [blanc]\n"
     "Proportion : 3 rouge / 1 blanc",
     "Tableau de Punnett 2×2 : le 3/4–1/4 est LA proportion à connaître.",
     V({"enonce": "Retrouver le génotype d'un F1 rouge : quel croisement test proposer ?",
        "solution": "Croisement avec blanc (rr) : si descendance 1 rouge/1 blanc → F1 = Rr"})),
    ("SVT", "1BAC", "Génétique humaine", 3, "Type Examen Régional",
     "Deux parents sains ont un enfant atteint d'une maladie héréditaire. "
     "1) Le caractère est-il dominant ou récessif ? 2) Quels sont les génotypes des parents ? "
     "3) Probabilité que le prochain enfant soit atteint ?",
     "1) Récessif : des parents SAINS peuvent transmettre la maladie seulement si elle "
     "est récessive (les parents porteurs sains).\n"
     "2) Parents : Aa × Aa (hétérozygotes) ; enfant malade : aa.\n"
     "3) Croisement Aa×Aa → 1/4 aa → probabilité 25 %.",
     "« Parents sains + enfant malade » = signature d'une maladie récessive autosomique.",
     V({"enonce": "Si la maladie était liée à l'X et récessive, quel parent transmet l'allèle au garçon ?",
        "solution": "La mère (X^a X^A → gamète X^a) ; le père transmet son Y au garçon."})),
    ("SVT", "1BAC", "Immunologie", 2, "Contrôle",
     "Distinguer réponse immunitaire innée et réponse immunitaire acquise (2 différences + 1 exemple).",
     "Innée : immédiate, non spécifique, sans mémoire (barrières, inflammation, "
     "phagocytose par les macrophages).\n"
     "Acquise : lente (jours), SPÉCIFIQUE d'un antigène, avec MÉMOIRE (lymphocytes B/T, "
     "anticorps). Ex : la vaccination met en place la mémoire immunitaire.",
     "Les 3 mots-clés de l'acquise : spécifique, lente, mémoire.", V()),

    # ---- FR TC ----
    ("FR", "TC", "Le texte argumentatif", 2, "Contrôle",
     "Analyser : « Il faut limiter le temps d'écran des adolescents. D'abord, l'excès "
     "d'écran perturbe le sommeil ; ensuite, il réduit le temps consacré à la lecture. "
     "Par exemple, les élèves qui passent plus de 3 h par jour sur leur téléphone lisent "
     "deux fois moins. »\n1) Quelle est la thèse ? 2) Relever les 2 arguments et l'exemple. "
     "3) Quels connecteurs structurent le texte ?",
     "1) Thèse : il faut limiter le temps d'écran des adolescents.\n"
     "2) Argument 1 : perturbation du sommeil ; Argument 2 : réduction du temps de lecture. "
     "Exemple : les élèves à +3 h/jour lisent deux fois moins.\n"
     "3) Connecteurs : « D'abord », « ensuite », « Par exemple » (énumération + illustration).",
     "Chercher les connecteurs en premier : ils balisent la structure.", V()),
    ("FR", "TC", "Les figures de style", 1, "Manuel",
     "Identifier la figure de style dans chaque phrase :\n1) « Cette femme est un roc. »\n"
     "2) « Le vent murmure dans les arbres. »\n3) « Il est mort de fatigue. »",
     "1) Métaphore (comparaison sans outil : femme = roc).\n"
     "2) Personnification (le vent « murmure » : trait humain).\n"
     "3) Hyperbole (exagération).",
     "Outil de comparaison présent → comparaison ; absent → métaphore.",
     V({"enonce": "« Je meurs de faim, je pourrais manger un éléphant. » Identifier les figures.",
        "solution": "Double hyperbole (exagération successives)"})),

    # ---- FR 1BAC ----
    ("FR", "1BAC", "La littérature d'idées", 3, "Type Examen Régional",
     "Sujet d'écriture : « Les réseaux sociaux rapprochent-ils véritablement les êtres "
     "humains ? » Rédiger un plan détaillé (thèse, 2 arguments avec exemples, objection "
     "nuancée, conclusion).",
     "Plan possible :\nI. Thèse : ils rapprochent — 1) communication instantanée à distance "
     "(familles séparées par l'immigration, appels vidéo) ; 2) communautés d'intérêt "
     "(groupes d'entraide scolaire).\nII. Objection nuancée : « Certes, le contact virtuel "
     "remplace parfois les liens réels et crée de l'isolement ; cependant l'outil est "
     "neutre, tout dépend de l'usage. »\nIII. Conclusion : le rapprochement dépend de "
     "l'usage raisonné, pas de la technologie elle-même.",
     "Le plan détaillé doit montrer : arguments + exemples concrets + concession.",
     V({"enonce": "Donner une amorce possible pour l'introduction de ce sujet.",
        "solution": "« En 2024, plus de 5 milliards de personnes utilisent les réseaux "
                    "sociaux : jamais l'humanité n'a été aussi « connectée ». Mais l'est-elle "
                    "véritablement ? »"})),
    ("FR", "1BAC", "Le commentaire et l'essai : méthodes de rédaction", 2, "Manuel",
     "Écrire l'introduction complète d'un commentaire sur un texte argumentatif de "
     "Victor Hugo défendant l'école pour tous (amorce, présentation, problématique, plan).",
     "Amorce : « L'instruction est un droit encore inégalé au XIXᵉ siècle… »\n"
     "Présentation : texte argumentatif de Victor Hugo (auteur, siècle, œuvre), thèse : "
     "l'école doit être accessible à tous.\nProblématique : « Par quels procédés "
     "l'auteur défend-il cette cause ? »\nAnnonce du plan : arguments et exemples ; "
     "procédés stylistiques ; force de la conclusion.",
     "Introduction = 4 étapes : amorce, présentation, problématique, annonce du plan.", V()),
]


def seed(db):
    import json as _json
    sub_ids = {}
    for code, nom, couleur, icone in SUBJECTS:
        sid = db.execute(
            "INSERT INTO subjects(code, nom, couleur, icone) VALUES (?,?,?,?)",
            (code, nom, couleur, icone))
        sub_ids[code] = sid
    print(f"[seed] {len(SUBJECTS)} matières")

    ch_ids = {}
    n_ch = 0
    for code, niveau, titre, resume, lecon in CHAPTERS:
        cid = db.execute(
            "INSERT INTO chapters(subject_id, niveau, titre, resume, lecon) VALUES (?,?,?,?,?)",
            (sub_ids[code], niveau, titre, resume,
             _json.dumps(lecon, ensure_ascii=False) if lecon else ""))
        ch_ids[(code, niveau, titre)] = cid
        n_ch += 1
    print(f"[seed] {n_ch} chapitres")

    n_ex = 0
    for code, niveau, chap, diff, source, enonce, solution, astuce, variantes in EXERCISES:
        cid = ch_ids[(code, niveau, chap)]
        db.execute(
            "INSERT INTO exercises(chapter_id, difficulte, source, enonce, solution, "
            "astuce, variantes) VALUES (?,?,?,?,?,?,?)",
            (cid, diff, source, enonce, solution, astuce,
             _json.dumps(variantes, ensure_ascii=False)))
        n_ex += 1
    print(f"[seed] {n_ex} exercices")
