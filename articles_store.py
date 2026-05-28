"""
articles_store.py — JSON 文件存储层
每篇文章一个 JSON 文件,位于 articles/ 目录
文件名规则: {YYYY-MM-DD}-{slug}.json
"""
import json
import re
from pathlib import Path
from datetime import datetime

ARTICLES_DIR = Path(__file__).parent / "articles"
ARTICLES_DIR.mkdir(exist_ok=True)


def _slugify(text: str, max_len: int = 40) -> str:
    """把标题转成文件名安全的 slug"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    return text[:max_len] or "untitled"


def _filename_for(article: dict) -> str:
    date = article.get("published") or datetime.now().strftime("%Y-%m-%d")
    slug = _slugify(article.get("title", "untitled"))
    return f"{date}-{slug}.json"


def list_articles() -> list:
    """返回所有文章(按 published 倒序),每项含 _id 字段(文件名去 .json)"""
    items = []
    for p in ARTICLES_DIR.glob("*.json"):
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            data["_id"] = p.stem
            items.append(data)
        except Exception:
            continue
    items.sort(key=lambda a: a.get("published", ""), reverse=True)
    return items


def get_article(article_id: str) -> dict | None:
    path = ARTICLES_DIR / f"{article_id}.json"
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["_id"] = article_id
    return data


def save_article(article: dict) -> str:
    """保存一篇文章,返回 _id。如果同名文件存在,数字后缀去重。"""
    base_name = _filename_for(article).replace(".json", "")
    name = base_name
    n = 1
    while (ARTICLES_DIR / f"{name}.json").exists():
        n += 1
        name = f"{base_name}-{n}"

    article.pop("_id", None)
    path = ARTICLES_DIR / f"{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)
    return name


def update_article(article_id: str, article: dict) -> bool:
    path = ARTICLES_DIR / f"{article_id}.json"
    if not path.exists():
        return False
    article.pop("_id", None)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)
    return True


def delete_article(article_id: str) -> bool:
    path = ARTICLES_DIR / f"{article_id}.json"
    if not path.exists():
        return False
    path.unlink()
    return True
