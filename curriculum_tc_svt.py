# -*- coding: utf-8 -*-
"""
curriculum_tc_svt.py — Programme COMPLET de SVT du Tronc Commun (programme
officiel marocain) : biodiversité, classification, origine de la biodiversité,
cellule + géologie externe (érosion, sédimentation, sols).

Chapitres existants enrichis + nouveaux chapitres + exercices de tous types.
"""

L_CELLULE = {
    "intro": "La cellule est l'unité structurelle (tout être vivant est fait de "
             "cellules) et fonctionnelle (chaque cellule accomplit les fonctions de la "
             "vie). Le microscope révèle son univers.",
    "methodes": [
        {"nom": "Méthode 1 — utiliser et grossir avec un microscope optique",
         "texte": "Grossissement = grossissement de l'objectif × celui de l'oculaire "
                  "(ex : 40 × 10 = 400 fois). La taille réelle d'un objet = taille "
                  "mesurée sur la photo (ou dessin) ÷ grossissement. Ordres de grandeur "
                  ": cellule animale ≈ 10-20 µm ; bactérie ≈ 1-5 µm."},
        {"nom": "Méthode 2 — comparer cellule animale et végétale",
         "texte": "Commun : membrane, cytoplasme, noyau, mitochondries. Spécifique au "
                  "végétal : PAROI cellulosique (rigide), CHLOROPLASTES "
                  "(photosynthèse), grande VACUOLE centrale. Reconnaître sur photo : "
                  "formes anguleuses + paroi → végétal."},
        {"nom": "Méthode 3 — distinguer procaryote et eucaryote",
         "texte": "Eucaryote : noyau délimité par une enveloppe + organites. "
                  "Procaryote (bactéries) : PAS de noyau (ADN libre dans le cytoplasme), "
                  "pas d'organites membranaires, petite taille. Les 5 règnes : animaux, "
                  "végétaux, champignons, protistes, monères (procaryotes)."},
    ],
    "exemples": [
        {"question": "Sur un schéma à ×400, une cellule mesure 48 mm. Quelle est sa "
                     "taille réelle ?",
         "etapes": ["Taille réelle = taille observée ÷ grossissement",
                    "48 mm ÷ 400 = 0,12 mm = 120 µm"],
         "reponse": "120 µm : taille typique d'une cellule animale."},
    ],
    "pieges": [
        "La paroi cellulosique n'existe QUE chez le végétal (les animaux n'en ont pas).",
        "Toutes les cellules eucaryotes ont un noyau : sans noyau → procaryote.",
        "Convertir mm → µm : 1 mm = 1000 µm.",
    ],
    "formules": ["G = G_objectif × G_oculaire",
                 "taille réelle = taille observée ÷ G",
                 "1 µm = 10⁻⁶ m ; 1 nm = 10⁻⁹ m"],
}

L_BIODIVERSITE = {
    "intro": "La biodiversité, c'est la richesse des êtres vivants : diversité des "
             "milieux, des espèces et des individus. Elle se répartit inégalement "
             "selon les conditions du milieu, auxquelles les espèces s'adaptent.",
    "methodes": [
        {"nom": "Méthode 1 — identifier les facteurs écologiques",
         "texte": "Facteurs ABIOTIQUES (non vivants) : température, lumière, humidité, "
                  "nature du sol, salinité. Facteurs BIOTIQUES (vivants) : "
                  "prédation, compétition, symbiose, pollinisation. Un facteur "
                  "écologique = élément du milieu qui agit sur les êtres vivants."},
        {"nom": "Méthode 2 — expliquer la répartition des êtres vivants",
         "texte": "Chaque espèce a des exigences écologiques (tolérance à la "
                  "température, à l'eau...). Ex : le thuya ne pousse que sur sol "
                  "calcaire ; les cactus en zones arides. La répartition s'explique "
                  "par la conjugaison des facteurs : comparer 2 milieux = comparer "
                  "leurs facteurs."},
        {"nom": "Méthode 3 — reconnaître une adaptation",
         "texte": "Adaptation morphologique (cactus : épines = feuilles réduites pour "
                  "limiter la transpiration), physiologique (chameau : résiste à la "
                  "déshydratation), comportementale (migration des oiseaux). Toujours "
                  "la relier à la contrainte du milieu."},
    ],
    "exemples": [
        {"question": "Pourquoi trouve-t-on des chênes-lièges dans la forêt de la "
                     "Mamora mais pas dans le Sahara ?",
         "etapes": ["Exigences du chêne-liège : climat humide, sols variés, pas de "
                    "grandes sécheresses",
                    "Mamora : pluviométrie suffisante, climat méditerranéen ✓",
                    "Sahara : pluviométrie < 100 mm/an, températures extrêmes ✗"],
         "reponse": "La répartition suit les facteurs abiotiques (eau, température)."},
    ],
    "pieges": [
        "L'humain, un prédateur ou un concurrent : les facteurs biotiques incluent l'action humaine.",
        "Adaptation ≠ choix : c'est le résultat de l'évolution, pas une décision de l'animal.",
        "Biodiversité = espèces MAIS aussi diversité génétique et des écosystèmes.",
    ],
    "formules": ["facteurs abiotiques + biotiques = conditions d'un milieu",
                 "espèce endémique : présente uniquement dans une aire limitée"],
}

L_CLASSIFICATION = {
    "intro": "Classer, c'est ranger les êtres vivants selon leurs ressemblances. La "
             "science de la classification utilise la nomenclature binominale et des "
             "clés de détermination hiérarchisées.",
    "methodes": [
        {"nom": "Méthode 1 — utiliser une clé de détermination",
         "texte": "Une clé propose des couples d'assertions numérotées : on choisit "
                  "celle qui correspond à l'individu, on suit la numération indiquée, "
                  "jusqu'au nom de l'espèce. Lire CHAQUE caractère attentivement "
                  "(nombre de doigts, présence de plumes...)."},
        {"nom": "Méthode 2 — la nomenclature binominale (Linné)",
         "texte": "Nom scientifique = Genre + espèce, en latin, souligné/italique. "
                  "Felis catus (chat domestique), Panthera leo (lion), Panthera tigris "
                  "(tigre). Même genre = très proches ; le binôme est UNIVERSEL "
                  "(même nom dans tous les pays)."},
        {"nom": "Méthode 3 — hiérarchiser les groupes",
         "texte": "Embranchement → classe → ordre → famille → genre → espèce. Plus "
                  "on descend, plus les critères sont précis et les individus "
                  "ressemblants. Deux individus de même espèce = interféconds et "
                  "descendance fertile."},
    ],
    "exemples": [
        {"question": "Lion : Panthera leo ; Tigre : Panthera tigris ; Chat : Felis "
                     "catus. Que déduire des noms scientifiques ?",
         "etapes": ["Lion et tigre : même genre Panthera → très proches",
                    "Chat : genre Felis → proche mais moins",
                    "Tous trois : même famille (félidés)"],
         "reponse": "La nomenclature reflète les parentés : même genre = ressemblances "
                    "fortes."},
    ],
    "pieges": [
        "Le nom scientifique s'écrit Genre (majuscule) + espèce (minuscule), en italique.",
        "Deux individus fertiles entre eux appartiennent à la même espèce.",
        "Suivre la numération de la clé : sauter une étape = faux chemin.",
    ],
    "formules": ["nom scientifique = Genre + espèce",
                 "hiérarchie : embranchement > classe > ordre > famille > genre > espèce"],
}

L_ORIGINE_BIO = {
    "intro": "D'où vient la biodiversité ? Des MUTATIONS qui créent de nouvelles "
             "versions de gènes, et de la SÉLECTION NATURELLE qui favorise les plus "
             "adaptées. L'évolution s'explique, elle n'est pas un hasard pur.",
    "methodes": [
        {"nom": "Méthode 1 — expliquer la source de la diversité",
         "texte": "Les MUTATIONS (modifications accidentelles de l'ADN, lors de la "
                  "réplication) créent de nouveaux allèles. Elles sont AU HASARD. La "
                  "reproduction sexuelle les mélange (brassage). Un individu plus "
                  "adapté survit mieux et se reproduit davantage."},
        {"nom": "Méthode 2 — appliquer la sélection naturelle",
         "texte": "Le milieu « sélectionne » : dans un milieu industriel sombre, les "
                  "papillons clairs sont repérés et mangés → les foncés dominent. "
                  "Résistance des bactéries aux antibiotiques : les souches résistantes "
                  "survivent au traitement et se multiplient."},
        {"nom": "Méthode 3 — relier preuves et évolution",
         "texte": "Preuves : fossiles (séries évolutives du cheval), analogies "
                  "(aile d'oiseau/nageoire de baleine : même plan d'organisation), "
                  "embryologie comparée. La biodiversité actuelle = résultat de "
                  "millions d'années de mutations + sélection + isolement."},
    ],
    "exemples": [
        {"question": "Les moustiques résistent de plus en plus aux insecticides. "
                     "Expliquer ce phénomène.",
         "etapes": ["Des mutations spontanées rendent certains moustiques résistants",
                    "L'insecticide tue les sensibles, épargne les résistants (sélection)",
                    "Les résistants se reproduisent → leur allèle devient majoritaire"],
         "reponse": "L'insecticide agit comme agent sélectif : c'est la sélection naturelle."},
    ],
    "pieges": [
        "Les mutations sont ALÉATOIRES ; la sélection ne crée rien, elle trie.",
        "Un individu ne « s'adapte » pas de son vivant : c'est la POPULATION qui évolue sur des générations.",
        "Les antibiotiques ne provoquent pas les résistances : ils les sélectionnent.",
    ],
    "formules": ["mutation (aléatoire) → sélection naturelle (milieu) → évolution",
                 "espèce : population interféconde isolée reproductivement"],
}

CH_EROSION = {
    "intro": "Les montagnes marocaines s'usent : l'eau, le gel et le vent détruisent "
             "les roches (érosion), transportent les débris vers les plaines et les "
             "mers. Un cycle géologique permanent qui façonne les paysages.",
    "methodes": [
        {"nom": "Méthode 1 — distinguer érosion mécanique et chimique",
         "texte": "MÉCANIQUE : la roche est fragmentée (gel/dégel de l'eau dans les "
                  "fissures, ruissellement, vent, vagues) → débris de toutes tailles. "
                  "CHIMIQUE : la roche est DISSOUTE — l'eau légèrement acide dissout "
                  "le calcaire (gouffres, grottes, eau « dure » riche en calcaire "
                  "dissous)."},
        {"nom": "Méthode 2 — reconnaître les agents d'érosion",
         "texte": "EAU COURANTE : vallées en V, cailloux arrondis dans les oueds. "
                  "GEL : roches éclatées en haute altitude. VENT : désert, "
                  "corrasion (polissage), dunes. VAGUES : falaises attaquées. "
                  "L'HUMAIN : déforestation → érosion accélérée (bassins versants)."},
        {"nom": "Méthode 3 — suivre le transport des matériaux",
         "texte": "Trois modes : par suspension (fines, eau trouble), par saltation "
                  "(sauts des grains de sable), par roulissement (galets au fond). "
                  "Plus le courant ralentit, plus les gros éléments se déposent : "
                  "c'est le TRI par taille."},
    ],
    "exemples": [
        {"question": "Une eau de source contient du calcaire dissous. Quel type "
                     "d'érosion l'a produit ? Que peut-on observer à long terme ?",
         "etapes": ["Le CO₂ de l'air + pluie → eau légèrement acide",
                    "Elle dissout la roche calcaire (érosion CHIMIQUE)",
                    "À long terme : grottes, avens, relief karstique ; l'eau reste « dure »"],
         "reponse": "Érosion chimique par dissolution du calcaire."},
    ],
    "pieges": [
        "La dissolution n'est pas une fragmentation : le calcaire disparait DANS l'eau (invisible).",
        "L'érosion mécanique produit des débris ; la chimique produit des ions dissous.",
        "Les galets ronds dans un oued = témoins du transport (polissage mutuel).",
    ],
    "formules": ["érosion mécanique → débris ; érosion chimique → dissolution",
                 "gel : +9 % de volume quand l'eau gèle (fissuration)"],
}

CH_SEDIMENTATION = {
    "intro": "Les débris érodés se déposent, se compactent et se cimentent : voici "
             "comment naissent les roches sédimentaires, archives de l'histoire de la "
             "Terre grâce à leurs fossiles et leurs strates.",
    "methodes": [
        {"nom": "Méthode 1 — classer les sédiments par taille",
         "texte": "Du plus gros au plus fin : blocs et galets (> 2 mm) → CONGLOMÉRAT "
                  "(poudingue) ; sables (0,06-2 mm) → GRÈS ; limons → limonite ; "
                  "argiles (< 4 µm) → ARGILITE/marnes. Le sédiment déposé annonce le "
                  "roche : sable consolidé = grès, etc."},
        {"nom": "Méthode 2 — comprendre la diagenèse",
         "texte": "3 étapes : ① COMPACTATION (le poids des couches supérieures chasse "
                  "l'eau) ② CIMENTATION (des minéraux dissous — calcite, silice — "
                  "soudent les grains) ③ transformations mineures. Sédiment meuble → "
                  "roche cohérente : sable + ciment = grès."},
        {"nom": "Méthode 3 — lire les milieux et les fossiles",
         "texte": "Milieu continental (lac, rivière, désert) ou marin (plage, plateau, "
                  "abysses) : chaque milieu laisse sa signature (granulométrie, "
                  "fossiles marins = milieu marin). STRATIFICATION : les couches se "
                  "déposent horizontalement, la plus BASSE est la plus ancienne "
                  "(principe de superposition)."},
    ],
    "exemples": [
        {"question": "Une roche présente des grains arrondis de 5 mm soudés par un "
                     "ciment calcaire. La nommer et raconter son histoire.",
         "etapes": ["Grains > 2 mm arrondis + ciment → CONGLOMÉRAT (poudingue)",
                    "Histoire : érosion forte → galets transportés (arrondis !) → dépôt "
                    "→ compactation → cimentation par la calcite"],
         "reponse": "Un ancien lit de rivière ou torrent consolidé en roche."},
        {"question": "Dans une falaise, une couche contient des coquilles marines. "
                     "Que peut-on en déduire ?",
         "etapes": ["Fossiles marins → dépôt en milieu marin",
                    "Cette couche est plus ancienne que celles du-dessus (superposition)",
                    "La mer occupait donc ce lieu à cette époque (transgression)"],
         "reponse": "Milieu marin ancien + chronologie relative de la falaise."},
    ],
    "pieges": [
        "Le plus ancien est EN BAS (superposition) — pas en haut !",
        "Grains arrondis = transport long ; grains anguleux = transport court.",
        "Le charbon et le pétrole sont des roches/ressources d'origine organique sédimentaire.",
    ],
    "formules": ["sédimentation = dépôt → compactation → cimentation (diagenèse)",
                 "superposition : couche basse = plus ancienne",
                 "galets → conglomérat ; sable → grès ; argile → argilite"],
}

CH_SOL = {
    "intro": "Le sol est le produit lent de la désagrégation de la roche-mère et de "
             "l'action des êtres vivants : des siècles pour quelques centimètres. Sa "
             "formation est un maillon entre géologie et biologie.",
    "methodes": [
        {"nom": "Méthode 1 — décrire le profil d'un sol",
         "texte": "De haut en bas : horizon A (litière + HUMUS sombre, riche en "
                  "matière organique), horizon B (minéral fin, argiles, souvent rouge "
                  "au Maroc), horizon C (roche-mère altérée/fragmentée), puis roche "
                  "saine. Lire un profil = identifier ces couches."},
        {"nom": "Méthode 2 — expliquer la formation",
         "texte": "① La roche-mère s'altère (érosion mécanique + chimique) → "
                  "particules minérales. ② Les êtres vivants s'installent (lichens "
                  "pionniers !) : litière → décomposeurs → HUMUS. ③ Mélange "
                  "minéral + organique : le sol s'épaissit. Vitesse : 1 cm en "
                  "100-400 ans."},
        {"nom": "Méthode 3 — relier sol et érosion",
         "texte": "Le sol nu (déforestation, surpâturage) est emporté par le "
                  "ruissellement : érosion accélérée, désertification (cas du Maroc). "
                  "La couverture végétale protège le sol : racines qui retiennent, "
                  "feuillage qui amortit les pluies."},
    ],
    "exemples": [
        {"question": "Après un défrichement, un sol s'érode de 5 mm/an. Combien "
                     "d'années de sol perdu par an de formation (1 cm / 200 ans) ?",
         "etapes": ["Formation : 1 cm en 200 ans → 0,05 mm/an",
                    "Érosion : 5 mm/an = 100 fois plus vite !",
                    "Le sol perdu mettra 100 × 200 = 20 000 ans à se reconstituer"],
         "reponse": "Érosion ≫ formation : le sol est une ressource quasi non renouvelable."},
    ],
    "pieges": [
        "L'humus est organique ; les argiles sont minérales : ne pas confondre les horizons.",
        "Les lichens sont souvent les PIONNIERS sur la roche nue.",
        "Un sol s'érode bien plus vite qu'il ne se forme.",
    ],
    "formules": ["profil : A (humus) / B (minéral) / C (roche altérée) / roche-mère",
                 "formation : ≈ 1 cm par 100-400 ans"],
}

V = lambda *xs: list(xs)

UPGRADES = {
    "La cellule, unité de la vie": {
        "semestre": 1, "lecon": L_CELLULE,
        "exos": [
            (1, "Manuel", "Citer 3 structures présentes dans une cellule végétale mais "
             "absentes d'une cellule animale.",
             "Paroi cellulosique ; chloroplastes ; grande vacuole centrale.",
             "Le trio végétal : paroi + chloroplastes + vacuole.",
             V({"enonce": "Et 3 structures communes aux deux ?",
                "solution": "Membrane plasmique, cytoplasme, noyau (et mitochondries)."})),
            (2, "Contrôle", "À ×400, une bactérie observée mesure 2 mm. Sa taille "
             "réelle ? Est-elle eucaryote ou procaryote ?",
             "Taille réelle = 2 mm ÷ 400 = 0,005 mm = 5 µm\n"
             "Bactérie → procaryote (pas de noyau, ADN libre, pas d'organites).",
             "mm ÷ grossissement, puis mm → µm (× 1000).",
             V({"enonce": "Comment distinguer une cellule procaryote sur photo ?",
                "solution": "Absence d'enveloppe nucléaire et de tout organite "
                            "membranaire ; petite taille (1-5 µm)."})),
            (2, "Manuel", "Relier chaque organelle à sa fonction : chloroplaste / "
             "mitochondrie / noyau / vacuole.",
             "Chloroplaste → photosynthèse (fabrique de la matière organique)\n"
             "Mitochondrie → respiration cellulaire (libère l'énergie)\n"
             "Noyau → contient l'ADN, centre d'information\n"
             "Vacuole → réserve d'eau et de substances, turgescence",
             "Fonctions à connaître par cœur pour l'examen régional.",
             V()),
        ],
    },
    "Biodiversité et classification": {
        "semestre": 1, "lecon": L_BIODIVERSITE,
        "exos": [
            (1, "Manuel", "Classer ces facteurs en abiotiques/biotiques : température, "
             "prédation, pluviométrie, compétition, salinité, pollinisation.",
             "Abiotiques : température, pluviométrie, salinité\n"
             "Biotiques : prédation, compétition, pollinisation",
             "Abiotique = non vivant ; biotique = lié aux êtres vivants.",
             V()),
            (2, "Contrôle", "Le caméléon du Maroc vit dans les zones broussailleuses "
             "chaudes. Citer une adaptation morphologique et expliquer son rôle.",
             "Exemples acceptés : pattes préhensiles (saisir les branches) ; langue "
             "protractile (chasse à distance) ; yeux mobiles indépendants (vision "
             "panoramique) ; coloration variable (camouflage → échapper aux "
             "prédateurs).\nChaque adaptation répond à une contrainte du milieu.",
             "Adaptation = structure + rôle + lien avec le milieu.",
             V()),
            (2, "Manuel", "Le nom scientifique du chêne-liège est Quercus suber. Le "
             "chêne vert est Quercus rotundifolia. Que peut-on en déduire ?",
             "Même genre Quercus → très proches (deux chênes) ; espèces distinctes → "
             "non interféconds. Écriture correcte : Quercus suber (genre majuscule, "
             "espèce minuscule, en italique).",
             "Même genre = parenté forte ; binôme universel de Linné.",
             V()),
        ],
    },
    "Origines géologiques de la vie": {
        "titre": "L'origine de la biodiversité",
        "semestre": 1, "lecon": L_ORIGINE_BIO,
        "exos": [
            (2, "Contrôle", "Remettre dans l'ordre : sélection naturelle, mutation, "
             "nouvel allèle majoritaire, milieu modifié.",
             "① Mutation (aléatoire) → ② nouveau allèle apparaît dans la population → "
             "③ milieu modifié qui sélectionne (ou sélection permanente) → ④ l'allèle "
             "favorable devient majoritaire sur des générations.",
             "La mutation CRÉE, le milieu TRI.",
             V()),
            (3, "Type Examen Régional", "Des bactéries deviennent résistantes à un "
             "antibiotique après des années d'utilisation. Expliquer en 4 étapes "
             "pourquoi NE PAS terminer son traitement aggrave le problème.",
             "① Des mutations rendent quelques bactéries résistantes (hasard)\n"
             "② Traitement incomplet : dose trop faible → tue les sensibles, laisse "
             "vivantes les résistantes\n"
             "③ Les résistantes se multiplient sans compétition → population résistante\n"
             "④ L'antibiotique devient inefficace (sélection naturelle accélérée)",
             "L'antibiotique SELECTE les résistantes : c'est l'exemple type de l'examen.",
             V()),
        ],
    },
}

NEW_CHAPTERS = [
    (2, "L'érosion : l'action de l'eau sur les roches", "Érosion mécanique et "
     "chimique, agents, transport des matériaux.", CH_EROSION, [
        (1, "Manuel", "Un bloc de granite se fissure : l'eau s'y infiltre et gèle la "
         "nuit. Quel phénomène est à l'œuvre ? Que se passe-t-il à long terme ?",
         "Eau qui gèle → +9 % de volume → pression dans les fissures → éclatement.\n"
         "Érosion MÉCANIQUE (gélifraction). À long terme : le bloc se fragmente en "
         "débris de plus en plus petits (arène granitique).",
         "Le gel casse, la dissolution dissout : deux érosions différentes.",
         V()),
        (2, "Contrôle", "L'eau d'un oued trouble après la pluie ; celle d'une source "
         "près d'une montagne calcaire est claire mais laisse des dépôts blancs en "
         "bouillant. Expliquer les 2 observations.",
         "Oued trouble : particules argileuses/sables en SUSPENSION (érosion "
         "mécanique, transport).\nSource : calcaire DISSOUS (érosion chimique, ions "
         "Ca²⁺ invisibles) → en bouillant, le calcaire précipite (tartre).",
         "Trouble = solide en suspension ; claire + tartre = dissous.",
         V({"enonce": "Citer 2 indices de transport par un oued.",
            "solution": "Cailloux arrondis (polissage) ; tri par taille : gros près "
                        "de la montagne, fins en aval."})),
        (2, "Manuel", "Relier l'agent d'érosion à sa trace caractéristique : gel / "
         "eau courante / vent / vagues.",
         "Gel → roches éclatées, éboulis en haute montagne\n"
         "Eau courante → vallées en V, galets arrondis\n"
         "Vent → roches polies (corrasion), dunes de sable\n"
         "Vagues → falaises rongées, plates-formes d'abrasion",
         "Chaque agent laisse une signature dans le paysage.",
         V()),
        (3, "Type Examen Régional", "La déforestation d'un bassin versant triple "
         "l'érosion. Expliquer le rôle protecteur de la végétation et les "
         "conséquences en aval (barrage).",
         "La végétation : feuillage amortit les pluies, racines retiennent le sol, "
         "litière freine le ruissellement.\nSans elle : ruissellement violent → "
         "arrachage du sol → transport massif.\nEn aval : les sédiments s'accumulent "
         "dans le barrage (envasement) → perte de capacité de stockage d'eau.",
         "Cas marocain type : envasement des barrages = conséquence directe de "
         "l'érosion accélérée.",
         V()),
    ]),

    (2, "La sédimentation et les roches sédimentaires", "Dépôt, stratification, "
     "diagenèse, milieux de sédimentation, fossiles.", CH_SEDIMENTATION, [
        (1, "Manuel", "Associer sédiment et roche : galets ; sable ; argile ; "
         "coquilles broyées.",
         "Galets → conglomérat (poudingue)\nSable → grès\nArgile → argilite (marnes "
         "si mélangée à la calcite)\nCoquilles → calcaire organogène",
         "Grain ≠ roche : la diagenèse consolide le sédiment en roche.",
         V()),
        (2, "Contrôle", "Dans une falaise : 3 couches horizontales. La couche 1 (en "
         "bas) contient des fossiles marins ; la couche 3 (en haut) des fossiles "
         "terrestres. Reconstituer l'histoire du lieu.",
         "Superposition : couche 1 la plus ancienne, 3 la plus récente.\n"
         "Couche 1 marine → la mer occupait le lieu ; puis sédimentation marine ;\n"
         "puis le milieu est devenu continental (régression de la mer) → couche 3.\n"
         "Histoire : mer → retrait de la mer → terre.",
         "Fossiles = reconstitution du MILIEU ; superposition = chronologie.",
         V()),
        (2, "Manuel", "Des grains de sable sont anguleux ; d'autres arrondis. Quel "
         "critère cela renseigne-t-il ? Quelle roche pour chaque cas après "
         "consolidation ?",
         "Arrondis → transport long (usure mutuelle) ; anguleux → transport court.\n"
         "Les deux → GRÈS après compactation + cimentation (silice ou calcite).",
         "La forme des grains = distance de transport.",
         V()),
        (3, "Type Examen Régional", "Définir la diagenèse en citant ses 2 mécanismes "
         "principaux, puis expliquer pourquoi les strates sont toujours déposées "
         "horizontalement.",
         "Diagenèse = ensemble des transformations d'un sédiment meuble en roche "
         "cohérente : ① compactation (tassement, expulsion de l'eau) ② cimentation "
         "(précipitation de calcite/silice entre les grains).\n"
         "Les strates se déposent horizontalement car la gravité fait déposer les "
         "particules à plat au fond du milieu (principe d'horizontalité).",
         "Définition + mécanismes + principe : le trio gagnant de l'examen.",
         V()),
    ]),

    (2, "La formation des sols", "Profil d'un sol, humus, rôle des êtres vivants, "
     "érosion des sols et désertification.", CH_SOL, [
        (1, "Manuel", "Décrire les horizons d'un sol de haut en bas et indiquer la "
         "composition de chacun.",
         "A : litière + humus (matière organique décomposée, sombre)\n"
         "B : horizon minéral fin (argiles, sables, souvent rougeâtre au Maroc)\n"
         "C : roche-mère altérée et fragmentée\n"
         "Roche saine : roche-mère non altérée",
         "A organique → B minéral → C altéré → roche saine.",
         V()),
        (2, "Contrôle", "Citer le rôle de 3 êtres vivants dans la formation d'un sol.",
         "Lichens pionniers : attaquent la roche (acides), préparent le premier sol\n"
         "Végétaux : apportent la litière, racines qui fragmentent et retiennent\n"
         "Décomposeurs (bactéries, champignons, vers de terre) : transforment la "
         "litière en humus",
         "Sans êtres vivants : pas de sol, seulement des débris minéraux.",
         V()),
        (3, "Type Examen Régional", "Au Maroc, le surpâturage et la déforestation "
         "provoquent la désertification. Expliquer le mécanisme et proposer 2 "
         "mesures de protection des sols.",
         "Surpâturage/déforestation → sol nu → ruissellement intense → l'horizon A "
         "(fertile) est emporté → sol pauvre → végétation ne repousse → désertification.\n"
         "Mesures : reboisement (fixation par les racines), rotation des pâturages / "
         "mise en défens, cultures en courbes de niveau, terrasses.",
         "Le sol perdu = 100-400 ans pour 1 cm : ressource quasi non renouvelable.",
         V()),
    ]),
]


def sync(db):
    """Enrichit les chapitres SVT existants (retraduit le 3ᵉ en « origine de la
    biodiversité ») + ajoute les chapitres géologie + exercices (non destructif)."""
    import json as _json

    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    sid = subjects["SVT"]
    n_up = n_ch = n_ex = 0

    def add_exos(cid, exos):
        nonlocal n_ex
        for diff, source, enonce, solution, astuce, variantes in exos:
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
                      "AND titre = ?", (sid, titre), one=True)
        if ch:
            new_titre = up.get("titre", titre)
            db.execute("UPDATE chapters SET titre = ?, lecon = ?, semestre = ? WHERE id = ?",
                       (new_titre, _json.dumps(up["lecon"], ensure_ascii=False),
                        up["semestre"], ch["id"]))
            add_exos(ch["id"], up["exos"])
            n_up += 1

    for semestre, titre, resume, lecon, exos in NEW_CHAPTERS:
        exists = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                          "AND titre = ?", (sid, titre), one=True)
        if not exists:
            cid = db.execute(
                "INSERT INTO chapters(subject_id, niveau, semestre, titre, resume, lecon) "
                "VALUES (?,?,?,?,?,?)",
                (sid, "TC", semestre, titre, resume,
                 _json.dumps(lecon, ensure_ascii=False)))
            n_ch += 1
        else:
            cid = exists["id"]
            db.execute("UPDATE chapters SET lecon = ?, semestre = ? WHERE id = ?",
                       (_json.dumps(lecon, ensure_ascii=False), semestre, cid))
        add_exos(cid, exos)

    print(f"[sync TC SVT] {n_up} leçons enrichies, +{n_ch} chapitres, +{n_ex} exercices")
