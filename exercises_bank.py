# -*- coding: utf-8 -*-
"""exercises_bank.py — Orchestrateur : insère les banques générées/rédigées (non destructif)."""


def sync(db):
    import bank_math, bank_pc, bank_svt_fr

    subjects = {r["code"]: r["id"] for r in db.query("SELECT * FROM subjects")}
    n_ins = n_skip = 0

    def add_exos(code, titre, exos):
        nonlocal n_ins, n_skip
        ch = db.query("SELECT id FROM chapters WHERE subject_id = ? AND niveau = 'TC' "
                      "AND titre = ?", (subjects[code], titre), one=True)
        if not ch:
            return
        for diff, source, enonce, solution, astuce, variantes in exos:
            dupe = db.query("SELECT id FROM exercises WHERE chapter_id = ? AND enonce = ?",
                            (ch["id"], enonce), one=True)
            if dupe:
                n_skip += 1
                continue
            db.execute(
                "INSERT INTO exercises(chapter_id, difficulte, source, enonce, solution, "
                "astuce, variantes) VALUES (?,?,?,?,?,?,?)",
                (ch["id"], diff, source, enonce, solution, astuce,
                 __import__("json").dumps(variantes, ensure_ascii=False)))
            n_ins += 1

    for titre, exos in bank_math.generators():
        add_exos("MATH", titre, exos)
    for titre, exos in bank_pc.generators():
        add_exos("PC", titre, exos)
    bank_svt_fr.sync(db)  # SVT/FR rédigés

    print(f"[exercises_bank] +{n_ins} exercices insérés ({n_skip} déjà présents)")
