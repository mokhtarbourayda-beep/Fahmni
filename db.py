"""
db.py — Couche base de données SQLite de la plateforme Fahmni.
Schéma complet + helpers. Aucune dépendance externe (sqlite3 stdlib).
"""
import os
import sqlite3

DB_PATH = os.environ.get("FAHMNI_DB") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "fahmni.db")

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS lycees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    ville TEXT NOT NULL,
    type TEXT DEFAULT 'public'
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lycee_id INTEGER NOT NULL REFERENCES lycees(id),
    niveau TEXT NOT NULL,          -- TC | 1BAC
    filiere TEXT NOT NULL,         -- Sciences | Lettres | Technologie | SE | SM | SEG | STE
    nom TEXT NOT NULL              -- ex: "TC Sciences A"
);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom TEXT NOT NULL,
    nom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    lycee_id INTEGER REFERENCES lycees(id),
    classe_id INTEGER REFERENCES classes(id),
    couleur TEXT DEFAULT '#16425b',
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,     -- MATH | PC | SVT | FR
    nom TEXT NOT NULL,
    couleur TEXT NOT NULL,
    icone TEXT NOT NULL            -- emoji
);

CREATE TABLE IF NOT EXISTS chapters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL REFERENCES subjects(id),
    niveau TEXT NOT NULL,          -- TC | 1BAC
    semestre INTEGER DEFAULT 1,    -- 1er ou 2e semestre
    titre TEXT NOT NULL,
    resume TEXT DEFAULT '',        -- accroche courte
    lecon TEXT DEFAULT ''          -- leçon structurée (JSON: méthodes, exemples, pièges)
);

CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chapter_id INTEGER NOT NULL REFERENCES chapters(id),
    difficulte INTEGER NOT NULL,   -- 1 basique | 2 moyen | 3 type examen
    source TEXT NOT NULL,          -- Manuel | Contrôle | Type Examen Régional | Type Examen National
    enonce TEXT NOT NULL,
    solution TEXT NOT NULL,
    astuce TEXT DEFAULT '',
    variantes TEXT DEFAULT '[]'    -- JSON [{enonce, solution}]
);

CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    description TEXT DEFAULT '',
    code TEXT NOT NULL UNIQUE,     -- code d'invitation (6 caractères)
    lycee_id INTEGER REFERENCES lycees(id),
    createur_id INTEGER NOT NULL REFERENCES users(id),
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS group_members (
    group_id INTEGER NOT NULL REFERENCES groups(id),
    user_id INTEGER NOT NULL REFERENCES users(id),
    joined_at TEXT DEFAULT (datetime('now')),
    PRIMARY KEY (group_id, user_id)
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL REFERENCES groups(id),
    user_id INTEGER NOT NULL REFERENCES users(id),
    content TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS tutor_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES users(id),
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);
"""


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(reset=False):
    if reset and os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = get_db()
    conn.executescript(SCHEMA)
    # migration douce : colonne semestre pour les bases existantes
    cols = [r[1] for r in conn.execute("PRAGMA table_info(chapters)")]
    if "semestre" not in cols:
        conn.execute("ALTER TABLE chapters ADD COLUMN semestre INTEGER DEFAULT 1")
    conn.commit()
    conn.close()


def query(sql, args=(), one=False):
    conn = get_db()
    rows = conn.execute(sql, args).fetchall()
    conn.close()
    return (rows[0] if rows else None) if one else rows


def execute(sql, args=()):
    conn = get_db()
    cur = conn.execute(sql, args)
    conn.commit()
    last = cur.lastrowid
    conn.close()
    return last
