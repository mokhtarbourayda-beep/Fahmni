# -*- coding: utf-8 -*-
"""bank_pc.py — Générateur d'exercices TC Physique-Chimie (solutions calculées)."""

from fractions import Fraction as F


def E(d, src, en, sol, ast=""):
    return (d, src, en, sol, ast, [])


def fmt(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fr(x, nd=2):
    s = f"{x:.{nd}f}".rstrip("0").rstrip(".")
    return s.replace(".", ",")


ATOMES = [("1", "1", "H", "hydrogène"), ("12", "6", "C", "carbone"), ("14", "7", "N", "azote"),
          ("16", "8", "O", "oxygène"), ("23", "11", "Na", "sodium"), ("24", "12", "Mg", "magnésium"),
          ("27", "13", "Al", "aluminium"), ("32", "16", "S", "soufre"), ("35", "17", "Cl", "chlore"),
          ("39", "19", "K", "potassium"), ("40", "20", "Ca", "calcium"), ("56", "26", "Fe", "fer"),
          ("63", "29", "Cu", "cuivre"), ("65", "30", "Zn", "zinc")]


def config(n_electrons):
    couches, capa = [], [2, 8, 18]
    rest = n_electrons
    for c in capa:
        if rest <= 0:
            break
        pris = min(rest, c)
        couches.append(f"({'KLM'[len(couches)]}){pris}")
        rest -= pris
    return " ".join(couches)


def atome():
    T = "L'atome et la structure de la matière"
    exos = []
    for a, z, sym, nom in ATOMES:
        a_i, z_i = int(a), int(z)
        n_e = z_i
        exos.append(E(1, "Manuel", f"L'atome {a}/{z_i} {sym} ({nom}). Déterminer sa composition "
                      "(protons, neutrons, électrons) puis sa configuration électronique.",
                      f"Protons = Z = {z_i} ; neutrons = A - Z = {a_i} - {z_i} = {a_i - z_i} ; "
                      f"électrons = {n_e} (atome neutre)\nConfiguration : {config(n_e)}",
                      "K (2), L (8), M (18) : remplir dans cet ordre."))
    ions = [("Cl", 17, "Cl-", 1, "anion"), ("Na", 11, "Na+", -1, "cation"),
            ("Mg", 12, "Mg2+", -2, "cation"), ("Al", 13, "Al3+", -1 * 3, "cation"),
            ("S", 16, "S2-", 2, "anion"), ("K", 19, "K+", -1, "cation"),
            ("Ca", 20, "Ca2+", -2, "cation"), ("O", 8, "O2-", 2, "anion")]
    for sym, z, ion, delta, typ in ions:
        n_e = z + delta
        cfg = config(n_e)
        dernier = cfg.rstrip()[-2]  # chiffre de la dernière couche
        if dernier in "89":
            etat = "dernière couche pleine (octet) → ion STABLE"
        elif dernier == "2" and len(cfg.split(" ")) == 1:
            etat = "duet atteint (couche K pleine) → ion STABLE"
        else:
            etat = "dernière couche non pleine"
        exos.append(E(2, "Contrôle", f"L'ion {ion} (Z = {z} pour {sym}) : combien d'électrons ? "
                      "Quelle configuration ? Est-il stable (règle de l'octet/duet) ?",
                      f"{ion} : {z} {'+' if delta < 0 else '-'} {abs(delta)} électrons = {n_e} électrons\n"
                      f"Configuration : {cfg}\n{etat}",
                      "Cation : perte d'e- ; anion : gain d'e-. Les PROTONS ne changent jamais."))
    exos.append(E(3, "Type Examen Régional",
                  "Le cuivre naturel est un mélange de 63/29 Cu (69 %) et de 65/29 Cu (31 %). "
                  "Expliquer pourquoi ces deux espèces sont des isotopes et calculer la masse "
                  "molaire atomique naturelle du cuivre.",
                  "Même Z = 29 (29 protons, même élément) mais A différents (63 et 65) → isotopes.\n"
                  "M = (63 × 0,69) + (65 × 0,31) = 43,47 + 20,15 = 63,62 ≈ 63,5 g/mol",
                  "Masse molaire naturelle = moyenne pondérée par les abondances."))
    return (T, exos)


MOLES = [("le glucose C6H12O6", 180), ("le saccharose C12H22O11", 342), ("l'urée CO(NH2)2", 60),
         ("l'éthanol C2H6O", 46), ("le sulfate de cuivre CuSO4", 159.5), ("le NaCl", 58.5),
         ("l'acide ascorbique C6H8O6", 176), ("le bicarbonate NaHCO3", 84)]


def mole():
    T = "La mole et les concentrations"
    exos = []
    for nom, m in MOLES:
        n = 0.25 if m < 100 else 0.10
        masse = round(n * m, 2)
        exos.append(E(1, "Manuel", f"Calculer la quantité de matière contenue dans {fr(masse)} g "
                      f"de {nom} (M = {fr(m)} g/mol).",
                      f"n = m/M = {fr(masse)}/{fr(m)} = {fr(n)} mol",
                      "n = m/M : cohérence : m plus petit que M → n < 1 mol."))
    for nom, m in MOLES[:5]:
        c = 0.20
        v = 250
        masse = round(c * (v / 1000) * m, 2)
        exos.append(E(2, "Contrôle", f"On prépare V = {v} mL de solution de {nom} de concentration "
                      f"C = {fr(c)} mol/L. Quelle masse de soluté peser ? (M = {fr(m)} g/mol)",
                      f"n = C×V = {fr(c)} × {v/1000} = {fr(c * v / 1000)} mol\n"
                      f"m = n×M = {fr(c * v / 1000)} × {fr(m)} = {fr(masse)} g",
                      "Convertir mL → L AVANT les calculs."))
    for c1, v2, c2 in ((2.0, 500, 0.2), (1.5, 250, 0.3), (0.5, 200, 0.05), (3.0, 400, 0.6),
                       (1.0, 350, 0.1), (2.5, 100, 0.5)):
        v1 = c2 * v2 / c1
        fac = c1 / c2
        exos.append(E(2, "Contrôle", f"Dilution : on dispose de solution mère C₁ = {fr(c1)} mol/L. "
                      f"Quel volume prélever pour obtenir V₂ = {v2} mL de solution fille "
                      f"C₂ = {fr(c2)} mol/L ? Quel est le facteur de dilution ?",
                      f"C₁V₁ = C₂V₂ → V₁ = C₂V₂/C₁ = {fr(c2)}×{v2}/{fr(c1)} = {fr(v1)} mL\n"
                      f"F = C₁/C₂ = {fmt(F(c1).limit_denominator(100))}/{fmt(F(c2).limit_denominator(100))} = {fr(fac)}",
                      "La quantité de soluté est conservée : C₁V₁ = C₂V₂."))
    for nom, m, cml in (("le glucose C6H12O6", 180, 36), ("le saccharose C12H22O11", 342, 85.5),
                        ("l'urée CO(NH2)2", 60, 15), ("l'éthanol C2H6O", 46, 92)):
        c = cml / m
        exos.append(E(2, "Contrôle", f"Une solution de {nom} a une concentration massique "
                      f"Cm = {fr(cml)} g/L (M = {fr(m)} g/mol). Calculer C puis n dans 500 mL.",
                      f"C = Cm/M = {fr(cml)}/{fr(m)} = {fr(c)} mol/L\n"
                      f"n = C×V = {fr(c)} × 0,500 = {fr(c * 0.5)} mol",
                      "C = Cm/M : les deux concentrations se relient par M."))
    for na in ((6.02, 0.5), (12.04, 1.0), (3.01, 0.25), (1.505, 0.125)):
        na_val, n = na
        exos.append(E(2, "Contrôle", f"Un échantillon contient N = {fr(na_val)} × 10²³ molécules. "
                      "Quelle quantité de matière (en mol) ?",
                      f"n = N/N_A = {fr(na_val)}×10²³/(6,02×10²³) = {fr(n)} mol",
                      "Diviser par le nombre d'Avogadro : 6,02 × 10²³ /mol."))
    exos.append(E(3, "Type Examen Régional",
                  "Protocole : obtenir V₂ = 200 mL de solution de sulfate de cuivre C₂ = 0,05 mol/L "
                  "à partir d'une solution mère C₁ = 0,50 mol/L. Décrire le protocole avec la verrerie "
                  "et calculer la masse de CuSO4 contenue dans la fiole (M = 159,5 g/mol).",
                  "V₁ = C₂V₂/C₁ = 0,05×200/0,50 = 20 mL\n"
                  "Prélever 20 mL à la pipette jaugée ; verser dans une fiole jaugée de 200 mL ; "
                  "compléter au trait de jauge avec de l'eau distillée ; homogénéiser.\n"
                  "m = n×M = (0,05 × 0,200) × 159,5 = 0,010 × 159,5 = 1,595 ≈ 1,6 g",
                  "Pipette jaugée (prélèvement) + fiole jaugée (volume exact)."))
    return (T, exos)


def reaction():
    T = "La réaction chimique et le bilan de matière"
    exos = []
    eqs = [("CH4 + 2O2 → CO2 + 2H2O (combustion du méthane)", "C : 1=1 ; H : 4=4 ; O : 2+4=2+4 ✓"),
           ("2H2 + O2 → 2H2O (synthèse de l'eau)", "H : 4=4 ; O : 2=2 ✓"),
           ("4Al + 3O2 → 2Al2O3 (combustion de l'aluminium)", "Al : 4=4 ; O : 6=6 ✓"),
           ("Fe + 2HCl → FeCl2 + H2 (attaque du fer)", "Fe : 1=1 ; H : 2=2 ; Cl : 2=2 ✓"),
           ("2CO + O2 → 2CO2 (combustion du CO)", "C : 2=2 ; O : 2+2=4=4 ✓"),
           ("Zn + 2HCl → ZnCl2 + H2", "Zn : 1=1 ; H : 2=2 ; Cl : 2=2 ✓"),
           ("C3H8 + 5O2 → 3CO2 + 4H2O (propane)", "C : 3=3 ; H : 8=8 ; O : 10=6+4 ✓")]
    for eq, verif in eqs:
        exos.append(E(1, "Contrôle", f"Ajuster puis vérifier l'équation-bilan : {eq}.",
                      f"Équation ajustée : {eq.split(' (')[0]}\nVérification : {verif}",
                      "Ajuster avec des coefficients ; ne jamais toucher aux formules."))
    for nch4 in (0.20, 0.50, 1.5, 2.0):
        exos.append(E(2, "Contrôle", f"On brûle n = {fr(nch4)} mol de méthane (CH4 + 2O2 → CO2 + 2H2O). "
                      "Calculer les quantités de O₂ consommé, CO₂ et H₂O formés.",
                      f"Coefficients : 1 ; 2 ; 1 ; 2\nn(O₂) = 2×{fr(nch4)} = {fr(2 * nch4)} mol\n"
                      f"n(CO₂) = {fr(nch4)} mol ; n(H₂O) = {fr(2 * nch4)} mol",
                      "Les coefficients donnent les proportions MOLAIRES."))
    for nz, nah in ((0.10, 0.15), (0.20, 0.30), (0.30, 0.50), (0.05, 0.12)):
        xmax_h = nah / 2
        lim = "H⁺" if xmax_h < nz else "Zn"
        xfinal = min(nz, xmax_h)
        exos.append(E(2, "Contrôle", f"On mélange {fr(nz)} mol de zinc et {fr(nah)} mol d'ions H⁺ "
                      "(Zn + 2H⁺ → Zn²⁺ + H₂). Réactif limitant ? Quantité de H₂ formé ?",
                      f"Pour Zn : xmax = {fr(nz)}/1 = {fr(nz)} mol\n"
                      f"Pour H⁺ : xmax = {fr(nah)}/2 = {fr(xmax_h)} mol\n"
                      f"Le plus petit : xmax = {fr(xfinal)} mol → {lim} est limitant\n"
                      f"n(H₂) = 1×{fr(xfinal)} = {fr(xfinal)} mol"
                      + (f" ; Zn restant = {fr(nz - xfinal)} mol" if nz > xfinal else " ; Zn épuisé aussi (mélange stœchiométrique)" if lim == "Zn" else f" ; Zn restant = {fr(nz - xfinal)} mol"),
                      "Diviser chaque n initial par son coefficient : le MINIMUM est limitant."))
    exos.append(E(3, "Type Examen Régional",
                  "On introduit 0,10 mol de zinc dans 100 mL d'acide chlorhydrique contenant 0,15 mol "
                  "de H⁺. Dresser le tableau d'avancement et calculer la composition finale.",
                  "Zn + 2H⁺ → Zn²⁺ + H₂\nxmax(Zn) = 0,10 ; xmax(H⁺) = 0,15/2 = 0,075 → H⁺ limitant\n"
                  "État final : Zn : 0,10 - 0,075 = 0,025 mol ; H⁺ : 0 mol ; Zn²⁺ : 0,075 mol ; H₂ : 0,075 mol",
                  "Le tableau suit les coefficients : chaque ligne = n_i ± coef×x."))
    return (T, exos)


def ph_exos():
    T = "Les solutions acides et basiques : le pH"
    exos = []
    for p in (1, 2, 3, 4, 5, 6):
        exos.append(E(1, "Manuel", f"Une solution a pH = {p}. Calculer [H₃O⁺] et donner son caractère.",
                      f"[H₃O⁺] = 10^{chr(8722)}{p} = {fr(10 ** (-(p)), 10)} mol/L\n"
                      f"pH {('<' if p < 7 else '=')} 7 → solution {'acide' if p < 7 else 'neutre'}",
                      "[H₃O⁺] = 10^-pH : une puissance de 10 négative."))
    for conc, p in ((1, 0), (0.1, 1), (0.01, 2), (0.001, 3), (10 ** -4, 4), (10 ** -5, 5)):
        cdisp = "1" if conc == 1 else ("0," + "0" * (p - 1) + "1")
        exos.append(E(2, "Contrôle", f"[H₃O⁺] = {cdisp} mol/L. Calculer le pH.",
                      f"pH = -log({cdisp}) = {p}",
                      "Compter les zéros : 10^-p → pH = p."))
    for p0, fact in ((2, 10), (1, 100), (3, 10), (2, 1000), (4, 100)):
        n = round(__import__('math').log10(fact))
        exos.append(E(2, "Contrôle", f"Un acide de pH = {p0} est dilué {fact} fois. Nouveau pH ?",
                      f"Dilution ×{fact} = ×10^{n} → pH augmente de {n}\n"
                      f"pH_final = {p0} + {n} = {p0 + n}",
                      "Diluer un acide : pH se rapproche de 7 (+1 par facteur 10)."))
    exos.append(E(3, "Type Examen Régional",
                  "Sécurité : décrire les précautions pour diluer un acide concentré, et expliquer "
                  "pourquoi on ne verse JAMAIS l'eau dans l'acide.",
                  "Blouse + lunettes + gants ; travailler dans un bac ; verser l'acide LENTEMENT "
                  "dans l'eau en agitant.\nLa dilution est FORTEMENT EXOTHERMIQUE : l'eau versée "
                  "sur l'acide pourrait projeter des gouttes d'acide concentré (ébullition locale "
                  "et projections dangereuses).",
                  "« On ne jette pas l'eau dans l'acide » : à retenir mot pour mot."))
    return (T, exos)


def electricite():
    T = "Le circuit électrique : courant et tension"
    exos = []
    for r, i_ma in ((100, 250), (220, 50), (330, 30), (47, 200), (470, 40), (68, 150), (12, 500)):
        u = r * i_ma / 1000
        exos.append(E(1, "Manuel", f"Un résistor de R = {r} Ω est parcouru par I = {i_ma} mA. "
                      "Calculer la tension U à ses bornes.",
                      f"I = {i_ma} mA = {fr(i_ma / 1000, 3)} A\nU = R×I = {r} × {fr(i_ma / 1000, 3)} = {fr(u)} V",
                      "Convertir mA → A AVANT la loi d'Ohm."))
    for u, r in ((6, 300), (9, 450), (12, 240), (4.5, 90), (24, 1200), (5, 250)):
        i = u / r * 1000
        exos.append(E(1, "Contrôle", f"Sous U = {fr(u)} V, un résistor de R = {r} Ω. Calculer I en mA.",
                      f"I = U/R = {fr(u)}/{r} = {fr(u / r, 4)} A = {fr(i)} mA",
                      "I = U/R ; 1 A = 1000 mA."))
    for i1, i2, i3 in ((2.0, 1.5, 0.8), (3.0, 0.7, 1.2), (0.5, 0.5, 0.6), (1.8, 2.4, 0.9),
                       (2.5, 1.0, 1.5), (4.0, 3.2, 0.5)):
        i4 = i1 + i2 - i3
        exos.append(E(2, "Contrôle", f"Loi des nœuds : I₁ = {fr(i1)} A et I₂ = {fr(i2)} A arrivent ; "
                      f"I₃ = {fr(i3)} A sort. Calculer I₄ (sortante).",
                      f"I₁ + I₂ = I₃ + I₄\n{fr(i1)} + {fr(i2)} = {fr(i3)} + I₄\n"
                      f"I₄ = {fr(i1 + i2)} - {fr(i3)} = {fr(i4)} A",
                      "Ce qui ENTRE = ce qui SORT."))
    for r1, r2, rep in ((30, 60, 20), (100, 150, 60), (20, 30, 12), (60, 120, 40), (75, 150, 50),
                        (200, 300, 120), (40, 60, 24), (90, 180, 60)):
        eq = r1 * r2 / (r1 + r2)
        assert abs(eq - rep) < 1e-9
        exos.append(E(2, "Contrôle", f"Calculer la résistance équivalente de R₁ = {r1} Ω et "
                      f"R₂ = {r2} Ω : en série, puis en parallèle.",
                      f"Série : R_eq = {r1} + {r2} = {r1 + r2} Ω\n"
                      f"Parallèle : 1/R_eq = 1/{r1} + 1/{r2} = 1/{rep} → R_eq = {rep} Ω\n"
                      f"(vérif produit/divisé : {r1}×{r2}/{r1 + r2} = {rep} ✓)",
                      "Parallèle : R_eq PLUS PETITE que chaque résistance."))
    for u, r1, r2 in ((12, 100, 150), (9, 60, 120), (12, 40, 60), (6, 30, 60), (24, 200, 300),
                      (9, 20, 30)):
        rp = r1 * r2 / (r1 + r2)
        req = r1 + rp
        i = u / req
        u2 = rp * i
        exos.append(E(3, "Type Examen Régional",
                      f"Générateur {fr(u)} V alimentant R₁ = {r1} Ω en série avec le groupement "
                      f"parallèle de R₂ = {r2} Ω et R₃ = {2 * r2} Ω. Calculer R_eq, I et U₂₃.",
                      f"Parallèle : R₂₃ = {r2}×{2 * r2}/{r2 + 2 * r2} = {fmt(F(rp).limit_denominator(1000))} Ω\n"
                      f"Série : R_eq = {r1} + {fmt(F(rp).limit_denominator(1000))} = {fmt(F(req).limit_denominator(1000))} Ω\n"
                      f"I = U/R_eq = {fr(u)}/{fmt(F(req).limit_denominator(1000))} = {fr(i, 3)} A\n"
                      f"U₂₃ = R₂₃×I = {fmt(F(rp).limit_denominator(1000))}×{fr(i, 3)} = {fr(u2)} V",
                      "Réduire le parallèle d'abord, puis le série ; loi d'Ohm à chaque étape."))
    return (T, exos)


def energie():
    T = "Puissance et énergie électriques"
    exos = []
    for p, u in ((1000, 230), (2000, 230), (750, 230), (1500, 230), (60, 230), (120, 12)):
        i = p / u
        exos.append(E(1, "Manuel", f"Un appareil porte « {u} V - {p} W ». Calculer l'intensité absorbée.",
                      f"I = P/U = {p}/{u} = {fr(i, 3)} A",
                      "I = P/U : détermine le calibre du fusible."))
    for p_w, h, jours, prix in ((1500, 3, 30, 1.2), (2000, 2, 30, 1.1), (100, 5, 30, 1.15),
                                (75, 8, 30, 1.2), (2500, 1.5, 30, 1.3), (60, 6, 30, 1.25)):
        e = p_w / 1000 * h * jours
        cout = e * prix
        exos.append(E(2, "Contrôle", f"Un appareil de {p_w} W fonctionne {fr(h)} h par jour pendant "
                      f"{jours} jours. Énergie en kWh puis coût à {fr(prix)} DH/kWh.",
                      f"E = P×t = {fr(p_w / 1000)} kW × {fr(h)} h × {jours} = {fr(e)} kWh\n"
                      f"Coût = {fr(e)} × {fr(prix)} = {fr(cout)} DH",
                      "P en kW, t en h → E en kWh ; 1 kWh = 3,6 × 10⁶ J."))
    for kwh in (2.5, 0.75, 5.5, 12, 0.2):
        j = kwh * 3.6
        exos.append(E(2, "Manuel", f"Convertir {fr(kwh)} kWh en joules.",
                      f"E = {fr(kwh)} × 3,6 × 10⁶ = {fr(j, 1)} × 10⁶ J = {fr(j * 10, 1)} × 10⁵ J",
                      "1 kWh = 3,6 × 10⁶ J = 3,6 MJ."))
    exos.append(E(3, "Type Examen Régional",
                  "Facture : 5 lampes de 20 W (5 h/j), un réfrigérateur 100 W en continu, une TV 80 W "
                  "(4 h/j), un lave-linge 500 W (1 h/j). Énergie mensuelle (30 j) et coût à 1,1 DH/kWh.",
                  "Lampes : 0,100 kW × 5 h × 30 = 15 kWh\nRéfrigérateur : 0,100 × 24 × 30 = 72 kWh\n"
                  "TV : 0,080 × 4 × 30 = 9,6 kWh\nLave-linge : 0,500 × 1 × 30 = 15 kWh\n"
                  "Total = 15 + 72 + 9,6 + 15 = 111,6 kWh → coût = 111,6 × 1,1 = 122,76 ≈ 123 DH",
                  "L'appareil EN CONTINU domine la facture malgré sa faible puissance."))
    return (T, exos)


def forces():
    T = "Principe des actions réciproques et inertie"
    exos = []
    for m, obj in ((0.2, "un téléphone"), (0.43, "un ballon"), (0.5, "un livre"),
                   (1.5, "un sachet de riz"), (75, "un élève"), (2.5, "une bouteille d'eau")):
        p = m * 9.8
        exos.append(E(1, "Manuel", f"Poids : {obj} de masse m = {fr(m)} kg. Calculer P "
                      "(g = 9,8 N/kg).",
                      f"P = m×g = {fr(m)} × 9,8 = {fr(p)} N",
                      "P = m·g avec m en KILOGRAMMES."))
    for m in (5, 2, 8, 12, 0.8, 3.5):
        p = m * 9.8
        exos.append(E(2, "Contrôle", f"Un objet de masse {fr(m)} kg est suspendu, immobile, à un câble. "
                      "Quelle est la tension du câble ? Justifier.",
                      f"Immobile → équilibre → les forces se compensent\n"
                      f"T = P = m×g = {fr(m)} × 9,8 = {fr(p)} N (verticale, vers le haut)",
                      "2 forces en équilibre : même norme, sens opposés."))
    for m, a in ((0.5, 6), (2, 3), (1.2, 5), (3, 2)):
        f = m * a
        exos.append(E(2, "Contrôle", f"(Pour aller plus loin) Un objet de masse {fr(m)} kg subit une "
                      f"force résultante F = {fr(f)} N. On admet F = m·a : calculer son accélération.",
                      f"a = F/m = {fr(f)}/{fr(m)} = {fr(a)} m/s²",
                      "Même structure que P = m·g : F = m·a (loi fondamentale, admise)."))
    exos.append(E(3, "Type Examen Régional",
                  "Une pomme (200 g) tombe : la Terre l'attire avec 1,96 N. Décrire la force réciproque "
                  "et expliquer pourquoi c'est la pomme qui « tombe » et pas la Terre.",
                  "Principe des actions réciproques : la pomme attire la Terre avec 1,96 N "
                  "(direction verticale, vers le haut, appliquée au centre de la Terre).\n"
                  "Même force, mais a = F/m : a(Terre) = 1,96/6×10²⁴ ≈ 0 (masse énorme) ; "
                  "a(pomme) = 1,96/0,2 = 9,8 m/s² → c'est la pomme qui bouge visiblement.",
                  "Même INTENSITÉ sur les deux corps ; les ACCÉLÉRATIONS diffèrent (F = m·a)."))
    return (T, exos)


def generators():
    return [atome(), mole(), reaction(), ph_exos(), electricite(), energie(), forces()]
