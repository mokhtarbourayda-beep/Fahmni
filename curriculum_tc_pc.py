# -*- coding: utf-8 -*-
"""
curriculum_tc_pc.py — Programme COMPLET de Physique-Chimie du Tronc Commun
(programme officiel marocain : Mécanique + Électricité / Constitution de la
matière + Transformations de la matière).

Chapitres existants enrichis (leçon complète) + nouveaux chapitres + exercices
de tous types (Manuel, Contrôle, Type Examen Régional) avec variantes.
"""

L_ATOME = {
    "intro": "Toute la matière est faite d'atomes : un noyau (protons + neutrons) "
             "autour duquel tournent les électrons. La structure électronique explique "
             "les ions, les molécules et bientôt toutes les réactions chimiques.",
    "methodes": [
        {"nom": "Méthode 1 — lire l'identité d'un atome",
         "texte": "Z = nombre de protons (numéro atomique), A = nombre de nucléons "
                  "(nombre de masse). Donc : protons = Z ; neutrons = A − Z ; "
                  "électrons = Z (atome neutre). L'atome est symbolisé "
                  "A/Z X : A en haut à gauche, Z en bas à gauche."},
        {"nom": "Méthode 2 — écrire la configuration électronique",
         "texte": "On remplit les couches par ordre croissant d'énergie : K (2 max), "
                  "L (8 max), M (18 max). Ex : l'aluminium Z = 13 → (K)² (L)⁸ (M)³. "
                  "Les électrons de la DERNIÈRE couche = électrons de valence (ici 3) : "
                  "ce sont eux qui font la chimie."},
        {"nom": "Méthode 3 — former un ion",
         "texte": "Un atome cherche la stabilité (règle de l'octet : dernière couche "
                  "pleine à 8, ou duet à 2). Il PERD ses électrons de valence → ion "
                  "positif (cation) : Al → Al³⁺ + 3e⁻. Il GAGNE des électrons → ion "
                  "négatif (anion) : Cl + e⁻ → Cl⁻. Les ions polyatomiques se retiennent "
                  ": hydroxyde OH⁻, sulfate SO₄²⁻, nitrate NO₃⁻."},
    ],
    "exemples": [
        {"question": "Déterminer la composition et la configuration de l'atome de "
                     "soufre 32/16 S, puis celle de l'ion S²⁻.",
         "etapes": ["Z = 16 → 16 protons ; A = 32 → 32 − 16 = 16 neutrons",
                    "Atome neutre → 16 électrons",
                    "Configuration : (K)² (L)⁸ (M)⁶ → 6 électrons de valence",
                    "S²⁻ a gagné 2 e⁻ : 18 électrons, config (K)² (L)⁸ (M)⁸ → octet ✓"],
         "reponse": "16 p⁺ ; 16 n ; 16 e⁻ → (K)² (L)⁸ (M)⁶ ; l'ion S²⁻ : 18 e⁻, stable."},
    ],
    "pieges": [
        "Neutrons = A − Z et non A (erreur classique !).",
        "Un ion ne change JAMAIS le nombre de protons : seulement les électrons.",
        "La couche M peut contenir jusqu'à 18 électrons (pas 8).",
    ],
    "formules": ["protons = Z ; neutrons = A − Z ; électrons = Z (atome neutre)",
                 "couches : K (2), L (8), M (18)", "octet : dernière couche = 8 e⁻"],
}

L_MOLE = {
    "intro": "La mole est l'unité de « paquet » des chimistes : 1 mol = 6,02 × 10²³ "
             "entités (nombre d'Avogadro). Elle relie la masse (visible) au nombre "
             "d'entités (invisible) et permet de doser les solutions.",
    "methodes": [
        {"nom": "Méthode 1 — passer de la masse à la quantité de matière",
         "texte": "Masse molaire M : on additionne les masses molaires atomiques "
                  "(données dans le tableau périodique). Glucose C₆H₁₂O₆ : "
                  "M = 6×12 + 12×1 + 6×16 = 180 g/mol. Puis n = m/M. "
                  "Inversement m = n × M."},
        {"nom": "Méthode 2 — compter les entités",
         "texte": "N = n × N_A avec N_A = 6,02 × 10²³ /mol. Ex : n = 0,5 mol de "
                  "glucose → 3,01 × 10²³ molécules. Chaque molécule de C₆H₁₂O₆ compte "
                  "24 atomes → N(atomes) = 24 × N(molécules)."},
        {"nom": "Méthode 3 — concentrations et dilution",
         "texte": "Concentration molaire C = n/V (mol/L) ; massique Cm = m/V (g/L) ; "
                  "lien : C = Cm/M. Dilution : on ajoute du solvant, n ne change pas → "
                  "C₁V₁ = C₂V₂. Facteur de dilution F = C₁/C₂ = V₂/V₁."},
    ],
    "exemples": [
        {"question": "Préparer V₂ = 500 mL d'une solution de sulfate de cuivre de "
                     "concentration C₂ = 0,20 mol/L à partir d'une solution mère "
                     "C₁ = 1,0 mol/L. Quelle verrerie ?",
         "etapes": ["V₁ = C₂V₂/C₁ = 0,20 × 500/1,0 = 100 mL de solution mère",
                    "Prélever 100 mL à la pipette jaugée",
                    "Verser dans une fiole jaugée de 500 mL",
                    "Compléter au trait de jauge avec de l'eau distillée, homogénéiser"],
         "reponse": "Pipette jaugée 100 mL + fiole jaugée 500 mL ; F = 5."},
        {"question": "Quelle masse de glucose pour V = 250 mL de solution à "
                     "C = 0,10 mol/L ? (M = 180 g/mol)",
         "etapes": ["n = C×V = 0,10 × 0,250 = 0,025 mol",
                    "m = n×M = 0,025 × 180 = 4,5 g"],
         "reponse": "m = 4,5 g (ne pas oublier de convertir les mL en L !)"},
    ],
    "pieges": [
        "Les volumes en mL doivent être convertis en L dans C = n/V.",
        "Masse molaire : multiplier par l'INDICE (nombre d'atomes), pas par 1.",
        "Dilution : C₁V₁ = C₂V₂ fonctionne seulement si n est conservé (pas de réaction).",
    ],
    "formules": ["n = m/M = N/N_A", "C = n/V ; Cm = m/V ; C = Cm/M",
                 "dilution : C₁V₁ = C₂V₂ ; F = V₂/V₁"],
}

L_MELANGES = {
    "intro": "L'eau naturelle n'est jamais pure : distinguer corps purs et mélanges, "
             "puis savoir séparer les constituants, est le socle du travail du chimiste. "
             "Ces techniques tombent presque chaque année à l'examen régional.",
    "methodes": [
        {"nom": "Méthode 1 — classer la matière",
         "texte": "Corps pur simple (1 seul élément : O₂, Fe) ; corps pur composé "
                  "(plusieurs éléments liés : H₂O, CO₂) ; mélange (plusieurs espèces "
                  "non liées). Homogène (une seule phase : eau salée, air) ou "
                  "hétérogène (plusieurs phases : eau + huile, eau + sable)."},
        {"nom": "Méthode 2 — choisir la technique de séparation",
         "texte": "Solide insoluble + liquide → FILTRATION. Deux liquides non "
                  "miscibles → DÉCANTATION (ampoule ou entonnoir). Solide dissous + "
                  "liquide → ÉVAPORATION ou CRISTALLISATION. Deux liquides miscibles "
                  "d'températures d'ébullition différentes → DISTILLATION. Espèces "
                  "colorées (encres, pigments) → CHROMATOGRAPHIE."},
        {"nom": "Méthode 3 — exploiter une chromatographie",
         "texte": "Chaque espèce migre à sa vitesse : on compare la hauteur de migration "
                  "de l'échantillon à celle des témoins. Même hauteur (même rapport "
                  "frontal) → même espèce. Le nombre de taches du mélange = nombre "
                  "d'espèces présentes."},
    ],
    "exemples": [
        {"question": "Comment récupérer du sel dissous dans de l'eau trouble "
                     "(contenant du sable) ?",
         "etapes": ["Filtration → on élimine le sable (insoluble), récupère l'eau salée "
                    "trouble... clarifiée",
                    "Évaporation ou cristallisation → l'eau s'échappe, le sel cristallise"],
         "reponse": "Filtration puis évaporation : deux techniques complémentaires."},
    ],
    "pieges": [
        "La filtration ne sépare JAMAIS un solide dissous (le sel passe au travers !).",
        "Homogène ≠ pur : l'eau salée est homogène mais c'est un mélange.",
        "À la distillation, c'est le liquide le PLUS volatil qui se vaporise en premier.",
    ],
    "formules": ["S = m(saturée)/V(solvent) : solubilité",
                 "1ᵉʳ degré de pureté : présence d'une seule espèce"],
}

L_RECIPROQUE = {
    "intro": "Toute action mécanique est une interaction : quand A agit sur B, B agit "
             "aussi sur A. Ce principe des actions réciproques est l'un des piliers de "
             "la mécanique du lycée.",
    "methodes": [
        {"nom": "Méthode 1 — caractériser une force",
         "texte": "Une force se décrit par 4 caractéristiques : point d'application, "
                  "direction (droite support), sens, intensité (en newtons, N). On la "
                  "mesure au dynamomètre et on la représente par un vecteur. "
                  "Notation : F(A→B) = force exercée par A sur B."},
        {"nom": "Méthode 2 — classer les actions",
         "texte": "Action LOCALISÉE (contact) : pousser une caisse, tension d'un fil, "
                  "réaction d'un support. Action À DISTANCE : poids (gravitation), "
                  "forces électriques/magnétiques. Le poids P = m·g (g ≈ 9,8 N/kg) "
                  "s'applique au centre de gravité, verticalement vers le bas."},
        {"nom": "Méthode 3 — appliquer le principe des actions réciproques",
         "texte": "Si A agit sur B avec F(A→B), alors B agit sur A avec F(B→A) de "
                  "MÊME direction, MÊME intensité, sens OPPOSÉ. Ex : la Terre attire "
                  "une pomme avec 1 N → la pomme attire la Terre avec 1 N aussi !"},
    ],
    "exemples": [
        {"question": "Un livre (m = 500 g) posé sur une table. Décrire toutes les "
                     "actions et vérifier le principe.",
         "etapes": ["Action à distance : la Terre attire le livre → poids P = 0,5×9,8 = 4,9 N",
                    "Action de contact : la table repousse le livre → réaction R = 4,9 N (vertical, vers le haut)",
                    "Actions réciproques : le livre attire la Terre (4,9 N) ; le livre appuie sur la table (4,9 N vers le bas)"],
         "reponse": "4 paires d'actions, chacune vérifie même intensité/sens opposés."},
    ],
    "pieges": [
        "Poids et réaction du support agissent sur le MÊME corps : ce ne sont pas des actions réciproques !",
        "Les deux forces réciproques s'appliquent à deux corps DIFFÉRENTS (elles ne se compensent jamais).",
        "Intensité en N : convertir les grammes avant P = m·g.",
    ],
    "formules": ["P = m·g (g ≈ 9,8 N/kg à Casablanca)",
                 "F(A→B) = −F(B→A) : même norme, sens opposés"],
}

CH_INERTIE = {
    "intro": "Pourquoi tout s'arrête-t-il toujours ? Parce que les frottements "
             "s'introduisent ! Le principe d'inertie explique le mouvement sans force "
             "résultante : c'est LA loi qui prépare la dynamique du lycée.",
    "methodes": [
        {"nom": "Méthode 1 — énoncer le principe d'inertie",
         "texte": "Dans un référentiel terrestre, si un corps est soumis à des forces "
                  "qui se COMPENSENT (résultante nulle), alors il est immobile ou en "
                  "mouvement rectiligne UNIFORME (vitesse constante). Réciproquement : "
                  "mouvement rectiligne uniforme → forces compensées."},
        {"nom": "Méthode 2 — reconnaître des forces qui se compensent",
         "texte": "2 forces se compensent ⟺ même direction, mêmes intensités, sens "
                  "opposés. 3 forces se compensent ⟺ leur somme vectorielle est nulle "
                  "(les 3 vecteurs, mis bout à bout, forment un triangle fermé) : on "
                  "dit qu'elles sont coplanaires et concourantes."},
        {"nom": "Méthode 3 — équilibre d'un solide",
         "texte": "Solide en équilibre = immobile + forces compensées. Cas de 2 "
                  "forces : elles sont forcément opposées sur la même droite. "
                  "Cas de 3 forces (ex : tableau suspendu par 2 fils) : construire le "
                  "triangle des forces à l'échelle et mesurer les intensités."},
    ],
    "exemples": [
        {"question": "Un skieur descend une piste en ligne droite à vitesse constante. "
                     "Que peut-on affirmer sur les forces ?",
         "etapes": ["Mouvement rectiligne uniforme (vitesse constante)",
                    "Principe d'inertie → la résultante est nulle",
                    "Poids + réaction + frottements se compensent : leur somme vectorielle est nulle"],
         "reponse": "Les trois forces se compensent (triangle des forces fermé)."},
    ],
    "pieges": [
        "« Vitesse constante » n'est pas « accélération constante » : seule la première implique l'inertie.",
        "Un objet au repos n'est pas « sans forces » : ses forces se compensent.",
        "Le principe ne s'applique que dans un référentiel terrestre (galiléen).",
    ],
    "formules": ["ΣF = 0 ⟹ repos ou mouvement rectiligne uniforme",
                 "2 forces compensées : même direction, normes égales, sens opposés"],
}

CH_REACTION = {
    "intro": "Une réaction chimique transforme des réactifs en produits : on la décrit "
             "par une équation-bilan AJUSTÉE qui respecte la loi de conservation "
             "(Lavoisier : rien ne se perd, rien ne se crée).",
    "methodes": [
        {"nom": "Méthode 1 — écrire et ajuster une équation-bilan",
         "texte": "① Écris les formules des réactifs (à gauche) et produits (à droite). "
                  "② Ajuste avec des coefficients entiers pour avoir le même nombre de "
                  "chaque atome des deux côtés. Ex : combustion du méthane : "
                  "CH₄ + 2O₂ → CO₂ + 2H₂O (vérifie : C :1=1 ; H :4=4 ; O :4=4 ✓). "
                  "Les coefficients donnent les proportions molaires."},
        {"nom": "Méthode 2 — tableau d'avancement",
         "texte": "Colonnes : réactifs/produits ; lignes : état initial (x=0), "
                  "intermédiaire (x), final (x_max). Chaque quantité = quantité "
                  "initiale + coefficient × (±x). Le tableau se construit à partir des "
                  "coefficients de l'équation ajustée."},
        {"nom": "Méthode 3 — bilan de matière et réactif limitant",
         "texte": "Le réactif limitant est celui dont l'avancement maximal annule la "
                  "quantité en premier : calcule x_max pour chaque réactif, le PLUS "
                  "PETIT gagne. À l'état final, le limitant est épuisé (n = 0) et les "
                  "autres sont en excès."},
    ],
    "exemples": [
        {"question": "On mélange 0,10 mol de zinc et 0,15 mol d'acide chlorhydrique : "
                     "Zn + 2H⁺ → Zn²⁺ + H₂. Trouver le réactif limitant.",
         "etapes": ["Pour Zn : x_max = 0,10/1 = 0,10 mol",
                    "Pour H⁺ : x_max = 0,15/2 = 0,075 mol",
                    "Le plus petit : x_max = 0,075 mol → H⁺ est limitant",
                    "État final : Zn restant = 0,10 − 0,075 = 0,025 mol ; H₂ formé = 0,075 mol"],
         "reponse": "H⁺ limitant ; on forme 0,075 mol de H₂ ; il reste 0,025 mol de Zn."},
    ],
    "pieges": [
        "Ajuster par les COEFFICIENTS, jamais en modifiant les formules (H₂O reste H₂O !).",
        "Un excès de réactif ne change pas la quantité de produits.",
        "Les coefficients donnent des proportions de MOLES, pas de masses.",
    ],
    "formules": ["conservation : Σ atomes réactifs = Σ atomes produits",
                 "n(produit) = coef × x_max", "réactif limitant : x_max minimal"],
}

CH_PH = {
    "intro": "Le pH mesure l'acidité d'une solution : pH < 7 acide, pH = 7 neutre, "
             "pH > 7 basique (à 25 °C). Sa relation avec la concentration en ions "
             "oxonium H₃O⁺ est une application directe des puissances de 10.",
    "methodes": [
        {"nom": "Méthode 1 — relier pH et concentration",
         "texte": "pH = −log[H₃O⁺] et [H₃O⁺] = 10^(−pH). Ex : pH = 3 → "
                  "[H₃O⁺] = 10⁻³ mol/L. Chaque unité de pH en moins = concentration "
                  "× 10 : une solution de pH 2 est 100 fois plus acide que pH 4."},
        {"nom": "Méthode 2 — mesurer le pH",
         "texte": "pH-mètre (précis, à étalonner) ou indicateurs colorés (BBT : jaune "
                  "acide → bleu basique ; hélianthine ; phénolphtaléine : incolore "
                  "acide → rose basique). Comparer la couleur au témoin/échelle."},
        {"nom": "Méthode 3 — sécurité et dilution d'acides",
         "texte": "On verse TOUJOURS l'acide DANS l'eau (jamais l'inverse !) : "
                  "« on ne jette pas l'eau dans l'acide ». Une dilution de facteur 10 "
                  "augmente le pH d'une unité (acide) : pH 2 dilué ×10 → pH 3."},
    ],
    "exemples": [
        {"question": "Une solution d'acide chlorhydrique a pH = 2,3. Calculer "
                     "[H₃O⁺]. On la dilue 100 fois : nouveau pH ?",
         "etapes": ["[H₃O⁺] = 10^(−2,3) ≈ 5,0 × 10⁻³ mol/L",
                    "Dilution ×100 : [H₃O⁺] divisé par 100 → 5,0 × 10⁻⁵ mol/L",
                    "pH = −log(5,0 × 10⁻⁵) = 4,3 (= 2,3 + 2)"],
         "reponse": "[H₃O⁺] ≈ 5,0 × 10⁻³ mol/L ; après dilution, pH = 4,3."},
    ],
    "pieges": [
        "pH = 0 est possible (très acide) : l'échelle ne s'arrête pas à 1 !",
        "10^(−pH), pas −10^pH : le signe est dans l'exposant.",
        "Un pH < 7 à 25 °C seulement — la neutralité dépend de la température (admis : 7).",
    ],
    "formules": ["pH = −log[H₃O⁺]", "[H₃O⁺] = 10^(−pH)",
                 "dilution ×10 → pH +1 (acide)"],
}

CH_ELEC = {
    "intro": "Un circuit électrique en courant continu : les électrons circulent dans "
             "le sens inverse du courant conventionnel. Intensité et tension obéissent "
             "à des lois simples : nœuds, mailles et loi d'Ohm.",
    "methodes": [
        {"nom": "Méthode 1 — mesurer correctement",
         "texte": "Intensité I en ampères (A) : AMPÈREMÈTRÉ en SÉRIE. Tension U en "
                  "volts (V) : VOLTMÈTRE en DÉRIVATION (parallèle) au dipôle. Sens "
                  "conventionnel du courant : du + vers le − à l'extérieur du "
                  "générateur (les électrons font l'inverse)."},
        {"nom": "Méthode 2 — lois des nœuds et d'additivité",
         "texte": "Nœud : ΣI entrantes = ΣI sortantes. Série : l'intensité est la "
                  "même partout ; l'additivité des tensions : U_générateur = "
                  "ΣU_récepteurs (loi des mailles). Parallèle : même tension aux bornes "
                  "de chaque branche."},
        {"nom": "Méthode 3 — loi d'Ohm et associations de résistors",
         "texte": "U = R·I (R en ohms Ω). Série : R_eq = R₁ + R₂ (plus grand). "
                  "Parallèle : 1/R_eq = 1/R₁ + 1/R₂ (plus petit que chaque résistance). "
                  "Deux résistors identiques en parallèle : R_eq = R/2."},
    ],
    "exemples": [
        {"question": "Un résistor R = 220 Ω est parcouru par I = 50 mA. Tension à ses "
                     "bornes ? Et si on lui ajoute R' = 330 Ω en série sous U = 12 V ?",
         "etapes": ["I = 50 mA = 0,050 A ; U = R×I = 220 × 0,050 = 11 V",
                    "Série : R_eq = 220 + 330 = 550 Ω",
                    "I' = U/R_eq = 12/550 ≈ 0,022 A ≈ 22 mA"],
         "reponse": "U = 11 V ; puis I' ≈ 22 mA (l'intensité baisse : R_eq augmente)."},
    ],
    "pieges": [
        "Convertir les mA en A avant la loi d'Ohm.",
        "En série l'intensité est commune ; en parallèle c'est la tension.",
        "Un voltmètre branché en série ne mesure rien de bon : il bloque le circuit.",
    ],
    "formules": ["U = R·I", "nœud : ΣI_in = ΣI_out",
                 "série : R_eq = ΣR ; parallèle : 1/R_eq = Σ(1/R)"],
}

CH_ENERGIE = {
    "intro": "Puissance et énergie électriques : elles relient le circuit à la facture "
             "d'électricité et aux plaques signalétiques des appareils du quotidien.",
    "methodes": [
        {"nom": "Méthode 1 — calculer une puissance",
         "texte": "P = U × I (watts). Plaque signalétique d'un radiateur : "
                  "« 230 V — 2000 W » → I = P/U = 2000/230 ≈ 8,7 A : l'installation "
                  "et le fusible doivent supporter ce courant."},
        {"nom": "Méthode 2 — énergie consommée",
         "texte": "E = P × t. En joules si t en secondes. Pour une facture : P en kW "
                  "et t en heures → E en kWh avec 1 kWh = 3,6 × 10⁶ J. "
                  "Coût = E(kWh) × prix unitaire."},
        {"nom": "Méthode 3 — lire une facture",
         "texte": "Additionne les énergies de chaque appareil : E_i = P_i × t_i "
                  "(convertir minutes en heures !). Ex : une lampe 60 W allumée 5 h/j "
                  "pendant 30 jours → E = 60 × 150 = 9000 Wh = 9 kWh."},
    ],
    "exemples": [
        {"question": "Un chauffe-eau de 2,2 kW fonctionne 2 h par jour. Énergie et "
                     "coût mensuel (30 jours) à 1,1 DH/kWh ?",
         "etapes": ["E/jour = 2,2 × 2 = 4,4 kWh",
                    "E/mois = 4,4 × 30 = 132 kWh",
                    "Coût = 132 × 1,1 = 145,2 DH"],
         "reponse": "132 kWh par mois, soit ≈ 145 DH."},
    ],
    "pieges": [
        "kWh n'est pas une unité SI (c'est le joule) mais c'est l'unité de facture : 1 kWh = 3,6 MJ.",
        "Convertir les minutes en heures (30 min = 0,5 h) avant E = P·t.",
        "P en W et U en V : I sort en A — vérifier les ordres de grandeur.",
    ],
    "formules": ["P = U·I (W)", "E = P·t (J ou kWh)", "1 kWh = 3,6 × 10⁶ J",
                 "coût = E × prix du kWh"],
}

V = lambda *xs: list(xs)

# chapitres existants : leçon remplacée + exercices supplémentaires
UPGRADES = {
    "L'atome et la structure de la matière": {
        "semestre": 1, "lecon": L_ATOME,
        "exos": [
            (1, "Manuel", "L'atome de chlore a pour symbole 35/17 Cl. Déterminer sa "
             "composition puis sa configuration électronique.",
             "Z = 17 protons ; neutrons = 35 − 17 = 18 ; électrons = 17\n"
             "Configuration : (K)² (L)⁸ (M)⁷ → 7 électrons de valence.",
             "K (2), L (8), puis ce qui reste en M.",
             V({"enonce": "L'ion chlorure Cl⁻ : combien d'électrons ?",
                "solution": "17 + 1 = 18 électrons → (K)² (L)⁸ (M)⁸ : octet ✓"})),
            (2, "Contrôle", "L'aluminium Z = 13 forme-t-il plutôt un cation ou un "
             "anion ? Justifier par sa configuration et écrire la formation de l'ion.",
             "Config : (K)² (L)⁸ (M)³ → 3 électrons de valence.\n"
             "Plus simple à perdre 3 e⁻ que d'en gagner 5 → cation Al³⁺.\n"
             "Al → Al³⁺ + 3e⁻ (octet atteint : couche M vide... couche L devient "
             "dernière couche pleine à 8).",
             "Compter les électrons de valence : < 4 → cation ; > 4 → anion.",
             V()),
        ],
    },
    "La mole et les concentrations": {
        "semestre": 1, "lecon": L_MOLE,
        "exos": [
            (1, "Manuel", "Calculer la masse molaire moléculaire du sulfate de cuivre "
             "CuSO₄. (M(Cu) = 63,5 ; M(S) = 32 ; M(O) = 16 g/mol)",
             "M = 63,5 + 32 + 4×16 = 63,5 + 32 + 64 = 159,5 g/mol",
             "Additionner avec les indices : Cu ×1, S ×1, O ×4.",
             V({"enonce": "Quelle quantité de matière dans 31,9 g de CuSO₄ ?",
                "solution": "n = m/M = 31,9/159,5 = 0,20 mol"})),
            (2, "Contrôle", "On dissout m = 8,5 g de glucose (M = 180 g/mol) dans "
             "V = 100 mL d'eau. Calculer n puis C.",
             "n = 8,5/180 ≈ 0,047 mol\nC = n/V = 0,047/0,100 ≈ 0,47 mol/L",
             "Convertir 100 mL = 0,100 L AVANT de diviser.",
             V({"enonce": "Et la concentration massique Cm ?",
                "solution": "Cm = m/V = 8,5/0,100 = 85 g/L ; vérif : C×M = 0,47×180 ≈ 85 ✓"})),
            (3, "Type Examen Régional", "On veut obtenir V₂ = 250 mL de solution de "
             "sérum physiologique dilué 5 fois (F = 5) à partir d'une solution mère. "
             "Décrire le protocole et calculer C₂ sachant C₁ = 9 g/L.",
             "Facteur F = V₂/V₁ → V₁ = V₂/F = 250/5 = 50 mL\n"
             "Protocole : prélever 50 mL à la pipette jaugée, verser dans une fiole "
             "jaugée de 250 mL, compléter au trait de jauge, homogénéiser.\n"
             "C₂ = C₁/F = 9/5 = 1,8 g/L",
             "F = V₂/V₁ = C₁/C₂ : deux expressions du même facteur.",
             V()),
        ],
    },
    "Les mélanges et la pureté": {
        "semestre": 1, "lecon": L_MELANGES,
        "exos": [
            (1, "Manuel", "Classer : eau distillée ; air ; eau + huile ; fer ; eau "
             "sucrée. Corps purs ou mélanges ? Homogènes ou hétérogènes ?",
             "Eau distillée : corps pur composé, homogène\nAir : mélange homogène\n"
             "Eau + huile : mélange hétérogène (2 phases)\nFer : corps pur simple\n"
             "Eau sucrée : mélange homogène (solution)",
             "Une seule phase = homogène ; plusieurs phases visibles = hétérogène.",
             V()),
        (2, "Contrôle", "Une encre verte est déposée sur un chromatogramme ; avec un "
         "solvant adapté, on observe 2 taches : une bleue et une jaune. Conclure. "
         "Quelle technique alternative pour séparer deux liquides miscibles ?",
         "2 taches → l'encre verte est un MÉLANGE de 2 espèces colorées (bleue et "
         "jaune) : ce n'est pas un corps pur.\nPour 2 liquides miscibles de températures "
         "d'ébullition différentes → DISTILLATION (fractionnée).",
         "Nombre de taches = nombre d'espèces migrées.",
         V({"enonce": "Comment séparer eau + sable ? eau + sel ?",
            "solution": "Eau + sable : filtration (sable insoluble). Eau + sel : "
                        "évaporation/cristallisation (sel dissous)."})),
        ],
    },
    "Principe des actions réciproques": {
        "semestre": 1, "lecon": L_RECIPROQUE,
        "exos": [
            (1, "Manuel", "Un ballon de football (m = 430 g) est attiré par la Terre "
             "avec une force de 4,2 N. Quelle est la force exercée par le ballon sur "
             "la Terre ? Donner ses caractéristiques.",
             "Principe des actions réciproques : F(ballon→Terre) = 4,2 N,\n"
             "direction : verticale, sens : vers le ballon (vers le haut),\n"
             "point d'application : centre de la Terre.",
             "Même intensité, même direction, sens opposé, deux corps différents.",
             V({"enonce": "Quel est le poids P de ce ballon ? (g = 9,8 N/kg)",
                "solution": "P = m·g = 0,430 × 9,8 ≈ 4,2 N ✓ cohérent"})),
            (2, "Contrôle", "Caractériser complètement la force exercée par le ressort "
             "d'un dynamomètre sur un objet de masse 200 g suspendu, à l'équilibre.",
             "Point d'application : attache du crochet ; direction : verticale ;\n"
             "sens : vers le haut ; intensité : T = P = m·g = 0,200 × 9,8 ≈ 2,0 N\n"
             "(le ressort compense le poids : équilibre).",
             "À l'équilibre, tension du ressort = poids de l'objet suspendu.",
             V()),
        ],
    },
}


CH_GRAVITATION = {
    "intro": "Tous les corps de l'Univers s'attirent : c'est la GRAVITATION UNIVERSELLE, "
             "décrite par Newton. Le poids d'un objet en est la manifestation locale.",
    "methodes": [
        {"nom": "Méthode 1 — la loi de Newton",
         "texte": "F = G × (m₁ × m₂) / d² : l'attraction est proportionnelle aux MASSes "
                  "et inversement proportionnelle au CARRÉ de la distance entre les "
                  "centres. G = 6,67 × 10⁻¹¹ N·m²·kg⁻² (constante universelle)."},
        {"nom": "Méthode 2 — du poids à la gravitation",
         "texte": "Le poids P = m×g est la force gravitationnelle exercée par la Terre : "
                  "g = G×M_T/R_T² (M_T : masse de la Terre, R_T : rayon). Sur la Lune, "
                  "M et R différents → g_Lune ≈ 1,6 N/kg (6 fois moins)."},
        {"nom": "Méthode 3 — le système solaire et les orbites",
         "texte": "La gravitation retient planètes autour du Soleil, satellites autour des "
                  "planètes. Un satellite en orbite est en CHUTE LIBRE permanente : sa "
                  "vitesse fait qu'il « tombe à côté » de la Terre sans jamais l'atteindre."},
    ],
    "exemples": [
        {"question": "Poids d'un astronaute de 80 kg sur Terre puis sur la Lune ?",
         "etapes": ["Terre : P = 80 × 9,8 = 784 N", "Lune : P = 80 × 1,6 = 128 N"],
         "reponse": "784 N sur Terre, 128 N sur la Lune — sa MASSE reste 80 kg partout."},
    ],
    "pieges": [
        "La masse (kg) ne change pas ; le POIDS (N) dépend de l'astre.",
        "F est divisée par 4 quand la distance double (d² au dénominateur).",
    ],
    "formules": ["F = G·m₁·m₂/d²", "P = m×g", "g = G·M/R²"],
}

CH_SYNTHESE = {
    "intro": "La SYNTHÈSE chimique permet de fabriquer au laboratoire ou en usine des "
             "espèces chimiques naturelles (aspirine, arômes) ou artificielles "
             "(plastiques, médicaments).",
    "methodes": [
        {"nom": "Méthode 1 — réaliser une synthèse",
         "texte": "Protocole type : réactifs dans un ballon → chauffage à reflux "
                  "(accélère la réaction sans perdre de matière) → purification "
                  "(filtration, lavage, recristallisation) → séchage → identification "
                  "(température de fusion, chromatographie) et pesée du produit."},
        {"nom": "Méthode 2 — calculer un rendement",
         "texte": "Rendement = (masse réellement obtenue ÷ masse théorique) × 100. "
                  "La masse théorique se calcule avec les quantités de matière : "
                  "n = m/M. Un rendement < 100 % est normal (pertes, réaction "
                  "incomplète)."},
        {"nom": "Méthode 3 — nature ou synthèse ?",
         "texte": "Une espèce synthétique a les MÊMES propriétés que la naturelle (même "
                  "molécule). L'intérêt : grande quantité, coût réduit, protection des "
                  "ressources (ex : aspirine au lieu d'écorce de saule), et création de "
                  "molécules inconnues dans la nature."},
    ],
    "exemples": [
        {"question": "n = 0,5 mol de réactif limitant donne au maximum 0,5 mol de "
                     "produit (M = 180 g/mol). Masse théorique et rendement si on "
                     "obtient 72 g ?",
         "etapes": ["m_théorique = n × M = 0,5 × 180 = 90 g",
                    "Rendement = 72/90 × 100 = 80 %"],
         "reponse": "90 g théoriques ; rendement 80 %."},
    ],
    "pieges": [
        "Le rendement n'est jamais supérieur à 100 %.",
        "Chauffage à REFLUX = chauffer sans perdre les vapeurs (condensateur).",
    ],
    "formules": ["n = m/M", "rendement = m_obtenue/m_théorique × 100"],
}

NEW_CHAPTERS = [
    (1, "La gravitation universelle", "Interaction gravitationnelle entre corps : formule, "
     "poids et gravitation, système solaire.",
     CH_GRAVITATION, [
        (1, "Manuel", "Énoncer la loi de gravitation universelle et donner sa formule.",
         "Deux corps s'attirent avec des forces opposées de même valeur :\n"
         "F = G × (m₁ × m₂) / d², avec G = 6,67 × 10⁻¹¹ (SI), masses en kg, distance "
         "d entre centres en m.\nLe poids est la force de gravitation exercée par la "
         "Terre : P = m × g, avec g = G × M_T / R_T² ≈ 9,8 N/kg.",
         "Gravitation = attraction mutuelle ; le poids en est un cas particulier.",
         V({"enonce": "Que vaut le poids d'un objet de 5 kg sur la Lune "
                       "(g_Lune ≈ 1,6 N/kg) ?",
            "solution": "P = m × g = 5 × 1,6 = 8 N (contre 49 N sur Terre : la Lune "
                        "attire 6 fois moins)."})),
        (2, "Contrôle", "Deux sphères de 10 kg et 20 kg ont leurs centres distants de "
         "2 m. Calculer la force d'attraction (G = 6,67 × 10⁻¹¹).",
         "F = G × (m₁ × m₂) / d²\n= 6,67 × 10⁻¹¹ × (10 × 20) / 4\n"
         "= 6,67 × 10⁻¹¹ × 50 = 3,3 × 10⁻⁹ N",
         "Puissance de 10 : masses se multiplient, distance au CARRÉ divise.",
         V({"enonce": "Si on double la distance d, que devient F ?",
            "solution": "F est divisée par 4 (d² passe de 4 à 16 : ×4 au dénominateur)."})),
        (3, "Type Examen Régional", "① Expliquer pourquoi la Lune tourne autour de la "
         "Terre sans s'écraser dessus. ② Calculer g à l'altitude de la Station spatiale "
         "(R_T = 6371 km, h ≈ 400 km) sachant g₀ = 9,8 N/kg. ③ Pourquoi les astronautes "
         "flottent-ils ?",
         "① La gravitation attire la Lune vers la Terre, mais sa vitesse la fait "
         "« tomber à côté » : orbite = chute perpétuelle.\n"
         "② g = g₀ × (R_T/(R_T+h))² = 9,8 × (6371/6771)² ≈ 9,8 × 0,885 ≈ 8,7 N/kg.\n"
         "③ Ils ne flottent pas parce qu'il n'y a pas de gravité (elle vaut encore "
         "≈ 8,7 N/kg !) : ils sont en CHUTE LIBRE permanente autour de la Terre.",
         "Orbite = chute libre ; g diminue en 1/d², pas brutalement à 400 km."),
     ]),
    (1, "La synthèse des espèces chimiques", "Fabriquer une espèce chimique naturelle au "
     "laboratoire : synthèse, rendement, intérêt industriel.",
     CH_SYNTHESE, [
        (1, "Manuel", "Qu'est-ce qu'une synthèse chimique et quel est son intérêt ?",
         "Fabriquer au laboratoire ou en usine une espèce chimique qui existe dans la "
         "nature (aspirine, arômes, colorants) ou qui est inconnue dans la nature "
         "(plastiques, médicaments nouveaux).\nIntérêt : produire en grande quantité, "
         "moins cher, avec pureté contrôlée, et protéger les ressources naturelles.",
         "Nature → copier (synthèse) → améliorer.",
         V({"enonce": "Citer 2 espèces chimiques synthétisées par l'industrie.",
            "solution": "L'aspirine (acide acétylsalicylique), l'ammoniac (NH₃), les "
                        "arômes artificiels, les colorants, les plastiques..."})),
        (2, "Contrôle", "Une synthèse théorique permettrait d'obtenir 12 g de produit ; "
         "on en recueille 9 g. Calculer le rendement.",
         "Rendement = masse obtenue / masse théorique × 100\n"
         "= 9/12 × 100 = 75 %",
         "Rendement = obtenu ÷ théorique (toujours ≤ 100 %).",
         V({"enonce": "Pourquoi le rendement est-il souvent inférieur à 100 % ?",
            "solution": "Pertes lors des transferts (verrerie), réaction incomplète, "
                        "produits secondaires, purification qui élimine une partie du "
                        "produit."})),
        (3, "Type Examen Régional", "On synthétise l'aspirine : 6,0 g d'acide "
         "salicylique (M = 138 g/mol) réagissent en excès d'anhydride acétique. "
         "① Calculer la quantité de matière d'acide salicylique. ② La masse "
         "d'aspirine théorique attendue est 8,7 g ; on en obtient 6,5 g : rendement ? "
         "③ Citer 2 précautions de sécurité au laboratoire.",
         "① n = m/M = 6,0/138 ≈ 0,043 mol.\n"
         "② Rendement = 6,5/8,7 × 100 ≈ 75 %.\n"
         "③ Blouse, lunettes et gants ; travailler sous hotte (vapors toxiques) ; ne "
         "jamais goûter les produits ; manipuler les réactifs corrosifs avec précaution.",
         "n = m/M puis rendement = obtenu/théorique."),
     ]),
]

# chapitres historiques du programme (inertie, actions réciproques...)
NEW_CHAPTERS += [
    (1, "Le principe d'inertie et l'équilibre", "Forces compensées, repos, mouvement "
     "rectiligne uniforme, équilibre d'un solide soumis à 2 ou 3 forces.",
     CH_INERTIE, [
        (1, "Manuel", "Une voiture roule sur autoroute en ligne droite à 110 km/h "
         "constante. Que peut-on dire de la somme des forces qu'elle subit ?",
         "Mouvement rectiligne uniforme → principe d'inertie → ΣF = 0\n"
         "Le moteur compense exactement les frottements et la résistance de l'air.",
         "Vitesse constante = forces compensées (pas « pas de forces »).",
         V({"enonce": "Le conducteur accélère. Que devient ΣF ?",
            "solution": "ΣF ≠ 0 : la vitesse varie, le principe d'inertie ne s'applique plus."})),
        (2, "Contrôle", "Un palet de hockey glisse sur une patinoire horizontale avec "
         "une vitesse quasi constante de 8 m/s. Frottements négligeables. Décrire "
         "les forces et conclure.",
         "Poids P (vertical, vers le bas) et réaction R de la glace (verticale, vers "
         "le haut).\nFrottements négligés → 2 forces.\nMouvement rectiligne uniforme → "
         "P et R se compensent : même direction, R = P, sens opposés.",
         "Le mouvement horizontal uniforme n'exige AUCUNE force horizontale !",
         V()),
        (2, "Manuel", "Un lustre de masse 5,0 kg est suspendu, immobile, à un câble. "
         "Calculer la tension du câble. (g = 9,8 N/kg)",
         "Équilibre → tension T compense le poids : T = P = m·g = 5,0 × 9,8 = 49 N\n"
         "T verticale, vers le haut, appliquée au point d'attache.",
         "Objet suspendu immobile : T = P (2 forces seulement).",
         V({"enonce": "Même lustre suspendu par DEUX câbles identiques symétriques : "
                      "que devient la tension de chaque câble ?",
            "solution": "Chaque câble porte la moitié du poids (si verticaux) : "
                        "T = 49/2 = 24,5 N (s'ils sont inclinés, T > 24,5 N)."})),
        (3, "Type Examen Régional", "Un tableur (m = 800 g) est posé immobile sur une "
         "table inclinée. La réaction de la table est modélisée par R. Expliquer "
         "pourquoi le tableur ne glisse pas, et donner la relation entre les forces.",
         "Le tableur est immobile → équilibre → les forces se compensent.\n"
         "3 forces : poids P (vertical, bas), réaction normale N (perpendiculaire à "
         "la table), frottement f (le long de la table, vers le haut).\n"
         "Relation : N + f + P = 0 (triangle des forces fermé).\n"
         "C'est le frottement f qui empêche le glissement.",
         "Immobile ⟺ somme vectorielle des forces = 0, même sur plan incliné.",
         V()),
    ]),

    (2, "La réaction chimique et le bilan de matière", "Équation-bilan ajustée, loi "
     "de Lavoisier, tableau d'avancement, réactif limitant.", CH_REACTION, [
        (1, "Manuel", "Ajuster les équations : ① H₂ + O₂ → H₂O ② Al + O₂ → Al₂O₃ "
         "③ C₃H₈ + O₂ → CO₂ + H₂O",
         "① 2H₂ + O₂ → 2H₂O\n② 4Al + 3O₂ → 2Al₂O₃\n"
         "③ C₃H₈ + 5O₂ → 3CO₂ + 4H₂O",
         "Équilibrer un élément à la fois : C, puis H, puis O (les diatomiques en dernier).",
         V({"enonce": "Vérifier la ③ : compter les O des deux côtés.",
            "solution": "Gauche : 5×2 = 10 O ; droite : 3×2 + 4×1 = 10 O ✓"})),
        (2, "Contrôle", "La combustion complète de 0,50 mol de méthane CH₄ : "
         "CH₄ + 2O₂ → CO₂ + 2H₂O. Quelles quantités de O₂ consommées et de CO₂ "
         "formées ?",
         "Coefficients : 1 CH₄ réagit avec 2 O₂ et donne 1 CO₂\n"
         "n(O₂) = 2 × 0,50 = 1,0 mol\nn(CO₂) = 1 × 0,50 = 0,50 mol\n"
         "n(H₂O) = 2 × 0,50 = 1,0 mol",
         "Les coefficients donnent les proportions MOLAIRES.",
         V()),
        (2, "Manuel", "On fait réagir 3,0 mol de H₂ avec 2,0 mol de N₂ : "
         "N₂ + 3H₂ → 2NH₃ (ammoniac). Trouver le réactif limitant et la quantité "
         "d'ammoniac formé.",
         "Pour N₂ : x_max = 2,0/1 = 2,0 mol\nPour H₂ : x_max = 3,0/3 = 1,0 mol\n"
         "x_max = 1,0 mol → H₂ limitant\nn(NH₃) = 2 × 1,0 = 2,0 mol\n"
         "N₂ restant : 2,0 − 1,0 = 1,0 mol",
         "Diviser chaque n initial par son coefficient : le minimum est limitant.",
         V()),
        (3, "Type Examen Régional", "On introduit 6,4 g de cuivre dans 100 mL de "
         "solution d'acide nitrique contenant 0,20 mol de NO₃⁻... (données adaptées) : "
         "Cu + 4H⁺ + 2NO₃⁻ → Cu²⁺ + 2NO₂ + 2H₂O. Sachant n(Cu) = 0,10 mol, montrer "
         "que Cu est le réactif limitant et calculer V(CO₂)... V(NO₂) dégagé à l'état "
         "final en mol.",
         "Pour Cu : x_max = 0,10/1 = 0,10 mol\n"
         "Pour NO₃⁻ : x_max = 0,20/2 = 0,10 mol → les deux s'épuisent ensemble "
         "(mélange stœchiométrique !)\nn(NO₂) = 2 × 0,10 = 0,20 mol\n"
         "Aucun excès : tout est consommé.",
         "Mélange stœchiométrique = proportions exactes de l'équation : rien ne reste.",
         V()),
    ]),

    (2, "Les solutions acides et basiques : le pH", "pH, concentration en ions "
     "oxonium, indicateurs colorés, sécurité.", CH_PH, [
        (1, "Manuel", "Calculer [H₃O⁺] pour pH = 5, puis pour pH = 8,6. Conclure sur "
         "le caractère de chaque solution.",
         "pH 5 : [H₃O⁺] = 10⁻⁵ mol/L → acide (pH < 7)\n"
         "pH 8,6 : [H₃O⁺] = 10^(−8,6) ≈ 2,5 × 10⁻⁹ mol/L → basique (pH > 7)",
         "pH < 7 acide, = 7 neutre, > 7 basique (à 25 °C).",
         V({"enonce": "Comparer l'acidité de pH 2 et pH 5.",
            "solution": "Différence de 3 unités → 10³ = 1000 fois plus acide à pH 2."})),
        (2, "Contrôle", "Une solution d'acide chlorhydrique contient "
         "[H₃O⁺] = 4,0 × 10⁻³ mol/L. Calculer son pH.",
         "pH = −log(4,0 × 10⁻³) = −(log 4,0 − 3) = 3 − 0,60 = 2,4",
         "pH = −log[H₃O⁺] : calculatrice en mode « log » ; résultat entre 2 et 3, "
         "cohérent avec 10⁻³.",
         V()),
        (2, "Manuel", "Le jus de citron (pH 2,3) est dilué 10 fois puis 100 fois. "
         "Quels sont les nouveaux pH (approximativement) ?",
         "Dilution ×10 : pH + 1 → 3,3\nDilution ×100 : pH + 2 → 4,3",
         "Dilution d'un acide : le pH se rapproche de 7 d'une unité par facteur 10.",
         V({"enonce": "Peut-on dépasser pH 7 en diluant un acide ?",
            "solution": "Non : le pH tend vers 7 sans l'atteindre ni le dépasser "
                        "(l'apport d'ions H₃O⁺ demeure)."})),
        (3, "Type Examen Régional", "Décrire un protocole de dilution ×100 d'acide "
         "sulfurique en précisant les règles de sécurité et la verrerie, puis le pH "
         "final sachant pH(initial) = 1,0.",
         "SÉCURITÉ : blouse + lunettes ; verser TOUJOURS l'acide DANS l'eau (jamais "
         "l'inverse), lentement.\nProtocole : prélever 5,0 mL de solution mère à la "
         "pipette jaugée ; verser dans une fiole jaugée de 500 mL contenant un peu "
         "d'eau distillée ; compléter au trait de jauge ; homogénéiser.\n"
         "F = 500/5 = 100 → pH_final = 1,0 + 2 = 3,0",
         "Dilution d'acide concentré : exothermique — jamais l'eau dans l'acide !",
         V()),
    ]),

    (2, "Le circuit électrique : courant et tension", "Intensité, tension, lois des "
     "nœuds et des mailles, loi d'Ohm, résistors série/parallèle.", CH_ELEC, [
        (1, "Manuel", "Un résistor de 100 Ω est traversé par un courant de 0,25 A. "
         "Quelle est la tension à ses bornes ?",
         "U = R × I = 100 × 0,25 = 25 V",
         "Loi d'Ohm : U = R·I (U en V, R en Ω, I en A).",
         V({"enonce": "Et si I = 25 mA ?",
            "solution": "I = 0,025 A → U = 100 × 0,025 = 2,5 V (bien convertir !)"})),
        (2, "Contrôle", "Dans un nœud arrivent I₁ = 2,0 A et I₂ = 1,5 A ; il en sort "
         "I₃ = 0,8 A et I₄. Calculer I₄.",
         "Loi des nœuds : I₁ + I₂ = I₃ + I₄\n3,5 = 0,8 + I₄ → I₄ = 2,7 A",
         "Ce qui entre = ce qui sort (le courant ne s'accumule pas).",
         V({"enonce": "Deux lampes en série sous 9 V : U₁ = 4,0 V. U₂ ?",
            "solution": "Additivité : U = U₁ + U₂ → U₂ = 9 − 4 = 5,0 V"})),
        (2, "Manuel", "Calculer la résistance équivalente : ① R₁ = 30 Ω et R₂ = 60 Ω "
         "en série ; ② les mêmes en parallèle.",
         "① R_eq = 30 + 60 = 90 Ω\n"
         "② 1/R_eq = 1/30 + 1/60 = 2/60 + 1/60 = 3/60 → R_eq = 20 Ω\n"
         "(plus petit que chaque résistance ✓)",
         "Série : on additionne. Parallèle : inverses, puis re-inverser.",
         V({"enonce": "Deux résistors identiques de 220 Ω en parallèle : R_eq ?",
            "solution": "R_eq = R/2 = 110 Ω"})),
        (3, "Type Examen Régional", "Un générateur 12 V alimente R₁ = 100 Ω en série "
         "avec (R₂ = 150 Ω ∥ R₃ = 300 Ω). Calculer R_eq, puis l'intensité débitée, "
         "puis la tension aux bornes du groupe parallèle.",
         "Parallèle : 1/R₂₃ = 1/150 + 1/300 = 2/300 + 1/300 = 3/300 → R₂₃ = 100 Ω\n"
         "R_eq = 100 + 100 = 200 Ω\nI = U/R_eq = 12/200 = 0,060 A = 60 mA\n"
         "U₂₃ = R₂₃ × I = 100 × 0,060 = 6,0 V",
         "Réduire le parallèle d'abord, puis traiter le série ; U₂₃ avec la loi d'Ohm.",
         V()),
    ]),

    (2, "Puissance et énergie électriques", "Puissance P = U·I, énergie E = P·t, "
     "kWh et facture d'électricité.", CH_ENERGIE, [
        (1, "Manuel", "Un fer à repasser porte « 230 V — 1000 W ». Calculer "
         "l'intensité absorbée.",
         "I = P/U = 1000/230 ≈ 4,3 A",
         "I = P/U : l'intensité détermine le fusible nécessaire.",
         V({"enonce": "Et pour une lampe 230 V — 15 W ?",
            "solution": "I = 15/230 ≈ 0,065 A = 65 mA"})),
        (2, "Contrôle", "Un radiateur de 1500 W fonctionne 3 h par jour. Énergie en "
         "kWh sur 30 jours, puis coût à 1,2 DH/kWh.",
         "E/j = 1,5 × 3 = 4,5 kWh\nE/mois = 4,5 × 30 = 135 kWh\n"
         "Coût = 135 × 1,2 = 162 DH",
         "P en kW × t en heures = kWh ; puis coût = E × prix.",
         V({"enonce": "Cette énergie en joules ?",
            "solution": "135 × 3,6 × 10⁶ = 4,86 × 10⁸ J"})),
        (2, "Manuel", "Convertir : ① 2,5 kWh en joules ② 900 kJ en kWh",
         "① 2,5 × 3,6 × 10⁶ = 9,0 × 10⁶ J\n② 900 kJ = 9,0 × 10⁵ J → "
         "9,0 × 10⁵/3,6 × 10⁶ = 0,25 kWh",
         "1 kWh = 3,6 × 10⁶ J = 3,6 MJ.",
         V()),
        (3, "Type Examen Régional", "Une famille utilise : 4 lampes de 20 W, 5 h/jour "
         "chacune ; un réfrigérateur de 100 W fonctionnant en continu (24 h/24) ; un "
         "téléviseur 80 W, 4 h/jour. Calculer l'énergie mensuelle (30 jours) et le "
         "coût à 1,1 DH/kWh.",
         "Lampes : 4 × 20 = 80 W → 0,080 kW × 5 h × 30 j = 12 kWh\n"
         "Réfrigérateur : 0,100 kW × 24 h × 30 j = 72 kWh\n"
         "TV : 0,080 kW × 4 h × 30 j = 9,6 kWh\n"
         "Total = 12 + 72 + 9,6 = 93,6 kWh → coût = 93,6 × 1,1 ≈ 103 DH",
         "Une appliance en continu domine la facture : le réfrigérateur pèse 3 fois "
         "plus que les lampes !",
         V()),
    ]),
]


def sync(db):
    """Enrichit les chapitres PC existants + ajoute les nouveaux (non destructif)."""
    import json as _json

    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    pid = subjects["PC"]
    n_up = n_ch = n_ex = 0

    def add_exos(cid, exos):
        nonlocal n_ex
        for ex in exos:
            diff, source, enonce, solution, astuce = ex[:5]
            variantes = ex[5] if len(ex) > 5 else {}
            dupe = db.query("SELECT id FROM exercises WHERE chapter_id = ? AND enonce = ?",
                            (cid, enonce), one=True)
            if not dupe:
                db.execute(
                    "INSERT INTO exercises(chapter_id, difficulte, source, enonce, "
                    "solution, astuce, variantes) VALUES (?,?,?,?,?,?,?)",
                    (cid, diff, source, enonce, solution, astuce,
                     _json.dumps(variantes, ensure_ascii=False)))
                n_ex += 1

    for titre, up in UPGRADES.items():
        ch = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                      "AND titre = ?", (pid, titre), one=True)
        if ch:
            db.execute("UPDATE chapters SET lecon = ?, semestre = ? WHERE id = ?",
                       (_json.dumps(up["lecon"], ensure_ascii=False),
                        up["semestre"], ch["id"]))
            add_exos(ch["id"], up["exos"])
            n_up += 1

    for semestre, titre, resume, lecon, exos in NEW_CHAPTERS:
        exists = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                          "AND titre = ?", (pid, titre), one=True)
        if not exists:
            cid = db.execute(
                "INSERT INTO chapters(subject_id, niveau, semestre, titre, resume, lecon) "
                "VALUES (?,?,?,?,?,?)",
                (pid, "TC", semestre, titre, resume,
                 _json.dumps(lecon, ensure_ascii=False)))
            n_ch += 1
        else:
            cid = exists["id"]
            db.execute("UPDATE chapters SET lecon = ?, semestre = ? WHERE id = ?",
                       (_json.dumps(lecon, ensure_ascii=False), semestre, cid))
        add_exos(cid, exos)

    print(f"[sync TC PC] {n_up} leçons enrichies, +{n_ch} chapitres, +{n_ex} exercices")
