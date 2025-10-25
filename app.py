from flask import Flask, request, jsonify, g
from flask import redirect, url_for, render_template
import sqlite3
from datetime import datetime

DATABASE = 'quiz.db'
POWERS = [128,64,32,16,8,4,2,1]
TARGETS = [82,117,66,55,102,51,84,62,5,7]

app = Flask(__name__)

def get_db():
    db = getattr(g, '_db', None)
    if db is None:
        db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        g._db = db
    return db

@app.teardown_appcontext
def close_db(exc):
    db = getattr(g, '_db', None)
    if db is not None:
        db.close()

def init_db():
    db = sqlite3.connect(DATABASE)
    c = db.cursor()
    c.execute('''
      CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        score INTEGER,
        total INTEGER,
        details TEXT,
        created_at TEXT
      )
    ''')
    db.commit()
    db.close()

@app.route("/")
def index():
    # opcion A: servir plantilla del quiz directamente (si tienes templates/quiz.html)
    return render_template("quiz.html", powers=POWERS, targets=TARGETS)
    # opción B: redirigir a la API que devuelve datos del quiz
    # return redirect(url_for('get_quiz'))
    
@app.route('/api/v1/quiz', methods=['GET'])
def get_quiz():
    payload = [{"id": i, "target": t} for i,t in enumerate(TARGETS)]
    return jsonify({"powers": POWERS, "rows": payload})

@app.route('/api/v1/grade', methods=['POST'])
def grade():
    body = request.get_json(force=True)
    rows = body.get('rows', [])
    results = []
    score = 0
    for i, t in enumerate(TARGETS):
        bits = rows[i] if i < len(rows) else [0]*len(POWERS)
        bits = [int(b) for b in bits]
        computed = sum(p for p,b in zip(POWERS, bits) if b)
        ok = (computed == t)
        results.append({"id": i, "computed": computed, "target": t, "correct": ok})
        if ok: score += 1
    return jsonify({"results": results, "score": score, "total": len(TARGETS)})

@app.route('/api/v1/results', methods=['POST'])
def save_result():
    body = request.get_json(force=True)
    user_id = body.get('user_id','anon')
    score = int(body.get('score', 0))
    total = int(body.get('total', len(TARGETS)))
    details = body.get('details', '')
    db = get_db()
    db.execute('INSERT INTO results (user_id,score,total,details,created_at) VALUES (?,?,?,?,?)',
               (user_id, score, total, details, datetime.utcnow().isoformat()))
    db.commit()
    return jsonify({"ok": True}), 201

@app.route('/api/v1/leaderboard', methods=['GET'])
def leaderboard():
    limit = int(request.args.get('limit', 10))
    db = get_db()
    cur = db.execute('SELECT user_id, MAX(score) as best_score, created_at FROM results GROUP BY user_id ORDER BY best_score DESC LIMIT ?',
                     (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    return jsonify({"leaderboard": rows})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
