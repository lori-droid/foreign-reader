"""
外刊精读 (Foreign Journal Reader) — v3 静态展示版
方案 1: 文章 JSON 在 articles/ 目录,Cowork 本地生成 → git push → Render 免费部署
Render 不需要任何 API key,网站只做展示。
"""
import json
import os
import time
import threading
import secrets
from datetime import datetime, timezone, timedelta
from pathlib import Path
from functools import wraps
import urllib.request

from flask import (
    Flask, render_template, jsonify, request,
    session, redirect, url_for,
)

import articles_store

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", secrets.token_hex(16))

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
CST = timezone(timedelta(hours=8))

# 可选: 整站访问密码(不填则公开访问)
SITE_PASSWORD = os.environ.get("SITE_PASSWORD", "")

CATEGORY_LABELS = {
    "editorial": "社论评论",
    "feature": "专题特写",
    "politics_economics": "政经科学",
    "culture": "文化艺术",
    "tech": "科技评论",
    "longread": "深度长文",
}

SOURCE_ICONS = {
    "The Guardian": "📰",
    "The Economist": "📊",
    "The New Yorker": "🗽",
    "The Atlantic": "🌊",
    "BBC": "🎙️",
    "BBC Future": "🔬",
    "Financial Times": "💼",
    "The New York Times": "🗞️",
    "Reuters": "📡",
    "Nature": "🔬",
}


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


# ─── 可选的整站密码保护 ───────────────────────────────────────
def login_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        if not SITE_PASSWORD:
            return fn(*a, **kw)
        if session.get("auth_site"):
            return fn(*a, **kw)
        if request.path.startswith("/api/"):
            return jsonify({"success": False, "error": "未授权"}), 401
        return redirect(url_for("login", next=request.path))
    return wrapper


@app.route("/login", methods=["GET", "POST"])
def login():
    nxt = request.args.get("next", "/")
    if request.method == "POST":
        if request.form.get("password", "") == SITE_PASSWORD and SITE_PASSWORD:
            session["auth_site"] = True
            return redirect(nxt)
        return render_template("login.html", error="密码错误", nxt=nxt, role="site")
    return render_template("login.html", error=None, nxt=nxt, role="site")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ─── 前台 ────────────────────────────────────────────────────
@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/api/daily-articles")
@login_required
def daily_articles():
    arts = articles_store.list_articles()
    stars = _read_json("starred.json", [])
    starred_ids = {s.get("article_id") for s in stars}
    for a in arts:
        a["starred"] = a["_id"] in starred_ids
        a["source_icon"] = a.get("source_icon") or SOURCE_ICONS.get(a.get("source", ""), "📄")
        a["category_label"] = a.get("category_label") or CATEGORY_LABELS.get(a.get("category", ""), "")
        a["has_full_text"] = bool(a.get("full_text"))

    today_key = datetime.now(CST).date().isoformat()
    history = _read_json("reading_history.json", {})
    if today_key not in history and arts:
        history[today_key] = [{
            "title": a.get("title"),
            "source": a.get("source"),
            "source_icon": a.get("source_icon"),
            "category_label": a.get("category_label"),
            "summary": a.get("summary"),
            "article_id": a["_id"],
            "has_full_text": True,
        } for a in arts]
        _write_json("reading_history.json", history)

    return jsonify({"success": True, "articles": arts})


@app.route("/api/article/<article_id>")
@login_required
def get_article(article_id):
    art = articles_store.get_article(article_id)
    if not art:
        return jsonify({"success": False, "error": "Article not found"}), 404
    return jsonify({"success": True, "article": art})


@app.route("/api/analyze", methods=["POST"])
@login_required
def analyze_article():
    """阅读页打开文章时调,直接返回已存好的精读注释"""
    data = request.get_json()
    article_id = data.get("article_id")
    text = data.get("text", "")
    title = data.get("title", "")

    if article_id:
        art = articles_store.get_article(article_id)
        if art:
            words = (text or art.get("full_text", "")).lower().split()
            return jsonify({"success": True, "analysis": {
                "title": art.get("title", title),
                "word_count": len(words),
                "unique_words": len(set(words)),
                "vocabulary": art.get("annotations_vocab", []),
                "phrases": art.get("annotations_phrases", []),
                "complex_sentences": art.get("annotations_sentences", []),
                "difficulty_assessment": {
                    "level": "intermediate",
                    "total_words": len(words),
                    "avg_word_length": round(sum(len(w) for w in words) / max(len(words), 1), 1),
                    "indicators": [],
                },
                "article_link": art.get("link", ""),
            }})

    return jsonify({"success": False, "error": "未找到文章"}), 404


@app.route("/api/history")
@login_required
def reading_history():
    history = _read_json("reading_history.json", {})
    return jsonify({"success": True, "history": dict(sorted(history.items(), reverse=True))})


@app.route("/api/starred", methods=["GET"])
@login_required
def get_starred():
    return jsonify({"success": True, "starred": _read_json("starred.json", [])})


@app.route("/api/starred", methods=["POST"])
@login_required
def toggle_star():
    data = request.get_json()
    article_id = data.get("article_id") or data.get("_id")
    title = data.get("title", "")
    if not article_id and not title:
        return jsonify({"success": False, "error": "需要 article_id 或 title"}), 400
    stars = _read_json("starred.json", [])
    key = article_id or title
    if any((s.get("article_id") or s.get("title")) == key for s in stars):
        stars = [s for s in stars if (s.get("article_id") or s.get("title")) != key]
        _write_json("starred.json", stars)
        return jsonify({"success": True, "starred": False})
    stars.append({
        "article_id": article_id, "title": title,
        "source": data.get("source", ""), "source_icon": data.get("source_icon", ""),
        "category_label": data.get("category_label", ""), "summary": data.get("summary", ""),
        "starred_at": datetime.now(CST).isoformat(),
    })
    _write_json("starred.json", stars)
    return jsonify({"success": True, "starred": True})


@app.route("/api/vocabulary", methods=["GET"])
@login_required
def get_vocab():
    return jsonify({"success": True, "vocabulary": _read_json("vocabulary.json", [])})


@app.route("/api/vocabulary", methods=["POST"])
@login_required
def add_vocab():
    data = request.get_json()
    vocab = _read_json("vocabulary.json", [])
    vocab.append({
        "word": data.get("word", ""), "definition": data.get("definition", ""),
        "example": data.get("example", ""), "source": data.get("source", ""),
        "added_at": datetime.now(CST).isoformat(),
        "review_count": 0, "last_reviewed": None,
    })
    _write_json("vocabulary.json", vocab)
    return jsonify({"success": True, "entry": vocab[-1]})


@app.route("/api/vocabulary/<int:idx>", methods=["DELETE"])
@login_required
def del_vocab(idx):
    vocab = _read_json("vocabulary.json", [])
    if 0 <= idx < len(vocab):
        removed = vocab.pop(idx)
        _write_json("vocabulary.json", vocab)
        return jsonify({"success": True, "removed": removed})
    return jsonify({"success": False}), 404


# ─── Keep-alive on Render ──────────────────────────────────────
def _keep_alive():
    url = os.environ.get("RENDER_EXTERNAL_URL", "")
    if not url:
        return
    while True:
        time.sleep(600)
        try:
            urllib.request.urlopen(url, timeout=10)
        except Exception:
            pass

if os.environ.get("RENDER"):
    threading.Thread(target=_keep_alive, daemon=True).start()


if __name__ == "__main__":
    print("=" * 60)
    print("  外刊精读 v3 — Foreign Journal Reader")
    print("  http://localhost:5000/")
    if not SITE_PASSWORD:
        print("  ℹ️  SITE_PASSWORD 未设置, 阅读端公开访问")
    print("=" * 60)
    app.run(debug=True, port=5000)
