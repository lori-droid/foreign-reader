"""
Xiaohongshu card generator for Foreign Journal Reader
Generates a set of 9 cards (1080x1440) for one article's intensive reading
"""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# ─── FONTS ────────────────────────────────────────────────────
FONT_DIR = "/Users/lorraine.li/.config/opencode/skills/canvas-design/canvas-fonts"
SYS_FONTS = "/System/Library/Fonts"

FONT_EN_BOLD = os.path.join(FONT_DIR, "IBMPlexSerif-Bold.ttf")
FONT_EN = os.path.join(FONT_DIR, "IBMPlexSerif-Regular.ttf")
FONT_EN_ITALIC = os.path.join(FONT_DIR, "IBMPlexSerif-Italic.ttf")
FONT_MONO = os.path.join(FONT_DIR, "IBMPlexMono-Regular.ttf")
FONT_MONO_BOLD = os.path.join(FONT_DIR, "IBMPlexMono-Bold.ttf")
FONT_SANS = os.path.join(FONT_DIR, "InstrumentSans-Regular.ttf")
FONT_SANS_BOLD = os.path.join(FONT_DIR, "InstrumentSans-Bold.ttf")
FONT_CN = os.path.join(SYS_FONTS, "STHeiti Medium.ttc")
FONT_CN_LIGHT = os.path.join(SYS_FONTS, "Hiragino Sans GB.ttc")

# ─── COLORS ───────────────────────────────────────────────────
BG = (250, 248, 245)         # warm paper
INK = (26, 26, 26)
INK_LIGHT = (61, 61, 61)
INK_MUTED = (107, 107, 107)
ACCENT = (184, 67, 47)       # warm red
BLUE = (43, 95, 138)
GREEN = (58, 125, 92)
GOLD = (196, 154, 42)
GOLD_SOFT = (245, 236, 208)
PURPLE = (107, 91, 149)
WHITE = (255, 255, 255)
BORDER = (217, 210, 199)

W, H = 1080, 1440


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()


def draw_rounded_rect(draw, xy, radius, fill, outline=None):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline)


def wrap_text_cn(text, font, max_width, draw):
    """Wrap text (supports Chinese) to fit within max_width."""
    lines = []
    current = ""
    for char in text:
        test = current + char
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width:
            if current:
                lines.append(current)
            current = char
        else:
            current = test
    if current:
        lines.append(current)
    return lines


def create_card(bg_color=BG):
    img = Image.new("RGB", (W, H), bg_color)
    draw = ImageDraw.Draw(img)
    return img, draw


def draw_header_bar(draw, source="THE ECONOMIST", page="1/9"):
    """Draw top bar with source and page number."""
    f_mono = load_font(FONT_MONO, 24)
    f_cn = load_font(FONT_CN, 24)
    draw.text((80, 60), source, font=f_mono, fill=ACCENT)
    draw.text((W - 80, 60), page, font=f_mono, fill=INK_MUTED, anchor="ra")
    # Thin line
    draw.line([(80, 100), (W - 80, 100)], fill=BORDER, width=1)


def draw_footer(draw, handle="@外刊精读FJR"):
    f_cn = load_font(FONT_CN, 22)
    draw.text((W // 2, H - 60), handle, font=f_cn, fill=INK_MUTED, anchor="mm")


# ═══════════════════════════════════════════════════════════════
# CARD 1: COVER
# ═══════════════════════════════════════════════════════════════
def card_cover():
    img, draw = create_card(INK)

    # Accent line at top
    draw.rectangle([(0, 0), (W, 8)], fill=ACCENT)

    # Source badge
    f_mono = load_font(FONT_MONO, 26)
    draw_rounded_rect(draw, (80, 120, 360, 168), 6, ACCENT)
    draw.text((220, 144), "THE ECONOMIST", font=f_mono, fill=WHITE, anchor="mm")

    # Category
    f_cn = load_font(FONT_CN, 28)
    draw.text((80, 200), "政治经济 · 外刊精读", font=f_cn, fill=(180, 170, 155))

    # Title
    f_title = load_font(FONT_EN_BOLD, 56)
    title_lines = textwrap.wrap("The Quiet Revolution in How We Think About Trade", width=22)
    y = 280
    for line in title_lines:
        draw.text((80, y), line, font=f_title, fill=WHITE)
        y += 72

    # Divider
    draw.line([(80, y + 20), (400, y + 20)], fill=ACCENT, width=3)

    # Chinese subtitle
    f_cn_sub = load_font(FONT_CN, 32)
    cn_lines = wrap_text_cn("我们对贸易的思考方式正在经历一场静悄悄的革命", f_cn_sub, W - 160, draw)
    y += 60
    for line in cn_lines:
        draw.text((80, y), line, font=f_cn_sub, fill=(200, 190, 175))
        y += 48

    # Difficulty badges
    y += 40
    f_badge = load_font(FONT_CN, 24)
    badges = ["难度: 雅思7.0+", "词汇量: 26个", "词组: 10个", "长难句: 8个"]
    x = 80
    for badge in badges:
        bbox = draw.textbbox((0, 0), badge, font=f_badge)
        bw = bbox[2] - bbox[0] + 32
        draw_rounded_rect(draw, (x, y, x + bw, y + 42), 6, (50, 45, 40))
        draw.text((x + 16, y + 10), badge, font=f_badge, fill=(180, 170, 155))
        x += bw + 12
        if x > W - 200:
            x = 80
            y += 54

    # Bottom accent
    draw.rectangle([(0, H - 120), (W, H - 116)], fill=ACCENT)
    f_bottom = load_font(FONT_CN, 26)
    draw.text((W // 2, H - 70), "左滑开始精读 →", font=f_bottom, fill=(150, 140, 130), anchor="mm")

    return img


# ═══════════════════════════════════════════════════════════════
# CARD 2: ARTICLE TEXT (paragraph 1-3)
# ═══════════════════════════════════════════════════════════════
def card_article_text():
    img, draw = create_card()
    draw_header_bar(draw, "THE ECONOMIST", "2/9")

    f_label = load_font(FONT_CN, 30)
    draw.text((80, 130), "原文精选 · 段落 1-3", font=f_label, fill=INK)
    draw.line([(80, 175), (W - 80, 175)], fill=BORDER, width=1)

    f_en = load_font(FONT_EN, 24)
    f_cn = load_font(FONT_CN, 22)

    paragraphs = [
        ("For decades, free trade was an article of faith among economists. The logic seemed irrefutable: countries should specialise in what they do best, and exchange goods freely.",
         "几十年来，自由贸易一直是经济学家们的信条。其逻辑看似无可辩驳：各国应该专注于自己最擅长的事情，自由交换商品。"),
        ("The proliferation of global supply chains, once hailed as a triumph of efficiency, has revealed an insidious vulnerability.",
         "全球供应链的激增曾被誉为效率的胜利，却暴露了一种隐蔽的脆弱性。"),
        ("Not only has this rethinking challenged the dominant economic orthodoxy, but it has also given rise to new schools of thought.",
         "这种反思不仅挑战了主流经济学正统观念，还催生了新的思想学派。"),
    ]

    y = 200
    for i, (en, cn) in enumerate(paragraphs):
        # Paragraph number
        f_num = load_font(FONT_MONO, 20)
        draw.text((80, y), f"¶{i + 1}", font=f_num, fill=ACCENT)

        # English text
        en_lines = textwrap.wrap(en, width=48)
        y += 30
        for line in en_lines:
            draw.text((80, y), line, font=f_en, fill=INK_LIGHT)
            y += 34

        # Chinese translation
        y += 8
        cn_lines = wrap_text_cn(cn, f_cn, W - 160, draw)
        for line in cn_lines:
            draw.text((80, y), line, font=f_cn, fill=INK_MUTED)
            y += 32

        y += 30
        if y > H - 150:
            break

    draw_footer(draw)
    return img


# ═══════════════════════════════════════════════════════════════
# CARD 3-4: VOCABULARY
# ═══════════════════════════════════════════════════════════════
def card_vocab(page_num, vocab_items, page_label):
    img, draw = create_card()
    draw_header_bar(draw, "核心词汇", f"{page_num}/9")

    f_label = load_font(FONT_CN, 30)
    draw.text((80, 130), page_label, font=f_label, fill=INK)
    draw.line([(80, 175), (W - 80, 175)], fill=BORDER, width=1)

    f_word = load_font(FONT_EN_BOLD, 32)
    f_phonetic = load_font(FONT_MONO, 20)
    f_cn = load_font(FONT_CN, 24)
    f_def = load_font(FONT_EN, 21)
    f_tip = load_font(FONT_CN, 20)

    y = 200
    for v in vocab_items:
        if y > H - 200:
            break

        # Word + phonetic
        draw.text((80, y), v["word"], font=f_word, fill=ACCENT)
        pw = draw.textbbox((0, 0), v["word"], font=f_word)[2] + 90
        draw.text((pw, y + 8), v.get("phonetic", ""), font=f_phonetic, fill=INK_MUTED)
        y += 44

        # Chinese meaning
        draw.text((80, y), v["chinese"], font=f_cn, fill=INK)
        y += 36

        # Definition (English)
        def_lines = textwrap.wrap(v["definition"], width=52)
        for line in def_lines[:2]:
            draw.text((80, y), line, font=f_def, fill=INK_LIGHT)
            y += 28

        # Linguistics note (key differentiator)
        if v.get("linguistics"):
            y += 4
            ling_lines = wrap_text_cn(v["linguistics"][:100], f_tip, W - 180, draw)
            for line in ling_lines[:2]:
                draw.text((96, y), line, font=f_tip, fill=PURPLE)
                y += 28

        # Divider
        y += 12
        draw.line([(80, y), (W - 80, y)], fill=GOLD_SOFT, width=1)
        y += 20

    draw_footer(draw)
    return img


# ═══════════════════════════════════════════════════════════════
# CARD 5-6: PHRASES
# ═══════════════════════════════════════════════════════════════
def card_phrases(page_num, phrase_items, page_label):
    img, draw = create_card()
    draw_header_bar(draw, "高级词组", f"{page_num}/9")

    f_label = load_font(FONT_CN, 30)
    draw.text((80, 130), page_label, font=f_label, fill=INK)
    draw.line([(80, 175), (W - 80, 175)], fill=BORDER, width=1)

    f_phrase = load_font(FONT_EN_BOLD, 28)
    f_cn = load_font(FONT_CN, 24)
    f_def = load_font(FONT_EN, 21)
    f_tip = load_font(FONT_CN, 20)

    y = 200
    for p in phrase_items:
        if y > H - 200:
            break

        # Blue accent bar
        draw.rectangle([(80, y), (84, y + 60)], fill=BLUE)

        # Phrase
        draw.text((100, y), p["phrase"], font=f_phrase, fill=BLUE)
        y += 38

        # Chinese
        draw.text((100, y), p["chinese"], font=f_cn, fill=INK)
        y += 36

        # Linguistics / usage
        if p.get("linguistics"):
            ling_lines = wrap_text_cn(p["linguistics"][:120], f_tip, W - 200, draw)
            for line in ling_lines[:2]:
                draw.text((100, y), line, font=f_tip, fill=INK_MUTED)
                y += 28

        if p.get("usage"):
            usage_lines = wrap_text_cn(p["usage"][:100], f_tip, W - 200, draw)
            for line in usage_lines[:2]:
                draw.text((100, y), line, font=f_tip, fill=GREEN)
                y += 28

        y += 20
        draw.line([(80, y), (W - 80, y)], fill=BORDER, width=1)
        y += 20

    draw_footer(draw)
    return img


# ═══════════════════════════════════════════════════════════════
# CARD 7-8: COMPLEX SENTENCES
# ═══════════════════════════════════════════════════════════════
def card_sentence(page_num, sentence_data):
    img, draw = create_card()
    draw_header_bar(draw, "长难句拆解", f"{page_num}/9")

    s = sentence_data
    f_label = load_font(FONT_CN, 28)
    f_en = load_font(FONT_EN, 22)
    f_en_italic = load_font(FONT_EN_ITALIC, 22)
    f_cn = load_font(FONT_CN, 22)
    f_tip = load_font(FONT_CN, 20)
    f_num = load_font(FONT_MONO_BOLD, 48)

    # Big number
    draw.text((80, 130), f"#{page_num - 6}", font=f_num, fill=ACCENT)

    # Original sentence
    y = 210
    draw_rounded_rect(draw, (70, y - 10, W - 70, y + 10), 0, None)  # placeholder
    draw.rectangle([(70, y - 10), (76, y + 140)], fill=ACCENT)  # left bar

    sent_lines = textwrap.wrap(s["sentence"], width=46)
    for line in sent_lines:
        draw.text((96, y), line, font=f_en_italic, fill=INK)
        y += 32
    y += 16

    # Translation
    draw.text((80, y), "翻译", font=f_label, fill=GOLD)
    y += 38
    trans_lines = wrap_text_cn(s["translation"], f_cn, W - 160, draw)
    for line in trans_lines:
        draw.text((80, y), line, font=f_cn, fill=INK_LIGHT)
        y += 32
    y += 16

    # Breakdown
    draw.text((80, y), "拆解", font=f_label, fill=BLUE)
    y += 38
    bd_lines = wrap_text_cn(s["breakdown"][:200], f_tip, W - 160, draw)
    for line in bd_lines:
        if y > H - 250:
            break
        draw.text((80, y), line, font=f_tip, fill=INK_LIGHT)
        y += 28
    y += 16

    # Writing tip
    if s.get("writing_tip") and y < H - 180:
        draw_rounded_rect(draw, (70, y, W - 70, min(y + 160, H - 100)), 8, GOLD_SOFT)
        draw.text((90, y + 12), "写作借鉴", font=f_label, fill=GOLD)
        y += 48
        tip_lines = wrap_text_cn(s["writing_tip"][:150], f_tip, W - 200, draw)
        for line in tip_lines:
            if y > H - 120:
                break
            draw.text((90, y), line, font=f_tip, fill=INK_LIGHT)
            y += 28

    draw_footer(draw)
    return img


# ═══════════════════════════════════════════════════════════════
# CARD 9: SUMMARY
# ═══════════════════════════════════════════════════════════════
def card_summary():
    img, draw = create_card()
    draw_header_bar(draw, "学习要点", "9/9")

    f_title = load_font(FONT_CN, 36)
    f_cn = load_font(FONT_CN, 26)
    f_en = load_font(FONT_EN, 24)
    f_tip = load_font(FONT_CN, 22)

    draw.text((80, 140), "本篇精读要点总结", font=f_title, fill=INK)
    draw.line([(80, 190), (W - 80, 190)], fill=ACCENT, width=2)

    points = [
        ("词汇收获", [
            "irrefutable（无可辩驳的）— ir-前缀否定规律",
            "paradigm（范式）— 学术必备词，注意g不发音",
            "semiconductors（半导体）— semi-前缀造词法",
            "policymakers — 复合造词法 policy+maker",
            "reshoring — re-前缀表示「回」的新造术语",
        ]),
        ("词组积累", [
            "an article of faith — 信条（宗教比喻）",
            "ripple effects — 涟漪效应（物理比喻）",
            "forge a consensus — 达成共识（锻造比喻）",
            "trade displacement — 贸易转移（经济术语）",
        ]),
        ("写作模板", [
            "X has changed in ways that have + 过去分词",
            "Not only + 倒装, but also...",
            "Were + 主语 + to do...（虚拟语气倒装）",
            "far from being X, Y is actually Z",
        ]),
    ]

    y = 220
    for section_title, items in points:
        # Section header
        draw_rounded_rect(draw, (80, y, 280, y + 40), 6, ACCENT)
        draw.text((180, y + 20), section_title, font=f_cn, fill=WHITE, anchor="mm")
        y += 56

        for item in items:
            if y > H - 180:
                break
            draw.text((100, y), "·", font=f_cn, fill=ACCENT)
            item_lines = wrap_text_cn(item, f_tip, W - 200, draw)
            for line in item_lines:
                draw.text((120, y), line, font=f_tip, fill=INK_LIGHT)
                y += 30
            y += 6
        y += 16

    # Call to action
    if y < H - 120:
        draw_rounded_rect(draw, (80, H - 150, W - 80, H - 90), 8, INK)
        f_cta = load_font(FONT_CN, 26)
        draw.text((W // 2, H - 120), "收藏本帖 · 每日精读一篇外刊", font=f_cta, fill=WHITE, anchor="mm")

    draw_footer(draw)
    return img


# ═══════════════════════════════════════════════════════════════
# MAIN: Generate all 9 cards
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    from classic_articles import CLASSIC_ARTICLES

    # Get the Economist article (first one)
    article = CLASSIC_ARTICLES[0]
    vocab = article["annotations_vocab"]
    phrases = article["annotations_phrases"]
    sentences = article["annotations_sentences"]

    output_dir = "/Users/lorraine.li/Documents/Opencode/个人成长/foreign-reader/xiaohongshu_cards"
    os.makedirs(output_dir, exist_ok=True)

    cards = [
        card_cover(),
        card_article_text(),
        card_vocab(3, vocab[:4], "核心词汇 · 第一组"),
        card_vocab(4, vocab[4:8], "核心词汇 · 第二组"),
        card_phrases(5, phrases[:5], "高级词组 · 第一组"),
        card_phrases(6, phrases[5:10], "高级词组 · 第二组"),
        card_sentence(7, sentences[0]),
        card_sentence(8, sentences[2]),  # "Some argue that..." - the one you asked about
        card_summary(),
    ]

    for i, card in enumerate(cards):
        path = os.path.join(output_dir, f"card_{i + 1:02d}.png")
        card.save(path, quality=95)
        print(f"Saved: {path}")

    print(f"\nDone! {len(cards)} cards saved to {output_dir}")
