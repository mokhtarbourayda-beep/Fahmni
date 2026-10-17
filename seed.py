#!/usr/bin/env python3
"""
seed.py — Initialise la base Fahmni : lycées, matières, chapitres, exercices,
comptes de démonstration, groupes et messages d'exemple.

Lancement :  python3 seed.py          (crée fahmni.db si absente)
             python3 seed.py --reset  (efface et recrée tout)
"""
import sys

import db
import seed_curriculum
import seed_lycees

reset = "--reset" in sys.argv
db.init_db(reset=reset)

# déjà peuplée ?
if db.query("SELECT COUNT(*) c FROM subjects", one=True)["c"] > 0 and not reset:
    print("[seed] Base déjà peuplée — rien à faire (utilise --reset pour repartir de zéro)")
    sys.exit(0)

seed_lycees.seed()
seed_curriculum.seed(db)

# ---------------------------------------------------- comptes de démo ------
def mk_user(prenom, nom, email, pwd, lycee, classe, couleur):
    from app import hash_password
    return db.execute(
        "INSERT INTO users(prenom, nom, email, password_hash, lycee_id, classe_id, couleur) "
        "VALUES (?,?,?,?,?,?,?)",
        (prenom, nom, email, hash_password(pwd), lycee, classe, couleur))

l_sale = db.query("SELECT id FROM lycees WHERE nom LIKE '%Mohammed V%'", one=True)
l_rabat = db.query("SELECT id FROM lycees WHERE nom LIKE '%Descartes%'", one=True)
cls_tc = db.query("SELECT id FROM classes WHERE lycee_id=? AND nom='TC Sciences A'",
                  (l_sale["id"],), one=True)
cls_1bac = db.query("SELECT id FROM classes WHERE lycee_id=? AND nom='1BAC SE A'",
                    (l_sale["id"],), one=True)
cls_desc = db.query("SELECT id FROM classes WHERE lycee_id=? AND nom='1BAC SE A'",
                    (l_rabat["id"],), one=True)

demo = mk_user("Yassine", "Démo", "demo@fahmni.ma", "demo1234",
               l_sale["id"], cls_1bac["id"], "#2a9d8f")
u2 = mk_user("Salma", "B.", "salma@fahmni.ma", "demo1234",
             l_sale["id"], cls_1bac["id"], "#8e44ad")
u3 = mk_user("Omar", "K.", "omar@fahmni.ma", "demo1234",
             l_rabat["id"], cls_desc["id"], "#d97706")
u4 = mk_user("Hiba", "R.", "hiba@fahmni.ma", "demo1234",
             l_sale["id"], cls_tc["id"], "#2563eb")
print(f"[seed] utilisateurs : demo@fahmni.ma / demo1234 (+3 camarades)")

# ---------------------------------------------------------------- groupes --
g1 = db.execute(
    "INSERT INTO groups(nom, description, code, lycee_id, createur_id) VALUES (?,?,?,?,?)",
    ("1BAC SE A — Révisions Maths", "On révise suites & limites chaque soir à 20h 🔥",
     "MATH24", l_sale["id"], demo))
g2 = db.execute(
    "INSERT INTO groups(nom, description, code, lycee_id, createur_id) VALUES (?,?,?,?,?)",
    ("PC — Entraide Nationale", "Questions/réponses physique-chimie, tous lycées",
     "PCGROUP", None, u3))
for gid, uids in [(g1, [demo, u2, u4]), (g2, [u3, demo])]:
    for uid in uids:
        db.execute("INSERT OR IGNORE INTO group_members(group_id, user_id) VALUES (?,?)", (gid, uid))

msgs = [
    (g1, u2, "Salam tout le monde ! Quelqu'un a compris la somme géométrique ? 😅"),
    (g1, demo, "Wa alaykom salam ! S = 1er terme × (1 − q^n)/(1 − q). Je te montre ce soir à 20h"),
    (g1, u4, "Moi je bloque sur la récurrence, l'initialisation c'est toujours rang 0 ?"),
    (g1, demo, "Oui sauf indication contraire ! Étape 1 : on vérifie u_0. Étape 2 : hérédité. Étape 3 : conclusion."),
    (g2, u3, "Le prof a donné un titrage acide-base pour demain, qui a la relation d'équivalence ?"),
    (g2, demo, "À l'équivalence : Ca·Va = Cb·Vb (pour un couple 1/1) 💪"),
]
for gid, uid, txt in msgs:
    db.execute("INSERT INTO messages(group_id, user_id, content) VALUES (?,?,?)", (gid, uid, txt))
print(f"[seed] {len(msgs)} messages d'exemple, 2 groupes")

print("\n✅ Base prête !  Lance :  python3 app.py   →  http://localhost:5000")
print("   Compte démo : demo@fahmni.ma / demo1234")
