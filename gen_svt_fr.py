# -*- coding: utf-8 -*-
"""gen_svt_fr.py — Générateurs SVT (programme officiel TC : écologie + botanique)
et Français. Importé par gen_exercices.py."""
import random
from fractions import Fraction as F
from gen_exercices import reg, fmt


# ═══════════════════════════════════════ S1 · ÉCOLOGIE ══
ABOND = ("+", "1", "2", "3", "4", "5")
ABOND_TXT = {"+": "espèce rare (1 seul individu)", "1": "quelques individus",
             "2": "espèce abondante", "3": "très abondante (25-50 % de recouvrement)",
             "4": "très abondante (50-75 % de recouvrement)",
             "5": "dominante (recouvrement > 75 %)"}


@reg("SVT", "Les techniques adaptatives à l'étude écologique sur le terrain", (1, 2))
def _svt_densite():
    nq = random.choice((4, 5, 6))
    n = random.randrange(2, nq)
    comptes = [random.randrange(1, 9) for _ in range(nq)]
    moy = F(sum(comptes), nq)
    surf = random.choice((100, 150, 200, 250))
    total = moy * surf
    esp = random.choice(("thym", "romarin", "lavande", "coquelicot", "armoise"))
    det = " + ".join(str(c) for c in comptes)
    return (f"Dans {nq} quadrats de 1 m², on compte respectivement {det} plants "
            f"d'{esp}. ① Densité moyenne ? ② Estimation du nombre total sur "
            f"{surf} m² ?",
            f"① Densité = ({det}) ÷ {nq} = {fmt(moy)} plants/m²\n"
            f"② Total = {fmt(moy)} × {surf} = {fmt(total)} plants",
            "Moyenne des comptes, puis × surface totale.")


@reg("SVT", "Les techniques adaptatives à l'étude écologique sur le terrain", (2, 3))
def _svt_frequence():
    nq = random.choice((5, 10, 20))
    n = random.randrange(1, nq)
    f = F(n * 100, nq)
    note = random.choice(("2", "3", "4", "5"))
    esp = random.choice(("chêne-liège", "genêt", "ziziphe", "pistachier"))
    return (f"L'espèce « {esp} » est présente dans {n} quadrats sur {nq}. "
            f"① Sa fréquence ? ② Une autre espèce a la note d'abondance-dominance "
            f"« {note} » : interpréter cette note.",
            f"① Fréquence = ({n} ÷ {nq}) × 100 = {fmt(f)} %\n"
            f"② Note {note} : {ABOND_TXT[note]}",
            "Fréquence = % de quadrats contenant l'espèce ; Braun-Blanquet : de + à 5.")


@reg("SVT", "Les facteurs édaphiques et leurs relations avec les êtres vivants", 1)
def _svt_texture():
    sab = random.randrange(15, 60, 5)
    arg = random.randrange(10, 45, 5)
    lim = 100 - sab - arg
    tex = ("sableux" if sab >= 45 else "argileux" if arg >= 45 else
           "limoneux" if lim >= 45 else "équilibré (limono-sablo-argileux)")
    dom = max(("sable", sab), ("limon", lim), ("argile", arg), key=lambda p: p[1])[0]
    return (f"Un sol contient {sab} % de sable, {lim} % de limon et {arg} % d'argile. "
            "① Vérifier que les pourcentages totalisent 100 %. ② Quelle est la texture "
            "dominante ? ③ Quel type de sol obtient-on ?",
            f"① {sab} + {lim} + {arg} = 100 %\n② Le constituant majoritaire : {dom} "
            f"({max(sab, lim, arg)} %)\n③ Sol {tex}",
            "Texture = constituant le plus abondant ; total forcément 100 %.")


@reg("SVT", "Les facteurs édaphiques et leurs relations avec les êtres vivants", (2, 3))
def _svt_sol_eau():
    sab = random.randrange(60, 90, 5)
    reste = 100 - sab
    return (f"Un sol sableux contient {sab} % de sable et {reste} % d'autres éléments. "
            "① Que peuvent-on dire de ses pores ? ② Comportement vis-à-vis de l'eau ? "
            "③ Quels êtres vivants l'améliorent et comment ?",
            "① Particules grosses → pores larges entre elles.\n"
            "② Très PERMÉABLE : l'eau s'infiltre et s'écoule vite, faible rétention → "
            "sol sec.\n③ Les LOMBRICS : galeries (aération, infiltration) + déjections "
            "en humus ; les décomposeurs produisent l'humus.",
            "Taille des particules → taille des pores → rétention d'eau.")


@reg("SVT", "Les facteurs climatiques et leurs relations avec les êtres vivants", (1, 2))
def _svt_amplitude():
    tmin = random.randrange(-2, 15)
    tmax = tmin + random.randrange(8, 22)
    amp = tmax - tmin
    instr = random.choice((("pluviomètre", "précipitations (mm d'eau)"),
                           ("hygromètre", "humidité de l'air (%)"),
                           ("anémomètre", "vitesse du vent (km/h)"),
                           ("photomètre", "l'intensité lumineuse (lux)")))
    return (f"① Une station enregistre {tmin} °C au minimum et {tmax} °C au maximum : "
            f"calculer l'amplitude thermique. ② Quel facteur climatique mesure un "
            f"{instr[0]} et en quelle unité ?",
            f"① Amplitude = {tmax} − ({tmin}) = {amp} °C\n"
            f"② Le {instr[0]} mesure {instr[1]}",
            "Amplitude = max − min ; connaître les 5 instruments du climat.")


@reg("SVT", "Les facteurs climatiques et leurs relations avec les êtres vivants", 3)
def _svt_ombro():
    p = random.choice((8, 12, 15, 20, 25))
    return (f"Un mois d'été enregistre {p} mm de précipitations et une température "
            "moyenne de 24 °C. ① Ce mois est-il sec ou humide ? Justifier. ② Citer 2 "
            "adaptations des végétaux à ce régime. ③ Donner le nom des plantes adaptées "
            "à la sécheresse.",
            f"① {p} mm est très faible : mois SEC (sur le diagramme ombrothermique, la "
            "courbe des pluies passe sous celle des températures).\n"
            "② Feuilles réduites ou transformées (aiguilles, épines) ; cuticule épaisse ; "
            "racines profondes.\n③ Les xérophytes (ex : arganier, olivier, genêt).",
            "Mois sec : pluies insuffisantes par rapport à la chaleur.")


@reg("SVT", "Flux de la matière et de l'énergie dans l'écosystème", 1)
def _svt_chaine():
    chaines = (("herbe", "sauterelle", "lézard", "faucon"),
               ("glands", "sanglier", "lynx"),
               ("algues", "zooplancton", "sardine", "thon"),
               ("roseaux", "criquet", "grenouille", "serpent"))
    c = random.choice(chaines)
    fleche = " → ".join(c)
    return (f"Construire la chaîne trophique à partir de : {', '.join(reversed(c))}. "
            "Préciser le rôle (niveau trophique) de chaque maillon.",
            f"{c[0]} → {c[1]} → " + (" → ".join(c[2:]) if len(c) > 3 else c[2]) + "\n"
            f"{c[0]} : producteur ; {c[1]} : consommateur C1 (herbivore) ; " +
            (f"{c[2]} : C2 (carnivore) ; {c[3]} : C3 (super-prédateur)."
             if len(c) > 3 else f"{c[2]} : C2 (carnivore)."),
            "Commencer par le producteur vert ; flèches = « est mangé par ».")


@reg("SVT", "Flux de la matière et de l'énergie dans l'écosystème", (2, 3))
def _svt_pyramide():
    b = random.choice((1000, 2000, 4000, 5000))
    niv = random.choice((2, 3))
    lignes = [f"Producteurs : {b} kg"]
    cour = b
    noms = ["herbivores (C1)", "carnivores (C2)", "super-prédateurs (C3)"]
    for i in range(niv):
        cour = cour * 10 // 100
        lignes.append(f"{noms[i]} : {cour} kg")
    return (f"Une prairie porte {b} kg de biomasse végétale. En admettant un rendement "
            f"de 10 % par niveau, calculer la biomasse maximale de {noms[0].split()[0]} "
            "puis des niveaux suivants (" + str(niv) + " niveaux).",
            "\n".join(lignes) + "\n\nÀ chaque niveau, seule ~10 % de l'énergie passe : "
            "d'où des pyramides écologiques décroissantes.",
            "Multiplier successivement par 10/100.")


@reg("SVT", "Les équilibres naturels", (1, 2))
def _svt_desequilibre():
    causes = (("déforestation", "érosion des sols, perte d'habitat, baisse de la nappe"),
              ("surpâturage", "disparition du couvert végétal, désertification"),
              ("rejets d'engrais dans un lac", "eutrophisation, mortalité des poissons"),
              ("braconnage", "disparition des espèces chassées, chaînes trophiques rompues"))
    c, eff = random.choice(causes)
    return (f"Quelles sont les conséquences possibles de {c} sur un écosystème ? "
            "Ce déséquilibre est-il naturel ou humain ? Citer un moyen de lutte.",
            f"Cause HUMAINE.\nConséquences : {eff}.\n"
            "Moyens : aire protégée / reboisement / réglementation / sensibilisation "
            "(au choix selon la cause).",
            "Raisonner en chaîne : cause → dégradation → effets en cascade.")


@reg("SVT", "Les équilibres naturels", 3)
def _svt_parc():
    parcs = (("Souss-Massa", "l'ibis chauve"), ("Toubkal", "le singe magot"),
             ("Ifrane", "le cèdre de l'Atlas"), ("Al Hoceima", "le phoque moindre"))
    p, esp = random.choice(parcs)
    return (f"① Citer un parc national marocain et une espèce qu'il protège (autre que "
            f"{p}). ② Pourquoi crée-t-on des aires protégées ? ③ Citer 2 actions "
            "concrètes de préservation de la nature.",
            "① Ex : Parc national de Souss-Massa → ibis chauve ; Toubkal → magot ; "
            "Ifrane → cèdre.\n② Protéger les espèces menacées ET leurs habitats : "
            "maintenir les équilibres naturels et la biodiversité.\n"
            "③ Reboisement ; lutte contre le braconnage (surveillance) ; épuration des "
            "eaux ; sensibilisation.",
            "Protéger l'espèce = protéger son milieu.")


# ═══════════════════════════════════════ S2 · BOTANIQUE ══
@reg("SVT", "La reproduction sexuée chez les plantes à fleurs", (1, 2))
def _svt_fleur():
    q = random.choice((
        ("Où sont produits les gamètes mâles et femelles d'une fleur ?",
         "Gamètes mâles : dans les ANTHÈRES des étamines (grains de pollen).\n"
         "Gamètes femelles : dans les SACS EMBRYONNAIRES des ovules, à l'intérieur du "
         "carpille."),
        ("Que deviennent l'ovule, l'ovaire et le zygote après la fécondation ?",
         "Ovule fécondé → GRAINE ; ovaire → FRUIT ; zygote (œuf) → EMBRYON de la "
         "nouvelle plante."),
        ("Nommer les pièces florales de l'extérieur vers l'intérieur avec leur rôle.",
         "Sépales (protection) → pétales (attraction) → étamines (pollen) → carpille "
         "(ovules)."),
        ("Distinguer pollinisation et fécondation.",
         "Pollinisation : TRANSPORT du pollen de l'étamine au stigmate (vent, insectes).\n"
         "Fécondation : FUSION des gamètes (tube pollinique → oosphère), dans l'ovule.")))
    return (f"{q[0]}", q[1],
            "Fleur : étamines = mâle, carpille = femelle ; après fécondation : graine + fruit.")


@reg("SVT", "La reproduction sexuée chez les plantes à fleurs", (2, 3))
def _svt_pollinisation():
    mode = random.choice(("vent (anémogame)", "insectes (entomogame)"))
    if "an" in mode:
        car = ("léger, sec, très abondant, petit",
               "fleurs discrètes, étamines saillantes (ex : pin, blé, olivier)")
    else:
        car = ("collant, rugueux, moins abondant",
               "fleurs grandes, colorées, parfumées, avec nectar (ex : rose, pommier)")
    n = random.choice((4, 5, 6, 8))
    return (f"① Caractériser la pollinisation par le {mode} : aspect du pollen et "
            "traits de la fleur. ② Une fleur de pois contient "
            f"{n} ovules : combien de graines maximum après fécondation ? Combien de "
            "fécondations de l'oosphère ?",
            f"① Pollen {car[0]} ; fleur : {car[1]}.\n"
            f"② 1 ovule fécondé → 1 graine : maximum {n} graines, donc {n} fécondations "
            "de l'oosphère (et autant de la cellule centrale : fécondation DOUBLE).",
            "Mode de pollinisation ↔ caractères du pollen et de la fleur.")


@reg("SVT", "La reproduction sexuée chez les plantes sans fleurs", (1, 2))
def _svt_sans_fleurs():
    q = random.choice((
        ("Décrire la reproduction sexuée de la mousse.",
         "Anéridies (mâles) produisent des spermatozoïdes NAGEURS → ils nagent (eau de "
         "pluie) vers l'archégone → fécondation de l'oosphère → sporophyte → SPORES par "
         "méiose → nouvelles mousses.\nL'eau est INDISPENSABLE."),
        ("Décrire le rôle du prothalle chez la fougère.",
         "La spore germe en PROTHALLE (gamétophyte miniature, indépendant) : il porte "
         "anéridies et archégones ; la fécondation y a lieu dans l'eau ; le zygote y "
         "donne le jeune sporophyte (la grande fougère)."),
        ("Pourquoi les plantes sans fleurs vivent-elles en milieux humides ?",
         "Leurs gamètes mâles sont flagellés et doivent NAGER jusqu'au gamète femelle : "
         "sans film d'eau, pas de fécondation (mousses, fougères, algues)."),
        ("Comparaison fougère / pin : deux différences majeures de reproduction.",
         "Fougère : spores + fécondation nécessitant l'eau.\nPin : GRAINES NUES dans des "
         "cônes + pollen par le vent (pas besoin d'eau libre).")))
    return (f"{q[0]}", q[1],
            "Sans fleurs : gamètes nageurs, spores ; l'eau conditionne la fécondation.")


@reg("SVT", "Les cycles de développement des plantes", (1, 2))
def _svt_cycle_n():
    n = random.choice((10, 12, 16, 20, 24, 30))
    plante = random.choice(("mousse", "fougère", "pin", "rosier"))
    gam = "gamétophyte" if plante == "mousse" else "sporophyte"
    return (f"Chez {plante == 'la mousse' and 'une mousse' or 'une ' + plante}, "
            f"la phase {gam} a n = {n} chromosomes. Donner le nombre de chromosomes de : "
            "ses cellules, ses spores, ses gamètes et son zygote.",
            f"Cellules {gam} : n = {n} ; spores : n = {n} (méiose) ; gamètes : n = {n} ; "
            f"zygote : 2n = {2 * n} (fécondation) → donne le sporophyte.",
            "Spores et gamètes = n ; zygote et sporophyte = 2n.")


@reg("SVT", "Les cycles de développement des plantes", 3)
def _svt_cycle_phase():
    return ("① Définir l'alternance des générations. ② Donner la phase dominante chez : "
            "mousse, fougère, plante à fleurs. ③ Où a lieu la méiose chez les plantes ?",
            "① Alternance régulière d'un sporophyte (2n, → spores par méiose) et d'un "
            "gamétophyte (n, → gamètes) : cycle haplodiploïque.\n"
            "② Mousse : GAMÉTOPHYTE dominant ; fougère : sporophyte dominant (prothalle "
            "réduit) ; plante à fleurs : sporophyte exclusif (gamétophytes miniatures "
            "dans la fleur).\n③ Dans les SPORANGES (anthères et ovules) : elle produit "
            "les spores — jamais les gamètes chez les plantes.",
            "Chez les plantes : méiose → spores ; gamètes par mitose du gamétophyte.")


@reg("SVT", "La reproduction asexuée chez les plantes", (1, 2))
def _svt_vegetative():
    modes = (("rhizome", "iris, bambou"), ("tubercule", "pomme de terre"),
             ("bulbe", "oignon, tulipe"), ("stolon", "fraisier"))
    m, ex = random.choice(modes)
    tech = random.choice(("bouture", "marcottage", "greffe"))
    det = {"bouture": "couper un fragment de tige/feuille et le planter : il s'enracine",
           "marcottage": "enterrer une branche SANS la couper, la séparer une fois "
                         "enracinée",
           "greffe": "fixer un greffon (fragment de la variété voulue) sur un "
                     "porte-greffe aux racines vigoureuses"}
    return (f"① Donner un exemple de multiplication naturelle par {m}. ② Décrire la "
            f"technique de {tech}. ③ Les plantes obtenues sont-elles identiques ? "
            "Justifier.",
            f"① {m.capitalize()} : {ex}.\n② {tech.capitalize()} : {det[tech]}.\n"
            "③ OUI : reproduction ASEXUÉE (végétative) → clones, même patrimoine "
            "génétique que la plante-mère.",
            "Asexuée = sans gamètes ni fécondation = clones.")


@reg("SVT", "La reproduction asexuée chez les plantes", 3)
def _svt_greffe_debat():
    nb, par = random.choice(((5, 4), (6, 3), (8, 4)))
    return (f"Un agriculteur plante {nb} tubercules portant chacun {par} bourgeons "
            "viables. ① Combien de plants espérer ? Sont-ils identiques ? ② Quel risque "
            "partagé par une culture entièrement clonée ?",
            f"① {nb} × {par} = {nb * par} plants, TOUS identiques à la plante-mère "
            "(clones).\n② Même patrimoine génétique = même sensibilité aux maladies : "
            "une maladie peut détruire toute la culture (d'où la diversité apportée par "
            "la reproduction sexuée).",
            "Clonage : fidélité + rapidité, mais vulnérabilité commune.")


@reg("SVT", "La modification génétique des plantes", (1, 2))
def _svt_transgenese():
    return ("① Rappeler les étapes de la transgenèse d'une plante. ② Citer un vecteur "
            "de transfert de gène. ③ Donner un exemple d'application agricole.",
            "① Isoler le gène d'intérêt → le transférer dans les cellules de la plante → "
            "régénérer des plantes complètes → sélectionner celles qui expriment le "
            "gène.\n② La bactérie Agrobacterium tumefaciens (ou le canon à "
            "particules).\n③ Maïs Bt résistant aux insectes ; soja tolérant un "
            "herbicide ; riz doré enrichi en provitamine A.",
            "Isoler → transférer → régénérer → sélectionner.")


@reg("SVT", "La modification génétique des plantes", 3)
def _svt_ogm_debat():
    return ("Un maïs transgénique produit lui-même un insecticide. ① S'agit-il d'un OGM ? "
            "Justifier. ② Citer 2 avantages et 2 risques discutés. ③ Un croisement du "
            "maïs avec une variété sauvage donne-t-il un OGM ?",
            "① OUI : son génome a été modifié par l'homme (gène Bt de bactérie inséré par "
            "transgenèse).\n② Avantages : moins d'insecticides chimiques, meilleur "
            "rendement. Risques : dissémination du gène par le pollen, effets sur les "
            "insectes utiles et la biodiversité, dépendance aux semenciers.\n"
            "③ NON : un croisement (hybridation) est un échange naturel de gènes entre "
            "plantes proches — pas un transfert par ingénierie génétique.",
            "OGM = modification par l'homme du génome ; hybridation = croisement naturel.")


@reg("SVT", "La classification des plantes", (1, 2))
def _svt_classer():
    groupes = random.sample(
        [("pin", "gymnosperme (graines nues dans des cônes)"),
         ("rosier", "angiosperme (fleurs, graines dans un fruit)"),
         ("fougère aigle", "fougère (vaisseaux, reproduction par spores)"),
         ("sphaigne", "mousse (sans vaisseaux, milieu humide, spores)"),
         ("laitue de mer", "algue (pas de vrais organes, milieu aquatique)")], 3)
    especes = ", ".join(g[0] for g in groupes)
    sol = "\n".join(f"{g[0]} → {g[1]}" for g in groupes)
    return (f"Classer les plantes suivantes dans leur groupe : {especes}. Justifier "
            "chaque choix par un critère.",
            sol,
            "Critères : vaisseaux ? graines ? nues ou dans un fruit ? fleurs ?")


@reg("SVT", "La classification des plantes", 3)
def _svt_cle():
    return ("Élaborer une clé de détermination simple permettant de classer une plante "
            "inconnue dans : algue, mousse, fougère, conifère, plante à fleurs.",
            "① Vrais organes avec vaisseaux ? NON → ② ; OUI → ③.\n"
            "② Milieu aquatique ? OUI → ALGUE ; NON (milieu humide) → MOUSSE.\n"
            "③ Reproduction par spores ? OUI → FOUGÈRE ; NON (graines) → ④.\n"
            "④ Graines nues (cônes) → CONIFÈRE (gymnosperme) ; graines dans un fruit → "
            "PLANTE À FLEURS (angiosperme).",
            "Clé = questions successives, chaque question sépare un groupe.")


# ════════════════════════════════════════════════════ FRANÇAIS ══
CONNECTEURS = {"CAUSE": ["car", "parce que", "en effet", "puisque"],
               "CONSÉQUENCE": ["donc", "ainsi", "par conséquent", "c'est pourquoi"],
               "ADDITION": ["de plus", "en outre", "d'abord", "ensuite"],
               "OPPOSITION": ["mais", "cependant", "toutefois", "en revanche"],
               "CONCESSION": ["certes", "bien que", "même si"],
               "CONCLUSION": ["en somme", "bref", "finalement"]}


@reg("FR", "Le texte argumentatif", 1)
def _fr_connecteur():
    cat = random.choice(sorted(CONNECTEURS))
    mot = random.choice(CONNECTEURS[cat])
    autres = [c for c in CONNECTEURS[cat] if c != mot]
    if random.random() < 0.5:
        return (f"De quel type logique est le connecteur « {mot} » ? Donner un autre connecteur "
                "du même type.",
                f"« {mot} » exprime la {cat}.\nAutres connecteurs du même type : "
                + ", ".join(autres) + ".",
                "Classer les connecteurs : cause, conséquence, addition, opposition, concession.")
    return (f"Citer 2 connecteurs de {cat} et construire une phrase avec l'un d'eux.",
            "Exemples : " + ", ".join(CONNECTEURS[cat][:2]) + f".\n"
            f"Phrase modèle : « … {CONNECTEURS[cat][0]} … » (la phrase doit relier 2 idées de "
            f"relation logique : {cat.lower()}).",
            "Le connecteur annonce la RELATION entre les deux idées.")


THESES = (("« Le téléphone nuit aux études. Certes, il facilite les recherches, mais il dévore "
           "le temps : les élèves qui l'utilisent 4 h par jour réussissent moins bien. »",
           "Thèse : le téléphone nuit aux études",
           "Antithèse (admise puis rejetée) : « il facilite les recherches » (après « certes »)"),
          ("« Le sport est indispensable. Certes, il prend du temps, mais il améliore la "
           "concentration et la santé : les élèves sportifs sont plus efficaces. »",
           "Thèse : le sport est indispensable",
           "Antithèse : « il prend du temps »"),
          ("« Lire chaque soir développe le vocabulaire. Certes, la télévision informe aussi, "
           "mais elle n'exige aucun effort : le livre reste irremplaçable. »",
           "Thèse : lire chaque soir développe le vocabulaire / le livre est irremplaçable",
           "Antithèse : « la télévision informe aussi »"))


@reg("FR", "Le texte argumentatif", 2)
def _fr_these():
    texte, these, anti = random.choice(THESES)
    return ("Identifier la THÈSE défendue et l'ANTITHÈSE admise :\n" + texte,
            these + "\n" + anti,
            "Ce qui suit « certes » est l'opinion ADVERSE.")


@reg("FR", "Le texte argumentatif", 2)
def _fr_strategie():
    m, rep, eff = random.choice((
        ("l'IMPÉRATIF (« Agissez maintenant ! »)", "persuader",
         "l'impératif pousse à l'action par l'émotion/l'ordre"),
        ("une QUESTION ORATOIRE (« Ne voyons-nous pas chaque jour… ? »)", "persuader",
         "la réponse est évidente : elle implique le lecteur émotionnellement"),
        ("des CHIFFRES (« 80 % des élèves… »)", "convaincre",
         "les données objectives font appel à la raison"),
        ("un ARGUMENT D'AUTORITÉ (« Selon les scientifiques… »)", "convaincre",
         "on s'appuie sur une référence crédible, rationnelle"),
        ("une HYPERBOLE (« un enfer quotidien »)", "persuader",
         "l'exagération frappe l'imagination et l'émotion")))
    return (f"Procédé repéré : {m}. L'auteur cherche-t-il à CONVAINCRE ou à PERSUADER ? "
            "Justifier.",
            f"→ {rep}.\nJustification : {eff}.",
            "Convaincre = raisonner (faits, logique) ; persuader = émouvoir.")


FIGURES = (("« Cette femme est un rayon de soleil. »", "MÉTAPHORE (pas d'outil de comparaison)",
            "image : joie, chaleur"),
           ("« Il est doux comme un agneau. »", "COMPARAISON (outil : « comme »)",
            "douceur comparée à l'agneau"),
           ("« La mer se fâche et fracasse ses vagues. »", "PERSONNIFICATION",
            "la mer agit comme un humain"),
           ("« Je suis mort de fatigue. »", "HYPERBOLE", "exagération volontaire"),
           ("« Il nous a quittés. » (pour « il est mort »)", "EUPHÉMISME", "atténuer la réalité dure"),
           ("« Ce n'est pas mauvais ! » (pour « c'est excellent »)", "LITOTE",
            "dire moins pour suggérer plus"),
           ("« Un mot, une phrase, un discours. »", "GRADATION", "intensité croissante"),
           ("« Il vivait le jour, elle la nuit. »", "ANTITHÈSE", "opposition de deux idées"),
           ("« Les sanglots longs des violons de l'automne » (Verlaine)",
            "ALLITÉRATION en [l]", "sonorités traînantes → langueur, tristesse"))


@reg("FR", "Les figures de style", 1)
def _fr_fig_identifier():
    phrase, fig, eff = random.choice(FIGURES)
    return (f"Identifier la figure de style et son effet : {phrase}",
            f"→ {fig}\nEffet : {eff}.",
            "Toujours nommer la figure ET son effet.")


@reg("FR", "Les figures de style", 2)
def _fr_fig_produire():
    fig, theme, modele, regle = random.choice((
        ("une MÉTAPHORE", "la mer", "« La mer est un miroir d'argent. »",
         "SANS outil de comparaison"),
        ("une COMPARAISON", "l'école", "« L'école est comme un jardin qui fait pousser les "
         "esprits. »", "AVEC un outil (comme, tel, semblable à)"),
        ("une PERSONNIFICATION", "le vent", "« Le vent siffle sa colère dans les fils. »",
         "comportement humain attribué à une chose")))
    return (f"Produire {fig} sur {theme}. Rappel : {regle}.",
            f"Exemple attendu : {modele}\n(Toute production respectant la règle est juste.)",
            f"{fig.split(' ')[1] if len(fig.split(' ')) > 1 else fig} : {regle}.")


@reg("FR", "Le texte narratif", 1)
def _fr_schema():
    recit, rep = random.choice((
        ("« Ali vivait paisiblement. Un matin, sa maison brûla. Il lutta contre les flammes, fut "
         "secouru par ses voisins, puis repeignit sa maison plus solide. »",
         "SI : vie paisible → ÉP : l'incendie → Péripéties : lutte + secours → Dénouement : fin "
         "de l'incendie → SF : maison reconstruite (nouvel équilibre)"),
        ("« Nous pêchions calmement. Soudain, la tempête se leva. Nous luttâmes toute la nuit, "
         "l'esquif tenant bon, et regagnâmes le port au matin, sauvés. »",
         "SI : pêche paisible → ÉP : la tempête → Péripéties : la lutte nocturne → Dénouement : "
         "fin de la tempête → SF : retour au port (sauvés)")))
    return ("Identifier les 5 étapes du schéma narratif :\n" + recit,
            rep, "Chercher d'abord la RUPTURE (élément perturbateur), placer le reste autour.")


@reg("FR", "Le texte narratif", 2)
def _fr_focalisation():
    extrait, rep, ast = random.choice((
        ("« Je sentis mon cœur se serrer : nul ne connaissait ma peine. »",
         "Narrateur PERSONNAGE (« je ») + FOCALISATION INTERNE (on accède à ses émotions)",
         "« je » + intériorité = interne"),
        ("« Il traversa la place sans voir l'ombre qui l'observait du toit. »",
         "FOCALISATION ZÉRO (omnisciente) : le narrateur sait ce que le personnage ignore",
         "narrateur qui en sait PLUS = zéro"),
        ("« L'homme entra, s'assit, commanda un thé. Rien ne laissait paraître ses pensées. »",
         "FOCALISATION EXTERNE : observateur neutre, seules les actions visibles",
         "caméra extérieure = externe")))
    return ("Narrateur et focalisation ?\n" + extrait, rep + "\nAstuce : " + ast,
            "Interne = dans la tête d'UN personnage ; externe = caméra ; zéro = tout savoir.")


@reg("FR", "Le texte narratif", 2)
def _fr_temps_recit():
    v1, v2 = random.choice((("marchais", "a sonné"), ("lisais", "a frappé"),
                            ("cuisinais", "est arrivé"), ("jouais", "s'est mis à pleuvoir")))
    return (f"Justifier les temps : « Je {v1} tranquillement quand soudain quelqu'un {v2}. »",
            f"« {v1} » : IMPARFAIT → action durative, arrière-plan (le cadre)\n"
            f"« {v2} » : PASSÉ COMPOSÉ → action ponctuelle qui INTERROMPT (l'événement)\n"
            "Structure type : imparfait du cadre + passé composé de l'incident.",
            "Durée/décor = imparfait ; fait nouveau et ponctuel = passé composé.")


PORTRAITS = (("« Élancé, le regard perçant, il semblait défier le monde. »",
              "physique (élancé) + moral (regard perçant) — ton MÉLIORATIF"),
             ("« Petite, mesquine, elle rongeait son frein en jalousant tout le monde. »",
              "physique + moral — ton PÉJORATIF (portrait satirique)"),
             ("« Ses yeux doux rassuraient les enfants ; sa patience semblait sans limite. »",
              "moral (douceur, patience) — ton MÉLIORATIF"))


@reg("FR", "Le texte descriptif", 1)
def _fr_portrait():
    extrait, rep = random.choice(PORTRAITS)
    return ("Portrait physique, moral, ou les deux ? Quel ton ?\n" + extrait,
            "→ " + rep + ".", "Portrait = physique (apparence) + moral (caractère).")


EXPANSIONS = {"maison": {"adj": "une maison ancienne", "cn": "une maison de campagne",
                         "rel": "une maison qui surplombe l'oued",
                         "tout": "une maison ancienne, de campagne, qui surplombe l'oued"},
              "chat": {"adj": "un chat noir", "cn": "un chat du voisin",
                       "rel": "un chat qui ronronne sans cesse",
                       "tout": "un chat noir, du voisin, qui ronronne sans cesse"},
              "mer": {"adj": "une mer immense", "cn": "une mer d'un bleu profond",
                      "rel": "une mer qui bordait la baie",
                      "tout": "une mer immense, d'un bleu profond, qui bordait la baie"},
              "arbre": {"adj": "un arbre majestueux", "cn": "un arbre de la cour",
                        "rel": "un arbre qui donne de l'ombre",
                        "tout": "un arbre majestueux, de la cour, qui donne de l'ombre"},
              "rue": {"adj": "une rue étroite", "cn": "une rue de la médina",
                      "rel": "une rue qui mène au souk",
                      "tout": "une rue étroite, de la médina, qui mène au souk"}}


@reg("FR", "Le texte descriptif", 2)
def _fr_expansion():
    nom = random.choice(sorted(EXPANSIONS))
    d = EXPANSIONS[nom]
    typ, cle = random.choice((("un ADJECTIF qualificatif", "adj"),
                              ("un COMPLÉMENT du nom", "cn"),
                              ("une PROPOSITION RELATIVE", "rel")))
    return (f"Enrichir « {d['adj'].split(' ')[1]} » (le nom) avec {typ}, puis cumuler les 3 "
            "expansions du nom.",
            f"Exemple avec {typ} : « {d[cle]} »\n"
            f"Cumul complet : « {d['tout']} »",
            "3 expansions possibles : adjectif + complément du nom + relative.")


@reg("FR", "Le texte descriptif", 1)
def _fr_organisateurs():
    texte, rep = random.choice((
        ("« À droite s'étendait une plage ; au fond, la baie ; autour, nulle âme. »",
         "organisateurs spatiaux : « à droite », « au fond », « autour » (imparfaits de "
         "description aussi)"),
        ("« Devant la porte, un vieux marchand ; derrière lui, des étals alignés ; entre les "
         "deux, un flot de clients. »",
         "organisateurs spatiaux : « devant », « derrière », « entre »")))
    return ("Relever les organisateurs spatiaux :\n" + texte, rep,
            "Organisateurs spatiaux : devant, derrière, à droite, au fond, autour, entre…")


EXPLICATIFS = (("« La sécheresse, c'est-à-dire un manque prolongé de pluie, appauvrit les sols "
                "parce que la végétation disparaît ; si bien que l'érosion s'accélère. »",
                "définition (« c'est-à-dire ») + cause (« parce que ») + conséquence "
                "(« si bien que »)"),
               ("« La photosynthèse, c'est-à-dire la fabrication de matière organique par les "
                "plantes, se produit grâce à la lumière : ainsi les feuilles transforment l'eau "
                "et le CO₂. »",
                "définition + cause (« grâce à ») + conséquence (« ainsi ») + présent de vérité "
                "générale (« se produit »)"))


@reg("FR", "Le texte explicatif", 1)
def _fr_marques():
    texte, rep = random.choice(EXPLICATIFS)
    return ("Relever : une définition, un connecteur de CAUSE, un connecteur de CONSÉQUENCE :\n"
            + texte, rep, "Chaîne logique : définition → cause → effet.")


POLARITES = (("les plantes poussent", "le soleil", "grâce à"),
             ("les récoltes ont échoué", "la sécheresse", "à cause de"),
             ("il a réussi son examen", "un travail régulier", "grâce à"),
             ("la route était bloquée", "une inondation", "à cause de"),
             ("l'équipe a gagné", "l'entraînement intensif", "grâce à"),
             ("les arbres sont morts", "la pollution", "à cause de"))


@reg("FR", "Le texte explicatif", 2)
def _fr_cause():
    evt, cause, bon = random.choice(POLARITES)
    return (f"Compléter avec « grâce à » ou « à cause de » : « {evt.capitalize()} "
            f"___ {cause}. » Justifier.",
            f"→ « {evt} {bon} {cause} »\nJustification : « {cause} » est un élément "
            f"{'FAVORABLE → grâce à' if bon == 'grâce à' else 'DÉFAVORABLE → à cause de'}.",
            "grâce à = cause favorable ; à cause de = cause défavorable.")


@reg("FR", "Le texte explicatif", 2)
def _fr_exp_vs_arg():
    texte, rep = random.choice((
        ("« Le tabac tue ; les publicités séduisantes devraient être interdites ; c'est une "
         "évidence. »", "ARGUMENTATIF : opinion (« devraient », « évidence »), jugement de "
         "valeur, but = convaincre"),
        ("« Le tabac contient de la nicotine, substance qui crée une dépendance : c'est-à-dire "
         "que le fumeur ressent un besoin irrésistible. »",
         "EXPLICATIF : définition, présent de vérité, neutralité, but = faire comprendre")))
    return ("Explicatif ou argumentatif ? Justifier par 2 indices :\n" + texte,
            rep, "Opinion présente = argumentatif ; neutralité + définitions = explicatif.")


@reg("FR", "Le résumé de texte", 1)
def _fr_resume_regles():
    q, rep = random.choice((
        ("Quelle est la longueur cible d'un résumé ?", "Environ 1/4 du texte original "
         "(sauf consigne contraire)."),
        ("Citer 4 catégories d'informations SUPPRIMABLES dans un résumé.",
         "Les exemples illustratifs, les répétitions, les citations, les chiffres/détails "
         "secondaires."),
        ("Citer 2 INTERDITS du résumé.", "Donner son opinion personnelle ; recopier des phrases "
         "entières du texte (il faut reformuler)."),
        ("Quelle est la démarche complète du résumé en 4 étapes ?",
         "① Lire 2 fois (global puis précis) ② Découper en paragraphes et relever l'idée "
         "principale de chacun ③ Rédiger en enchaînant avec des connecteurs ④ Vérifier fidélité "
         "et proportion.")))
    return (q, rep, "Résumer = l'essentiel, avec ses mots, sans opinion.")


CONDENSE = ((["chaise", "table", "armoire"], "le mobilier"),
            (["lion", "tigre", "chat"], "les félins (ou : les animaux)"),
            (["rouge", "bleu", "vert"], "les couleurs"),
            (["tristesse", "joie", "colère"], "les émotions/sentiments"),
            (["marcher", "courir", "nager"], "les déplacements (verbes de mouvement)"))


@reg("FR", "Le résumé de texte", 2)
def _fr_condenser():
    liste, general = random.choice(CONDENSE)
    return (f"Condenser par généralisation : « {', '.join(liste)} » → un mot ?",
            f"→ {general}.",
            "Généraliser : remplacer une énumération par le terme englobant.")


SUB = {"relative": ["le livre que tu m'as prêté", "la fille qui chante juste",
                    "le joueur dont l'équipe a gagné"],
       "complétive": ["je pense que tu réussiras", "elle sait que nous viendrons",
                      "il croit que tout est perdu"],
       "circonstancielle de temps": ["quand la pluie cessa", "dès que le car arriva",
                                     "avant que le soleil se lève"],
       "circonstancielle de cause": ["parce qu'il était en retard", "puisqu'il pleut",
                                     "comme la route était fermée"],
       "circonstancielle de condition": ["si tu travailles", "à condition que tu viennes"]}


@reg("FR", "Les propositions subordonnées", 1)
def _fr_nature_sub():
    nature = random.choice(sorted(SUB))
    sub = random.choice(SUB[nature])
    fonction = {"relative": "complément de l'antécédent (le nom qui précède)",
                "complétive": "COD du verbe principal",
                "circonstancielle de temps": "complément circonstanciel de temps",
                "circonstancielle de cause": "complément circonstanciel de cause",
                "circonstancielle de condition": "complément circonstanciel de condition"}[nature]
    return (f"Nature et fonction de la subordonnée : « {sub} » ?",
            f"Nature : {nature}.\nFonction : {fonction}.",
            "Relative → pronom relatif + antécédent ; complétive → que + verbe complété ; "
            "circonstancielle → quand/parce que/si…")


@reg("FR", "Les propositions subordonnées", 2)
def _fr_que_rel_conj():
    rep_rel, rep_conj = random.choice((
        (("le gâteau que tu as fait", "pronom RELATIF (antécédent : le gâteau)"),
         ("je sais que tu viens", "conjonction (complète le verbe « sais », pas d'antécédent)")),))
    return ("« que » : pronom relatif ou conjonction ? Distinguer :\n"
            f"① « {rep_rel[0]} »\n② « {rep_conj[0]} »",
            f"① « que » = {rep_rel[1]}\n② « que » = {rep_conj[1]}",
            "Antécédent présent → relatif ; verbe complété → conjonction.")


@reg("FR", "Les propositions subordonnées", 3)
def _fr_analyse_complete():
    conj, p, rel = random.choice((("Lorsque", "les voyageurs", "qui attendaient depuis l'aube"),
                                  ("Quand", "les enfants", "qui jouaient dehors"),
                                  ("Dès que", "les élèves", "qui étaient en rang")))
    verbe = random.choice(("poussèrent un soupir de soulagement", "acclamèrent", "se précipitèrent"))
    return (f"Analyser complètement : « {conj} le {random.choice(('car', 'train', 'bus'))} arriva, "
            f"{p} {rel} {verbe}. »",
            f"• « {conj} … arriva » : circonstancielle de TEMPS\n"
            f"• Principale : « {p} {verbe} »\n"
            f"• « {rel} » : relative (antécédent : {p})\n"
            "Valeurs : passé simple = actions ; imparfait = durée/arrière-plan",
            "Toujours : principale + subordonnées + valeurs des temps.")


POLYSEMIE = {"une feuille": ["de papier (page)", "de vigne (organe de la plante)",
                             "de présence (registre)"],
             "une opération": ["chirurgicale (médecine)", "bancaire (calcul/compte)",
                               "militaire (action stratégique)"],
             "une carte": ["de géographie", "de restaurant (menu)", "à jouer"],
             "une batterie": ["de cuisine (ustensiles)", "de musique (instrument)",
                              "de téléphone (accumulateur)"]}


@reg("FR", "Le lexique : sens et nuances", 1)
def _fr_polysemie():
    mot = random.choice(sorted(POLYSEMIE))
    sens = POLYSEMIE[mot]
    return (f"« {mot} » est polysémique. Donner 3 sens différents et expliquer pourquoi le "
            "contexte est décisif.",
            "Sens possibles :\n" + "\n".join(f"• {mot} {s}" for s in sens)
            + "\nLe CONTEXTE (mots voisins, phrase) choisit le bon sens.",
            "Un mot, plusieurs sens : c'est le contexte qui tranche.")


CONNOT = (("maigre / frêle", "« frêle » est MÉLIORATIF (fragilité attendrissante) ; « maigre » "
           "neutre ou péjoratif"),
          ("têtu / persévérant", "« persévérant » est MÉLIORATIF (qualité) ; « têtu » PÉJORATIF "
           "(défaut)"),
          ("économe / radin", "« économe » est MÉLIORATIF (sage) ; « radin » PÉJORATIF "
           "(avarice moquée)"))


@reg("FR", "Le lexique : sens et nuances", 2)
def _fr_connotation():
    paire, rep = random.choice(CONNOT)
    return (f"« {paire.split(' / ')[0]} » vs « {paire.split(' / ')[1]} » : sens dénoté proche, "
            "mais quelle différence de CONNOTATION ?",
            rep + ".",
            "Synonymes ≠ nuances : la connotation (méliorative/péjorative) change l'effet.")


CHAMPS = {"la mer": ["vagues", "port", "marin", "sel", "tempête"],
          "l'école": ["cahier", "maître", "leçon", "classe", "récréation"],
          "la peur": ["frisson", "trembler", "angoisse", "fuir", "cauchemar"],
          "la guerre": ["soldat", "bataille", "arme", "tranchée", "ennemi"]}


@reg("FR", "Le lexique : sens et nuances", 1)
def _fr_champ_lexical():
    theme = random.choice(sorted(CHAMPS))
    mots = CHAMPS[theme]
    intru = random.choice(("frein", "cahier" if theme != "l'école" else "ancre",
                           "nuage", "fourchette"))
    serie = mots[:4] + [intru]
    random.shuffle(serie)
    return (f"Repérer l'INTRUS et nommer le champ lexical des 4 autres : "
            + ", ".join(serie) + ".",
            f"Intrus : « {intru} »\nChamp lexical : {theme} (mots : {', '.join(mots[:4])})",
            "Champ lexical = mots liés au même thème, toutes classes confondues.")


@reg("FR", "Les valeurs des temps verbaux", 1)
def _fr_valeur_present():
    ex, val = random.choice((
        ("« L'eau bout à 100 °C »", "présent de VÉRITÉ GÉNÉRALE (fait permanent/scientifique)"),
        ("« Chaque matin, je me lève à 6 h »", "présent d'HABITUDE (répétition)"),
        ("« Il neige ! »", "présent d'ÉNONCIATION (action en cours au moment où l'on parle)"),
        ("« La Terre tourne autour du Soleil »", "présent de VÉRITÉ GÉNÉRALE"),
        ("« Nous déjeunons à midi chaque jour »", "présent d'HABITUDE")))
    return (f"Quelle valeur du présent ?\n{ex}", f"→ {val}.",
            "3 valeurs majeures : vérité générale, habitude, action en cours.")


@reg("FR", "Les valeurs des temps verbaux", 2)
def _fr_imparfait_pc():
    phrase, rep = random.choice((
        ("« Tous les étés, nous allions à Agadir. »",
         "IMPARFAIT d'HABITUDE (répétition dans le passé : « tous les étés »)"),
        ("« Elle a cassé son téléphone hier. »",
         "PASSÉ COMPOSÉ : action PONCTUELLE et achevée, datée"),
        ("« Il pleuvait sans arrêt ce jour-là. »",
         "IMPARFAIT de DESCRIPTION/durée (arrière-plan)"),
        ("« Le train était parti quand il est arrivé. »",
         "PLUS-QUE-PARFAIT : action ANTÉRIEURE à un autre passé")))
    return (f"Identifier le temps et sa valeur :\n{phrase}", f"→ {rep}.",
            "Habitude/durée = imparfait ; fait ponctuel = passé composé ; antériorité = "
            "plus-que-parfait.")


@reg("FR", "Les valeurs des temps verbaux", 3)
def _fr_futur_cond():
    phrase, rep = random.choice((
        ("« Dès que tu auras signé, tu recevras la clé. »",
         "« auras signé » = FUTUR ANTÉRIEUR (achevé AVANT une action future) ; "
         "« recevras » = futur simple"),
        ("« Selon la météo, il ferait beau demain. »",
         "CONDITIONNEL : information NON CONFIRMÉE (rapportée, hypothèse)"),
        ("« Quand il aurait fini, elle partirait. » (récit)",
         "conditionnel = FUTUR DU PASSÉ (vue depuis un passé)")))
    return (f"Analyser les temps et leurs valeurs :\n{phrase}", f"→ {rep}.",
            "Futur antérieur = 1ʳᵉ action de deux futurs ; conditionnel = incertitude.")
