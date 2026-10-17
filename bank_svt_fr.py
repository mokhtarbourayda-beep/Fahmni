# -*- coding: utf-8 -*-
"""bank_svt_fr.py — Banque d'exercices rédigés TC SVT et TC Français."""


def E(d, src, en, sol, ast=""):
    return (d, src, en, sol, ast, [])


# ==================================================================== SVT ====
SVT = {}

SVT["Les techniques adaptatives à l'étude écologique sur le terrain"] = [
    (1, "Manuel", "Qu'est-ce qu'un quadrat et à quoi sert-il ?",
     "Cadre métallique divisé en carrés (souvent 1 m²), posé au hasard dans la station pour "
     "dénombrer les espèces et calculer des moyennes représentatives.",
     "Échantillon au hasard → estimation fiable de toute la station."),
    (2, "Contrôle", "Dans 6 quadrats, on compte l'espèce A dans 3 quadrats et l'espèce B "
     "dans 5. Calculer les fréquences des deux espèces.",
     "Fréquence A = 3/6 × 100 = 50 %\nFréquence B = 5/6 × 100 ≈ 83 %",
     "Fréquence = (quadrats contenant l'espèce ÷ total) × 100."),
    (2, "Contrôle", "Un quadrat de 1 m² contient 8 coquelicots. La station mesure 250 m². "
     "Estimer la population totale.",
     "Densité = 8 individus/m²\nPopulation estimée = 8 × 250 = 2000 coquelicots",
     "Densité moyenne × surface totale."),
    (3, "Type Examen Régional", "Une espèce a une note d'abondance-dominance 5 dans une "
     "station. ① Interpréter. ② Expliquer pourquoi les quadrats doivent être posés au "
     "hasard. ③ Pourquoi étudier plusieurs quadrats plutôt qu'un seul ?",
     "① Note 5 : l'espèce DOMINE la station (recouvrement > 75 % du sol).\n"
     "② Pour éviter un choix orienté (biais) et refléter fidèlement l'ensemble de la "
     "station.\n③ Un seul quadrat peut tomber sur une zone atypique : plusieurs quadrats "
     "donnent une moyenne représentative.",
     "Dominance = recouvrement maximal ; hasard = fiabilité."),
]

SVT["Les facteurs édaphiques et leurs relations avec les êtres vivants"] = [
    (1, "Manuel", "Classer par taille décroissante : limon, sable, argile.",
     "Sable (Ø > 50 µm) > limon (2-50 µm) > argile (Ø < 2 µm).",
     "S-L-A : du plus gros au plus fin."),
    (2, "Contrôle", "Un sol contient 45 % de sable, 35 % de limon, 20 % d'argile. "
     "① Qualifier ce sol. ② Son comportement vis-à-vis de l'eau ?",
     "① Sable dominant (45 %) → sol SABLEUX.\n② Très perméable : l'eau s'infiltre vite, "
     "il sèche rapidement — peu de rétention.",
     "Texture dominante = constituant le plus abondant."),
    (2, "Contrôle", "Citer 2 rôles des lombrics dans le sol.",
     "① Ils creusent des galeries : aération et infiltration de l'eau.\n"
     "② Leurs déjections enrichissent le sol en humus (éléments minéraux disponibles).",
     "Lombrics = ingénieurs + engrais naturels."),
    (3, "Type Examen Régional", "Deux parcelles : P1 sableuse, P2 argileuse, arrosées "
     "identiquement. ② Laquelle se dessèche la première ? Justifier. ② Sur laquelle "
     "planter une plante qui craint l'excès d'eau ?",
     "① P1 (sableuse) : grosses particules → grands pores → l'eau s'infiltre et s'écoule "
     "vite, faible rétention.\n② P2 retient trop l'eau (fines particules) — une plante "
     "craignant l'excès d'eau sera mieux sur P1.",
     "Taille des particules ↔ taille des pores ↔ rétention d'eau."),
]

SVT["Les facteurs climatiques et leurs relations avec les êtres vivants"] = [
    (1, "Manuel", "Donner l'instrument de mesure : température, précipitations, vitesse "
     "du vent, humidité de l'air.",
     "Thermomètre ; pluviomètre ; anémomètre ; hygromètre.",
     "-mètre : therm-o = chaleur, pluvi = pluie, aném = vent, hygr = humidité."),
    (2, "Contrôle", "Températures d'une journée : min 12 °C, max 29 °C. Amplitude "
     "thermique ? Interpréter une amplitude forte.",
     "Amplitude = 29 − 12 = 17 °C.\nUne forte amplitude = grandes différences "
     "jour/nuit (climat continental ou d'altitude) : seules les espèces résistantes "
     "s'y installent.",
     "Amplitude = max − min."),
    (2, "Contrôle", "Sur un diagramme ombrothermique, la courbe des pluies passe SOUS "
     "celle des températures de juin à septembre. Que se passe-t-il ?",
     "Période SÈCHE (juin-septembre) : les précipitations sont insuffisantes par rapport "
     "à la chaleur — c'est l'été sec du climat méditerranéen.",
     "Pluies sous température = saison sèche."),
    (3, "Type Examen Régional", "Les arganiers poussent dans le Sud-Ouest marocain "
     "(faibles pluies). ① Nommer ce type de plante. ② Citer 2 adaptations attendues. "
     "③ Que devient la végétation si les pluies augmentent nettement ?",
     "① XÉROPHYLE (adaptée à la sécheresse).\n② Feuilles petites/dures (moins "
     "d'évaporation), racines profondes, cuticule épaisse.\n③ Des espèces plus "
     "exigeantes en eau s'installent : la végétation s'enrichit et se densifie "
     "(évolution vers une forêt).",
     "Végétation ↔ climat : tout changement climatique change le paysage."),
]

SVT["Flux de la matière et de l'énergie dans l'écosystème"] = [
    (1, "Manuel", "Rédiger la chaîne trophique : chêne, sanglier, lynx — avec les rôles.",
     "Chêne (glands) → sanglier → lynx\nProducteur → consommateur C1 (herbivore) → "
     "consommateur C2 (carnivore).",
     "Toujours commencer par le végétal vert."),
    (2, "Contrôle", "Une biomasse de plantes de 2000 kg nourrit des criquets. "
     "Calculer la biomasse maximale des criquets puis des oiseaux qui les mangent "
     "(rendement 10 % par niveau).",
     "Criquets : 2000 × 10 % = 200 kg\nOiseaux : 200 × 10 % = 20 kg",
     "×0,1 à chaque maillon."),
    (2, "Contrôle", "Quel est le rôle des décomposeurs dans le cycle de la matière ?",
     "Ils décomposent les cadavres, déjections et débris → éléments minéraux remis au "
     "sol → repris par les racines des producteurs : la matière CYCLE, l'énergie ne fait "
     "que passer.",
     "Décomposeurs = recycleurs du sol."),
    (3, "Type Examen Régional", "Une pesticide tue les sauterelles d'une prairie. "
     "① Schématiser la chaîne concernée et indiquer les conséquences sur chaque maillon. "
     "② Pourquoi le poison se retrouve-t-il concentré chez les prédateurs ?",
     "① Herbe → sauterelle → lézard → faucon : les sauterelles meurent (empoisonnées) → "
     "les lézards et faucons manquent de proies (et s'empoisonnent en mangeant les "
     "cadavres).\n② Bioaccumulation : en mangeant de nombreuses proies contaminées, le "
     "prédateur concentre le poison dans ses tissus (plus on est haut, plus la "
     "concentration est forte).",
     "Un maillon touché = toute la chaîne perturbée."),
]

SVT["Les équilibres naturels"] = [
    (1, "Manuel", "Distinguer un déséquilibre naturel d'un déséquilibre humain (2 "
     "exemples de chacun).",
     "Naturel : sécheresse, incendie naturel (aussi inondation, éruption).\n"
     "Humain : déforestation, pollution (aussi surpâturage, braconnage).",
     "Cause humaine = liée à l'activité de l'homme."),
    (2, "Contrôle", "Pourquoi le reboisement aide-t-il à protéger un sol contre "
     "l'érosion ?",
     "Les racines retiennent les particules du sol ; la canopée casse la force des "
     "pluies et du vent ; la litière freine le ruissellement : le sol est protégé et "
     "l'eau s'infiltre.",
     "Végétation = armure du sol."),
    (2, "Contrôle", "Citer 2 espèces marocaines menacées et 2 parcs nationaux qui les "
     "protègent.",
     "Ibis chauve, gazelle dorcas, singe magot, addax...\nParcs : Souss-Massa, Toubkal, "
     "Ifrane, Al Hoceima, Talassemtane...",
     "Exemples du programme : ibis chauve ↔ Souss-Massa."),
    (3, "Type Examen Régional", "Un lac reçoit les eaux chargées d'engrais de champs "
     "voisins. ① Nommer ce phénomène. ② Décrire ses conséquences en chaîne. ③ Proposer "
     "2 solutions.",
     "① L'eutrophisation.\n② Engrais → prolifération d'algues en surface → baisse de la "
     "lumière et de l'oxygène dissous → mortalité des poissons et des plantes → "
     "déséquilibre total.\n③ Bandes tampons végétales entre champs et lac ; réduire les "
     "engrais ; épuration des eaux rejetées.",
     "Excès de nutriments = asphyxie de l'écosystème aquatique."),
]

SVT["La reproduction sexuée chez les plantes à fleurs"] = [
    (1, "Manuel", "Nommer les 4 verticilles d'une fleur complète et leur rôle.",
     "Sépales (protection), pétales (attraction des pollinisateurs), étamines "
     "(gamètes mâles : pollen), carpille(s) (gamètes femelles : ovules).",
     "De l'extérieur vers l'intérieur : S-P-É-C."),
    (2, "Contrôle", "Comparer les caractères du pollen anémogame et entomogame.",
     "Anémogame (vent) : léger, sec, très abondant, petit.\nEntomogame (insectes) : "
     "collant, rugueux, moins abondant ; fleur grande, colorée, parfumée, nectar.",
     "Le pollen « a la forme » de son transporteur."),
    (2, "Contrôle", "Une fleur a 4 ovules fécondés. Combien de graines attendues ? Que "
     "devient chaque ovule fécondé ?",
     "4 graines (1 ovule fécondé → 1 graine).\nChaque ovule : l'oosphère fécondée → "
     "embryon ; la cellule centrale fécondée → albumen (réserves) ; les téguments de "
     "l'ovule → enveloppes de la graine.",
     "Fécondation double : 2 fusions à chaque ovule."),
    (3, "Type Examen Régional", "La pollinisation du blé est autogame, celle du pommier "
     "allogame par abeilles. ① Définir autogamie et allogamie. ② Pourquoi installe-t-on "
     "des ruches dans les vergers de pommiers ? ③ Une variété autofécondée est-elle plus "
     "« pure » génétiquement ?",
     "① Autogamie : le pollen féconde la même fleur (ou la même plante). Allogamie : "
     "fécondation croisée entre plantes différentes.\n② Les abeilles transportent le "
     "pollen d'un pommier à l'autre : sans elles, pas (ou peu) de fruits.\n③ OUI : "
     "l'autogamie fixe les caractères (homozygotie), l'allogamie mélange les gènes.",
     "Autogamie = stabilité ; allogamie = diversité."),
]

SVT["La reproduction sexuée chez les plantes sans fleurs"] = [
    (1, "Manuel", "Citer les organes reproducteurs mâle et femelle de la mousse.",
     "Anéridie (mâle : produit les spermatozoïdes biflagellés) ; archégone (femel : "
     "contient l'oosphère).",
     "A pour mâle (anéridie), arché- pour femelle (archégone)."),
    (2, "Contrôle", "Pourquoi la pluie déclenche-t-elle la fécondation chez les mousses ?",
     "Les spermatozoïdes sont NAGEURS (flagelles) : ils doivent nager dans un film d'eau "
     "jusqu'à l'oosphère. Sans eau, pas de fécondation possible.",
     "Fécondation des plantes sans fleurs = besoin d'eau."),
    (2, "Contrôle", "Décrire le devenir d'une spore de fougère.",
     "La spore (n) germe sur sol humide → petit PROTHALLE (gamétophyte) portant anéridies "
     "et archégones → fécondation dans l'eau → zygote (2n) → jeune sporophyte qui pousse "
     "sur le prothalle → grande fougère.",
     "Spore → prothalle → fécondation → sporophyte."),
    (3, "Type Examen Régional", "① Expliquer pourquoi les fougères sont plus grandes que "
     "les mousses alors que les deux n'ont pas de graines. ② Quelle condition du milieu "
     "partagent leurs fécondations ? ③ Citer la différence majeure entre fougère et pin.",
     "① La fougère possède de vrais VAISSAUX conducteurs (et de vraies racines) : elle "
     "transporte l'eau loin et peut grandir ; la mousse n'en a pas (petite taille, "
     "milieux humides obligatoires).\n② L'eau (gamètes nageurs dans les deux cas).\n"
     "③ Fougère = spores, pas de graines ; pin = GRAINES NUES (pas besoin d'eau pour la "
     "fécondation : pollen par le vent).",
     "Vaisseaux → taille ; graines → indépendance de l'eau."),
]

SVT["Les cycles de développement des plantes"] = [
    (1, "Manuel", "Définir l'alternance des générations (cycle haplodiploïque).",
     "Alternance régulière d'une génération diploïde (sporophyte 2n, produit des spores "
     "par méiose) et d'une génération haploïde (gamétophyte n, produit les gamètes) ; la "
     "fécondation rétablit 2n.",
     "2n → n (méiose) → n → 2n (fécondation)."),
    (2, "Contrôle", "La fougère a n = 30 chromosomes. Nombre de chromosomes : spores, "
     "cellules du prothalle, oosphère, zygote, cellules de la grande fougère ?",
     "Spores : n = 30 ; prothalle : n = 30 ; oosphère : n = 30 ; zygote : 2n = 60 ; "
     "grande fougère : 2n = 60.",
     "Tout ce qui est gamétophyte/gamète = n ; sporophyte/zygote = 2n."),
    (2, "Contrôle", "Indiquer la phase dominante (visible) chez : mousse, fougère, "
     "plante à fleurs.",
     "Mousse : GAMÉTOPHYTE dominant.\nFougère : SPOROPHYTE dominant (prothalle minuscule "
     "et passager).\nPlante à fleurs : SPOROPHYTE exclusivement (gamétophytes réduits à "
     "quelques cellules dans la fleur).",
     "Plus évolué = sporophyte plus dominant."),
    (3, "Type Examen Régional", "① Où a lieu la méiose chez une plante à fleurs ? "
     "② Chez la mousse, la plante verte est-elle n ou 2n ? Justifier par le cycle. "
     "③ Montrer que la réduction du gamétophyte est un avantage terrestre.",
     "① Dans les SPORANGES : anthères (grains de pollen) et ovules (sacs embryonnaires) — "
     "elle produit les spores.\n② n (gamétophyte) : c'est elle qui porte les anéridies et "
     "archégones qui produisent directement les gamètes (sans méiose).\n③ Le jeune "
     "gamétophyte nu (spore, prothalle) est fragile : en le réduisant et le PROTÉGEANT "
     "dans l'organe du sporophyte (fleur, ovule), la plante survit mieux au milieu "
     "terrestre sec.",
     "Chez les plantes, méiose = spores (PAS les gamètes)."),
]

SVT["La reproduction asexuée chez les plantes"] = [
    (1, "Manuel", "Citer 2 modes naturels et 2 techniques artificielles de multiplication "
     "végétative.",
     "Naturels : rhizomes, tubercules, bulbes, stolons.\nArtificiels : bouture, "
     "marcottage, greffe.",
     "Naturel = l'organe le fait seul ; artificiel = l'homme intervient."),
    (2, "Contrôle", "Un fraisier émet 4 stolons, chacun s'enracinant en 2 endroits. "
     "Combien de nouveaux plants, et seront-ils identiques ?",
     "4 × 2 = 8 nouveaux plants.\nOUI, identiques (clones : reproduction asexuée, même "
     "ADN que la plante-mère).",
     "Asexuée = clone garantie."),
    (2, "Contrôle", "Que gagne un arboriculteur à greffer une variété de bonne qualité "
     "sur un porte-greffe rustique ?",
     "Il combine : les FRUITS de la variété greffée (qualité, goût) et les RACINES du "
     "porte-greffe (vigueur, résistance au sol et aux maladies) ; de plus la mise à fruit "
     "est plus rapide qu'avec un semis.",
     "Greffe = mariage des qualités."),
    (3, "Type Examen Régional", "Une maladie nouvelle attaque une variété de vigne "
     "multipliée par boutures sur toute une région. ① Pourquoi toutes les vignes sont-elles "
     "touchées ? ② Quel mode de reproduction aurait limité ce risque ? ③ Citer un "
     "avantage malgré tout de la multiplication par boutures.",
     "① Boutures = clones : mêmes gènes → même sensibilité à la maladie (aucune plante "
     "résistante).\n② La reproduction SEXUÉE (semis) : le mélange des gènes crée de la "
     "diversité, certains individus pouvant être résistants.\n③ Fidélité totale à la "
     "variété (qualité du raisin), simplicité, rapidité, sans partenaire.",
     "Uniformité génétique = vulnérabilité commune."),
]

SVT["La modification génétique des plantes"] = [
    (1, "Manuel", "Définir transgenèse et OGM, et citer un vecteur de transfert de gène.",
     "Transgenèse : transfert d'un gène d'un organisme vers un autre.\nOGM : organisme "
     "dont le génome a été modifié par l'homme.\nVecteur : Agrobacterium tumefaciens "
     "(ou canon à particules).",
     "Agrobacterium = « taxi à gènes »."),
    (2, "Contrôle", "Un maïs contient un gène de bactérie le rendant toxique pour ses "
     "insectes ravageurs. ① Nommer cette technique. ② Citer 2 avantages attendus.",
     "① Transgenèse (maïs Bt = OGM).\n② Moins d'insecticides chimiques (économie, moins "
     "de pollution) ; meilleur rendement (moins de dégâts).",
     "Gène Bt de Bacillus thuringiensis."),
    (2, "Contrôle", "Une nouvelle variété de blé obtenue par croisement avec une variété "
     "sauvage est-elle un OGM ?",
     "NON : c'est une hybridation (croisement sexuel naturel entre variétés proches) — "
     "pas de transfert de gène par laboratoire entre espèces éloignées.",
     "Croisement naturel ≠ transgenèse."),
    (3, "Type Examen Régional", "① Décrire les 4 étapes de la transgenèse d'une plante "
     "résistante à un insecte. ② Pourquoi une réglementation (étiquetage, essais) "
     "encadre-t-elle les OGM ? Citer 2 raisons.",
     "① Isolation du gène d'intérêt (de la bactérie) → transfert dans les cellules "
     "végétales (Agrobacterium ou canon à gènes) → régénération de plantes complètes → "
     "sélection des plantes exprimant réellement le gène.\n"
     "② Sécurité sanitaire (effets à long terme évalués) ; environnement (dissémination "
     "du pollen aux plantes sauvages, effet sur les insectes utiles) ; transparence du "
     "consommateur.",
     "Étapes : isoler → transférer → régénérer → sélectionner."),
]

SVT["La classification des plantes"] = [
    (1, "Manuel", "Citer les 5 grands groupes de végétaux avec un exemple de chacun.",
     "Angiospermes (rosier) ; gymnospermes (pin/cèdre) ; fougères (fougère aigle) ; "
     "mousses (sphaigne) ; algues (laitue de mer).",
     "Des fleurs aux algues : du plus évolué au plus simple."),
    (2, "Contrôle", "Une plante verte possède des vaisseaux conducteurs et se reproduit "
     "par spores. Quel groupe ? Justifier.",
     "FOUGÈRE : les vaisseaux excluent algues et mousses ; les spores excluent "
     "gymnospermes et angiospermes (graines).",
     "Clé : vaisseaux ? → graines ? → fleurs ?"),
    (2, "Contrôle", "Quel critère unique sépare les conifères des plantes à fleurs ?",
     "Les conifères ont des GRAINES NUES (dans des cônes, pas de fleurs) ; les plantes à "
     "fleurs ont des graines enfermées dans un FRUIT issu de l'ovaire.",
     "Nues (gymno) vs dans le fruit (angio)."),
    (3, "Type Examen Régional", "Construire une clé à 4 questions permettant de classer "
     "une plante inconnue dans : algue, mousse, fougère, conifère, plante à fleurs.",
     "① La plante a-t-elle de vrais organes (racines/tiges avec vaisseaux) ? NON → "
     "milieu aquatique ? OUI → ALGUE ; NON → MOUSSE.\n"
     "② OUI → se reproduit-elle par spores ? OUI → FOUGÈRE.\n"
     "③ NON (graines) → graines nues (cônes) → CONIFÈRE ; graines dans un fruit → "
     "PLANTE À FLEURS.",
     "Clé = questions successives, chacune sépare un groupe."),
]

# ================================================================ FRANÇAIS ===
FR = {}

FR["Le texte argumentatif"] = [
    (1, "Manuel", "« Le tabac coûte cher à la société. En effet, les maladies liées au tabagisme "
     "engorgent les hôpitaux ; de plus, il prive les familles de ressources. » Relever 2 connecteurs "
     "et les classer.",
     "« En effet » : explication/cause ; « de plus » : addition.\nStructure : thèse + 2 arguments.",
     "Classer : cause, conséquence, addition, opposition."),
    (2, "Contrôle", "« Certes, les voitures électriques polluent moins, mais leur batterie pose des "
     "problèmes environnementaux. » Identifier thèse implicite et stratégie.",
     "Admission (« certes ») puis OPPOSITION (« mais ») : l'auteur nuance l'argument écologique.\n"
     "Stratégie : concéder pour mieux réfuter (anticiper l'objection).",
     "Ce qui suit « certes » est l'opinion ADVERSE."),
    (2, "Contrôle", "Distinguer argument et exemple dans : « La lecture développe l'esprit critique. "
     "Par exemple, analyser un roman policier apprend à deviner la suite. »",
     "Argument : « La lecture développe l'esprit critique » (idée générale).\n"
     "Exemple : le cas du roman policier (illustration concrète).",
     "L'argument justifie ; l'exemple ILLUSTRE."),
    (2, "Contrôle", "Citer 4 procédés de PERSUASION (vs convaincre).",
     "Questions oratoires, impératifs (« Agissez ! »), hyperboles, vocabulaire émotionnel, "
     "appel aux émotions/peurs.",
     "Convaincre = raisonner ; persuader = émouvoir."),
    (3, "Type Examen Régional",
     "Rédiger un paragraphe argumenté (5 lignes) : « Les réseaux sociaux menacent-ils la "
     "réussite scolaire ? » avec thèse, 2 arguments + exemples, 3 connecteurs.",
     "Modèle : « Les réseaux sociaux menacent la réussite scolaire. D'abord, ils dévorent le temps "
     "d'étude : trois heures de scroll remplacent les devoirs. En effet, l'usage nocturne dégrade le "
     "sommeil et la concentration. De plus, la comparaison permanente nuit à la confiance. Par "
     "conséquent, un usage encadré s'impose. »",
     "Thèse → argument 1 + ex → argument 2 + ex → conclusion (« par conséquent »)."),
    (1, "Manuel", "Relever le modalisateur : « Il est probable que les écrans réduisent le sommeil. » "
     "Quel est son effet ?",
     "Modalisateur : « il est probable que » → atténue l'affirmation (non vérifiée à 100 %).\n"
     "Effet : prudence scientifique, nuance.",
     "Modalisateurs : probable, certain, peut-être, il semble…"),
]

FR["Les figures de style"] = [
    (1, "Manuel", "Identifier : « Cette femme est un rayon de soleil. »",
     "MÉTAPHORE (pas d'outil de comparaison) : femme = rayon de soleil → joie, chaleur.",
     "Outil absent → métaphore ; présent (comme, tel) → comparaison."),
    (1, "Manuel", "Identifier : « Il est doux comme un agneau. »",
     "COMPARAISON (outil : « comme ») : douceur comparée à l'agneau.",
     "Chercher l'outil de comparaison."),
    (1, "Manuel", "Identifier : « La mer se fâche et fracasse ses vagues sur le rocher. »",
     "PERSONNIFICATION : la mer agit comme un humain (se fâche, fracasse).",
     "Comportement humain attribué à une chose."),
    (2, "Contrôle", "Identifier : « Je suis mort de fatigue » et « Il nous a quittés ».",
     "« Mort de fatigue » : HYPERBOLE (exagération).\n« Il nous a quittés » : EUPHÉMISME "
     "(atténue la mort).",
     "Exagérer vs atténuer : deux extrêmes du style."),
    (2, "Contrôle", "Identifier : « Un mot, une phrase, un discours » puis « ce n'est pas mauvais » "
     "(pour « c'est excellent »).",
     "« Un mot, une phrase, un discours » : GRADATION (intensité croissante).\n"
     "« Ce n'est pas mauvais » : LITOTE (dire moins pour suggérer plus).",
     "Gradation = escalade ; litote = minimisation calculée."),
    (2, "Contrôle", "« Les sanglots longs des violons de l'automne » (Verlaine) : figure de son ? "
     "Effet ?",
     "ALLITÉRATION en [l] : sonorités douces et traînantes → langueur, tristesse de l'automne.",
     "Relier la figure à son EFFET (jamais seulement la nommer)."),
    (2, "Contrôle", "« Il vivait le jour, elle la nuit » : figure ? Puis « Vivre pour soi ou vivre "
     "pour les autres : il fallait choisir. »",
     "① ANTITHÈSE (opposition jour/nuit, il/elle)\n② Antithèse également (vivre pour soi vs pour "
     "les autres) — via une alternative.",
     "Antithèse = 2 idées opposées confrontées."),
    (2, "Contrôle", "« Partout, dans la rue, dans les cafés, dans les écoles, on parlait du match. » : "
     "figure ?",
     "ANAPHORE (répétition de « dans » en tête de groupes) → insiste sur l'OMNIPRÉSENCE du sujet.",
     "Répétition en tête = anaphore."),
    (3, "Type Examen Régional",
     "« Tes yeux sont deux étoiles qui éclairent ma nuit. » Identifier la figure, puis en produire "
     "une semblable sur la mer.",
     "Métaphore filée : yeux = étoiles (lumière, guidance, beauté).\n"
     "Production attendue (métaphore) : « La mer est un miroir d'argent » ou "
     "« La mer, un géant qui soupire. »",
     "Produire une figure = respecter sa DÉFINITION (pas de « comme » pour une métaphore)."),
    (1, "Manuel", "« Cette femme est une rose » : métaphore. Réécrire en comparaison.",
     "« Cette femme est COMME une rose. » (outil ajouté → comparaison)",
     "Ajouter l'outil transforme la métaphore en comparaison."),
]

FR["Le texte narratif"] = [
    (1, "Manuel", "Ordonner le schéma narratif et le repérer dans : « Ali vivait paisiblement. Un "
     "matin, sa maison brûla. Il lutta contre les flammes, fut secouru par ses voisins, et repeignit "
     "sa maison plus solide. »",
     "Ordre : SI → ÉP → péripéties → dénouement → SF.\nSI : vie paisible ; ÉP : incendie ; "
     "Péripéties : lutte + secours ; Dénouement : fin de l'incendie ; SF : maison reconstruite "
     "(nouvel équilibre).",
     "Trouver la RUPTURE d'abord, placer le reste autour."),
    (2, "Contrôle", "« Je sentis mon cœur se serrer : nul ne connaissait ma peine. » Narrateur ? "
     "Focalisation ?",
     "Narrateur PERSONNAGE (« je ») ; focalisation INTERNE (émotions intimes accessibles : "
     "« mon cœur », « ma peine »).",
     "« je » + intériorité = focalisation interne."),
    (2, "Contrôle", "« Il traversa la place sans voir l'ombre qui l'observait du toit. » Focalisation ? "
     "Justifier.",
     "Focalisation ZÉRO (omnisciente) : le narrateur sait ce que le personnage ignore "
     "(l'observateur du toit).",
     "Narrateur qui en sait PLUS que le personnage = zéro."),
    (2, "Contrôle", "Justifier les temps : « Il marchait depuis une heure quand il aperçut une "
     "lumière. Il s'approcha et frappa. »",
     "« marchait » : imparfait (durée, arrière-plan) ; « aperçut, s'approcha, frappa » : passé "
     "simple (actions ponctuelles de premier plan).",
     "Imparfait = décor/durée ; passé simple = actions."),
    (2, "Manuel", "« Tous les dimanches, il rendait visite à sa grand-mère. » : imparfait de quelle "
     "valeur ?",
     "IMPARFAIT D'HABITUDE (répétition : « tous les dimanches ») — pas de description ni d'action "
     "ponctuelle.",
     "Indice de répétition → imparfait d'habitude."),
    (3, "Type Examen Régional",
     "Écrire le début d'un récit (4 lignes) avec situation initiale à l'imparfait et élément "
     "perturbateur au passé composé, marqué par un connecteur.",
     "Modèle : « Ce soir-là, nous dinions tranquillement quand, soudain, un bruit sourd a secoué la "
     "maison. Les vitres ont tremblé. Mon père s'est levé d'un bond. »\n(SI à l'imparfait, "
     "connecteur « soudain », ÉP au passé composé.)",
     "Bascule des temps + connecteur de rupture = récit maîtrisé."),
]

FR["Le texte descriptif"] = [
    (1, "Manuel", "Relever 4 indices descriptifs : « À droite s'étendait une plage de sable fin. Une "
     "mer calme, d'un bleu profond, bordait la baie. »",
     "Organisateur spatial « à droite » ; imparfaits « s'étendait, bordait » ; adjectifs « fin, "
     "calme, profond » ; compléments du nom « plage de sable fin, mer d'un bleu profond ».",
     "4 familles : organisateurs, temps, adjectifs, expansions."),
    (2, "Contrôle", "« Élancé, le regard Perçant, il semblait défier le monde. » Portrait physique, "
     "moral, ou les deux ? Ton ?",
     "Les DEUX : physique (élancé) + moral (regard perçant, défi).\nTon valorisant (mélioratif) "
     "— portrait presque héroïque.",
     "Portrait = physique + moral ; ton mélioratif ou péjoratif."),
    (2, "Contrôle", "Enrichir « un chat » avec : un adjectif, un complément du nom, une relative.",
     "Ex : « un chat noir » ; « un chat du voisin » ; « un chat qui ronronne dès qu'on le "
     "caresse ».\nCumul : « un chat noir du voisin qui ronronne dès qu'on le caresse ».",
     "3 expansions du nom à combiner."),
    (2, "Manuel", "Classement : « tous les jours, il allait au marché » — narratif ou descriptif ?",
     "NARRATIF (habitude, action répétée à l'imparfait d'habitude). Pas de description d'objet/lieu.",
     "Chercher la DOMINANTE du passage."),
    (3, "Type Examen Régional",
     "Décrire un souk marocain (4-5 lignes) : 2 organisateurs spatiaux, imparfait/présent cohérent, "
     "1 personnification, vocabulaire des 5 sens.",
     "Modèle : « Au cœur de la médina, le souk débordait de vie. Sous les auvents colorés, les "
     "épices étalaient leurs monticules rouges et jaunes ; leurs parfums piquaient le nez. Le "
     "marchandage chantait dans toutes les langues, et le cuivre scintillait comme un feu. »",
     "Grille : organisateurs ✓ temps ✓ figure ✓ sens ✓."),
]

FR["Le texte explicatif"] = [
    (1, "Manuel", "Relever définition + cause + conséquence : « La sécheresse, c'est-à-dire un manque "
     "prolongé de pluie, appauvrit les sols parce que la végétation disparaît ; si bien que "
     "l'érosion s'accélère. »",
     "Définition : « c'est-à-dire un manque prolongé de pluie » ; cause : « parce que » ; "
     "conséquence : « si bien que ».",
     "Chaîne logique : définition → cause → effet."),
    (2, "Contrôle", "« Le tabac tue ; les publicités devraient être interdites. » Explicatif ou "
     "argumentatif ? 2 justifications.",
     "ARGUMENTATIF : opinion (« devraient ») + jugement ; pas de définition ni explication neutre.",
     "Opinion présente = argumentatif, même thème « informatif »."),
    (2, "Contrôle", "Compléter : « Les plantes fabriquent leur matière ___ la lumière ; ___, une "
     "plante privée de lumière meurt. »",
     "« grâce à la lumière » (cause favorable) ; « Ainsi/Par conséquent » (conséquence).",
     "grâce à (+) / à cause de (-) ; ainsi = conséquence."),
    (2, "Contrôle", "Pourquoi l'explicatif utilise-t-il surtout le présent et la voix passive ?",
     "Présent de VÉRITÉ GÉNÉRALE (lois, faits permanents) ; passif/impersonnel = neutralité et "
     "objectivité (pas de « je »).",
     "Objectivité : présent général + pas de sujet personnel."),
    (3, "Type Examen Régional",
     "Rédiger 4 lignes explicatives sur le cycle de l'eau : définition, cause, conséquence, présent "
     "de vérité générale.",
     "Modèle : « Le cycle de l'eau, c'est-à-dire le parcours permanent de l'eau entre mer, air et "
     "terre, se déroule sans fin. Sous l'effet du soleil, l'eau s'évapore ; comme la vapeur monte en "
     "altitude, elle se condense en nuages ; si bien que la pluie ramène l'eau vers l'océan. »",
     "Définition + cause + conséquence + présent général : quota complet."),
]

FR["Le résumé de texte"] = [
    (2, "Contrôle", "Citer 4 catégories d'informations SUPPRIMABLES dans un résumé.",
     "Exemples illustratifs ; répétitions ; citations ; détails/chiffres secondaires.",
     "Supprimer l'illustration, garder l'idée."),
    (2, "Contrôle", "Un texte de 200 lignes : longueur cible du résumé ?",
     "Environ 1/4 du texte → ~50 lignes.",
     "Proportion : 1/4 (à ajuster selon la consigne)."),
    (2, "Contrôle", "Reformuler sans recopier : « Les océans absorbent chaque année des millions de "
     "tonnes de CO₂ ; par exemple, l'Atlantique capte un quart des émissions. Ce service atténue le "
     "réchauffement. »",
     "« Les océans, en absorbant une grande partie du CO₂ émis, atténuent le réchauffement "
     "climatique. » (exemple supprimé, idée conservée, reformulation).",
     "Généraliser l'exemple, fusionner les idées."),
    (3, "Type Examen Régional",
     "Résumer en 2 phrases : « Le Maroc connaît une urbanisation rapide. Casablanca, Rabat et "
     "Tanger grossissent chaque année de milliers d'habitants venus chercher du travail. Cette "
     "affluence provoque une pénurie de logements et une pression sur les transports. Les autorités "
     "multiplient donc les programmes de villes nouvelles. »",
     "« Le Maroc s'urbanise rapidement, ses grandes villes attirant une main-d'œuvre nombreuse. "
     "Cette croissance engendre des difficultés (logement, transports) auxquelles les autorités "
     "répondent par la construction de villes nouvelles. »",
     "Idée par paragraphe + connecteurs + reformulation."),
]

FR["Les propositions subordonnées"] = [
    (1, "Manuel", "Identifier : « Le livre que tu m'as offert plaît à tous ceux qui aiment l'histoire. »",
     "« que tu m'as offert » : RELATIVE (antécédent : le livre) ; « qui aiment l'histoire » : "
     "RELATIVE (antécédent : ceux).",
     "Pronom relatif + antécédent = relative."),
    (2, "Contrôle", "« Je pense que tu réussiras si tu travailles. » Analyser chaque proposition.",
     "Principale : « je pense » ; « que tu réussiras » : COMPLÉTIVE (COD de « pense ») ; "
     "« si tu travailles » : circonstancielle de CONDITION.",
     "que + verbe complété = complétive ; si = condition."),
    (2, "Contrôle", "« Il est parti parce qu'il était en retard. » / « Bien qu'il soit malade, il "
     "vient. » : nature et sens des subordonnées ?",
     "« parce qu'il était en retard » : circonstancielle de CAUSE.\n« Bien qu'il soit malade » : "
     "circonstancielle de CONCESSION (fait admis malgré l'obstacle).",
     "Cause = pourquoi ; concession = malgré quoi."),
    (2, "Manuel", "Relier : ① il pleuvait… nous sommes sortis (opposition) ② … tu finis, nous "
     "commencerons (temps) ③ … il soit malade, il vient (concession).",
     "① Bien que/Quoiqu'il plût… (opposition : « pourtant » aussi accepté)\n"
     "② Dès que/Aussitôt que tu finis\n③ Bien qu'il soit malade (concession)",
     "Bien que = concession ; quand/dès que = temps ; parce que = cause."),
    (2, "Contrôle", "« que » pronom relatif ou conjonction ? Distinguer dans : « le gâteau que tu as "
     "fait » / « je sais que tu viens ».",
     "① « que » pronom relatif (antécédent : le gâteau ; complète un NOM).\n"
     "② « que » conjonction (pas d'antécédent ; complète le VERBE « sais »).",
     "Antécédent ? → relatif ; verbe complété → conjonction."),
    (3, "Type Examen Régional",
     "Analyser : « Lorsque le car arriva, les voyageurs qui attendaient depuis l'aube poussèrent un "
     "soupir de soulagement. »",
     "« Lorsque le car arriva » : circonstancielle de TEMPS ; Principale : « les voyageurs… "
     "poussèrent un soupir » ; « qui attendaient depuis l'aube » : relative (antécédent : les "
     "voyageurs).\nValeurs : passé simple (arriva, poussèrent) = actions ; imparfait "
     "(attendaient) = durée.",
     "Structure : principale + subordonnées + valeurs des temps."),
]

FR["Le lexique : sens et nuances"] = [
    (1, "Manuel", "Constituer le champ lexical de la mer dans : « Le marin contemplait les vagues ; "
     "le vent salé parfumait le port. »",
     "marin, contemplait (regard), vagues, salé, vent, port → champ lexical de la MER.",
     "Champ lexical = thème commun, toutes classes confondues."),
    (2, "Contrôle", "« une feuille » : sens dans ① « une feuille de papier » ② « une feuille de "
     "vigne » ③ « faire la feuille » (absence) ?",
     "① page ② organe de la plante ③ registre de présence → mot POLYSÉMIQUE : le contexte choisit.",
     "Un mot, plusieurs sens : le contexte tranche."),
    (2, "Contrôle", "« un enfant maigre » vs « un enfant frêle » : différence ?",
     "Sens dénoté proche ; connotations opposées : « maigre » neutre/péjoratif, « frêle » "
     "mélioratif (fragilité attendrissante).",
     "Synonymes ≠ nuances : la connotation change tout."),
    (2, "Contrôle", "Relever 2 mots à connotation péjorative : « Cette bande s'agitait bruyamment, "
     "bousculant les passants inoffensifs. »",
     "« bande » (désordre), « s'agitait », « bousculant », « bruyamment » → le lecteur juge le "
     "groupe négativement AVANT tout fait.",
     "La connotation ORIENTE le jugement du lecteur."),
    (2, "Manuel", "Donner le sens dénoté et une connotation de « rouge ».",
     "Dénoté : couleur du sang/coquelicot.\nConnotations : danger, passion, colère, interdit — "
     "selon le contexte.",
     "Dénotation = dictionnaire ; connotation = émotions/culture."),
    (3, "Type Examen Régional",
     "Analyser le lexique d'un passage publicitaire : « Brillant, délicieux, irrésistible : le "
     "nouveau jus Sunfruit ! » Quel effet recherché ?",
     "Champ lexical mélioratif (brillant, délicieux, irrésistible) + hyperbole.\n"
     "Effet : PERSUADER par les émotions (désir), non par l'argument — registre laudatif.",
     "Lexique mélioratif + hyperboles = stratégie publicitaire."),
]

FR["Les valeurs des temps verbaux"] = [
    (1, "Manuel", "Valeur du présent dans : ① « La Terre tourne » ② « Chaque samedi, je vais au "
     "stade » ③ « Il neige ! »",
     "① vérité générale ② habitude ③ action en cours (énonciation).",
     "3 valeurs majeures du présent."),
    (2, "Contrôle", "« Quand j'étais petit, je jouais dehors ; un jour, j'ai cassé la vitrine. » "
     "Justifier les temps.",
     "« étais », « jouais » : imparfaits (description + habitude) ; « ai cassé » : passé composé "
     "(action ponctuelle qui ROMPT l'habitude).",
     "Habitude → imparfait ; événement → passé composé."),
    (2, "Contrôle", "« Le train était parti quand il est arrivé. » Quelle antériorité ? Quel temps ?",
     "« était parti » : PLUS-QUE-PARFAIT → action antérieure à un autre passé (le train parti AVANT "
     "son arrivée).",
     "Antériorité au passé = plus-que-parfait."),
    (2, "Manuel", "« Dès que tu auras signé, tu recevras la clé. » Identifier les temps.",
     "« auras signé » : futur antérieur (achevé AVANT une action future) ; « recevras » : futur "
     "simple.",
     "Futur antérieur = « la première action » de deux futurs."),
    (2, "Contrôle", "« Selon la météo, il ferait beau demain. » Valeur du conditionnel ?",
     "Information NON CONFIRMÉE (rapportée : « selon ») ; le conditionnel marque la prudence, "
     "l'hypothèse, la politesse ou le futur du passé.",
     "Conditionnel ≠ certain : incertitude/rapport."),
    (3, "Type Examen Régional",
     "« Hier, je lisais tranquillement quand soudain le téléphone a sonné. » Expliquer la "
     "complémentarité des temps (structure type d'examen).",
     "Imparfait « lisais » : action DURATIVE en arrière-plan (cadre).\nPassé composé « a sonné » : "
     "action PONCTUELLE qui l'INTERROMPT (fait nouveau).\nStructure classique : imparfait du cadre + "
     "passé composé de l'incident.",
     "Le cadre à l'imparfait, l'incident au passé composé."),
]


def sync(db):
    """Insère les exercices rédigés SVT/FR (non destructif, dédoublonné)."""
    n_ex = 0
    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    for code, bank in (("SVT", SVT), ("FR", FR)):
        sid = subjects[code]
        for titre, exos in bank.items():
            ch = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                          "AND titre = ?", (sid, titre), one=True)
            if not ch:
                continue
            for diff, source, enonce, solution, astuce in exos:
                dupe = db.query("SELECT id FROM exercises WHERE chapter_id = ? AND enonce = ?",
                                (ch["id"], enonce), one=True)
                if not dupe:
                    db.execute(
                        "INSERT INTO exercises(chapter_id, difficulte, source, enonce, "
                        "solution, astuce, variantes) VALUES (?,?,?,?,?,?,?)",
                        (ch["id"], diff, source, enonce, solution, astuce, "[]"))
                    n_ex += 1
    print(f"[bank SVT/FR] +{n_ex} exercices rédigés")
