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


# ─── P2: 学习数据 / 统计 / 搜索 / 目标 ───────────────────────
@app.route("/api/activity")
@login_required
def api_activity():
    """返回过去 365 天每日活动量,用于热力图。
    return: { "2026-05-29": { opened: 2, vocab_added: 5, vocab_reviewed: 10, score: 17 }, ... }
    """
    out = {}
    # 阅读历史
    history = _read_json("reading_history.json", {})
    for date_key, articles in history.items():
        out.setdefault(date_key, {"opened": 0, "vocab_added": 0, "vocab_reviewed": 0})
        out[date_key]["opened"] += len(articles)
    # 生词添加 (按 added_at)
    vocab = _read_json("vocabulary.json", [])
    for v in vocab:
        if v.get("added_at"):
            d = v["added_at"][:10]
            out.setdefault(d, {"opened": 0, "vocab_added": 0, "vocab_reviewed": 0})
            out[d]["vocab_added"] += 1
        if v.get("last_reviewed"):
            d = v["last_reviewed"][:10]
            out.setdefault(d, {"opened": 0, "vocab_added": 0, "vocab_reviewed": 0})
            out[d]["vocab_reviewed"] += 1
    # 综合活动分
    for d, c in out.items():
        c["score"] = c.get("opened", 0) * 3 + c.get("vocab_added", 0) + c.get("vocab_reviewed", 0)
    return jsonify({"success": True, "activity": out})


@app.route("/api/stats")
@login_required
def api_stats():
    """总览统计 + 连续打卡。"""
    arts = articles_store.list_articles()
    vocab = _read_json("vocabulary.json", [])
    stars = _read_json("starred.json", [])
    history = _read_json("reading_history.json", {})

    total_words = sum(len((a.get("full_text") or "").split()) for a in arts)
    mastered = sum(1 for v in vocab if (v.get("review_count") or 0) >= 3)

    # 连续打卡 streak: 从今天往前数,只要 history 里有那一天就 +1
    today = datetime.now(CST).date()
    streak = 0
    cur = today
    while cur.isoformat() in history or cur == today and any(
        (v.get("added_at") or "").startswith(today.isoformat()) for v in vocab
    ):
        streak += 1
        cur = cur - timedelta(days=1)
    # 总学习天数(任何 history 或 vocab 活动的日子)
    active_dates = set(history.keys())
    for v in vocab:
        if v.get("added_at"): active_dates.add(v["added_at"][:10])
        if v.get("last_reviewed"): active_dates.add(v["last_reviewed"][:10])

    # 本周 / 本月
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    month_start = today.replace(day=1).isoformat()
    week_articles = sum(len(arts_list) for d, arts_list in history.items() if d >= week_start)
    month_articles = sum(len(arts_list) for d, arts_list in history.items() if d >= month_start)

    return jsonify({"success": True, "stats": {
        "total_articles": len(arts),
        "total_words": total_words,
        "total_vocab": len(vocab),
        "mastered_vocab": mastered,
        "total_starred": len(stars),
        "current_streak": streak,
        "total_active_days": len(active_dates),
        "this_week_articles": week_articles,
        "this_month_articles": month_articles,
    }})


@app.route("/api/today-progress")
@login_required
def api_today_progress():
    """今日打卡进度。"""
    today = datetime.now(CST).date().isoformat()
    history = _read_json("reading_history.json", {})
    vocab = _read_json("vocabulary.json", [])
    goals = _read_json("goals.json", {"articles_per_day": 1, "reviews_per_day": 10})

    today_articles = len(history.get(today, []))
    today_reviews = sum(1 for v in vocab if (v.get("last_reviewed") or "").startswith(today))
    today_added = sum(1 for v in vocab if (v.get("added_at") or "").startswith(today))

    return jsonify({"success": True, "progress": {
        "today_articles": today_articles,
        "today_reviews": today_reviews,
        "today_added": today_added,
        "target_articles": goals.get("articles_per_day", 1),
        "target_reviews": goals.get("reviews_per_day", 10),
    }})


@app.route("/api/goals", methods=["GET", "POST"])
@login_required
def api_goals():
    if request.method == "POST":
        data = request.get_json()
        goals = {
            "articles_per_day": max(1, int(data.get("articles_per_day", 1))),
            "reviews_per_day": max(1, int(data.get("reviews_per_day", 10))),
        }
        _write_json("goals.json", goals)
        return jsonify({"success": True, "goals": goals})
    return jsonify({"success": True, "goals": _read_json("goals.json", {"articles_per_day": 1, "reviews_per_day": 10})})


@app.route("/api/search")
@login_required
def api_search():
    """跨文章搜索单词,返回带上下文的命中(KWIC)。"""
    q = (request.args.get("q") or "").strip()
    if len(q) < 2:
        return jsonify({"success": False, "error": "查询词太短"}), 400
    arts = articles_store.list_articles()
    hits = []
    import re
    q_re = re.compile(r"(?<![\w])(" + re.escape(q) + r"\w*)(?![\w])", re.I)
    for a in arts:
        text = a.get("full_text") or ""
        for m in q_re.finditer(text):
            start = max(0, m.start() - 80)
            end = min(len(text), m.end() + 80)
            snippet = text[start:end]
            # 在 snippet 内高亮匹配
            highlighted = q_re.sub(lambda x: "<<<" + x.group(0) + ">>>", snippet)
            hits.append({
                "article_id": a["_id"],
                "title": a.get("title"),
                "source": a.get("source"),
                "published": a.get("published"),
                "position": m.start(),
                "snippet": ("..." if start > 0 else "") + highlighted + ("..." if end < len(text) else ""),
                "matched": m.group(0),
            })
        # 同时检查该词是否在 vocab/phrases 注释中
    # 也搜生词本
    vocab = _read_json("vocabulary.json", [])
    saved_matches = [v for v in vocab if q.lower() in (v.get("word") or "").lower()]

    return jsonify({"success": True, "hits": hits, "total": len(hits), "saved": saved_matches})


@app.route("/api/article-stats/<article_id>")
@login_required
def api_article_stats(article_id):
    """单篇文章的难度分析。"""
    art = articles_store.get_article(article_id)
    if not art: return jsonify({"success": False}), 404
    text = art.get("full_text") or ""
    import re
    words = re.findall(r"[A-Za-z']+", text)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    word_count = len(words)
    unique_words = len(set(w.lower() for w in words))
    avg_sentence_len = round(word_count / max(len(sentences), 1), 1)
    avg_word_len = round(sum(len(w) for w in words) / max(word_count, 1), 1)

    vocab_items = art.get("annotations_vocab", [])
    # 词汇等级分布(基于注释里的 level 字段)
    level_buckets = {"CET-4": 0, "CET-6": 0, "IELTS 7.0+": 0, "考研/IELTS 7.5+": 0, "其他": 0}
    for v in vocab_items:
        lv = (v.get("level") or "").upper()
        if "CET-4" in lv and "CET-6" not in lv: level_buckets["CET-4"] += 1
        elif "CET-6" in lv: level_buckets["CET-6"] += 1
        elif "7.5" in lv or "考研" in (v.get("level") or ""): level_buckets["考研/IELTS 7.5+"] += 1
        elif "IELTS" in lv: level_buckets["IELTS 7.0+"] += 1
        else: level_buckets["其他"] += 1

    complex_sentence_count = len(art.get("annotations_sentences", []))
    complex_density = round(complex_sentence_count / max(len(sentences), 1) * 100, 1)

    # 推荐阅读策略
    if avg_sentence_len > 28 or complex_density > 12:
        strategy = "深度精读"
        strategy_reason = "句长偏长、长难句密度高,建议逐句拆解,重点学语法和句式"
    elif level_buckets["考研/IELTS 7.5+"] >= 5:
        strategy = "词汇拓展"
        strategy_reason = "高难度词汇较多,适合精读积累生词和写作素材"
    elif avg_sentence_len < 18 and word_count < 600:
        strategy = "快速泛读"
        strategy_reason = "篇幅较短、句式平实,适合 5-10 分钟快速阅读"
    else:
        strategy = "常规精读"
        strategy_reason = "难度适中,推荐 20-30 分钟完整精读"

    return jsonify({"success": True, "stats": {
        "word_count": word_count,
        "unique_words": unique_words,
        "sentence_count": len(sentences),
        "avg_sentence_length": avg_sentence_len,
        "avg_word_length": avg_word_len,
        "level_distribution": level_buckets,
        "complex_sentence_count": complex_sentence_count,
        "complex_sentence_density": complex_density,
        "recommended_strategy": strategy,
        "strategy_reason": strategy_reason,
    }})


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
