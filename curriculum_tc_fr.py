# -*- coding: utf-8 -*-
"""
curriculum_tc_fr.py — Programme COMPLET de Français du Tronc Commun (programme
officiel marocain) : typologie des textes (narratif, descriptif, explicatif,
argumentatif), figures de style, résumé, grammaire (subordonnées), lexique,
valeurs des temps verbaux.

Chapitres existants enrichis + nouveaux chapitres + exercices de tous types.
"""

L_ARGUMENTATIF = {
    "intro": "Le texte argumentatif défend une THÈSE (une opinion) à l'aide "
             "d'arguments soutenus par des exemples. On le rencontre dans l'essai, "
             "l'éditorial, le discours, la critique.",
    "methodes": [
        {"nom": "Méthode 1 — reconnaître la structure",
         "texte": "Thèse (ce que l'auteur défend) → arguments (raisons qui la "
                  "soutiennent) → exemples (preuves concrètes). Parfois une "
                  "antithèse (opinion adverse) puis sa réfutation. Demande-toi "
                  "toujours : QUELLE opinion ? avec QUELS arguments ?"},
        {"nom": "Méthode 2 — repérer les connecteurs logiques",
         "texte": "CAUSE : car, parce que, en effet, puisque. CONSÉQUENCE : donc, "
                  "ainsi, par conséquent, c'est pourquoi. ADDITION : de plus, "
                  "en outre, d'abord, ensuite. OPPOSITION : mais, cependant, "
                  "toutefois, en revanche, néanmoins. CONCESSION/ADMISSION : certes, "
                  "il est vrai que. CONCLUSION : en somme, bref, finalement."},
        {"nom": "Méthode 3 — identifier les stratégies argumentatives",
         "texte": "L'auteur peut : convaincre (logique, faits, chiffres — argument "
                  "d'autorité, argument par l'exemple) ; persuader (émotions, "
                  "questions oratoires, impératifs, hyperboles) ; délibérer "
                  "(peser le pour et le contre). Les modalisateurs (peut-être, "
                  "certainement, il semble) nuancent l'affirmation."},
    ],
    "exemples": [
        {"question": "« Le téléphone nuit aux études. Certes, il facilite les "
                     "recherches, mais il dévore le temps : les élèves consultants "
                     "leurs écrans 4 h par jour réussissent moins bien. » Identifier "
                     "thèse, antithèse, argument + exemple.",
         "etapes": ["Thèse : le téléphone nuit aux études",
                    "Antithèse (admission) : « Certes, il facilite les recherches »",
                    "Opposition : « mais » ; Argument : il dévore le temps",
                    "Exemple chiffré : 4 h/jour ↔ moins bons résultats"],
         "reponse": "Structure complète en 4 éléments, avec modalisation par les chiffres."},
    ],
    "pieges": [
        "L'opinion de l'auteur se trouve dans la THÈSE, pas dans les exemples.",
        "Un exemple n'est pas un argument : l'un illustre, l'autre justifie.",
        "« Certes... mais » : ce qui suit « certes » est l'opinion ADVERSE !",
    ],
    "formules": ["texte argumentatif = thèse + arguments + exemples (+ antithèse)",
                 "convaincre = raisonner ; persuader = émouvoir"],
}

L_NARRATIF = {
    "intro": "Le texte narratif raconte une histoire : événements enchaînés dans le "
             "temps, personnages, point de vue du narrateur. Roman, nouvelle, conte, "
             "fable — mais aussi récit d'actualité.",
    "methodes": [
        {"nom": "Méthode 1 — reconstituer le schéma narratif",
         "texte": "5 étapes : SITUATION INITIALE (équilibre) → ÉLÉMENT "
                  "PERTURBATEUR (déséquilibre) → PÉRIPÉTIES (actions, complications) → "
                  "DÉNOUEMENT (résolution) → SITUATION FINALE (nouvel équilibre). "
                  "Les temps du récit : passé simple/imparfait ; présent de narration "
                  "est possible."},
        {"nom": "Méthode 2 — analyser narrateur et point de vue (focalisation)",
         "texte": "Narrateur personnage (je) ou narrateur extérieur (il). "
                  "Focalisation ZÉRO : tout savoir omniscient. INTERNE : on voit à "
                  "travers un personnage (ses pensées seulement). EXTERNE : "
                  "observateur neutre (actions visibles uniquement)."},
        {"nom": "Méthode 3 — repérer les indices narratifs",
         "texte": "Connecteurs temporels (soudain, alors, le lendemain, longtemps "
                  "après), verbes d'action, discours direct (dialogue, « — » ou "
                  "guillemets) qui anime le récit, valeurs des temps : imparfait = "
                  "description/arrière-plan ; passé simple = actions de premier plan."},
    ],
    "exemples": [
        {"question": "« Il pleuvait depuis des jours. Soudain, la porte s'ouvrit : un "
                     "inconnu entra et demanda l'hospitalité. » Identifier les temps "
                     "et l'élément perturbateur.",
         "etapes": ["« Il pleuvait » : imparfait → arrière-plan (description)",
                    "« s'ouvrit, entra, demanda » : passé simple → actions de premier plan",
                    "« Soudain » : connecteur temporel marquant la rupture",
                    "Élément perturbateur : l'arrivée de l'inconnu"],
         "reponse": "Imparfait = décor ; passé simple = événements ; l'inconnu "
                    "déclenche le récit."},
    ],
    "pieges": [
        "Passé simple = ACTION ; imparfait = DESCRIPTION/HABITUDE. Ne pas les confondre.",
        "Le narrateur n'est pas l'auteur !",
        "Focalisation interne : « il pensait que... » — on accède à ses pensées.",
    ],
    "formules": ["schéma : situation initiale → perturbation → péripéties → dénouement → finale",
                 "focalisations : zéro / interne / externe"],
}

L_DESCRIPTIF = {
    "intro": "Le texte descriptif peint un lieu, un objet, une personne ou un "
             "paysage. Il insère des impressions et vise à faire « voir » : on le "
             "trouve dans le portrait, la description de cadre, le carnet de voyage.",
    "methodes": [
        {"nom": "Méthode 1 — reconnaître un texte descriptif",
         "texte": "Indices : verbes d'état (être, sembler, paraître), imparfait ou "
                  "présent de description, abondance d'adjectifs qualificatifs et de "
                  "compléments du nom, verbes de perception (voir, apercevoir, "
                  "distinguer), organisateurs spatiaux (au fond, à droite, autour)."},
        {"nom": "Méthode 2 — analyser un portrait",
         "texte": "Portrait PHYSIQUE (veston, traits, taille) et portrait MORAL "
                  "(caractère, qualités, défauts) — souvent mêlés (portrait "
                  "physiologique). Vérifier si le portrait est réaliste, flatteur ou "
                  "caricatural (satirique)."},
        {"nom": "Méthode 3 — repérer les procédés d'expansion du nom",
         "texte": "Pour enrichir un nom : adjectifs qualificatifs (« un vieil homme "
                  "dignifique »), compléments du nom (« la maison de campagne »), "
                  "propositions relatives (« le toit qui fuyait »), appositions. "
                  "Plus le nom est développé, plus l'image est précise."},
    ],
    "exemples": [
        {"question": "« Au fond du jardin, une vieille maison de pierre dont le toit "
                     "de tuiles rouges s'inclinait tristement. » Relever un complément "
                     "du nom, une relative, un organisateur spatial.",
         "etapes": ["Organisateur spatial : « Au fond du jardin »",
                    "Complément du nom : « maison de pierre », « toit de tuiles rouges »",
                    "Relative : « dont le toit... s'inclinait »",
                    "Adjectifs : vieille, rouges + adverbe modalisateur « tristement »"],
         "reponse": "Les expansions du nom construisent l'image précise du lieu."},
    ],
    "pieges": [
        "La description sert souvent la narration : identifier la DOMINANTE du texte.",
        "Imparfait de description ≠ imparfait d'habitude (« tous les jours »).",
        "Les organisateurs spatiaux décrivent aussi les mouvements (texte descriptif-dynamique).",
    ],
    "formules": ["expansion du nom : adj. + complément + relative + apposition",
                 "portrait = physique + moral"],
}

L_EXPLICATIF = {
    "intro": "Le texte explicatif fait COMPRENDRE : il définit, décrit un "
             "fonctionnement, expose des causes et des conséquences. Encyclopédie, "
             "manuel scolaire, documentaire, article de vulgarisation.",
    "methodes": [
        {"nom": "Méthode 1 — reconnaître les marques de l'explication",
         "texte": "Définitions (« X est... », « on appelle X... »), présent de vérité "
                  "générale, voix passive et tournures impersonnelles (« il faut "
                  "savoir »), vocabulaire technique défini, exemples introits par "
                  "« par exemple », reformulations (« c'est-à-dire », « autrement dit »)."},
        {"nom": "Méthode 2 — suivre les connecteurs d'organisation",
         "texte": "CAUSE : parce que, en raison de, grâce à, à cause de. "
                  "CONSÉQUENCE : donc, d'où, si bien que. BUT : pour, afin de, dans le "
                  "but de. CLASSIFICATION : d'une part/d'autre part, premièrement, "
                  "ensuite, enfin. COMPARAISON : comme, contrairement à, de même que."},
        {"nom": "Méthode 3 — distinguer explicatif et argumentatif",
         "texte": "Explicatif : fait comprendre un savoir OBJECTIF, sans opinion "
                  "(présent de vérité, neutre). Argumentatif : défend une OPINION "
                  "(modalisateurs, jugements de valeur). Question-test : l'auteur "
                  "essaie-t-il de me faire COMPRENDRE ou de me CONVAINCRE ?"},
    ],
    "exemples": [
        {"question": "« La photosynthèse, c'est-à-dire la fabrication de matière "
                     "organique par les plantes, se produit grâce à la lumière : ainsi "
                     "les feuilles vertes transforment l'eau et le CO₂. » Relever "
                     "une définition, une reformulation, un connecteur.",
         "etapes": ["Définition : « la fabrication de matière organique par les plantes »",
                    "Reformulation : « c'est-à-dire »",
                    "Connecteur de cause : « grâce à » ; de conséquence : « ainsi »",
                    "Présent de vérité générale : « se produit »"],
         "reponse": "Toutes les marques de l'explicatif sont réunies."},
    ],
    "pieges": [
        "« Parce que » introduit la cause ; « donc » la conséquence — ne pas inverser.",
        "L'explicatif n'exprime pas d'opinion : tout jugement de valeur signale l'argumentatif.",
        "Les définitions peuvent être explicites (« X est... ») ou implicites (entre virgules).",
    ],
    "formules": ["explicatif = définir + expliquer + exemplifier",
                 "marques : définitions, présent de vérité, passif, connecteurs logiques"],
}

L_SUBORDONNEES = {
    "intro": "Une proposition subordonnée est enchâssée dans une principale et ne "
             "peut pas vivre seule. Trois grandes familles : relatives, conjonctives "
             "complétives, circonstancielles. Les reconnaître structure toute l'analyse.",
    "methodes": [
        {"nom": "Méthode 1 — identifier la subordonnée relative",
         "texte": "Introduite par un PRONOM RELATIF (qui, que, quoi, dont, où, "
                  "lequel...) et complète un NOM (antécédent). Ex : « le livre "
                  "[que je t'ai prêté] est passionnant ». Fonction : complément de "
                  "l'antécédent. Astuce : remplace qui/que par un nom pour tester."},
        {"nom": "Méthode 2 — identifier la complétive (conjonctive)",
         "texte": "Introduite par la conjonction QUE (ou si) et complète un VERBE : "
                  "COD (« Je crois [que tu as raison] »), sujet (« [Qu'il mente] est "
                  "évident »). Test : elle répond à « quoi ? » après le verbe."},
        {"nom": "Méthode 3 — identifier la circonstancielle",
         "texte": "Introduite par une conjonction de circonstance : TEMPS (quand, "
                  "lorsque, dès que, avant que), CAUSE (parce que, puisque, comme), "
                  "CONSÉQUENCE (si bien que, de sorte que), BUT (pour que, afin que), "
                  "CONDITION (si, à condition que), OPPOSITION (bien que, quoique), "
                  "COMPARAISON (comme si). Elle dit QUAND, POURQUOI, À QUELLE "
                  "CONDITION..."},
    ],
    "exemples": [
        {"question": "Analyser : « Quand la pluie cessa, les enfants qui attendaient "
                     "dehors poussèrent des cris parce qu'ils étaient trempés. »",
         "etapes": ["« Quand la pluie cessa » : circonstancielle de TEMPS",
                    "« qui attendaient dehors » : relative (antécédent : les enfants)",
                    "« parce qu'ils étaient trempés » : circonstancielle de CAUSE",
                    "Principale : « les enfants... poussèrent des cris »"],
         "reponse": "1 principale + 1 relative + 2 circonstancielles (temps, cause)."},
    ],
    "pieges": [
        "« que » pronom relatif (complète un nom) ≠ « que » conjonction (complète un verbe).",
        "La relative a toujours un antécédent ; la complétive, jamais.",
        "« si » peut être condition (« si tu viens ») ou interrogation indirecte (« je demande si »).",
    ],
    "formules": ["relative → complète un nom (pronom relatif)",
                 "complétive → complète un verbe (que/si)",
                 "circonstancielle → temps, cause, but, condition, opposition"],
}

L_LEXIQUE = {
    "intro": "Le sens d'un mot dépend de son contexte : champ lexical, polysémie, "
             "connotations — maîtriser le lexique, c'est affiner sa lecture ET sa "
             "production écrite.",
    "methodes": [
        {"nom": "Méthode 1 — réunir un champ lexical",
         "texte": "Le champ lexical regroupe les mots (de classes différentes !) liés "
                  "au même thème. Texte sur la mer : vagues, salé, navigator, "
                  "marin... Il révèle le thème dominant d'un passage. Repérer le "
                  "champ lexical = repérer le sujet véritable du texte."},
        {"nom": "Méthode 2 — gérer la polysémie et le contexte",
         "texte": "Un mot polysémique a plusieurs sens : « une feuille » (arbre, "
                  "papier). C'est le CONTEXTE (mots voisins, phrase) qui choisit le "
                  "bon sens. Face à un mot inconnu : chercher le sens par le "
                  "contexte avant le dictionnaire."},
        {"nom": "Méthode 3 — distinguer dénotation et connotation",
         "texte": "Dénotation = sens du dictionnaire, neutre (« rouge » : couleur). "
                  "Connotation = sens additionnel, images et émotions (« rouge » : "
                  "danger, passion, colère). Les connotations créent le TON d'un "
                  "texte : poétique, ironique, péjoratif, mélioratif."},
    ],
    "exemples": [
        {"question": "« Cet animal de contrat » : quel est le sens de « animal » ici ? "
                     "Dénoté ou connoté ?",
         "etapes": ["Sens du dictionnaire : être vivant (dénotation)",
                    "Ici : personne brutale, sans finesse (connotation péjorative)",
                    "Le contexte (« contrat ») impose ce sens figuré"],
         "reponse": "Sens connoté (péjoratif) : l'image de l'animal s'applique à une personne."},
    ],
    "pieges": [
        "Le champ lexical n'est pas le champ sémantique d'un seul mot : il traverse les classes grammaticales.",
        "Connotation péjorative ≠ faute : c'est un CHOIX de l'auteur à analyser.",
        "Un synonyme n'est jamais parfaitement équivalent : nuances différentes.",
    ],
    "formules": ["dénotation = sens neutre du dictionnaire",
                 "connotation = sens émotionnel/culturel additionnel"],
}

L_TEMPS = {
    "intro": "Chaque temps verbal porte une VALEUR : le présent peut exprimer une "
             "habitude, une vérité générale ou une action en cours. Savoir justifier "
             "un temps par sa valeur est demandé à presque chaque examen.",
    "methodes": [
        {"nom": "Méthode 1 — les valeurs du présent",
         "texte": "VÉRITÉ GÉNÉRALE (« l'eau bout à 100 °C »), HABITUDE (« je me lève "
                  "à 6 h »), ACTION EN COURS (« il pleut maintenant »), PASSE "
                  "COMPOSÉ PRÉSENT (présent de narration, passé récent « venir de »), "
                  "FUTUR PROCHE (« je pars demain »). Le contexte tranche."},
        {"nom": "Méthode 2 — imparfait vs passé composé / passé simple",
         "texte": "IMPARFAIT : description, arrière-plan, habitude du passé, action "
                  "durative inachevée. PASSÉ COMPOSÉ : action achevée, ponctuelle, "
                  "successive (« il est entré et s'est assis »). PASSÉ SIMPLE : même "
                  "valeur d'action au récit littéraire."},
        {"nom": "Méthode 3 — les autres temps clés",
         "texte": "FUTUR SIMPLE : action à venir ou ordre. FUTUR ANTÉRIEUR : "
                  "antériorité dans le futur (« quand tu auras fini »). PLUS-QUE-PARFAIT : "
                  "antériorité dans le passé (« il avait déjà mangé ») — le temps du "
                  "flash-back. CONDITIONNEL PRÉSENT : hypothèse, futur du passé, "
                  "politesse, information non confirmée."},
    ],
    "exemples": [
        {"question": "« Hier, je lisais tranquillement quand soudain le téléphone a "
                     "sonné. » Justifier les temps.",
         "etapes": ["« lisais » : imparfait → action durative, arrière-plan",
                    "« a sonné » : passé composé → action ponctuelle qui INTERROMPT",
                    "Structure type : imparfait (durée) interrompu par passé composé (fait)"],
         "reponse": "Imparfait = cadre ; passé composé = événement interrupteur."},
    ],
    "pieges": [
        "Imparfait d'habitude (« tous les matins, j'allais... ») ≠ imparfait de description.",
        "Le plus-que-parfait indique TOUJOURS l'antériorité par rapport à un autre passé.",
        "Conditionnel ≠ futur : « il viendrait » (futur du passé/hypothèse) vs « il viendra ».",
    ],
    "formules": ["présent : vérité / habitude / action en cours",
                 "imparfait : description-durée-habitude ; PS/PC : action achevée",
                 "plus-que-parfait : antérieur au passé"],
}

V = lambda *xs: list(xs)

UPGRADES = {
    "Le texte argumentatif": {
        "semestre": 1, "lecon": L_ARGUMENTATIF,
        "exos": [
            (1, "Manuel", "Relever les connecteurs logiques : « D'abord, la lecture "
             "enrichit le vocabulaire ; en effet, elle expose à des tournures "
             "variées. De plus, elle améliore la concentration. Certes, les écrans "
             "occupent les jeunes, mais un livre reste irremplaçable. »",
             "« D'abord » : addition/énumération ; « en effet » : cause/explication ; "
             "« De plus » : addition ; « Certes » : concession/admission ; "
             "« mais » : opposition.",
             "Classer les connecteurs : cause, conséquence, addition, opposition.",
             V()),
            (2, "Contrôle", "Dans le texte précédent, identifier la thèse défendue et "
             "l'antithèse admise.",
             "Thèse : la lecture est irremplaçable (enrichit vocabulaire, concentration).\n"
             "Antithèse admise : « les écrans occupent les jeunes » (introduite par "
             "« certes » puis rejetée par « mais »).",
             "L'antithèse est ADMISE temporairement puis récusée.",
             V()),
            (3, "Type Examen Régional", "Rédiger un paragraphe argumenté (4-5 lignes) "
             "sur : « Le sport est indispensable à la réussite scolaire », avec 2 "
             "arguments, un exemple et 3 connecteurs.",
             "Modèle : « Le sport est indispensable à la réussite scolaire. D'abord, "
             "il permet de se détendre après l'effort intellectuel ; en effet, une "
             "séance de foot libère le stress des contrôles. De plus, il développe la "
             "discipline : un élève qui s'entraîne régulièrement apprend à organiser "
             "son temps. Par conséquent, le sport nourrit la réussite au lieu de la "
             "nuire. » (connecteurs : d'abord, en effet, de plus, par conséquent)",
             "Structure : thèse → argument 1 + exemple → argument 2 → conclusion.",
             V()),
        ],
    },
    "Les figures de style": {
        "semestre": 1, "lecon": {
            "intro": "Les figures de style donnent puissance et beauté au langage : "
                     "les reconnaître, c'est comprendre comment l'auteur joue avec les "
                     "mots, les sons et les images.",
            "methodes": [
                {"nom": "Méthode 1 — les figures d'image",
                 "texte": "COMPARAISON : rapproche 2 éléments avec un outil de "
                          "comparaison (comme, tel, semblable à) — « doux comme un "
                          "agneau ». MÉTAPHORE : même rapprochement SANS outil — "
                          "« ce lion d'homme ». PERSONNIFICATION : attributes "
                          "humaines à une chose — « la mer se fâche »."},
                {"nom": "Méthode 2 — les figures d'insistance",
                 "texte": "RÉPÉTITION/ANAPHORE : même mot en tête de phrase/vers. "
                          "HYPERBOLE : exagération — « mourir de rire ». GRADATION : "
                          "montée d'intensité — « un mot, une phrase, un discours ». "
                          "ANTITHÈSE : opposition de 2 idées — « il vivait le jour, "
                          "elle la nuit »."},
                {"nom": "Méthode 3 — les figures de son et de atténuation",
                 "texte": "ALLITÉRATION : répétition de consonnes — « les sanglots "
                          "longs » (l). ASSONANCE : répétition de voyelles. "
                          "EUPHÉMISME : atténuation (« il nous a quittés » = il est "
                          "mort). LITOTE : dire moins pour suggérer plus (« ce n'est "
                          "pas mauvais » = c'est excellent)."},
            ],
            "exemples": [
                {"question": "Identifier les figures : « Cette femme est une rose ; "
                             "elle fleurit le matin et se fane le soir. »",
                 "etapes": ["« Cette femme est une rose » : métaphore (pas d'outil)",
                            "« fleurit », « se fane » : métaphores verbales prolongées",
                            "« le matin... le soir » : antithèse (jeunesse/vieillesse)"],
                 "reponse": "Métaphores filées + antithèse."},
            ],
            "pieges": [
                "Comparaison AVEC outil (comme, tel) ; métaphrase SANS outil.",
                "Personnification : la chose AGIT comme un humain (verbes humains).",
                "Hyperbole ≠ mensonge : c'est une exagération stylistique voulue.",
            ],
            "formules": ["comparaison = A comme B ; métaphore = A est B",
                         "allitération = consonnes ; assonance = voyelles"],
        },
        "exos": [
            (1, "Manuel", "Identifier : « Le vent gémissait dans les Branches nues. » "
             "et « Il est plus glacial qu'un iceberg. »",
             "« Le vent gémissait » : personnification (verbe humain)\n"
             "« plus glacial qu'un iceberg » : comparaison (outil : que)",
             "Chercher l'outil : présent → comparaison ; absent → métaphore.",
             V()),
            (2, "Contrôle", "Relever une allitération et en expliquer l'effet : « Les "
             "sanglots longs des violons de l'automne » (Verlaine).",
             "Allitération en [l] : « sanglots longs... violons... automne »\n"
             "Effet : douceur, langueur, sonorité plaintive qui imite la tristesse "
             "de l'automne.",
             "Relier TOUJOURS la figure à son EFFET (jamais seulement la nommer).",
             V()),
            (3, "Type Examen Régional", "« Tes yeux, deux étoiles éclairant ma nuit. » "
             "Identifier la figure, puis écrire une phrase avec la même figure sur "
             "la mer.",
             "Figure : métaphore (yeux = étoiles, sans outil de comparaison).\n"
             "Exemple attendu (métaphore) : « La mer, un miroir d'argent sous le "
             "soleil. » ou « La mer dévore la plage. » (personnification acceptée si "
             "justifiée).",
             "Produire une figure = respecter sa définition (ici : pas de « comme »).",
             V()),
        ],
    },
    "Le résumé de texte": {
        "semestre": 2, "lecon": {
            "intro": "Résumer, c'est restituer L'ESSENTIEL d'un texte avec ses propres "
                     "mots, dans un nombre limité de lignes, sans opinion personnelle. "
                     "Compétence-clé de l'examen régional.",
            "methodes": [
                {"nom": "Méthode 1 — la démarche en 4 étapes",
                 "texte": "① LIRE 2 fois (global puis précis). ② DÉCOUPER en "
                          "paragraphes et repérer l'idée principale de CHACUN "
                          "(souvent dans la 1ʳᵉ ou dernière phrase). ③ RÉDIGER en "
                          "enchaînant ces idées avec des connecteurs. ④ VÉRIFIER : "
                          "fidélité, proportion (1/4 du texte), pas de jugement."},
                {"nom": "Méthode 2 — condenser sans déformer",
                 "texte": "SUPPRIMER : exemples, répétitions, citations, chiffres "
                          "secondaires. GÉNÉRALISER : « chaise, table, armoire » → "
                          "« le mobilier ». REFORMULER : synonymes, changement de "
                          "construction — NE JAMAIS recopier des phrases entières."},
                {"nom": "Méthode 3 — les pièges à éviter",
                 "texte": "Ajouter son opinion (interdit !) ; sauter une idée "
                          "essentielle ; dépasser la longueur demandée ; changer le "
                          "sens par une mauvaise généralisation ; utiliser le "
                          "discours direct. Le résumé reste au MÊME temps que le texte."},
            ],
            "exemples": [
                {"question": "Résumer en 1 phrase : « Les océans absorbent chaque "
                             "année des millions de tonnes de CO₂. Par exemple, "
                             "l'Atlantique nord capte à lui seul un quart des émissions. "
                             "Ce service rend le climat plus supportable. »",
                 "etapes": ["Idée 1 : les océans absorbent le CO₂ (l'exemple : supprimable)",
                            "Idée 2 : conséquence — il atténue le climat",
                            "Fusion : « Les océans, en absorbant une grande partie du "
                            "CO₂ émis, atténuent le réchauffement climatique. »"],
                 "reponse": "Une phrase fidèle, sans exemple, au présent comme l'original."},
            ],
            "pieges": [
                "Le résumé n'est PAS une analyse : zéro commentaire personnel.",
                "Respecter la proportion : trop court = idées manquées ; trop long = hors sujet.",
                "Reprendre des mots du texte est permis, des PHRASES entières non.",
            ],
            "formules": ["résumé ≈ 1/4 du texte", "méthode : lire → découper → rédiger → vérifier"],
        },
        "exos": [
            (2, "Contrôle", "Quelles informations peut-on SUPPRIMER d'un résumé ? "
             "Citer 4 types.",
             "Les exemples illustratifs ; les répétitions et redites ; les citations ; "
             "les chiffres/détails secondaires ; les digressions.",
             "Supprimer l'illustration, garder l'idée qu'elle illustre.",
             V()),
            (3, "Type Examen Régional", "Résumer en 2 phrases : « Le Maroc connaît une "
             "urbanisation rapide. Casablanca, Rabat et Tanger grossissent chaque "
             "année de milliers d'habitants venus chercher du travail. Cette "
             "affluence provoque une pénurie de logements et une pression sur les "
             "transports. Les autorités multiplient donc les programmes de villes "
             "nouvelles. »",
             "Modèle : « Le Maroc s'urbanise rapidement, ses grandes villes attirant "
             "une main-d'œuvre nombreuse. Cette croissance engendre des difficultés "
             "(logement, transports) auxquelles les autorités répondent par de "
             "nouvelles villes. »",
             "Généraliser les exemples de villes → « ses grandes villes ».",
             V()),
        ],
    },
}

NEW_CHAPTERS = [
    (1, "Le texte narratif", "Schéma narratif, narrateur et focalisation, temps du "
     "récit.", L_NARRATIF, [
        (1, "Manuel", "Ordonner les 5 étapes du schéma narratif, puis les identifier "
         "dans un récit où « un pêcheur part au large, une tempête se lève, il "
         "lutte toute la nuit, rejoint le port au matin et promet d'écouter la météo ».",
         "Ordre : situation initiale → élément perturbateur → péripéties → "
         "dénouement → situation finale.\nSI : départ au large ; ÉP : la tempête se "
         "lève ; Péripéties : la lutte toute la nuit ; Dénouement : arrivée au port ; "
         "SF : la promesse (nouvel équilibre).",
         "Chercher d'abord la RUPTURE (perturbateur) : tout le reste se place autour.",
         V()),
        (2, "Contrôle", "« Je m'arrêtai devant la vitrine, incapable de détourner le "
         "regard. Mon cœur battait. » Quel narrateur ? Quelle focalisation ?",
         "Narrateur PERSONNAGE (emploi de « je »).\nFocalisation INTERNE : on accède "
         "à ses émotions (« incapable de... », « mon cœur battait ») — vision limitée "
         "à ce qu'il ressent.",
         "« je » + pensées/émotions du « je » = focalisation interne.",
         V({"enonce": "Et dans « Il traversa la place sans voir l'ombre qui "
                      "l'observait du toit. »",
            "solution": "Focalisation zéro (omnisciente) : le narrateur sait ce que "
                        "le personnage ignore."})),
        (2, "Manuel", "Justifier les temps : « Il marchait depuis une heure quand il "
         "aperçut une lumière. Il s'approcha et frappa à la porte. »",
         "« marchait » : imparfait (action durative, arrière-plan)\n"
         "« aperçut, s'approcha, frappa » : passé simple (actions ponctuelles, "
         "premier plan, successives)",
         "Imparfait = durée/décor ; passé simple = actions qui font avancer le récit.",
         V()),
        (3, "Type Examen Régional", "Écrire le début d'un récit (3-4 lignes) au passé "
         "composé/imparfait avec un élément perturbateur clairement marqué.",
         "Modèle : « Dimanche, nous nous promenions calmement au bord de l'oued. "
         "Soudain, un cri a déchiré le silence : un enfant glissait vers l'eau. »\n"
         "Attendus : situation initiale (imparfait), connecteur de rupture "
         "(« soudain »), élément perturbateur clair.",
         "Marquer la rupture par un connecteur temporel + bascule des temps.",
         V()),
    ]),

    (1, "Le texte descriptif", "Marques descriptives, portrait, expansion du nom, "
     "organisateurs spatiaux.", L_DESCRIPTIF, [
        (1, "Manuel", "Relever 3 indices du texte descriptif dans : « À droite "
         "s'étendait une plage de sable fin. Une mer calme, d'un bleu profond, "
         "bordait la baie qui semblait endormie. »",
         "Organisateur spatial : « À droite » ; imparfaits de description : "
         "« s'étendait », « bordait », « semblait » ; adjectifs : « fin », « calme », "
         "« profond » ; relative : « qui semblait endormie » (personnification).",
         "4 familles d'indices : temps verbaux, adjectifs, organisateurs, verbes d'état.",
         V()),
        (2, "Contrôle", "Construire un portrait moral à partir de : « Elle n'a jamais "
         "refusé son aide ; elle pardonne tout ; on la consulte pour chaque "
         "décision. » Puis dire si le portrait est mélioratif ou péjoratif.",
         "Portrait moral : généreuse (aide), indulgente (pardonne), sage/considérée "
         "(consultée).\nPortrait MÉLIORATIF : les traits valorisent la personne.",
         "Portrait moral = caractère et comportement, pas l'apparence.",
         V({"enonce": "Reformuler un trait pour rendre le portrait péjoratif.",
            "solution": "« Elle pardonne tout » → « elle se laisse marcher dessus » "
                        "(naïve, faible) : les mêmes faits, une autre valeur."})),
        (2, "Manuel", "Enrichir le nom « une maison » avec : ① un adjectif ② un "
         "complément du nom ③ une relative.",
         "① une maison ancienne\n② une maison de campagne\n③ une maison qui surplombe "
         "l'oued\n(possibles en combinaison : « une ancienne maison de campagne qui "
         "surplombe l'oued »)",
         "Expansion du nom : adj. + complément + relative — les cumuler pour préciser.",
         V()),
        (3, "Type Examen Régional", "Rédiger une description de paysage (4-5 lignes) "
         "avec 2 organisateurs spatiaux, l'imparfait et une personnification.",
         "Modèle : « Au fond de la vallée, l'oued serpente paresseusement entre les "
         "oliviers. Sur la rive gauche, des terrasses de culture grimpaient comme un "
         "escalier géant. Le soleil, du matin, embrassait la colline nue. »\n"
         "(organisateurs : au fond, sur la rive gauche ; personnifications : "
         "serpente, embrassait ; imparfait ✓)",
         "Évaluation : organisateurs ✓ temps ✓ figure de style ✓ cohérence spatiale ✓.",
         V()),
    ]),

    (1, "Le texte explicatif", "Définitions, connecteurs de cause/conséquence, "
     "présent de vérité générale.", L_EXPLICATIF, [
        (1, "Manuel", "Relever : une définition, un connecteur de cause, un connecteur "
         "de conséquence dans : « La sécheresse, c'est-à-dire un manque prolongé de "
         "pluie, appauvrit les sols parce que la végétation disparait ; si bien que "
         "l'érosion s'accélère. »",
         "Définition : « c'est-à-dire un manque prolongé de pluie »\n"
         "Cause : « parce que la végétation disparait »\n"
         "Conséquence : « si bien que l'érosion s'accélère »",
         "Chaîne logique : cause (parce que) → effet (si bien que).",
         V()),
        (2, "Contrôle", "Le texte « Le tabac tue. Les publicités séduisantes devraient "
         "être interdites ; c'est une évidence » est-il explicatif ou argumentatif ? "
         "Justifier par 2 indices.",
         "ARGUMENTATIF.\n① Jugement de valeur + opinion : « devraient être "
         "interdites », « c'est une évidence »\n② Objectif de convaincre (pas de "
         "définition ni d'explication neutre ; modalisateurs appréciatifs).",
         "Présence d'OPINION = argumentatif, même si le thème est « explicatif ».",
         V()),
        (2, "Manuel", "Compléter avec le connecteur logique adapté : « Les plantes "
         "vertes fabriquent leur matière organique ___ la lumière ; ___, une plante "
         "privée de lumière finit par mourir. »",
         "« grâce à la lumière » (cause/condition favorable)\n"
         "« Ainsi/Par conséquent, une plante privée de lumière finit par mourir » "
         "(conséquence)",
         "grâce à (+ favorable) / à cause de (+ défavorable) ; ainsi = conséquence.",
         V()),
        (3, "Type Examen Régional", "Rédiger un court paragraphe explicatif (4 lignes) "
         "sur le cycle de l'eau : une définition, un connecteur de cause et un de "
         "conséquence, au présent de vérité générale.",
         "Modèle : « Le cycle de l'eau, c'est-à-dire le parcours permanent de l'eau "
         "entre mer, air et terre, se déroule sans fin. Sous l'effet du soleil, l'eau "
         "s'évapore ; comme la vapeur s'élève en altitude, elle se condense en "
         "nuages ; si bien que la pluie ramène l'eau vers les océans. »",
         "Présent de vérité + définition + cause + conséquence : le quota complet.",
         V()),
    ]),

    (2, "Les propositions subordonnées", "Relatives, complétives, circonstancielles : "
     "reconnaissance et fonctions.", L_SUBORDONNEES, [
        (1, "Manuel", "Identifier les subordonnées : « Le livre que tu m'as offert "
         "plait à tous ceux qui aiment l'histoire. »",
         "« que tu m'as offert » : relative (antécédent : le livre)\n"
         "« qui aiment l'histoire » : relative (antécédent : ceux)",
         "Relative = introduite par pronom relatif + antécédent nominal.",
         V()),
        (2, "Contrôle", "« Je pense que tu réussiras si tu travailles. » Identifier "
         "chaque proposition et son type.",
         "Principale : « Je pense »\n« que tu réussiras » : complétive (COD de "
         "« pense », introduite par que)\n« si tu travailles » : circonstancielle de "
         "CONDITION",
         "que + verbe complété = complétive ; si + condition = circonstancielle.",
         V({"enonce": "Et dans « Il est parti parce qu'il était en retard. » ?",
            "solution": "« parce qu'il était en retard » : circonstancielle de CAUSE."})),
        (2, "Manuel", "Relier par le connecteur qui convient : ① il pleuvait... nous "
         "sommes sortis (opposition) ② ... tu finis, nous commencerons (temps) "
         "③ ... il soit malade, il vient (concession).",
         "① Bien que/Quoiqu'il pleuvât... nous sommes sortis\n"
         "② Dès que/Aussitôt que tu finis, nous commencerons\n"
         "③ Bien qu'il soit malade, il vient (concession) — même connecteur qu'en ①, "
         "accepté : « quoiqu'il soit malade »",
         "Concession (bien que) ≠ opposition simple (mais) : la concession admet un fait.",
         V()),
        (3, "Type Examen Régional", "Analyser complètement : « Lorsque le car arriva, "
         "les voyageurs qui attendaient depuis l'aube poussèrent un soupir de "
         "soulagement. »",
         "« Lorsque le car arriva » : circonstancielle de TEMPS\n"
         "Principale : « les voyageurs... poussèrent un soupir »\n"
         "« qui attendaient depuis l'aube » : relative, antécédent « les voyageurs »\n"
         "Valeurs : passé simple (arriva, poussèrent) = actions ; imparfait "
         "(attendaient) = durée/arrière-plan",
         "Toujours structurer : principale / relative / circonstancielle + temps.",
         V()),
    ]),

    (2, "Le lexique : sens et nuances", "Champ lexical, polysémie, dénotation et "
     "connotation, synonymie.", L_LEXIQUE, [
        (1, "Manuel", "Constituer le champ lexical de la mer dans : « Le marin "
         "contemplait les vagues ; le vent marin parfumait le port de sel. »",
         "marin, contemplait (regard), vagues, vent, port, sel → champ lexical de "
         "la MER / du MARITIME (mots de classes différentes : noms, adjectifs, verbes).",
         "Champ lexical = thème commun, toutes classes grammaticales confondues.",
         V()),
        (2, "Contrôle", "« Une feuille » a plusieurs sens. Expliquer le sens dans : "
         "① « une feuille de papier » ② « une feuille de vigne » ③ « prendre une "
         "feuille (absence) ».",
         "① feuille = page (papier)\n② feuille = organe de la plante\n③ feuille = "
         "liste de présence/registre (faire l'école buissonnière)\n"
         "→ « feuille » est un mot POLYSÉMIQUE : le contexte choisit le sens.",
         "Mot polysémique + contexte = sens précis.",
         V()),
        (2, "Manuel", "« Un enfant maigre » vs « un enfant frêle » : même sens "
         "dénoté ? Quelle différence de connotation ?",
         "Sens dénoté proche (peu de chair) ; connotations opposées :\n"
         "« maigre » → neutre, voire péjoratif (malnutrition) ; « frêle » → "
         "mélioratif, attendrissant (fragilité délicate).",
         "Synonymes = sens proches mais CONNOTATIONS différentes : choisir selon l'effet.",
         V()),
        (3, "Type Examen Régional", "Relever 2 mots à connotation péjorative dans : "
         "« Cette bande d'individus s'agitait bruyamment, bousculant les passants "
         "inoffensifs » et expliquer leur effet.",
         "Péjoratifs : « bande » (désordre, suspicion), « s'agitait » (agitation "
         "négative), « bousculant » (violence), « bruyamment » (nuisance).\n"
         "Effet : le lecteur juge négativement le groupe AVANT toute explication — "
         "l'auteur oriente l'interprétation par le lexique.",
         "La connotation oriente le jugement du lecteur : c'est un choix d'auteur à analyser.",
         V()),
    ]),

    (2, "Les valeurs des temps verbaux", "Valeurs du présent, imparfait/passé "
     "composé, plus-que-parfait, futur et conditionnel.", L_TEMPS, [
        (1, "Manuel", "Quelle valeur du présent dans : ① « La Terre tourne autour du "
         "Soleil » ② « Chaque samedi, je vais au stade » ③ « Il neige ! » ?",
         "① présent de VÉRITÉ GÉNÉRALE (scientifique)\n② présent d'HABITUDE "
         "(« chaque samedi »)\n③ présent d'énonciation/ACTION EN COURS (au moment "
         "où je parle)",
         "3 valeurs majeures : vérité générale, habitude, action en cours.",
         V()),
        (2, "Contrôle", "« Quand j'étais petit, je jouais chaque soir dehors ; un "
         "jour, j'ai cassé la vitrine du voisin. » Justifier imparfait et passé "
         "composé.",
         "« étais », « jouais » : imparfaits → description + HABITUDE répétée "
         "(« chaque soir »)\n« ai cassé » : passé composé → action PONCTUELLE, "
         "achevée, qui sort de l'habitude",
         "L'habitude est à l'imparfait ; l'événement isolé au passé composé.",
         V()),
        (2, "Manuel", "Analyser les temps : « Le train était parti quand il est "
         "arrivé. » Puis : « Dès que tu auras signé, tu recevras la clé. »",
         "« était parti » : plus-que-parfait → antériorité par rapport à « est "
         "arrivé » (premier plan au passé)\n« auras signé » : futur antérieur → "
         "action achevée AVANT une autre future (« recevras », futur simple)",
         "Antériorité au passé = plus-que-parfait ; dans le futur = futur antérieur.",
         V()),
        (3, "Type Examen Régional", "« Selon la météo, il ferait beau demain ; "
         "alors nous irions... enfin, nous irons si rien ne change. » Expliquer la "
         "valeur des 2 conditionnels puis pourquoi le dernier verbe est au futur.",
         "« ferait », « irions » : conditionnel → information NON CONFIRMÉE "
         "(« selon ») / hypothèse (futur du passé rapporté)\n« irons » : futur "
         "simple → action envisagée comme certaine (condition « si rien ne change »)\n"
         "Le passage conditionnel → futur traduit le gain de certitude.",
         "Conditionnel = incertain/politesse ; futur = engagement de l'énonciateur.",
         V()),
    ]),
]


def sync(db):
    """Enrichit les chapitres FR existants + ajoute les nouveaux (non destructif)."""
    import json as _json

    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    fid = subjects["FR"]
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
                      "AND titre = ?", (fid, titre), one=True)
        if ch:
            db.execute("UPDATE chapters SET lecon = ?, semestre = ? WHERE id = ?",
                       (_json.dumps(up["lecon"], ensure_ascii=False),
                        up["semestre"], ch["id"]))
            add_exos(ch["id"], up["exos"])
            n_up += 1

    for semestre, titre, resume, lecon, exos in NEW_CHAPTERS:
        exists = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                          "AND titre = ?", (fid, titre), one=True)
        if not exists:
            cid = db.execute(
                "INSERT INTO chapters(subject_id, niveau, semestre, titre, resume, lecon) "
                "VALUES (?,?,?,?,?,?)",
                (fid, "TC", semestre, titre, resume,
                 _json.dumps(lecon, ensure_ascii=False)))
            n_ch += 1
        else:
            cid = exists["id"]
            db.execute("UPDATE chapters SET lecon = ?, semestre = ? WHERE id = ?",
                       (_json.dumps(lecon, ensure_ascii=False), semestre, cid))
        add_exos(cid, exos)

    print(f"[sync TC FR] {n_up} leçons enrichies, +{n_ch} chapitres, +{n_ex} exercices")
