"""
seed_lycees.py — Annuaire initial des lycées et classes.
Priorité Salé/Rabat (zone cible), puis grandes villes. Chaque lycée reçoit
un jeu standard de classes TC et 1BAC.
"""
import db

# (nom, ville, type)
LYCEES = [
    ("Lycée Mohammed V d'Abbassi", "Salé", "public"),
    ("Lycée Al Massira", "Salé", "public"),
    ("Lycée Tabari", "Salé", "public"),
    ("Lycée Salé Al Jadida", "Salé", "public"),
    ("Lycée Descartes", "Rabat", "public"),
    ("Lycée Moulay Youssef", "Rabat", "public"),
    ("Lycée Ibn Timiya", "Rabat", "public"),
    ("Lycée Lyautey", "Casablanca", "public"),
    ("Lycée Mohammed VI d'Excellence", "Marrakech", "public"),
    ("Lycée Regnault", "Tanger", "public"),
    ("Lycée Ibn Battuta", "Tanger", "public"),
    ("Lycée Al Fida", "Fès", "public"),
]

# Classes standard créées pour chaque lycée : (niveau, filière, nb de divisions)
CLASSES_STD = [
    ("TC", "Sciences", 2),
    ("TC", "Lettres", 1),
    ("TC", "Technologie", 1),
    ("1BAC", "SE", 2),        # Sciences Expérimentales
    ("1BAC", "SM", 1),        # Sciences Maths
    ("1BAC", "SEG", 1),       # Sciences Économiques et Gestion
    ("1BAC", "STE", 1),       # Sciences et Technologies
]

LETTRES_DIV = ["A", "B", "C"]


def seed():
    n_lycees, n_classes = 0, 0
    for nom, ville, typ in LYCEES:
        lid = db.execute("INSERT INTO lycees(nom, ville, type) VALUES (?,?,?)",
                         (nom, ville, typ))
        n_lycees += 1
        for niveau, filiere, nb in CLASSES_STD:
            for i in range(nb):
                div = LETTRES_DIV[i]
                cls_nom = f"{niveau} {filiere} {div}".strip()
                db.execute(
                    "INSERT INTO classes(lycee_id, niveau, filiere, nom) VALUES (?,?,?,?)",
                    (lid, niveau, filiere, cls_nom))
                n_classes += 1
    print(f"[seed] {n_lycees} lycées, {n_classes} classes")


if __name__ == "__main__":
    db.init_db()
    seed()
