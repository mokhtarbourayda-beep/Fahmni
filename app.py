#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
app.py — Plateforme FAHMNI (فهمني) : cours, Prof IA, exercices, annuaire,
communauté. Flask + SQLite, sans autre dépendance.

Lancement :  python3 app.py   (http://0.0.0.0:5000)
"""
import hashlib
import hmac
import json
import os
import re
import secrets
import string
from datetime import datetime
import hashlib as _hl
import urllib.request

from flask import (Flask, abort, g, jsonify, redirect, render_template,
                   request, send_file, url_for)

import db
import tutor_engine

app = Flask(__name__)
SECRET_FILE = os.environ.get("FAHMNI_SECRET") or os.path.join(os.path.dirname(__file__), ".secret")


class SessionPrefixMiddleware:
    """Accepte les URLs préfixées /s/<token>/... : permet la session sans
    cookies (indispensable dans les aperçus iframe qui les bloquent)."""
    def __init__(self, wsgi):
        self.wsgi = wsgi

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "/")
        m = re.match(r"^/s/([A-Za-z0-9\.\-_]+)(/.*)?$", path)
        if m:
            environ["FAHMNI_TOKEN"] = m.group(1)
            environ["PATH_INFO"] = m.group(2) or "/"
        return self.wsgi(environ, start_response)


def get_secret():
    if os.path.exists(SECRET_FILE):
        return open(SECRET_FILE, "rb").read()
    s = secrets.token_bytes(32)
    open(SECRET_FILE, "wb").write(s)
    return s


COOKIE = "fahmni_session"
NIVEAU_LABEL = {"TC": "Tronc Commun", "1BAC": "1ère Bac"}
DIFF_LABEL = {1: "Basique", 2: "Moyen", 3: "Type examen"}
DIFF_COLOR = {1: "#059669", 2: "#d97706", 3: "#dc2626"}


# ------------------------------------------------------------------- auth ---
def hash_password(pwd, salt=None):
    salt = salt or secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac("sha256", pwd.encode(), bytes.fromhex(salt), 200_000)
    return f"{salt}${h.hex()}"


def check_password(pwd, stored):
    try:
        salt, _ = stored.split("$", 1)
        return hmac.compare_digest(hash_password(pwd, salt), stored)
    except Exception:
        return False


def sign(value):
    return hmac.new(get_secret(), value.encode(), hashlib.sha256).hexdigest()


def set_session(user_id):
    val = str(user_id)
    token = f"{val}.{sign(val)}"
    resp = redirect(f"/s/{token}/dashboard")
    resp.set_cookie(COOKIE, token, httponly=True, samesite="Lax")
    return resp


def current_user():
    if hasattr(g, "user"):
        return g.user
    g.user = None
    raw = request.cookies.get(COOKIE, "") or request.environ.get("FAHMNI_TOKEN", "")
    if "." in raw:
        val, sig = raw.rsplit(".", 1)
        if hmac.compare_digest(sign(val), sig) and val.isdigit():
            g.user = db.query("SELECT * FROM users WHERE id = ?", (int(val),), one=True)
    return g.user


def login_required(f):
    from functools import wraps

    @wraps(f)
    def wrapper(*a, **kw):
        if not current_user():
            return redirect(url_for("connexion", next=request.path))
        return f(*a, **kw)
    return wrapper


app.jinja_env.globals.update(
    current_user=current_user,
    NIVEAU_LABEL=NIVEAU_LABEL, DIFF_LABEL=DIFF_LABEL, DIFF_COLOR=DIFF_COLOR,
    now=datetime.now().strftime("%Y"))


def user_niveau(user):
    if user and user["classe_id"]:
        cls = db.query("SELECT niveau FROM classes WHERE id = ?", (user["classe_id"],), one=True)
        if cls:
            return cls["niveau"]
    return "TC"


# ---------------------------------------------------------------- landing ---
@app.route("/")
def landing():
    stats = {
        "lycees": db.query("SELECT COUNT(*) c FROM lycees", one=True)["c"],
        "chapitres": db.query("SELECT COUNT(*) c FROM chapters", one=True)["c"],
        "exercices": db.query("SELECT COUNT(*) c FROM exercises", one=True)["c"],
        "eleves": db.query("SELECT COUNT(*) c FROM users", one=True)["c"],
    }
    subjects = db.query("SELECT * FROM subjects")
    return render_template("landing.html", stats=stats, subjects=subjects)


@app.route("/api/classes")
def api_classes():
    lid = request.args.get("lycee_id", type=int)
    if not lid:
        return jsonify([])
    rows = db.query("SELECT id, nom, niveau, filiere FROM classes WHERE lycee_id = ? ORDER BY id", (lid,))
    return jsonify([dict(r) for r in rows])


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    erreurs = []
    lycees = db.query("SELECT * FROM lycees ORDER BY (ville='Salé') DESC, ville, nom")
    form = {}
    if request.method == "POST":
        form = {k: request.form.get(k, "").strip() for k in
                ("prenom", "nom", "email", "motdepasse", "lycee_id", "classe_id")}
        if not re.fullmatch(r".{2,40}", form["prenom"]):
            erreurs.append("Prénom requis.")
        if not re.fullmatch(r".{2,40}", form["nom"]):
            erreurs.append("Nom requis.")
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", form["email"]):
            erreurs.append("Email invalide.")
        if len(form["motdepasse"]) < 6:
            erreurs.append("Mot de passe : 6 caractères minimum.")
        if not form["lycee_id"] or not form["classe_id"]:
            erreurs.append("Choisis ton lycée et ta classe.")
        if not erreurs and db.query("SELECT id FROM users WHERE email = ?", (form["email"],), one=True):
            erreurs.append("Cet email est déjà inscrit. Connecte-toi.")
        if not erreurs:
            uid = db.execute(
                "INSERT INTO users(prenom, nom, email, password_hash, lycee_id, classe_id, couleur) "
                "VALUES (?,?,?,?,?,?,?)",
                (form["prenom"], form["nom"], form["email"].lower(),
                 hash_password(form["motdepasse"]), int(form["lycee_id"]),
                 int(form["classe_id"]),
                 "#%06x" % secrets.randbelow(0xFFFFFF)))
            return set_session(uid)
    return render_template("inscription.html", lycees=lycees, erreurs=erreurs, form=form)


@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    erreurs = []
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        pwd = request.form.get("motdepasse", "")
        user = db.query("SELECT * FROM users WHERE email = ?", (email,), one=True)
        if user and check_password(pwd, user["password_hash"]):
            return set_session(user["id"])
        erreurs.append("Email ou mot de passe incorrect.")
    demo = db.query("SELECT email FROM users WHERE email LIKE 'demo%' LIMIT 1", one=True)
    return render_template("connexion.html", erreurs=erreurs, demo_email=demo["email"] if demo else None)


@app.route("/deconnexion")
def deconnexion():
    resp = redirect(url_for("landing"))
    resp.delete_cookie(COOKIE)
    return resp


# --------------------------------------------------------------- dashboard --
@app.route("/dashboard")
@login_required
def dashboard():
    u = current_user()
    niveau = request.args.get("niveau") or user_niveau(u)
    if niveau not in NIVEAU_LABEL:
        niveau = user_niveau(u)
    subjects = db.query("SELECT * FROM subjects")
    counts = {
        (r["subject_id"], r["niveau"]): r["c"]
        for r in db.query("SELECT subject_id, niveau, COUNT(*) c FROM chapters GROUP BY subject_id, niveau")}
    ex_counts = {
        (r["subject_id"], r["niveau"]): r["c"]
        for r in db.query(
            "SELECT c.subject_id, c.niveau, COUNT(*) c FROM exercises e "
            "JOIN chapters c ON c.id = e.chapter_id GROUP BY c.subject_id, c.niveau")}
    mes_groupes = db.query(
        "SELECT gr.*, (SELECT COUNT(*) FROM group_members m WHERE m.group_id = gr.id) membres "
        "FROM groups gr JOIN group_members m ON m.group_id = gr.id "
        "WHERE m.user_id = ? ORDER BY gr.id DESC", (u["id"],))
    tutor_count = db.query("SELECT COUNT(*) c FROM tutor_logs WHERE user_id = ?",
                           (u["id"],), one=True)["c"]
    return render_template("dashboard.html", user=u, niveau=niveau, subjects=subjects,
                           counts=counts, ex_counts=ex_counts, mes_groupes=mes_groupes,
                           tutor_count=tutor_count)


# ------------------------------------------------------------------ cours ---
@app.route("/cours")
@login_required
def cours():
    niveau = request.args.get("niveau", user_niveau(current_user()))
    if niveau not in NIVEAU_LABEL:
        niveau = "TC"
    subjects = db.query("SELECT * FROM subjects")
    chapters = db.query(
        "SELECT c.*, s.code, s.nom as sujet, s.couleur, s.icone, "
        "(SELECT COUNT(*) FROM exercises e WHERE e.chapter_id = c.id) n_ex "
        "FROM chapters c JOIN subjects s ON s.id = c.subject_id "
        "WHERE c.niveau = ? ORDER BY s.id, c.semestre, c.id", (niveau,))
    par_matiere = {s["code"]: {1: [], 2: []} for s in subjects}
    for c in chapters:
        par_matiere[c["code"]].get(c["semestre"] or 1, par_matiere[c["code"]][2])\
            .append(c)
    return render_template("cours.html", niveau=niveau, subjects=subjects,
                           par_matiere=par_matiere)


@app.route("/chapitre/<int:cid>")
@login_required
def chapitre(cid):
    ch = db.query(
        "SELECT c.*, s.code, s.nom as sujet, s.couleur, s.icone FROM chapters c "
        "JOIN subjects s ON s.id = c.subject_id WHERE c.id = ?", (cid,), one=True)
    if not ch:
        abort(404)
    lecon = {}
    if ch["lecon"]:
        lecon = json.loads(ch["lecon"])
    exercices = db.query(
        "SELECT id, difficulte, source, substr(enonce, 1, 90) apercu FROM exercises "
        "WHERE chapter_id = ? ORDER BY difficulte", (cid,))
    return render_template("chapitre.html", ch=ch, lecon=lecon, exercices=exercices)


# -------------------------------------------------------------- exercices ---
@app.route("/exercices")
@login_required
def exercices():
    code = request.args.get("matiere", "")
    diff = request.args.get("difficulte", type=int)
    if not diff and request.args.get("difficile"):
        diff = 3                      # case « exercices difficiles »
    ch_id = request.args.get("chapitre", type=int)
    sql = ("SELECT e.*, c.titre as chapitre, c.niveau, s.code, s.icone, s.couleur "
           "FROM exercises e JOIN chapters c ON c.id = e.chapter_id "
           "JOIN subjects s ON s.id = c.subject_id WHERE 1=1")
    args = []
    if code:
        sql += " AND s.code = ?"
        args.append(code)
    if diff:
        sql += " AND e.difficulte = ?"
        args.append(diff)
    if ch_id:
        sql += " AND e.chapter_id = ?"
        args.append(ch_id)
    sql += " ORDER BY c.niveau, c.id, e.difficulte"
    exos = db.query(sql, args)
    subjects = db.query("SELECT * FROM subjects")
    chapitres = db.query(
        "SELECT c.id, c.titre, c.semestre, s.code FROM chapters c "
        "JOIN subjects s ON s.id = c.subject_id ORDER BY s.id, c.semestre, c.id")
    return render_template("exercices.html", exos=exos, subjects=subjects,
                           chapitres=chapitres, f_matiere=code, f_diff=diff,
                           f_chapitre=ch_id, f_difficile=bool(request.args.get("difficile")))


# ------------------------------------------------------------- générateur ---
@app.route("/generateur")
@login_required
def generateur():
    import gen_exercices
    dispo = gen_exercices.themes_disponibles()
    themes = {}
    for code, titres in dispo.items():
        rows = db.query(
            "SELECT c.titre, c.semestre FROM chapters c JOIN subjects s ON s.id = c.subject_id "
            "WHERE s.code = ? AND c.niveau = 'TC' ORDER BY c.semestre, c.id", (code,))
        ordre = {r["titre"]: r["semestre"] or 1 for r in rows}
        themes[code] = sorted((t for t in titres if t in ordre),
                              key=lambda t: (ordre[t], t))
    return render_template("gen.html", themes=themes)


@app.route("/api/generateur", methods=["POST"])
@login_required
def api_generateur():
    import gen_exercices
    data = request.get_json(silent=True) or {}
    code = data.get("matiere", "MATH")
    if code not in ("MATH", "PC", "SVT", "FR"):
        code = "MATH"
    ex = gen_exercices.generer(code, data.get("chapitre") or "", data.get("difficulte") or None)
    if not ex:
        return jsonify({"error": "Aucun générateur pour cette matière"}), 404
    return jsonify(ex)


@app.route("/exercice/<int:eid>")
@login_required
def exercice(eid):
    ex = db.query(
        "SELECT e.*, c.titre as chapitre, c.niveau, c.subject_id, s.code, s.nom as sujet, "
        "s.icone, s.couleur FROM exercises e JOIN chapters c ON c.id = e.chapter_id "
        "JOIN subjects s ON s.id = c.subject_id WHERE e.id = ?", (eid,), one=True)
    if not ex:
        abort(404)
    variantes = json.loads(ex["variantes"]) if ex["variantes"] else []
    suivants = db.query(
        "SELECT id FROM exercises WHERE chapter_id = ? AND id != ? ORDER BY difficulte, id",
        (ex["chapter_id"], eid))
    return render_template("exercice.html", ex=ex, variantes=variantes,
                           suivants=suivants)


# -------------------------------------------------------------------- prof --
@app.route("/prof")
@login_required
def prof():
    u = current_user()
    historique = db.query(
        "SELECT question, answer, created_at FROM tutor_logs WHERE user_id = ? "
        "ORDER BY id DESC LIMIT 10", (u["id"],))
    tutor, live = tutor_engine.get_tutor()
    matieres = db.query("SELECT * FROM subjects")
    initial_q = request.args.get("question", "")
    return render_template("prof.html", historique=list(reversed(historique)),
                           live=live, matieres=matieres, initial_q=initial_q)


@app.route("/api/prof", methods=["POST"])
@login_required
def api_prof():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()[:1000]
    if not question:
        return jsonify({"error": "question vide"}), 400
    tutor, live = tutor_engine.get_tutor()
    try:
        answer = tutor.respond(question, db, user_id=current_user()["id"])
    except Exception as e:
        answer = f"⚠️ Erreur du moteur ({e}). Réessaie ou reformule."
    db.execute("INSERT INTO tutor_logs(user_id, question, answer) VALUES (?,?,?)",
               (current_user()["id"], question, answer))
    return jsonify({"answer": answer, "mode": "live" if live else "demo"})


@app.route("/api/public_url")
def api_public_url():
    """URL publique (tunnel) utilisée pour ouvrir l'app hors aperçu (micro...)."""
    cfg = tutor_engine.load_config()
    return jsonify({"url": cfg.get("public_url") or ""})


# ---------------------------------------------------- voix du prof (TTS) ---
TTS_CACHE = os.environ.get("FAHMNI_TTSCACHE") or os.path.join(app.static_folder, "tts_cache")


@app.route("/api/tts", methods=["POST"])
@login_required
def api_tts():
    """Voix neurale FRANÇAISE du Prof (Edge TTS, gratuit, haute qualité).
    Fallback automatique côté client si indisponible."""
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()[:600]
    if not text:
        return jsonify({"error": "vide"}), 400
    cfg = tutor_engine.load_config()
    voice = cfg.get("tts_voice", "fr-FR-HenriNeural")
    os.makedirs(TTS_CACHE, exist_ok=True)
    import hashlib as _h
    h = _h.md5(f"{voice}|{text}".encode()).hexdigest()
    path = os.path.join(TTS_CACHE, h + ".mp3")
    if not os.path.exists(path):
        try:
            import asyncio
            import edge_tts

            async def _gen():
                await edge_tts.Communicate(text, voice).save(path)

            asyncio.run(_gen())
        except Exception as e:
            return jsonify({"fallback": "navigateur", "err": str(e)[:120]}), 501
    return send_file(path, mimetype="audio/mpeg")


# ---------------------------------------------------------------- annuaire --
@app.route("/annuaire")
@login_required
def annuaire():
    ville = request.args.get("ville", "")
    villes = [r["ville"] for r in db.query("SELECT DISTINCT ville FROM lycees ORDER BY ville")]
    sql = ("SELECT l.*, COUNT(c.id) n_classes, "
           "(SELECT COUNT(*) FROM users u WHERE u.lycee_id = l.id) n_eleves "
           "FROM lycees l LEFT JOIN classes c ON c.lycee_id = l.id WHERE 1=1")
    args = []
    if ville:
        sql += " AND l.ville = ?"
        args.append(ville)
    sql += " GROUP BY l.id ORDER BY (l.ville='Salé') DESC, l.ville, l.nom"
    lycees = db.query(sql, args)
    return render_template("annuaire.html", lycees=lycees, villes=villes, f_ville=ville)


@app.route("/annuaire/<int:lid>")
@login_required
def lycee(lid):
    l = db.query("SELECT * FROM lycees WHERE id = ?", (lid,), one=True)
    if not l:
        abort(404)
    classes = db.query(
        "SELECT c.*, (SELECT COUNT(*) FROM users u WHERE u.classe_id = c.id) n_eleves "
        "FROM classes c WHERE c.lycee_id = ? ORDER BY c.niveau, c.filiere, c.nom", (lid,))
    groupes = db.query(
        "SELECT g.*, (SELECT COUNT(*) FROM group_members m WHERE m.group_id = g.id) membres "
        "FROM groups g WHERE g.lycee_id = ? ORDER BY g.id DESC", (lid,))
    return render_template("lycee.html", l=l, classes=classes, groupes=groupes)


# -------------------------------------------------------------- communauté --
@app.route("/communaute")
@login_required
def communaute():
    u = current_user()
    groupes = db.query(
        "SELECT g.*, l.nom as lycee_nom, (SELECT COUNT(*) FROM group_members m "
        "WHERE m.group_id = g.id) membres, "
        "EXISTS(SELECT 1 FROM group_members x WHERE x.group_id = g.id AND x.user_id = ?) membre "
        "FROM groups g LEFT JOIN lycees l ON l.id = g.lycee_id ORDER BY g.id DESC", (u["id"],))
    return render_template("communaute.html", groupes=groupes)


def gen_code():
    alphabet = string.ascii_uppercase + string.digits
    while True:
        code = "".join(secrets.choice(alphabet) for _ in range(6))
        if not db.query("SELECT id FROM groups WHERE code = ?", (code,), one=True):
            return code


@app.route("/communaute/creer", methods=["POST"])
@login_required
def creer_groupe():
    u = current_user()
    nom = request.form.get("nom", "").strip()[:50]
    desc = request.form.get("description", "").strip()[:200]
    scope = request.form.get("scope", "")
    if len(nom) < 3:
        return redirect(url_for("communaute"))
    lid = u["lycee_id"] if scope == "lycee" else None
    gid = db.execute(
        "INSERT INTO groups(nom, description, code, lycee_id, createur_id) VALUES (?,?,?,?,?)",
        (nom, desc, gen_code(), lid, u["id"]))
    db.execute("INSERT INTO group_members(group_id, user_id) VALUES (?,?)", (gid, u["id"]))
    return redirect(url_for("groupe", gid=gid))


@app.route("/communaute/rejoindre", methods=["POST"])
@login_required
def rejoindre_groupe():
    u = current_user()
    code = request.form.get("code", "").strip().upper()
    gr = db.query("SELECT * FROM groups WHERE code = ?", (code,), one=True)
    if not gr:
        return redirect(url_for("communaute"))
    db.execute("INSERT OR IGNORE INTO group_members(group_id, user_id) VALUES (?,?)",
               (gr["id"], u["id"]))
    return redirect(url_for("groupe", gid=gr["id"]))


@app.route("/communaute/quitter/<int:gid>", methods=["POST"])
@login_required
def quitter_groupe(gid):
    u = current_user()
    db.execute("DELETE FROM group_members WHERE group_id = ? AND user_id = ?", (gid, u["id"]))
    return redirect(url_for("communaute"))


@app.route("/groupe/<int:gid>")
@login_required
def groupe(gid):
    u = current_user()
    gr = db.query(
        "SELECT g.*, l.nom as lycee_nom FROM groups g LEFT JOIN lycees l ON l.id = g.lycee_id "
        "WHERE g.id = ?", (gid,), one=True)
    if not gr:
        abort(404)
    membre = db.query("SELECT 1 FROM group_members WHERE group_id = ? AND user_id = ?",
                      (gid, u["id"]), one=True)
    if not membre:
        return redirect(url_for("communaute"))
    messages = db.query(
        "SELECT m.*, u.prenom, u.nom, u.couleur FROM messages m "
        "JOIN users u ON u.id = m.user_id WHERE m.group_id = ? ORDER BY m.id DESC LIMIT 50",
        (gid,))
    return render_template("groupe.html", gr=gr, messages=list(reversed(messages)))


@app.route("/api/groupe/<int:gid>/messages")
@login_required
def api_messages(gid):
    u = current_user()
    if not db.query("SELECT 1 FROM group_members WHERE group_id = ? AND user_id = ?",
                    (gid, u["id"]), one=True):
        return jsonify({"error": "non membre"}), 403
    after = request.args.get("after", type=int) or 0
    rows = db.query(
        "SELECT m.id, m.content, m.created_at, u.prenom, u.nom, u.couleur, m.user_id "
        "FROM messages m JOIN users u ON u.id = m.user_id "
        "WHERE m.group_id = ? AND m.id > ? ORDER BY m.id", (gid, after))
    return jsonify([dict(r) for r in rows])


@app.route("/api/groupe/<int:gid>/envoyer", methods=["POST"])
@login_required
def api_envoyer(gid):
    u = current_user()
    if not db.query("SELECT 1 FROM group_members WHERE group_id = ? AND user_id = ?",
                    (gid, u["id"]), one=True):
        return jsonify({"error": "non membre"}), 403
    data = request.get_json(silent=True) or {}
    content = (data.get("content") or "").strip()[:1000]
    if not content:
        return jsonify({"error": "vide"}), 400
    mid = db.execute("INSERT INTO messages(group_id, user_id, content) VALUES (?,?,?)",
                     (gid, u["id"], content))
    return jsonify({"id": mid})


# ------------------------------------------------------------------ profil --
@app.route("/profil")
@login_required
def profil():
    u = current_user()
    info = db.query(
        "SELECT u.*, l.nom lycee_nom, c.nom classe_nom FROM users u "
        "LEFT JOIN lycees l ON l.id = u.lycee_id LEFT JOIN classes c ON c.id = u.classe_id "
        "WHERE u.id = ?", (u["id"],), one=True)
    n_questions = db.query("SELECT COUNT(*) c FROM tutor_logs WHERE user_id = ?",
                           (u["id"],), one=True)["c"]
    mes_groupes = db.query(
        "SELECT g.*, g.code FROM groups g JOIN group_members m ON m.group_id = g.id "
        "WHERE m.user_id = ?", (u["id"],))
    return render_template("profil.html", u=info, n_questions=n_questions,
                           mes_groupes=mes_groupes)


# ------------------------------------------------------------------- main ---
@app.after_request
def rewrite_links(resp):
    """Si l'utilisateur est identifié par token d'URL (pas de cookie), réécrit
    toutes les URLs internes du HTML pour propager la session."""
    tok = request.environ.get("FAHMNI_TOKEN", "")
    if (tok and resp.content_type.startswith("text/html")
            and resp.status_code == 200 and resp.direct_passthrough is False):
        body = resp.get_data(as_text=True)
        body = body.replace('href="/', f'href="/s/{tok}/')
        body = body.replace("href='/", f"href='/s/{tok}/")
        body = body.replace('action="/', f'action="/s/{tok}/')
        body = body.replace("fetch('/", f"fetch('/s/{tok}/")
        body = body.replace("fetch(`/", f"fetch(`/s/{tok}/")
        body = body.replace('fetch("/', f'fetch("/s/{tok}/')
        resp.set_data(body)
    return resp


# activation du middleware
app.wsgi_app = SessionPrefixMiddleware(app.wsgi_app)


@app.teardown_appcontext
def close_db(exc):
    # chaque helper ouvre sa connexion courte : rien à faire ici
    pass


if __name__ == "__main__":
    if not os.path.exists(db.DB_PATH):
        print("Base absente — lance d'abord : python3 seed.py")
        db.init_db()
    try:
        import curriculum_tc_math, curriculum_tc_pc, curriculum_tc_svt, curriculum_tc_fr
        for mod in (curriculum_tc_math, curriculum_tc_pc, curriculum_tc_svt,
                    curriculum_tc_fr):
            mod.sync(db)                     # ajoute/enrichit chapitres + exercices
        import exercises_bank
        exercises_bank.sync(db)              # banque massive d'exercices (générés vérifiés)
    except Exception as e:
        print("[curriculum] sync ignorée :", e)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=False)
