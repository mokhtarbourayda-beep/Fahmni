# -*- coding: utf-8 -*-
"""gen_svt_fr.py — Générateurs DYNAMIQUES de SVT et Français (TC).
Importé par gen_exercices.py : enregistre ses modèles via reg()."""

import random
from fractions import Fraction as F

from gen_exercices import reg, fmt

# ══════════════════════════════════════════════════════════ SVT ══
MICRO = ((100, 50), (200, 20), (400, 10), (400, 50), (1000, 5),
         (200, 100), (400, 120), (1000, 20), (100, 200))


@reg("SVT", "La cellule, unité de la vie", 2)
def _svt_micro():
    g, reel = random.choice(MICRO)
    obs = g * reel // 1000         # mm observés (entier)
    return (f"Observée au microscope au grossissement ×{g}, une cellule mesure "
            f"{obs} mm sur la photo. Calculer sa taille réelle en µm.",
            f"Taille réelle = taille observée ÷ grossissement\n"
            f"= {obs} mm ÷ {g} = {fmt(F(reel))} µm",
            "Convertir le résultat mm → µm (× 1000).")


@reg("SVT", "La cellule, unité de la vie", 1)
def _svt_conversions():
    val, u, micro, nano = random.choice(
        (("0,02 mm", "0,02", "20", "20 000"), ("0,15 mm", "0,15", "150", "150 000"),
         ("20 µm", "20", "20", "20 000"), ("5 µm", "5", "5", "5 000"),
         ("250 µm", "250", "250", "250 000")))
    return (f"Une cellule mesure {val}. Exprimer sa taille en µm PUIS en nm "
            "(1 mm = 1000 µm ; 1 µm = 1000 nm).",
            f"• En micromètres : {micro} µm\n• En nanomètres : {nano} nm",
            "mm → µm : ×1000 ; µm → nm : ×1000.")


@reg("SVT", "La cellule, unité de la vie", 1)
def _svt_structures():
    q, rep, ast = random.choice((
        ("Citer 3 structures présentes dans une cellule VÉGÉTALE mais absentes d'une cellule animale.",
         "La paroi cellulosique (rigidité), les chloroplastes (photosynthèse) et la grande vacuole "
         "centrale (réserve d'eau).", "Le trio végétal : paroi + chloroplastes + vacuole."),
        ("Citer 3 structures communes aux cellules animale ET végétale.",
         "La membrane plasmique, le cytoplasme et le noyau (ainsi que les mitochondries).",
         "Le socle commun des cellules eucaryotes."),
        ("Qu'est-ce qui distingue une cellule PROCARYOTE d'une cellule eucaryote ?",
         "Le procaryote (bactéries) n'a PAS de noyau (ADN libre dans le cytoplasme) ni "
         "d'organites membranaires ; l'eucaryote a un noyau délimité par une enveloppe.",
         "Pas de noyau = procaryote."),
        ("Quelle est la fonction des mitochondries ? Et des chloroplastes ?",
         "Mitochondries → respiration cellulaire (libèrent l'énergie) ; chloroplastes → "
         "photosynthèse (fabriquent la matière organique avec la lumière).",
         "Énergie = mitochondrie ; fabrication avec lumière = chloroplaste.")))
    return (q, rep, ast)


@reg("SVT", "Biodiversité et classification", 1)
def _svt_facteurs():
    banc = {"la température": "abiotique", "la prédation": "biotique",
            "la pluviométrie": "abiotique", "la compétition": "biotique",
            "la salinité du sol": "abiotique", "la pollinisation": "biotique",
            "la lumière": "abiotique", "l'action humaine": "biotique",
            "la nature du sol": "abiotique", "la symbiose": "biotique"}
    items = random.sample(sorted(banc), 5)
    abio = [i for i in items if banc[i] == "abiotique"]
    bio = [i for i in items if banc[i] == "biotique"]
    return ("Classer ces facteurs écologiques en ABIOTIQUES / BIOTIQUES :\n"
            + "\n".join(f"• {i}" for i in items),
            "Abiotiques (non vivants) : " + ", ".join(abio) + "\n"
            "Biotiques (liés aux êtres vivants) : " + ", ".join(bio),
            "Abiotique = élément physique du milieu ; biotique = interaction avec le vivant.")


ESPECES = [("Panthera", "leo", "lion"), ("Panthera", "tigris", "tigre"),
           ("Felis", "catus", "chat domestique"), ("Quercus", "suber", "chêne-liège"),
           ("Quercus", "rotundifolia", "chêne vert"), ("Pinus", "halepensis", "pin d'Alep"),
           ("Giraffa", "camelopardalis", "girafe")]


@reg("SVT", "Biodiversité et classification", 2)
def _svt_nomenclature():
    genres = {}
    for g, e, n in ESPECES:
        genres.setdefault(g, []).append((e, n))
    genre = random.choice([g for g, l in genres.items() if len(l) >= 2])
    (e1, n1), (e2, n2) = random.sample(genres[genre], 2)
    autre = random.choice([x for x in ESPECES if x[0] != genre])
    return (f"{genre} {e1} ({n1}) et {genre} {e2} ({n2}) ; {autre[0]} {autre[1]} ({autre[2]}). "
            "Que déduire des noms scientifiques ?",
            f"• {n1} et {n2} : même GENRE ({genre}) → très proches (ressemblances fortes)\n"
            f"• {autre[2]} : genre différent ({autre[0]}) → parenté plus éloignée\n"
            "Le binôme de Linné (Genre espèce) reflète la classification.",
            "Même genre = grands-parents communs dans l'arbre de classification.")


RANGS = ["embranchement", "classe", "ordre", "famille", "genre", "espèce"]


@reg("SVT", "Biodiversité et classification", 2)
def _svt_hierarchie():
    sous = sorted(random.sample(RANGS, 4), key=RANGS.index)
    melange = sous[:]
    while melange == sous:
        random.shuffle(melange)
    return ("Remettre dans l'ordre hiérarchique (du plus grand au plus précis) : "
            + " > ".join(melange) + ".",
            " > ".join(sous),
            "Mémo : « Embrasse Claude Ou Franchement Georges Espère ».")


@reg("SVT", "L'origine de la biodiversité", 2)
def _svt_etapes():
    etapes = ["Une mutation aléatoire modifie l'ADN d'un individu",
              "Le nouvel allèle se transmet à la descendance",
              "Le milieu sélectionne les individus les mieux adaptés",
              "L'allèle favorable devient majoritaire dans la population"]
    melange = etapes[:]
    while melange == etapes:
        random.shuffle(melange)
    lettres = "ABCD"
    return ("Remettre dans l'ordre logique de l'évolution :\n"
            + "\n".join(f"{lettres[i]}) {e}" for i, e in enumerate(melange)),
            " → ".join(f"{lettres[etapes.index(e)]}) {e}" for e in etapes),
            "La mutation CRÉE (hasard) ; le milieu TRI (sélection) ; la population évolue.")


@reg("SVT", "L'origine de la biodiversité", 3)
def _svt_antibio():
    ab = random.choice(("la pénicilline", "l'amoxicilline", "l'érythromycine"))
    return (f"Après des années d'utilisation de {ab}, certaines bactéries y résistent. "
            "Expliquer en 4 étapes (sélection naturelle).",
            f"① Des mutations ALÉATOIRES rendent quelques bactéries résistantes\n"
            f"② {ab.capitalize()} tue les sensibles, épargne les résistantes (pression de sélection)\n"
            "③ Les résistantes se multiplient sans compétition\n"
            "④ La population devient résistante : l'antibiotique est inefficace",
            "L'antibiotique NE CRÉE PAS la résistance : il la SÉLECTIONNE.")


@reg("SVT", "L'origine de la biodiversité", 1)
def _svt_preuves():
    p, ex = random.choice((
        ("les FOSSILES", "les séries évolutives du cheval ou des cétacés"),
        ("l'ANATOMIE comparée", "le même plan du membre antérieur chez l'humain, la chauve-souris "
                                "et la baleine"),
        ("l'EMBRYOLOGIE comparée", "les embryons de vertébrés très semblables aux premiers stades")))
    return (f"Citer une preuve de l'évolution parmi les traces du passé et donner un exemple.",
            f"Preuve : {p}\nExemple : {ex}.",
            "3 familles de preuves : fossiles, anatomie, embryologie.")


EROSIONS = (("un bloc de granite éclaté en haute montagne où l'eau gèle la nuit",
             "érosion MÉCANIQUE", "le gel fissure et fragmente la roche (+9 % de volume en "
             "gelant)"),
            ("une eau de source claire qui contient du calcaire dissous",
             "érosion CHIMIQUE", "l'eau légèrement acide DISSOUT la roche calcaire (ions invisibles)"),
            ("des galets bien ronds au fond d'un oued", "érosion MÉCANIQUE (transport)",
             "les frottements mutuels pendant le transport polissent les galets"),
            ("des roches polies et des dunes dans le désert", "érosion MÉCANIQUE (vent)",
             "le vent ponce les roches (corrasion) et déplace le sable"),
            ("une falaise attaquée par les vagues", "érosion MÉCANIQUE (vagues)",
             "le choc répété des vagues arrache des fragments de falaise"),
            ("une grotte creusée dans un massif calcaire", "érosion CHIMIQUE",
             "dissolution lente du calcaire par les eaux acides"))


@reg("SVT", "L'érosion : l'action de l'eau sur les roches", 2)
def _svt_type_erosion():
    sit, typ, just = random.choice(EROSIONS)
    return (f"Identifier le type d'érosion : {sit}. Justifier.",
            f"→ {typ}\nJustification : {just}.",
            "Fragmentation/débbris visibles = mécanique ; ions dissous/grottes = chimique.")


AGENTS = {"le gel": "éboulis et roches éclatées en haute montagne",
          "l'eau courante": "vallées en V et galets arrondis",
          "le vent": "roches polies (corrasion) et dunes de sable",
          "les vagues": "falaises rongées et plateformes d'abrasion",
          "l'humain": "érosion accélérée après déforestation (ruissellement)"}


@reg("SVT", "L'érosion : l'action de l'eau sur les roches", 1)
def _svt_agents():
    agent = random.choice(sorted(AGENTS))
    autres = [a for a in AGENTS if a != agent]
    intru = random.choice(autres)
    return (f"Quel agent d'érosion laisse cette trace : « {AGENTS[agent]} » ? "
            f"(Attention : un des propos est un piège, « {intru} » est possible mais pas ici)",
            f"→ {agent}.",
            "Chaque agent a sa signature : relis le paysage décrit.")


@reg("SVT", "L'érosion : l'action de l'eau sur les roches", 1)
def _svt_transport():
    mode, det = random.choice((
        ("par SUSPENSION", "les particules fines (argiles) restent en suspension → eau trouble"),
        ("par SALTATION", "les grains de sable progressent par petits sauts sur le fond"),
        ("par ROULISSEMENT", "les galets roulent sur le fond et se polissent mutuellement")))
    return (f"Décrire le transport {mode} dans un cours d'eau.",
            det + "\nPlus le courant ralentit, plus les gros éléments se déposent (tri par taille).",
            "Fines → suspension ; sable → saltation ; galets → roulissement.")


ROCHES = (("des galets (> 2 mm) soudés", "un CONGLOMÉRAT (poudingue)"),
          ("des grains de sable", "un GRÈS"),
          ("des particules d'argile très fines", "une ARGILITE (ou marnes si + calcaire)"),
          ("des débris de coquilles", "un CALCAIRE ORGANOGÈNE"))


@reg("SVT", "La sédimentation et les roches sédimentaires", 1)
def _svt_roche():
    sed, roc = random.choice(ROCHES)
    sens = random.random() < 0.5
    if sens:
        return (f"Quelle roche sédimentaire se forme à partir de {sed} (après diagenèse) ?", roc,
                "Galets → conglomérat ; sable → grès ; argile → argilite ; coquilles → calcaire.")
    return (f"De quel sédiment provient {roc} ?", sed,
            "Grain = sédiment ; roche = sédiment consolidé par la diagenèse.")


@reg("SVT", "La sédimentation et les roches sédimentaires", 2)
def _svt_falaise():
    fm, ft = (random.choice(("des ammonites", "des oursins fossiles", "des coquilles marines")),
              random.choice(("des os de mammifères", "du pollen terrestre", "des feuilles fossiles")))
    return (f"Une falaise montre 3 couches horizontales : couche 1 (en bas) contient {fm}, "
            f"la couche 2 est sableuse, la couche 3 (en haut) contient {ft}. "
            "Reconstituer l'histoire du lieu.",
            "Superposition : couche 1 la plus ANCIENNE, couche 3 la plus récente.\n"
            f"① Couche 1 ({fm}) → dépôt en milieu MARIN : la mer occupait le lieu\n"
            "② Couche 2 sableuse → littoral (plage)\n"
            f"③ Couche 3 ({ft}) → milieu TERRESTRE : la mer s'est retirée (régression)\n"
            "Histoire : mer → littoral → terre.",
            "Fossiles = milieu ; superposition = chronologie.")


@reg("SVT", "La sédimentation et les roches sédimentaires", 2)
def _svt_diagenese():
    ciment = random.choice(("la calcite", "la silice"))
    return (f"Définir la diagenèse et citer ses 2 mécanismes principaux. Quel ciment si c'est "
            f"{ciment} qui soude les grains ?",
            "Diagenèse = passage du sédiment meuble à la roche cohérente.\n"
            "① COMPACTATION : le poids des couches supérieures tasse le sédiment et chasse l'eau\n"
            f"② CIMENTATION : des minéraux dissous ({ciment}) précipitent entre les grains et les "
            "soudent.",
            "Tasser + coller = diagenèse.")


@reg("SVT", "La formation des sols", 1)
def _svt_profil():
    niveaux = ["horizon A (litière + humus sombre)", "horizon B (minéral fin, argiles)",
               "horizon C (roche-mère altérée)", "roche saine"]
    melange = niveaux[:]
    while melange == niveaux:
        random.shuffle(melange)
    return ("Remettre dans l'ordre (de la SURFACE vers la PROFONDEUR) :\n"
            + "\n".join(f"{chr(65 + i)}) {n}" for i, n in enumerate(melange)),
            " → ".join(f"{chr(65 + niveaux.index(n))}) {n}" for n in niveaux),
            "A organique → B minéral → C altéré → roche saine.")


@reg("SVT", "La formation des sols", (2, 3))
def _svt_vitesse():
    x = random.choice((100, 200, 250, 400))
    e = random.choice((1, 2, 5))
    taux = F(10, x)                       # mm/an de formation
    rapport = F(e) / taux                 # érosion / formation
    return (f"Un sol se forme à raison de 1 cm tous les {x} ans. Après un défrichement, "
            f"l'érosion emporte {e} mm par an. Comparer formation et érosion.",
            f"Formation : 1 cm = 10 mm en {x} ans → {fmt(taux)} mm/an\n"
            f"Érosion : {e} mm/an → l'érosion est {fmt(rapport)} fois PLUS RAPIDE que la formation\n"
            f"Conclusion : le sol est une ressource QUASI NON RENOUVELABLE (il faudrait {x} ans "
            "pour reconstituer 1 cm).",
            "Convertir 1 cm = 10 mm avant de diviser.")


@reg("SVT", "La formation des sols", 2)
def _svt_acteurs():
    org, role = random.choice((
        ("les LICHENS pionniers", "ils attaquent chimiquement la roche nue et produisent les "
         "premières particules"),
        ("les VÉGÉTAUX", "ils apportent la litière (futur humus) et leurs racines fragmentent et "
         "retiennent le sol"),
        ("les VERS DE TERRE", "ils brassent, aèrent et mélangent la matière organique aux "
         "particules minérales"),
        ("les DÉCOMPOSEURS (bactéries, champignons)", "ils transforment la litière morte en humus")))
    return (f"Quel est le rôle des {org.replace('les ', '', 1)} dans la formation d'un sol ?",
            role + ".", "Sans êtres vivants : des débris minéraux, mais pas de sol.")


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
