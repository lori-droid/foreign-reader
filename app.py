"""
外刊精读 (Foreign Journal Reader)
A web application for intensive reading of English articles from
foreign publications, with vocabulary and expression analysis.
"""

import json
import os
import time
import threading
from datetime import datetime, date, timezone, timedelta
from pathlib import Path
import urllib.request

from flask import Flask, render_template, jsonify, request

from reading_analyzer import ReadingAnalyzer
from classic_articles import CLASSIC_ARTICLES

app = Flask(__name__)

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

analyzer = ReadingAnalyzer()

# Beijing timezone (UTC+8)
CST = timezone(timedelta(hours=8))


def today_cst():
    """Get today's date in CST (UTC+8)."""
    return datetime.now(CST).date()


# ─── JSON persistence helpers ────────────────────────────────────

def _read_json(filename, default=None):
    path = DATA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def _write_json(filename, data):
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ─── Daily article selection (3 articles, rotates daily at CST midnight) ───

def get_daily_articles():
    """Select exactly 3 articles for today, one per category, rotating daily."""
    day_ord = today_cst().toordinal()

    # Group articles by category
    by_cat = {"politics_economics": [], "editorial": [], "literature": []}
    for i, a in enumerate(CLASSIC_ARTICLES):
        cat = a.get("category", "editorial")
        if cat in by_cat:
            by_cat[cat].append((i, a))

    selected = []
    for cat in ["politics_economics", "editorial", "literature"]:
        pool = by_cat.get(cat, [])
        if pool:
            idx = day_ord % len(pool)
            orig_idx, article = pool[idx]
            art = article.copy()
            art["source_type"] = "classic"
            art["_classic_index"] = orig_idx
            selected.append(art)

    return selected


def record_daily_articles(articles):
    """Archive today's articles into reading history."""
    today_key = today_cst().isoformat()
    history = _read_json("reading_history.json", {})
    if today_key not in history:
        archived = []
        for a in articles:
            archived.append({
                "title": a.get("title", ""),
                "source": a.get("source", ""),
                "source_icon": a.get("source_icon", ""),
                "category": a.get("category", ""),
                "category_label": a.get("category_label", ""),
                "summary": a.get("summary", ""),
                "source_type": a.get("source_type", ""),
                "has_full_text": a.get("has_full_text", False),
                "article_index": a.get("_classic_index"),
            })
        history[today_key] = archived
        _write_json("reading_history.json", history)


# ─── Routes ────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/daily-articles")
def daily_articles():
    """Get today's 3 recommended articles (one per category)."""
    articles = get_daily_articles()
    record_daily_articles(articles)

    # Include starred status
    stars = _read_json("starred.json", [])
    starred_titles = {s["title"] for s in stars}
    for a in articles:
        a["starred"] = a["title"] in starred_titles

    return jsonify({"success": True, "articles": articles})


@app.route("/api/history")
def reading_history():
    """Get reading history organized by date (descending)."""
    history = _read_json("reading_history.json", {})
    sorted_history = dict(sorted(history.items(), reverse=True))
    return jsonify({"success": True, "history": sorted_history})


@app.route("/api/article/<int:article_id>")
def get_article(article_id):
    """Get a specific classic article by index."""
    if 0 <= article_id < len(CLASSIC_ARTICLES):
        article = CLASSIC_ARTICLES[article_id]
        return jsonify({"success": True, "article": article})
    return jsonify({"success": False, "error": "Article not found"}), 404


@app.route("/api/analyze", methods=["POST"])
def analyze_article():
    """Analyze an article for intensive reading."""
    data = request.get_json()
    text = data.get("text", "")
    title = data.get("title", "")
    if not text:
        return jsonify({"success": False, "error": "No text provided"}), 400
    analysis = analyzer.analyze(text, title)
    return jsonify({"success": True, "analysis": analysis})


# ─── Starred articles ─────────────────────────────────────────────

@app.route("/api/starred", methods=["GET"])
def get_starred():
    """Get all starred articles."""
    stars = _read_json("starred.json", [])
    return jsonify({"success": True, "starred": stars})


@app.route("/api/starred", methods=["POST"])
def toggle_star():
    """Toggle star on an article. Body: {title, source, source_icon, category, ...}"""
    data = request.get_json()
    title = data.get("title", "")
    if not title:
        return jsonify({"success": False, "error": "No title"}), 400

    stars = _read_json("starred.json", [])
    existing = [s for s in stars if s["title"] == title]

    if existing:
        # Unstar
        stars = [s for s in stars if s["title"] != title]
        _write_json("starred.json", stars)
        return jsonify({"success": True, "starred": False})
    else:
        # Star
        stars.append({
            "title": title,
            "source": data.get("source", ""),
            "source_icon": data.get("source_icon", ""),
            "category": data.get("category", ""),
            "category_label": data.get("category_label", ""),
            "summary": data.get("summary", ""),
            "has_full_text": data.get("has_full_text", False),
            "article_index": data.get("_classic_index"),
            "starred_at": datetime.now(CST).isoformat(),
        })
        _write_json("starred.json", stars)
        return jsonify({"success": True, "starred": True})


# ─── Vocabulary CRUD ───────────────────────────────────────────────

@app.route("/api/vocabulary", methods=["GET"])
def get_vocabulary():
    vocab = _read_json("vocabulary.json", [])
    return jsonify({"success": True, "vocabulary": vocab})


@app.route("/api/vocabulary", methods=["POST"])
def add_vocabulary():
    data = request.get_json()
    vocab = _read_json("vocabulary.json", [])
    entry = {
        "word": data.get("word", ""),
        "definition": data.get("definition", ""),
        "example": data.get("example", ""),
        "source": data.get("source", ""),
        "added_at": datetime.now(CST).isoformat(),
        "review_count": 0,
        "last_reviewed": None,
    }
    vocab.append(entry)
    _write_json("vocabulary.json", vocab)
    return jsonify({"success": True, "entry": entry})


@app.route("/api/vocabulary/<int:index>", methods=["DELETE"])
def delete_vocabulary(index):
    vocab = _read_json("vocabulary.json", [])
    if 0 <= index < len(vocab):
        removed = vocab.pop(index)
        _write_json("vocabulary.json", vocab)
        return jsonify({"success": True, "removed": removed})
    return jsonify({"success": False, "error": "Index out of range"}), 404


@app.route("/api/vocabulary/<int:index>/review", methods=["POST"])
def review_vocabulary(index):
    vocab = _read_json("vocabulary.json", [])
    if 0 <= index < len(vocab):
        vocab[index]["review_count"] += 1
        vocab[index]["last_reviewed"] = datetime.now(CST).isoformat()
        _write_json("vocabulary.json", vocab)
        return jsonify({"success": True, "entry": vocab[index]})
    return jsonify({"success": False, "error": "Index out of range"}), 404


# ─── Keep-alive: prevent Render free tier from sleeping ──────────

def _keep_alive():
    """Ping self every 10 minutes to prevent Render free tier sleep."""
    url = os.environ.get("RENDER_EXTERNAL_URL", "")
    if not url:
        return  # Not on Render, skip
    while True:
        time.sleep(600)  # 10 minutes
        try:
            urllib.request.urlopen(url, timeout=10)
        except Exception:
            pass

# Start keep-alive thread on Render
if os.environ.get("RENDER"):
    threading.Thread(target=_keep_alive, daemon=True).start()


if __name__ == "__main__":
    print("=" * 60)
    print("  外刊精读 - Foreign Journal Reader")
    print("  Open http://localhost:5000 in your browser")
    print("  Articles rotate daily at CST midnight (UTC+8 00:00)")
    print("=" * 60)
    app.run(debug=True, port=5000)
