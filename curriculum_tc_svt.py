# -*- coding: utf-8 -*-
"""
curriculum_tc_svt.py — Programme OFFICIEL de SVT du Tronc Commun Sciences
(Ministère de l'Éducation Nationale — programme marocain).

S1 — ÉCOLOGIE :
  1. Les techniques adaptatives à l'étude écologique sur le terrain
  2. Les facteurs édaphiques et leurs relations avec les êtres vivants
  3. Les facteurs climatiques et leurs relations avec les êtres vivants
  4. Flux de la matière et de l'énergie dans l'écosystème
  5. Les équilibres naturels
S2 — BOTANIQUE :
  6. La reproduction sexuée chez les plantes à fleurs
  7. La reproduction sexuée chez les plantes sans fleurs
  8. Les cycles de développement des plantes
  9. La reproduction asexuée chez les plantes
  10. La modification génétique des plantes
  11. La classification des plantes

Les anciens chapitres hors programme sont SUPPRIMÉS par sync().
"""
import json as _json


def V(**kw):
    return kw


# ════════════════════════════════════════════════════ S1 · ÉCOLOGIE ══
CH = []

CH.append({
 "semestre": 1,
 "titre": "Les techniques adaptatives à l'étude écologique sur le terrain",
 "resume": "Méthodes d'étude d'un écosystème : quadrats, abondance-dominance, densité, "
           "fréquence et préservation des espèces.",
 "lecon": {
  "intro": "L'écologie étudie les êtres vivants dans leur MILIEU. Pour étudier une station "
           "(surface homogène, même climat, même relief), on utilise des techniques "
           "d'échantillonnage et des échelles d'abondance.",
  "methodes": [
   {"nom": "Méthode 1 — échantillonner avec des quadrats",
    "texte": "Un QUADRAT (ou carroyage) = cadre métallique divisé en carrés (souvent 1 m² "
             "ou 0,5 m²), posé au hasard dans la station. On compte les individus de chaque "
             "espèce dans plusieurs quadrats, puis on calcule la MOYENNE, extrapolée à la "
             "surface totale de la station."},
   {"nom": "Méthode 2 — mesurer densité et fréquence",
    "texte": "DENSITÉ = nombre moyen d'individus par quadrat (ou par m²). "
             "FRÉQUENCE = (nombre de quadrats contenant l'espèce ÷ nombre total de "
             "quadrats) × 100 %. On peut aussi calculer le taux de RECOUVREMENT "
             "(% de surface occupée par une espèce)."},
   {"nom": "Méthode 3 — utiliser l'échelle d'abondance-dominance",
    "texte": "Échelle de Braun-Blanquet : + = espèce rare (1 individu) ; 1 = quelques "
             "individus ; 2 = abondante ; 3 = très abondante, recouvrement 25-50 % ; "
             "4 = 50-75 % ; 5 = recouvrement > 75 % (dominante). Elle permet de comparer "
             "les espèces d'une station sans tout compter."},
  ],
  "exemples": [
   {"question": "Dans 4 quadrats de 1 m², on compte 6, 8, 4 et 6 plants de thym. Densité "
                "moyenne et estimation pour 100 m² ?",
    "etapes": ["Densité moyenne = (6 + 8 + 4 + 6) ÷ 4 = 6 plants/m²",
               "Estimation = 6 × 100 = 600 plants"],
    "reponse": "6 plants par m², soit environ 600 plants sur 100 m²."},
  ],
  "pieges": [
   "Les quadrats doivent être posés au HASARD, dans une station HOMOGÈNE.",
   "Fréquence = % de quadrats CONTENANT l'espèce — pas le nombre d'individus.",
  ],
 },
 "exos": [
  (1, "Manuel", "Citer les étapes de l'étude écologique d'une station sur le terrain.",
   "① Délimitation de la station (surface homogène) ② Pose de quadrats au hasard "
   "③ Dénombrement des espèces par quadrat ④ Calcul de la densité moyenne et de la "
   "fréquence ⑤ Utilisation de l'échelle d'abondance-dominance.",
   "Quadrat = cadre gradué posé au hasard.",
   V(enonce="Que mesure l'échelle d'abondance-dominance de Braun-Blanquet ?",
     solution="La richesse d'une espèce dans la station : de « + » (rare) à « 5 » "
              "(recouvrement > 75 %, espèce dominante).")),
  (2, "Contrôle", "Dans 5 quadrats, on relève : muguet dans 2 quadrats, romarin dans 4. "
   "Fréquence de chaque espèce ?",
   "Fréquence = (nb de quadrats contenant l'espèce ÷ total) × 100\n"
   "Muguet : (2 ÷ 5) × 100 = 40 % ; Romarin : (4 ÷ 5) × 100 = 80 %",
   "Le dénominateur est TOUJOURS le nombre total de quadrats.",
   V(enonce="Le romarin a une fréquence de 60 % avec 3 quadrats. Combien de quadrats "
     "ont été posés ?",
     solution="3 ÷ 0,60 = 5 quadrats.")),
  (3, "Type Examen Régional", "Une station de 200 m² contient en moyenne 3 plants de "
   "lavande par m². ① Estimer le nombre total de plants. ② La lavande a une note "
   "d'abondance-dominance 2 : interpréter. ③ Citer 2 précautions pour que l'étude soit fiable.",
   "① 3 × 200 = 600 plants.\n② Note 2 : espèce ABONDANTE, recouvrement faible à moyen "
   "(elle est bien représentée mais ne domine pas).\n③ Quadrats posés au hasard ; "
   "suffisamment de quadrats ; station homogène (même relief, même exposition).",
   "Estimation = densité moyenne × surface totale."),
 ],
})

CH.append({
 "semestre": 1,
 "titre": "Les facteurs édaphiques et leurs relations avec les êtres vivants",
 "resume": "Le sol : composition, granulométrie, rétention d'eau — et son rôle dans la "
           "répartition des êtres vivants.",
 "lecon": {
  "intro": "Le SOL est la couche superficielle de la croûte terrestre où vivent les êtres "
           "vivants : c'est un facteur ÉDAPHIQUE (= lié au sol). Sa texture et sa "
           "composition contrôlent la vie qu'il abrite.",
  "methodes": [
   {"nom": "Méthode 1 — décrire la composition d'un sol",
    "texte": "Un sol contient : ① des PARTICULES MINÉRALES (issues de la roche mère : "
             "sable, limon, argile), ② de la MATIÈRE ORGANIQUE (restes d'êtres vivants, "
             "humus), ③ de l'EAU et des GAZ (dans les pores), ④ des ÊTRES VIVANTS "
             "(lombrics, insectes, bactéries, champignons)."},
   {"nom": "Méthode 2 — classer les particules par granulométrie",
    "texte": "Sable : Ø > 50 µm (grosses particules, sol perméable mais retient mal l'eau) ; "
             "Limon : 2 à 50 µm ; Argile : Ø < 2 µm (très petites, sol qui retient l'eau "
             "mais s'assèche en craquelant). Un sol équilibré (limon argilo-sableux) est "
             "le plus fertile : c'est un bon sol agricole."},
   {"nom": "Méthode 3 — relier sol et êtres vivants",
    "texte": "Le sol nourrit et abrite les êtres vivants (racines, lombrics qui aèrent et "
             "enrichissent, décomposeurs qui produisent l'humus). En retour, les êtres "
             "vivants FONT évoluer le sol : la roche mère se transforme progressivement "
             "en sol grâce à eux (érosion + humus)."},
  ],
  "exemples": [
   {"question": "Un sol contient 30 % de sable, 50 % de limon, 20 % d'argile. Est-il "
                "plutôt sableux, limoneux ou argileux ?",
    "etapes": ["Comparer les pourcentages : le limon domine (50 %)",
               "Texture dominante → type de sol"],
    "reponse": "Sol LIMONEUX : fertile et facile à travailler, mais sensible à l'érosion."},
  ],
  "pieges": [
   "Plus les particules sont GROSSES (sable), plus l'eau s'infiltre vite : sol sec.",
   "L'humus est de la matière organique DÉCOMPOSÉE — pas de simples débris frais.",
  ],
 },
 "exos": [
  (1, "Manuel", "Citer les 4 constituants d'un sol.",
   "① Particules minérales (sable, limon, argile) ② Matière organique (humus) "
   "③ Eau et gaz (air) ④ Êtres vivants (lombrics, insectes, micro-organismes).",
   "Minéral + organique + liquide + gazeux + vivant.",
   V(enonce="Quel constituant du sol provient de la décomposition des restes d'êtres "
     "vivants ?", solution="L'humus (matière organique décomposée).")),
  (2, "Contrôle", "Classer du plus gros au plus petit : argile, sable, limon.",
   "Sable (Ø > 50 µm) > Limon (2 à 50 µm) > Argile (Ø < 2 µm).",
   "Ordre alphabétique inversé de la taille : S-L-A = du grand au petit.",
   V(enonce="Quel sol retient le mieux l'eau : sableux ou argileux ? Pourquoi ?",
     solution="Le sol ARGILEUX : ses particules très fines (Ø < 2 µm) laissent peu "
              "d'espace entre elles, l'eau s'écoule mal et reste retenue.")),
  (3, "Type Examen Régional", "Un sol agricole contient 20 % de sable, 40 % de limon et "
   "40 % d'argile. ① Qualifier sa texture. ② Expliquer pourquoi les lombrics améliorent "
   "ce sol. ③ Un sol sableux convient-il à la culture du riz (plante aquatique) ? Justifier.",
   "① Sol limono-argileux (pas de texture dominante nette entre limon et argile).\n"
   "② Les lombrics CREUSENT des galeries (aération, infiltration de l'eau) et "
   "ENRICHISSENT le sol en humus (leurs déjections) : sol plus fertile.\n"
   "③ NON : un sol sableux est très PERMÉABLE, l'eau s'infiltre immédiatement — "
   "il ne retient pas l'eau dont le riz a besoin.",
   "Lombrics = « ingénieurs du sol » : aération + humus."),
 ],
})

CH.append({
 "semestre": 1,
 "titre": "Les facteurs climatiques et leurs relations avec les êtres vivants",
 "resume": "Lumière, température, eau, vent, humidité : leurs mesures et leur rôle dans la "
           "répartition des végétaux et des animaux.",
 "lecon": {
  "intro": "Les FACTEURS CLIMATIQUES sont les éléments du climat qui agissent sur les êtres "
           "vivants : température, lumière, précipitations, humidité, vent. On les mesure "
           "dans les stations météorologiques.",
  "methodes": [
   {"nom": "Méthode 1 — connaître les facteurs et leurs instruments",
    "texte": "TEMPÉRATURE → thermomètre (en °C) ; PRÉCIPITATIONS → pluviomètre (en mm "
             "d'eau) ; HUMIDITÉ DE L'AIR → hygromètre (% ) ; LUMIÈRE → photomètre "
             "(en lux) ; VENT → anémomètre (en km/h)."},
   {"nom": "Méthode 2 — exploiter les données climatiques",
    "texte": "AMITUDE THERMIQUE = température maximale − température minimale (sur un "
             "mois ou une année). Le diagramme OMBROTHERMIQUE (température + précipitations "
             "par mois) permet de repérer les saisons sèches (courbe des pluies sous celle "
             "des températures) et humides."},
   {"nom": "Méthode 3 — expliquer la répartition des êtres vivants",
    "texte": "Chaque espèce a des EXIGENCES climatiques : le chêne-liège et l'olivier "
             "supportent la sécheresse (feuilles dures, petites) ; le cèdre exige de la "
             "frais-eur en montagne. Les ADAPTATIONS (feuilles en aiguilles, réduction des "
             "feuilles, racines profondes) traduisent ces exigences."},
  ],
  "exemples": [
   {"question": "Températures de juillet : minimale 18 °C, maximale 35 °C. Amplitude "
                "thermique ?",
    "etapes": ["Amplitude = maximale − minimale", "35 − 18 = 17"],
    "reponse": "17 °C : climat à fortes différences jour/nuit (climat continental ou "
               "montagnard)."},
  ],
  "pieges": [
   "Amplitude thermique = max − min (toujours un nombre POSITIF).",
   "Le vent n'apporte pas d'eau : il augmente l'ÉVAPORATION et dessèche.",
  ],
 },
 "exos": [
  (1, "Manuel", "Associer chaque instrument à ce qu'il mesure : pluviomètre, thermomètre, "
   "anémomètre, hygromètre.",
   "Pluviomètre → précipitations (mm d'eau) ; Thermomètre → température (°C) ; "
   "Anémomètre → vitesse du vent (km/h) ; Hygromètre → humidité de l'air (%).",
   "Pluvi-o = pluie ; aném-o = vent ; hygr-o = humidité.",
   V(enonce="Quel facteur climatique mesure-t-on en millimètres ?",
     solution="Les précipitations (hauteur d'eau recueillie par le pluviomètre).")),
  (2, "Contrôle", "Températures mensuelles d'une station : max 30 °C, min 10 °C ; "
   "précipitations totales : 12 mm. ① Calculer l'amplitude thermique. ② Le mois est-il "
   "sec ou humide ?",
   "① Amplitude = 30 − 10 = 20 °C.\n② 12 mm de pluie en un mois est faible (< 30 mm) → "
   "mois SEC.",
   "Un mois est « sec » si ses précipitations sont très inférieures à 2 × la température "
   "moyenne (diagramme ombrothermique).",
   V(enonce="Pourquoi les feuilles du pins sont-elles en aiguilles ?",
     solution="Adaptation à la sécheresse et au froid : surface réduite → moins "
              "d'évaporation, et neige qui glisse sans casser les branches.")),
  (3, "Type Examen Régional", "Deux stations A et B : A = 400 mm de pluie/an, 18 °C de "
   "moyenne ; B = 900 mm/an, 12 °C. ① Quelle station abrite une forêt, laquelle une "
   "steppe ? ② Expliquer pourquoi l'olivier pousse en A et pas le chêne-zéen. ③ Citer "
   "2 adaptations des végétaux au climat de A.",
   "① A (peu de pluie, chaleur) → STEPPE ou maquis ; B (beaucoup de pluie, fraîcheur) → "
   "FORÊT.\n② L'olivier est XÉROPHYLE (adapté à la sécheresse : feuilles étroites et "
   "coriaces) ; le chêne-zéen exige de l'humidité.\n③ Feuilles réduites ou transformées "
   "(aiguilles, épines) ; racines profondes ; cuticule épaisse.",
   "Relier toujours quantité d'eau ↔ type de végétation."),
 ],
})

CH.append({
 "semestre": 1,
 "titre": "Flux de la matière et de l'énergie dans l'écosystème",
 "resume": "Chaînes et réseaux trophiques, producteurs-consommateurs-décomposeurs, "
           "pyramides écologiques et dynamique de l'écosystème.",
 "lecon": {
  "intro": "Dans un écosystème, la MATIÈRE et l'ÉNERGIE circulent : l'énergie du Soleil "
           "est captée par les plantes, puis transmise le long des CHAÎNES ALIMENTAIRES "
           "(trophiques).",
  "methodes": [
   {"nom": "Méthode 1 — construire une chaîne trophique",
    "texte": "Une chaîne commence TOUJOURS par un PRODUCTEUR (végétal vert), suivi de "
             "consommateurs : C1 (herbivore) → C2 (carnivore) → C3... Chaque flèche se lit "
             "« est mangé par » et représente le sens du passage de la matière et de "
             "l'énergie. Les DÉCOMPOSEURS (bactéries, champignons) renvoient les éléments "
             "minéraux au sol."},
   {"nom": "Méthode 2 — utiliser la pyramide écologique",
    "texte": "Les PYRAMIDES (nombres, biomasse ou énergie) montrent qu'en remontant les "
             "niveaux, les effectifs/la biomasse DIMINUENT : il faut beaucoup de plantes "
             "pour nourrir peu d'herbivores, qui nourrissent encore moins de carnivores. "
             "Seule une fraction (~10 %) de l'énergie passe d'un niveau au suivant."},
   {"nom": "Méthode 3 — comprendre la dynamique de l'écosystème",
    "texte": "Un écosystème ÉVOLUE : après une perturbation (feu, culture abandonnée), des "
             "espèces pionnières s'installent, puis d'autres les remplacent jusqu'à un état "
             "d'équilibre (climax). Tout déséquilibre d'un maillon se répercute sur toute "
             "la chaîne."},
  ],
  "exemples": [
   {"question": "Construire la chaîne trophique : faucon, herbe, sauterelle, lézard.",
    "etapes": ["Identifier le producteur : l'herbe",
               "Puis l'herbivore (C1) : la sauterelle ; le carnivore (C2) : le lézard ; "
               "le super-prédateur (C3) : le faucon"],
    "reponse": "Herbe → sauterelle → lézard → faucon."},
  ],
  "pieges": [
   "Une chaîne ne commence JAMAIS par un animal — toujours un producteur vert.",
   "Les décomposeurs n'appartiennent pas aux maillons de la chaîne : ils agissent sur "
   "TOUS les niveaux morts et recyclent la matière.",
  ],
 },
 "exos": [
  (1, "Manuel", "Définir : producteur, consommateur de 1er ordre, décomposeur.",
   "Producteur : organisme chlorophyllien qui fabrique sa matière organique (photosynthèse).\n"
   "Consommateur C1 : herbivore qui se nourrit des producteurs.\n"
   "Décomposeur : micro-organisme qui décompose les cadavres/débris et rend les éléments "
   "minéraux au sol.",
   "Vert = producteur ; mangeur de vert = C1 ; recycleur = décomposeur.",
   V(enonce="Donner un exemple de décomposeur.",
     solution="Les bactéries et les champignons du sol (ex : champignon de la litière).")),
  (2, "Contrôle", "Construire la chaîne à partir de : sanglier, glands, lynx. Préciser le "
   "rôle de chaque maillon.",
   "Glands → sanglier → lynx\nGlands : producteur (fruit du chêne) ; sanglier : "
   "consommateur C1 (herbivore) ; lynx : consommateur C2 (carnivore).",
   "Chercher d'abord le végétal, puis suivre « qui mange qui ».",
   V(enonce="Dans cette chaîne, qui perd le plus d'énergie entre deux niveaux ?",
     solution="À chaque niveau, ~90 % de l'énergie est perdue (respiration, déchets) : "
              "le passage glands → sanglier n'en transmet qu'environ 10 %.")),
  (3, "Type Examen Régional", "Une prairie de 1000 kg de biomasse végétale nourrit des "
   "sauterelles. ① Calculer la biomasse maximale de sauterelles (rendement 10 %) puis "
   "celle des lézards qui les mangent. ② Expliquer pourquoi il y a rarement plus de 4-5 "
   "maillons dans une chaîne. ③ Une chaîne est un schéma simplifié : pourquoi parle-t-on "
   "de RÉSEAU trophique dans la nature ?",
   "① Sauterelles : 1000 × 10/100 = 100 kg ; lézards : 100 × 10/100 = 10 kg.\n"
   "② L'énergie diminue fortement à chaque maillon (~10 % transmis) : trop de maillons = "
   "plus assez d'énergie pour le dernier.\n③ Un consommateur mange plusieurs proies et est "
   "chassé par plusieurs prédateurs : les chaînes s'entrecroisent → RÉSEAU trophique.",
   "Chaque maillon ×0,1 : multiplier successivement."),
 ],
})

CH.append({
 "semestre": 1,
 "titre": "Les équilibres naturels",
 "resume": "Équilibre écologique, causes naturelles et humaines de déséquilibre, pollution "
           "et moyens de préservation (parcs nationaux du Maroc).",
 "lecon": {
  "intro": "Un ÉCOSYSTÈME est en ÉQUILIBRE quand ses populations restent stables : "
           "naissances ≈ morts, proies ≈ prédateurs. Des perturbations naturelles ou "
           "humaines peuvent rompre cet équilibre.",
  "methodes": [
   {"nom": "Méthode 1 — distinguer déséquilibres naturels et humains",
    "texte": "Naturels : sécheresse prolongée, inondations, incendies naturels, éruptions. "
             "HUMAINS (les plus graves par leur fréquence) : déforestation, surpâturage, "
             "culture sur brûlis, urbanisation, braconnage, pollution."},
   {"nom": "Méthode 2 — analyser une pollution",
    "texte": "POLLUTION = introduction dans le milieu d'éléments qui le rendent malsain. "
             "Types : eau (rejets industriels, détergents), air (fumées, CO₂), sol "
             "(pesticides, déchets). Conséquences : mortalité d'espèces, eutrophisation "
             "(prolifération d'algues par excès d'engrais), chaînes trophiques perturbées."},
   {"nom": "Méthode 3 — les moyens de préservation",
    "texte": "① Aires protégées : PARCS NATIONAUX du Maroc (Toubkal, Souss-Massa, Ifrane, "
             "Al Hoceima...), réserves biologiques. ② Reboisement et lutte contre "
             "l'érosion. ③ Protection d'espèces menacées (ibis chauve, gazelle dorcas, "
             "singe magot). ④ Épuration des eaux, énergies propres, sensibilisation."},
  ],
  "exemples": [
   {"question": "Le surpâturage d'un parcours : conséquences en chaîne ?",
    "etapes": ["Trop de troupeaux → la végétation ne se régénère pas",
               "Sol nu → érosion → désertification"],
    "reponse": "Dégradation du couvert végétal puis du sol : désertification — "
               "l'équilibre est rompu."},
  ],
  "pieges": [
   "Un équilibre naturel est DYNAMIQUE : les populations fluctuent mais restent stables "
   "en moyenne.",
   "La protection ne concerne pas que les animaux : les HABITATS aussi (réserves, parcs).",
  ],
 },
 "exos": [
  (1, "Manuel", "Citer 2 causes naturelles et 2 causes humaines de déséquilibre d'un "
   "écosystème.",
   "Naturelles : sécheresse prolongée, incendie naturel (aussi : inondation, éruption).\n"
   "Humaines : déforestation, surpâturage (aussi : pollution, braconnage, urbanisation).",
   "Naturel = sans intervention de l'homme.",
   V(enonce="Citer un parc national marocain et une espèce qu'il protège.",
     solution="Parc national de Souss-Massa → ibis chauve (aussi : Toubkal → magot, "
              "Ifrane → cèdre et macaque).")),
  (2, "Contrôle", "Une forêt de 5000 ha perd 15 % de sa surface par an à cause des "
   "coupes. ① Calculer la surface détruite en un an. ② Citer 2 conséquences pour la "
   "faune. ③ Proposer 2 mesures de protection.",
   "① 5000 × 15/100 = 750 ha détruits par an.\n② Perte d'habitat → migration ou "
   "disparition des espèces ; rupture des chaînes trophiques.\n③ Reboisement ; "
   "classement en aire protégée ; surveillance (gardes) ; sensibilisation.",
   "% d'une valeur = valeur × %/100.",
   V(enonce="Pourquoi l'eutrophisation d'un lac tue-t-elle les poissons ?",
     solution="Excès d'engrais → prolifération d'algues en surface → moins de lumière "
              "et d'oxygène dissous → mortalité des êtres aquatiques.")),
  (3, "Type Examen Régional", "Dans une région, l'analyse montre : baisse de la nappe "
   "phréatique, disparition du gazelle dorcas, sol dégradé. ① Proposer une cause unique "
   "expliquant ces 3 constats. ② Schématiser la chaîne des conséquences. ③ Citer 2 "
   "actions pour restaurer l'équilibre.",
   "① Le SURPÂTURAGE (trop de troupeaux qui consomment et piétinent tout).\n"
   "② Surpâturage → disparition du couvert végétal → moins d'infiltration (baisse de la "
   "nappe) + sol nu érodé → disparition des animaux (gazelle) qui en dépendent.\n"
   "③ Limiter le nombre de têtes de bétail ; mise en défens (interdiction de pâturer) et "
   "reboisement ; création d'une réserve pour la gazelle.",
   "Un seul déséquilibre peut expliquer plusieurs constats : raisonner en chaîne."),
 ],
})

# ═══════════════════════════════════════════ S2 · BOTANIQUE ══
CH.append({
 "semestre": 2,
 "titre": "La reproduction sexuée chez les plantes à fleurs",
 "resume": "Fleur, gamètes, pollinisation, double fécondation, graine et fruit chez les "
           "angiospermes.",
 "lecon": {
  "intro": "Les plantes à FLEURS (angiospermes) se reproduisent sexuellement : rencontre "
           "d'un gamète mâle (cellule reproductrice) et d'un gamète femelle, qui donne une "
           "GRAINE contenant l'embryon.",
  "methodes": [
   {"nom": "Méthode 1 — décrire la fleur et ses gamètes",
    "texte": "La fleur porte : sépales (protection), pétales (attraction), ÉTAMINES "
             "(organe mâle : anthère qui produit le POLLEN = gamètes mâles) et CARPILLE "
             "(organe femelle : ovaire contenant les SACS EMBRYONNAIRES avec l'oosphère = "
             "gamète femelle)."},
   {"nom": "Méthode 2 — expliquer pollinisation puis fécondation",
    "texte": "POLLINISATION = transport du pollen de l'étamine vers le stigmate "
             "(réceptacle du carpille) : par le VENT (anémogame : pollen léger et abondant) "
             "ou par les INSECTES (entomogame : pollen collant, fleurs colorées et "
             "parfumées). Puis FÉCONDATION : le grain de pollen germe, un tube pollinique "
             "descend vers l'ovaire ; 2 gamètes mâles fécondent l'oosphère (→ embryon, 2n) "
             "et la cellule centrale (→ albumen, réserve) : DOUBLE fécondation."},
   {"nom": "Méthode 3 — relier fleur, graine et fruit",
    "texte": "Après fécondation : l'OVULE devient GRAINE (embryon + réserves + téguments), "
             "l'OVAIRE devient FRUIT (protège et diffuse les graines). Les graines sont "
             "dispersées par le vent, l'eau, les animaux, puis GERMENT si conditions "
             "favorables (eau, air, température)."},
  ],
  "exemples": [
   {"question": "Une fleur de pois contient 5 ovules. Combien de graines et combien de "
                "fécondations de l'oosphère pour les remplir toutes ?",
    "etapes": ["1 ovule → 1 graine (si fécondé)", "5 ovules → 5 graines",
               "1 fécondation de l'oosphère par ovule"],
    "reponse": "5 graines au maximum, donc 5 fécondations de l'oosphère "
               "(+5 de la cellule centrale : fécondation double)."},
  ],
  "pieges": [
   "Pollinisation ≠ fécondation : la pollinisation TRANSPORTE le pollen, la fécondation "
   "UNIT les gamètes.",
   "Le fruit provient de l'ovaire, la graine de l'ovule — ne pas confondre.",
  ],
 },
 "exos": [
  (1, "Manuel", "Nommer les pièces florales et donner le rôle de chacune.",
   "Sépales → protègent le bouton floral ; Pétales → attirent les insectes (couleurs, "
   "parfum) ; Étamines → produisent le pollen (gamètes mâles) ; Carpille → contient les "
   "ovules (gamètes femelles).",
   "S-P-É-C de l'extérieur vers l'intérieur.",
   V(enonce="Où sont produits les gamètes mâles des plantes à fleurs ?",
     solution="Dans les anthères des étamines (grains de pollen).")),
  (2, "Contrôle", "Comparer un pollen de pin (transporté par le vent) et un pollen de "
   "rose (transporté par l'abeille).",
   "Pin (anémogame) : pollen très léger, abondant, sec — dispersé au hasard par le vent.\n"
   "Rose (entomogame) : pollen peu abondant mais COLLANT et rugueux, fleur grande, "
   "colorée et parfumée, nectar : cible l'insecte.",
   "Forme du pollen ↔ agent pollinisateur.",
   V(enonce="Que devient l'ovaire après la fécondation ?",
     solution="Il grossit et devient le FRUIT (la paroi de l'ovaire = paroi du fruit).")),
  (3, "Type Examen Régional", "Une variété de blé autogame (s'autopollinise) et une "
   "variété de pommier allogame (pollinisation croisée par les abeilles). ① Expliquer le "
   "terme « double fécondation » chez le pommier. ② Pourquoi l'absence d'abeilles "
   "réduirait-elle fortement la récolte de pommes ? ③ Que devient chaque partie : ovule, "
   "ovaire, zygote (œuf) ?",
   "① 2 gamètes mâles du grain de pollen : l'un féconde l'oosphère (→ embryon 2n), "
   "l'autre féconde la cellule centrale (→ albumen, tissu de réserve 3n).\n"
   "② Sans abeilles : pas de transport du pollen → pas de fécondation → pas de graines ni "
   "de fruits (la pomme ne se développe pas).\n"
   "Ovule → graine ; ovaire → fruit (pomme) ; zygote → embryon de la nouvelle plante.",
   "Fleur → fruit : tout se transforme selon des règles précises."),
 ],
})

CH.append({
 "semestre": 2,
 "titre": "La reproduction sexuée chez les plantes sans fleurs",
 "resume": "Reproduction sexuée des algues, mousses et fougères : gamètes, spores et "
           "organes reproducteurs.",
 "lecon": {
  "intro": "Les plantes SANS FLEURS (algues, mousses, fougères) se reproduisent aussi "
           "sexuellement, mais avec des gamètes nus et des SPORES au lieu de graines et "
           "de fleurs.",
  "methodes": [
   {"nom": "Méthode 1 — algues : gamètes et milieu aquatique",
    "texte": "Chez certaines algues (ex : Spirogyre, Ulva), les gamètes mâles et femelles "
             "sont identiques (ISOGAMÈTES) ou différents. La fécondation se fait dans "
             "l'EAU (milieu obligatoire : les gamètes nagent). Le zygote (œuf) donne une "
             "spore qui redevient une algue."},
   {"nom": "Méthode 2 — mousses : archégones et anéridies",
    "texte": "La mousse produit dans ses organes reproducteurs : ANÉRIDIES (mâles, "
             "produisant des spermatozoïdes biflagellés) et ARCHÉGONES (femels, contenant "
             "l'oosphère). L'eau de pluie permet aux spermatozoïdes de nager vers "
             "l'oosphère → fécondation → sporophyte qui produit des SPORES par méiose."},
   {"nom": "Méthode 3 — fougères : spores et prothalle",
    "texte": "La fougère visible = SPOROPHYTE ; ses sporanges (sous les feuilles) produisent "
             "des spores. Une spore germe en PROTHALLE (petite plante gamétophyte portant "
             "anéridies et archégones) : après fécondation dans l'eau, le jeune sporophyte "
             "pousse sur le prothalle."},
  ],
  "exemples": [
   {"question": "Pourquoi les mousses vivent-elles toujours en milieux humides ?",
    "etapes": ["Leurs spermatozoïdes sont flagellés", "Ils doivent NAGER jusqu'à "
               "l'oosphère"],
    "reponse": "La fécondation exige la présence d'eau : sans humidité, pas de "
               "reproduction sexuée possible."},
  ],
  "pieges": [
   "Les spores ne sont PAS des gamètes : elles germent sans fécondation.",
   "Le prothalle de fougère est INDEPÉNDANT et minuscule — la grande fougère est le "
   "sporophyte.",
  ],
 },
 "exos": [
  (1, "Manuel", "Citer 3 plantes sans fleurs et le milieu exigé par leur fécondation.",
   "Algues, mousses, fougères (aussi : prêles, conifères pour les graines nues).\n"
   "Leur fécondation sexuée exige un MILIEU HUMIDE ou l'eau (gamètes nageurs).",
   "Pas de fleur = gamètes nus + besoin d'eau.",
   V(enonce="Qu'est-ce qu'une spore ?",
     solution="Une cellule reproductive capable de germer SANS fécondation pour donner "
              "un nouvel organisme (ex : prothalle de fougère).")),
  (2, "Contrôle", "Ordonner le cycle de la fougère : prothalle, spores, jeune "
   "sporophyte, fécondation, grande fougère.",
   "Grande fougère (sporophyte) → spores → prothalle (gamétophyte) → fécondation dans "
   "l'eau → jeune sporophyte → grande fougère.",
   "Suivre l'alternance sporophyte (2n) / gamétophyte (n).",
   V(enonce="Où se trouvent les sporanges chez la fougère ?",
     solution="À la face inférieure des feuilles (petites amas bruns visibles).")),
  (3, "Type Examen Régional", "Un élève affirme : « la mousse et le conifère n'ont pas de "
   "fleurs, ils ont donc la même reproduction ». ① A-t-il raison ? ② Comparer la "
   "reproduction des deux. ③ Pourquoi les conifères sont-ils mieux adaptés à la vie "
   "terrestre que les mousses ?",
   "① NON, il se trompe.\n② Mousse : fécondation par gamètes nageurs nécessitant l'eau, "
   "dissém-ination par SPORES.\nConifère : PAS besoin d'eau (pollen transporté par le "
   "vent vers l'ovule), reproduction par GRAINES NUES dans des cônes.\n"
   "③ La graine protège l'embryon avec des réserves, le pollen dispense de l'eau libre : "
   "le conifère colonise les milieux secs.",
   "Sans fleur ≠ même mode de reproduction."),
 ],
})

CH.append({
 "semestre": 2,
 "titre": "Les cycles de développement des plantes",
 "resume": "Alternance des générations : phase sporophytique (2n) et gamétophytique (n), "
           "cycles dominants chez les plantes.",
 "lecon": {
  "intro": "Toutes les plantes alternent deux générations : le SPOROPHYTE (2n, produit des "
           "spores par méiose) et le GAMÉTOPHYTE (n, produit les gamètes). C'est le cycle "
           "haplodiploïque.",
  "methodes": [
   {"nom": "Méthode 1 — comprendre l'alternance des phases",
    "texte": "Sporophyte (2n) → méiose → spores (n) → gamétophyte (n) → gamètes (n) → "
             "FÉCONDATION → zygote (2n) → sporophyte (2n)... Le nombre de chromosomes "
             "alterne : 2n puis n puis 2n."},
   {"nom": "Méthode 2 — identifier la phase dominante",
    "texte": "Mousse : la plante verte visible = GAMÉTOPHYTE dominant (le sporophyte est "
             "petit, fixé sur lui). Fougère, conifères, plantes à fleurs : le SPOROPHYTE "
             "domine (le gamétophyte est réduit : prothalle, ou minuscule dans la fleur). "
             "Plus la plante est évoluée, plus le sporophyte domine."},
   {"nom": "Méthode 3 — lire un cycle de développement",
    "texte": "Repérer : ① qui produit des spores (sporophyte, méiose), ② qui produit les "
             "gamètes (gamétophyte, mitose), ③ où a lieu la fécondation. Flèches de "
             "réduction chromosomique = méiose ; flèches de fécondation = retour à 2n."},
  ],
  "exemples": [
   {"question": "Les cellules du prothalle de fougère comptent 20 chromosomes (n = 20). "
                "Combien chez les cellules de la grande fougère ?",
    "etapes": ["Prothalle = gamétophyte = n = 20",
               "Grande fougère = sporophyte = 2n"],
    "reponse": "2n = 40 chromosomes."},
  ],
  "pieges": [
   "La méiose se produit lors de la formation des SPORES — pas des gamètes, chez les "
   "plantes.",
   "La phase dominante est celle de la plante VISIBLE et durable.",
  ],
 },
 "exos": [
  (1, "Manuel", "Définir : sporophyte, gamétophyte, cycle haplodiploïque.",
   "Sporophyte : génération diploïde (2n) qui produit des spores par méiose.\n"
   "Gamétophyte : génération haploïde (n) qui produit les gamètes.\n"
   "Cycle haplodiploïque : alternance régulière de ces deux générations.",
   "Sporo = spores ; gaméto = gamètes.",
   V(enonce="Chez quelle plante la phase dominante est-elle le gamétophyte ?",
     solution="Chez les MOUSSES (la plante verte visible est haploïde n).")),
  (2, "Contrôle", "Une mousse : n = 12 chromosomes. Donner le nombre de chromosomes de "
   "ses cellules, de ses spores et de son zygote.",
   "Cellules de la mousse (gamétophyte) : n = 12 ; spores : n = 12 ; zygote : 2n = 24.",
   "Spores et gamètes = n ; zygote = 2n.",
   V(enonce="Par quel processus le zygote (2n) redonne-t-il un sporophyte (2n) ?",
     solution="Par MITOSES (divisions cellulaires conservant le nombre de chromosomes).")),
  (3, "Type Examen Régional", "On compare 4 plantes : mousse, fougère, pin, rosier. "
   "① Classer-les de la phase gamétophytique dominante à la phase sporophytique "
   "exclusivement dominante. ② Expliquer l'intérêt évolutif de la dominance du "
   "sporophyte. ③ Chez le rosier, où se cachent les gamétophytes ?",
   "① Mousse (gamétophyte dominant) → fougère (sporophyte dominant, gamétophyte libre : "
   "prothalle) → pin et rosier (sporophyte exclusivement dominant).\n"
   "② Le sporophyte (2n) est plus robuste (deux jeux de gènes), mieux protégé contre les "
   "variations du milieu : meilleure conquête de la terre ferme.\n"
   "③ Dans la FLEUR : le gamétophyte mâle = grain de pollen (dans l'an-thère), le "
   "gamétophyte femelle = sac embryonnaire (dans l'ovule).",
   "Plus évoluée = gamétophyte réduit et protégé."),
 ],
})

CH.append({
 "semestre": 2,
 "titre": "La reproduction asexuée chez les plantes",
 "resume": "Multiplication végétative naturelle et artificielle : bouture, marcottage, "
           "greffe, rhizomes, tubercules — et applications agricoles.",
 "lecon": {
  "intro": "La reproduction ASEXUÉE (végétative) ne fait intervenir NI gamètes NI "
           "fécondation : un fragment de plante donne une NOUVELLE plante identique au "
           "parent (clone).",
  "methodes": [
   {"nom": "Méthode 1 — connaître la multiplication naturelle",
    "texte": "Certaines organes permettent la multiplication : RHIZOMES (tiges "
             "souterraines horizontales : iris, bambou), TUBERCULES (pomme de terre : "
             "bourgeons = yeux), BULBES (oignon, tulipe), STOLONS (fraisier : tiges "
             "aériennes qui s'enracinent), BOUTURE naturelle."},
   {"nom": "Méthode 2 — maîtriser les techniques artificielles",
    "texte": "BOUTURE : couper un fragment (tige/feuille) et le mettre en terre → il "
             "s'enracine. MARCOTTAGE : enterrer une branche sans la couper, la séparer "
             "une fois enracinée. GREFFE : un fragment d'une plante (greffon) est fixé sur "
             "une autre (portegreffe) — permet de combiner les qualités (fruits du greffon "
             "+ racines robustes du porte-greffe)."},
   {"nom": "Méthode 3 — avantages et limites",
    "texte": "AVANTAGES : reproduction rapide, sans partenaire ; plante IDENTIQUE "
             "(clone) : on conserve les bonnes variétés (fruits savoureux). LIMITES : pas "
             "de diversité génétique → même sensibilité aux maladies ; épuisement du sol."},
  ],
  "exemples": [
   {"question": "Un agriculteur plante 5 tubercules de pomme de terre portant chacun 4 "
                "bourgeons viables. Combien de plants peut-il espérer ?",
    "etapes": ["Chaque bourgeon (yeux) donne un plant", "5 × 4 = 20"],
    "reponse": "Jusqu'à 20 plants, tous identiques à la plante mère."},
  ],
  "pieges": [
   "Plantes issues de reproduction asexuée = CLONES (même patrimoine génétique).",
   "La greffe réussit seulement entre espèces proches (ex : oranger sur oranger amer).",
  ],
 },
 "exos": [
  (1, "Manuel", "Citer 3 techniques artificielles de multiplication végétative.",
   "Bouture, marcottage, greffe (aussi : culture in vitro).",
   "Bouture = couper ; marcotte = enterrer sans couper ; greffe = assembler.",
   V(enonce="Citer 2 organes de multiplication naturelle.",
     solution="Rhizome (iris), tubercule (pomme de terre), bulbe (oignon), "
              "stolon (fraisier).")),
  (2, "Contrôle", "Un verger de 30 pommiers « Golden » : tous issus de greffes de la même "
   "variété. ① Que sont ces 30 pommiers l'un par rapport à l'autre ? ② Un avantage de ce "
   "choix ? ③ Un risque ?",
   "① Des CLONES (patrimoine génétique identique).\n"
   "② Tous donnent les mêmes fruits de qualité (calibre, goût) : variété conservée.\n"
   "③ Si une maladie les attaque, TOUS y sont sensibles (même fragilité génétique) : "
   "perte possible de tout le verger.",
   "Identique = pratique, mais fragile en masse.",
   V(enonce="Quel organe de la pomme de terre assure la multiplication ?",
     solution="Le tubercule, par ses bourgeons (les « yeux »).")),
  (3, "Type Examen Régional", "Un pépiniériste hésite : semer des graines d'oranger ou "
   "greffer. ① Quelle technique garde exactement les qualités d'une variété ? Justifier. "
   "② Quel intérêt de greffer sur un porte-greffe à racines vigoureuses ? ③ Citer un "
   "inconvénient commun aux deux greffes réussies.",
   "① La GREFFE (reproduction végétative) : le greffon a le même patrimoine génétique que "
   "l'arbre-mère → mêmes fruits. Les graines (reproduction sexuée) donnent des plantes "
   "DIFFÉRENTES (mélanges de gènes).\n"
   "② Le porte-greffe apporte des racines fortes : résistance à la sécheresse/maladies du "
   "sol, croissance vigoureuse, précocité.\n"
   "③ La diversité génétique est nulle → sensibilité commune aux maladies ; il faut des "
   "outils et un savoir-faire (réussite non garantie).",
   "Sexuée = diversité ; végétative = fidélité."),
 ],
})

CH.append({
 "semestre": 2,
 "titre": "La modification génétique des plantes",
 "resume": "Modification génétique naturelle (hybridation, mutations) et dirigée "
           "(transgenèse, OGM) : méthodes, applications et débat.",
 "lecon": {
  "intro": "Le patrimoine génétique des plantes peut être modifié : naturellement "
           "(hybridations, mutations spontanées) ou par l'homme (sélection, mutagenèse, "
           "TRANSGÉNÈSE).",
  "methodes": [
   {"nom": "Méthode 1 — la modification génétique naturelle",
    "texte": "HYBRIDATION naturelle : croisement entre variétés/espèces voisines (ex : "
             "pollen d'une variété fécondant une autre) → nouvelles combinaisons de gènes. "
             "MUTATIONS SPONTANÉES : changements accidentels de l'ADN, parfois favorables, "
             "transmis à la descendance. C'est ainsi que les blés anciens ont évolué."},
   {"nom": "Méthode 2 — comprendre la transgenèse",
    "texte": "TRANSGÉNÈSE = transférer un gène d'un organisme vers un autre : ① identifier "
             "et isoler le gène d'intérêt (ex : gène de résistance) ② l'introduire dans le "
             "génome de la plante (vecteur : bactérie Agrobacterium, « canon à gènes ») "
             "③ régénérer la plante modifiée et sélectionner celles qui expriment le gène. "
             "Résultat : une plante TRANSGÉNIQUE (OGM)."},
   {"nom": "Méthode 3 — applications et débat",
    "texte": "Applications : maïs résistant aux insectes (gène Bt), soja tolérant un "
             "herbicide, « riz doré » enrichi en provitamine A. AVANTAGES : rendements, "
             "moins de pesticides, valeur nutritionnelle. RISQUES discutés : dissémination "
             "des gènes (pollen), impact sur la biodiversité et la santé, brevets. "
             "D'où une RÉGLEMENTATION stricte (étiquetage, essais)."},
  ],
  "exemples": [
   {"question": "Ordre des étapes de la transgenèse d'un maïs résistant aux insectes ?",
    "etapes": ["Isoler le gène Bt de la bactérie", "Transférer le gène dans les cellules "
               "de maïs (Agrobacterium)", "Régénérer les plantes et vérifier l'expression "
               "du gène", "Sélectionner et multiplier"],
    "reponse": "Isolation → transfert → régénération → sélection."},
  ],
  "pieges": [
   "Un OGM n'est pas forcément dangereux ni miraculeux : chaque cas est évalué.",
   "Hybridation naturelle = croisement entre êtres vivants proches ; transgenèse = "
   "transfert possible entre espèces très éloignées.",
  ],
 },
 "exos": [
  (1, "Manuel", "Définir : transgenèse, OGM.",
   "Transgenèse : technique qui transfère un gène d'un organisme vers un autre (souvent "
   "d'espèces différentes).\nOGM : Organisme Génétiquement Modifié — dont le génome a été "
   "modifié par l'homme (transgenèse ou autre technique).",
   "Gène transféré → plante transgénique = un OGM.",
   V(enonce="Citer un vecteur utilisé pour transférer un gène dans une plante.",
     solution="La bactérie Agrobacterium tumefaciens (ou le canon à particules).")),
  (2, "Contrôle", "Un riz classique est croisé avec un riz sauvage résistant à la "
   "sécheresse. S'agit-il de transgenèse ? Justifier.",
   "NON : c'est une HYBRIDATION (croisement sexuel entre plantes voisines) — pas de "
   "transfert d'un gène d'une espèce très éloignée ni de manipulation en laboratoire du "
   "génome.",
   "Croisement naturel ≠ transfert de gène par ingénierie.",
   V(enonce="Citer 2 avantages et 2 risques discutés des plantes transgéniques.",
     solution="Avantages : meilleur rendement, moins d'insecticides, valeur "
              "nutritionnelle (riz doré).\nRisques : dissémination du gène par le pollen, "
              "impact sur la biodiversité, dépendance aux semenciers, santé "
              "(évaluée au cas par cas).")),
  (3, "Type Examen Régional", "Une région subit des invasions d'insectes qui détruisent "
   "le maïs ; l'agriculteur traite 8 fois par an avec un insecticide. ① Proposer une "
   "solution fondée sur la modification génétique. ② Décrire ses étapes. ③ Citer 2 "
   "précautions avant généralisation.",
   "① Cultiver un maïs transgénique produisant lui-même la protéine insecticide (gène Bt "
   "de la bactérie Bacillus thuringiensis).\n"
   "② Isoler le gène Bt → le transférer dans des cellules de maïs (Agrobacterium) → "
   "régénérer les plantes → sélectionner celles qui expriment le gène → multiplier.\n"
   "③ Évaluer l'impact sur les insectes utiles (abeilles) et la biodiversité ; éviter la "
   "dissémination du pollen (distances, essais confinés) ; étiquetage et suivi sanitaire.",
   "Solution technique + précautions : toujours les deux."),
 ],
})

CH.append({
 "semestre": 2,
 "titre": "La classification des plantes",
 "resume": "Critères de classification des végétaux et classification générale : algues, "
           "mousses, fougères, conifères, plantes à fleurs.",
 "lecon": {
  "intro": "CLASSIFIER = regrouper les êtres vivants selon des CRITÈRES précis. Pour les "
           "plantes, les critères principaux portent sur la présence de fleurs, de graines, "
           "de vaisseaux conducteurs et de chlorophylle.",
  "methodes": [
   {"nom": "Méthode 1 — utiliser les critères progressifs",
    "texte": "① Présence de chlorophylle → végétaux verts. ② Vaisseaux conducteurs "
             "(racines/tiges vraies) ? ③ Graines ? ④ Fleurs et fruits ? Chaque question "
             "sépare un groupe : c'est une clé de détermination (critère → groupe)."},
   {"nom": "Méthode 2 — la classification générale des végétaux",
    "texte": "PLANTES À FLEURS (angiospermes : fleurs, graines dans un fruit) ; PLANTES À "
             "GRAINES NUES (gymnospermes : conifères, cônes) ; FOUGÈRES (vaisseaux, pas de "
             "graines : spores) ; MOUSSES (pas de vraies racines ni vaisseaux, spores, "
             "milieu humide) ; ALGUES (pas d'organes vrais, souvent aquatiques)."},
   {"nom": "Méthode 3 — classer une plante inconnue",
    "texte": "Observer dans l'ordre : organes vrais ? → spores ou graines ? → graines "
             "nues ou dans un fruit ? Ex : plante avec cônes et feuilles en aiguilles = "
             "conifère (graines nues) ; plante à fleurs colorées avec fruits = "
             "angiosperme."},
  ],
  "exemples": [
   {"question": "Classer : fougère, rosier, pin, mousse.",
    "etapes": ["Fougère : vaisseaux + spores", "Rosier : fleurs + graines dans un fruit",
               "Pin : graines nues dans des cônes", "Mousse : sans vaisseaux, spores, "
               "petite"],
    "reponse": "Angiosperme (rosier) ; gymnosperme (pin) ; fougère ; mousse."},
  ],
  "pieges": [
   "Le pin A des graines (nues) mais pas de fleurs : gymnosperme.",
   "Les mousses n'ont pas de vraies racines — seulement des poïls (rhizoïdes).",
  ],
 },
 "exos": [
  (1, "Manuel", "Citer les 5 grands groupes de végétaux et un exemple de chacun.",
   "Angiospermes (rosier) ; gymnospermes (pin) ; fougères (fougère aigle) ; mousses "
   "(sphaigne) ; algues (laitue de mer).",
   "Des plus évoluées (fleurs) aux plus simples (algues).",
   V(enonce="Quel critère sépare gymnospermes et angiospermes ?",
     solution="Les graines nues (cônes) vs graines enfermées dans un fruit (fleurs).")),
  (2, "Contrôle", "Une plante verte, avec racines et tiges, portant des amas de spores "
   "sous ses feuilles. Quel groupe ? Justifier.",
   "FOUGÈRE : vaisseaux conducteurs (vraies racines et tiges) mais SANS graines ni "
   "fleurs — reproduction par spores.",
   "Spores + vaisseaux = fougère, toujours.",
   V(enonce="Placer dans l'ordre évolutif : algue, fougère, rosier, mousse.",
     solution="Algue → mousse → fougère → rosier (organes de plus en plus "
              "différenciés, graines et fleurs).")),
  (3, "Type Examen Régional", "Une clé de détermination est proposée : "
   "1) plante sans vaisseaux conducteurs → aller à 2 ; avec vaisseaux → aller à 3. "
   "2) plante aquatique → ALGUE ; terrestre humide → MOUSSE. "
   "3) reproduction par spores → FOUGÈRE ; par graines → aller à 4. "
   "4) graines nues → GYMNOSPERME ; dans un fruit → ANGIOSPERME. "
   "Classer : cèdre, lentille d'eau (algue verte), sphaigne, fougère aigle, olivier.",
   "Cèdre : vaisseaux + graines nues → gymnosperme.\nLentille d'eau : sans vaisseaux, "
   "aquatique → algue.\nSphaigne : sans vaisseaux, terrestre humide → mousse.\n"
   "Fougère aigle : vaisseaux + spores → fougère.\nOlivier : vaisseaux + graines dans un "
   "fruit → angiosperme.",
   "Suivre la clé PAS À PAS, un critère à la fois."),
 ],
})


# ============================== sync ======================================
def sync(db):
    """Crée/enrichit les 11 chapitres officiels et SUPPRIME les chapitres
    SVT TC hors programme (cellule, biodiversité, érosion...)."""
    n_up = n_ch = n_ex = 0
    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    sid = subjects.get("SVT")
    if not sid:
        print("[sync TC SVT] matière SVT absente")
        return

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

    titres_officiels = set()
    for unit in CH:
        titre = unit["titre"]
        titres_officiels.add(titre)
        ch = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                      "AND titre = ?", (sid, titre), one=True)
        if not ch:
            cid = db.execute(
                "INSERT INTO chapters(subject_id, niveau, semestre, titre, resume, lecon) "
                "VALUES (?,?,?,?,?,?)",
                (sid, "TC", unit["semestre"], titre, unit["resume"],
                 _json.dumps(unit["lecon"], ensure_ascii=False)))
            n_ch += 1
        else:
            cid = ch["id"]
            db.execute("UPDATE chapters SET lecon = ?, semestre = ?, resume = ? WHERE id = ?",
                       (_json.dumps(unit["lecon"], ensure_ascii=False),
                        unit["semestre"], unit["resume"], cid))
            n_up += 1
        add_exos(cid, unit["exos"])

    # suppression des anciens chapitres hors programme
    n_del = 0
    for row in db.query("SELECT id, titre FROM chapters WHERE subject_id = ? AND niveau = 'TC'",
                        (sid,)):
        if row["titre"] not in titres_officiels:
            db.execute("DELETE FROM exercises WHERE chapter_id = ?", (row["id"],))
            db.execute("DELETE FROM chapters WHERE id = ?", (row["id"],))
            n_del += 1

    print(f"[sync TC SVT] {n_up} leçons enrichies, +{n_ch} chapitres, "
          f"+{n_ex} exercices, -{n_del} chapitres hors programme")
