"""
Reading Analyzer Module
Analyzes English text for intensive reading purposes:
- Advanced vocabulary extraction
- Useful phrases and collocations
- Notable sentence patterns
- Provides example sentences with authoritative sources and Chinese explanations
"""

import re
from collections import Counter


# ─── Advanced Vocabulary Database ──────────────────────────────────
# Words at CET-6 / IELTS 7-8+ / TEM-8 level with definitions and examples

ADVANCED_VOCAB = {
    # ── Politics & Economics ──
    "exacerbate": {
        "pos": "v.",
        "definition": "to make a problem, bad situation, or negative feeling worse",
        "chinese": "加剧，恶化",
        "phonetic": "/ɪɡˈzæs.ər.beɪt/",
        "examples": [
            {"text": "The rising inflation has exacerbated the cost-of-living crisis for millions.", "source": "The Economist, 2023"},
            {"text": "Climate change will exacerbate existing inequalities between nations.", "source": "IPCC Report, 2022"},
        ],
        "collocations": ["exacerbate the problem", "exacerbate tensions", "exacerbate inequality"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "unprecedented": {
        "pos": "adj.",
        "definition": "never having happened or existed in the past",
        "chinese": "前所未有的，史无前例的",
        "phonetic": "/ʌnˈpres.ɪ.den.tɪd/",
        "examples": [
            {"text": "The pandemic led to unprecedented levels of government intervention.", "source": "The Atlantic, 2021"},
            {"text": "We are witnessing an unprecedented shift in global power dynamics.", "source": "Foreign Affairs, 2023"},
        ],
        "collocations": ["unprecedented scale", "unprecedented challenge", "unprecedented growth"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "proliferation": {
        "pos": "n.",
        "definition": "a rapid increase in the number or amount of something",
        "chinese": "激增，扩散",
        "phonetic": "/prəˌlɪf.əˈreɪ.ʃən/",
        "examples": [
            {"text": "The proliferation of misinformation on social media threatens democracy.", "source": "The New Yorker, 2022"},
            {"text": "Nuclear proliferation remains one of the gravest security concerns.", "source": "Oxford Advanced Learner's Dictionary"},
        ],
        "collocations": ["nuclear proliferation", "proliferation of weapons", "rapid proliferation"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "volatile": {
        "pos": "adj.",
        "definition": "liable to change rapidly and unpredictably, especially for the worse",
        "chinese": "不稳定的，动荡的",
        "phonetic": "/ˈvɒl.ə.taɪl/",
        "examples": [
            {"text": "The stock market has been particularly volatile in recent months.", "source": "Financial Times, 2023"},
            {"text": "The political situation in the region remains volatile.", "source": "BBC News, 2023"},
        ],
        "collocations": ["volatile market", "volatile situation", "highly volatile"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "austerity": {
        "pos": "n.",
        "definition": "difficult economic conditions created by government measures to reduce public expenditure",
        "chinese": "紧缩（政策），节俭",
        "phonetic": "/ɒˈster.ɪ.ti/",
        "examples": [
            {"text": "Years of austerity have left public services severely underfunded.", "source": "The Guardian, 2022"},
            {"text": "The government's austerity measures sparked widespread protests.", "source": "The Economist, 2019"},
        ],
        "collocations": ["austerity measures", "austerity programme", "era of austerity"],
        "level": "IELTS 7.0+ / TEM-8",
    },
    "ubiquitous": {
        "pos": "adj.",
        "definition": "present, appearing, or found everywhere",
        "chinese": "无处不在的",
        "phonetic": "/juːˈbɪk.wɪ.təs/",
        "examples": [
            {"text": "Smartphones have become ubiquitous in modern society.", "source": "Cambridge Dictionary"},
            {"text": "The ubiquitous surveillance cameras raised privacy concerns.", "source": "The Atlantic, 2022"},
        ],
        "collocations": ["ubiquitous presence", "increasingly ubiquitous", "ubiquitous technology"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "paradigm": {
        "pos": "n.",
        "definition": "a typical example or pattern of something; a model",
        "chinese": "范式，典范",
        "phonetic": "/ˈpær.ə.daɪm/",
        "examples": [
            {"text": "The discovery represented a paradigm shift in our understanding of the universe.", "source": "Nature, 2020"},
            {"text": "The old economic paradigm is being challenged by new technologies.", "source": "Harvard Business Review, 2023"},
        ],
        "collocations": ["paradigm shift", "new paradigm", "dominant paradigm"],
        "level": "TEM-8 / IELTS 7.0+",
    },
    "commensurate": {
        "pos": "adj.",
        "definition": "corresponding in size or degree; in proportion",
        "chinese": "相称的，相当的",
        "phonetic": "/kəˈmen.sjʊ.rət/",
        "examples": [
            {"text": "Salary will be commensurate with experience and qualifications.", "source": "Oxford Advanced Learner's Dictionary"},
            {"text": "The punishment should be commensurate with the severity of the crime.", "source": "Merriam-Webster Dictionary"},
        ],
        "collocations": ["commensurate with", "commensurate increase", "commensurate level"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "exorbitant": {
        "pos": "adj.",
        "definition": "(of a price or amount charged) unreasonably high",
        "chinese": "过高的，离谱的",
        "phonetic": "/ɪɡˈzɔː.bɪ.tənt/",
        "examples": [
            {"text": "The exorbitant cost of healthcare forces many to forgo treatment.", "source": "The New York Times, 2023"},
            {"text": "Tourists are often charged exorbitant prices in popular destinations.", "source": "Longman Dictionary of Contemporary English"},
        ],
        "collocations": ["exorbitant price", "exorbitant fees", "exorbitant cost"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "rampant": {
        "pos": "adj.",
        "definition": "(of something unwelcome) flourishing or spreading unchecked",
        "chinese": "猖獗的，肆虐的",
        "phonetic": "/ˈræm.pənt/",
        "examples": [
            {"text": "Corruption remains rampant in many developing nations.", "source": "Transparency International Report, 2023"},
            {"text": "Rampant inflation has eroded the purchasing power of ordinary citizens.", "source": "The Economist, 2022"},
        ],
        "collocations": ["rampant corruption", "rampant inflation", "run rampant"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "conundrum": {
        "pos": "n.",
        "definition": "a confusing and difficult problem or question",
        "chinese": "难题，困境",
        "phonetic": "/kəˈnʌn.drəm/",
        "examples": [
            {"text": "The ethical conundrum of AI development has no easy solution.", "source": "MIT Technology Review, 2023"},
            {"text": "Central bankers face the conundrum of controlling inflation without triggering recession.", "source": "Financial Times, 2023"},
        ],
        "collocations": ["moral conundrum", "face a conundrum", "solve the conundrum"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "burgeon": {
        "pos": "v.",
        "definition": "begin to grow or increase rapidly; flourish",
        "chinese": "迅速发展，蓬勃增长",
        "phonetic": "/ˈbɜː.dʒən/",
        "examples": [
            {"text": "The burgeoning tech sector has transformed the city's economy.", "source": "The Economist, 2023"},
            {"text": "A burgeoning middle class is driving consumer demand in Asia.", "source": "World Bank Report, 2022"},
        ],
        "collocations": ["burgeoning industry", "burgeoning population", "burgeoning demand"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "insidious": {
        "pos": "adj.",
        "definition": "proceeding in a gradual, subtle way, but with harmful effects",
        "chinese": "阴险的，潜伏的",
        "phonetic": "/ɪnˈsɪd.i.əs/",
        "examples": [
            {"text": "The insidious effects of air pollution take years to manifest.", "source": "The Lancet, 2021"},
            {"text": "Misinformation can be insidious, slowly eroding public trust in institutions.", "source": "The Atlantic, 2022"},
        ],
        "collocations": ["insidious threat", "insidious influence", "insidious nature"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "precipitate": {
        "pos": "v.",
        "definition": "cause (an event or situation) to happen suddenly, unexpectedly, or prematurely",
        "chinese": "促使，加速（通常指不好的事）",
        "phonetic": "/prɪˈsɪp.ɪ.teɪt/",
        "examples": [
            {"text": "The assassination precipitated a full-scale military conflict.", "source": "Oxford Advanced Learner's Dictionary"},
            {"text": "Fear of bank failures can precipitate a broader financial crisis.", "source": "Financial Times, 2023"},
        ],
        "collocations": ["precipitate a crisis", "precipitate change", "precipitate a decline"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "imperious": {
        "pos": "adj.",
        "definition": "assuming power or authority without justification; domineering",
        "chinese": "专横的，傲慢的",
        "phonetic": "/ɪmˈpɪə.ri.əs/",
        "examples": [
            {"text": "Her imperious manner alienated many of her colleagues.", "source": "Collins English Dictionary"},
            {"text": "The CEO's imperious leadership style left no room for dissent.", "source": "Harvard Business Review, 2021"},
        ],
        "collocations": ["imperious tone", "imperious manner", "imperious leader"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "ameliorate": {
        "pos": "v.",
        "definition": "make (something bad or unsatisfactory) better",
        "chinese": "改善，改良",
        "phonetic": "/əˈmiː.li.ə.reɪt/",
        "examples": [
            {"text": "The new policy aims to ameliorate the housing shortage.", "source": "The Guardian, 2023"},
            {"text": "Technology alone cannot ameliorate deep-rooted social inequalities.", "source": "The New Yorker, 2022"},
        ],
        "collocations": ["ameliorate conditions", "ameliorate the situation", "ameliorate suffering"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "pernicious": {
        "pos": "adj.",
        "definition": "having a harmful effect, especially in a gradual or subtle way",
        "chinese": "有害的，恶性的",
        "phonetic": "/pəˈnɪʃ.əs/",
        "examples": [
            {"text": "The pernicious influence of lobbying on democratic governance is well documented.", "source": "Foreign Affairs, 2022"},
            {"text": "Conspiracy theories have a pernicious effect on public discourse.", "source": "The Atlantic, 2021"},
        ],
        "collocations": ["pernicious effect", "pernicious influence", "pernicious myth"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "intransigent": {
        "pos": "adj.",
        "definition": "unwilling or refusing to change one's views or to agree about something",
        "chinese": "不妥协的，固执的",
        "phonetic": "/ɪnˈtræn.sɪ.dʒənt/",
        "examples": [
            {"text": "The intransigent stance of both parties made negotiations impossible.", "source": "The Economist, 2023"},
            {"text": "Government intransigence on reform has frustrated voters.", "source": "BBC News, 2022"},
        ],
        "collocations": ["intransigent position", "intransigent attitude", "remain intransigent"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "equivocal": {
        "pos": "adj.",
        "definition": "open to more than one interpretation; ambiguous",
        "chinese": "模棱两可的，含糊的",
        "phonetic": "/ɪˈkwɪv.ə.kəl/",
        "examples": [
            {"text": "The minister gave an equivocal response, satisfying neither side.", "source": "The Guardian, 2023"},
            {"text": "The scientific evidence remains equivocal on this point.", "source": "Nature, 2022"},
        ],
        "collocations": ["equivocal answer", "equivocal evidence", "equivocal results"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "eschew": {
        "pos": "v.",
        "definition": "deliberately avoid using; abstain from",
        "chinese": "避免，回避",
        "phonetic": "/ɪsˈtʃuː/",
        "examples": [
            {"text": "The author eschews jargon in favour of plain language.", "source": "Merriam-Webster Dictionary"},
            {"text": "Many young professionals eschew traditional career paths.", "source": "The Economist, 2023"},
        ],
        "collocations": ["eschew violence", "eschew convention", "eschew responsibility"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "obfuscate": {
        "pos": "v.",
        "definition": "make obscure, unclear, or unintelligible",
        "chinese": "使模糊，使混淆",
        "phonetic": "/ˈɒb.fʌ.skeɪt/",
        "examples": [
            {"text": "Politicians often obfuscate the issue with misleading statistics.", "source": "The New York Times, 2022"},
            {"text": "Complex legal language can obfuscate rather than clarify meaning.", "source": "Cambridge Dictionary"},
        ],
        "collocations": ["obfuscate the truth", "obfuscate the issue", "deliberately obfuscate"],
        "level": "TEM-8 / IELTS 8.0+",
    },
    "cogent": {
        "pos": "adj.",
        "definition": "(of an argument or case) clear, logical, and convincing",
        "chinese": "有说服力的，令人信服的",
        "phonetic": "/ˈkəʊ.dʒənt/",
        "examples": [
            {"text": "She made a cogent argument for increasing public investment.", "source": "Oxford Advanced Learner's Dictionary"},
            {"text": "The report presents a cogent analysis of the crisis.", "source": "The Economist, 2023"},
        ],
        "collocations": ["cogent argument", "cogent reasoning", "cogent analysis"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "galvanize": {
        "pos": "v.",
        "definition": "shock or excite (someone) into taking action",
        "chinese": "激励，刺激",
        "phonetic": "/ˈɡæl.və.naɪz/",
        "examples": [
            {"text": "The tragedy galvanized public opinion in favour of stricter gun laws.", "source": "The New York Times, 2022"},
            {"text": "The speech galvanized the crowd into action.", "source": "Longman Dictionary of Contemporary English"},
        ],
        "collocations": ["galvanize support", "galvanize action", "galvanize the public"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "dichotomy": {
        "pos": "n.",
        "definition": "a division or contrast between two things that are opposed or entirely different",
        "chinese": "二分法，对立",
        "phonetic": "/daɪˈkɒt.ə.mi/",
        "examples": [
            {"text": "The dichotomy between rich and poor continues to widen.", "source": "The Economist, 2023"},
            {"text": "The false dichotomy of nature versus nurture oversimplifies human development.", "source": "Scientific American, 2021"},
        ],
        "collocations": ["false dichotomy", "sharp dichotomy", "dichotomy between"],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "inexorable": {
        "pos": "adj.",
        "definition": "impossible to stop or prevent",
        "chinese": "不可阻挡的，无法改变的",
        "phonetic": "/ɪnˈek.sər.ə.bəl/",
        "examples": [
            {"text": "The inexorable rise of sea levels threatens coastal communities.", "source": "IPCC Report, 2023"},
            {"text": "Technology's inexorable march has reshaped every industry.", "source": "MIT Technology Review, 2022"},
        ],
        "collocations": ["inexorable rise", "inexorable decline", "inexorable march"],
        "level": "TEM-8 / IELTS 8.0+",
    },
}

# ─── Useful Phrases and Collocations ──────────────────────────────

USEFUL_PHRASES = {
    "in the wake of": {
        "definition": "as a result of; following",
        "chinese": "在……之后，由于",
        "examples": [
            {"text": "In the wake of the financial crisis, regulators tightened banking rules.", "source": "Financial Times, 2020"},
            {"text": "In the wake of the scandal, several executives resigned.", "source": "The Guardian, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "at the expense of": {
        "definition": "so as to cause harm to or neglect of",
        "chinese": "以……为代价",
        "examples": [
            {"text": "Economic growth should not come at the expense of environmental protection.", "source": "The Economist, 2023"},
            {"text": "He pursued his career at the expense of his family relationships.", "source": "Cambridge Dictionary"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "by and large": {
        "definition": "on the whole; everything considered",
        "chinese": "总的来说，大体上",
        "examples": [
            {"text": "By and large, the reforms have been successful.", "source": "Oxford Advanced Learner's Dictionary"},
            {"text": "The project, by and large, met its objectives.", "source": "Harvard Business Review, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "come to terms with": {
        "definition": "to accept or become resigned to something difficult",
        "chinese": "接受，妥协",
        "examples": [
            {"text": "The nation is still coming to terms with the aftermath of the crisis.", "source": "The Atlantic, 2022"},
            {"text": "She has finally come to terms with her diagnosis.", "source": "Longman Dictionary of Contemporary English"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "on the grounds that": {
        "definition": "for the reason that",
        "chinese": "以……为理由",
        "examples": [
            {"text": "The application was rejected on the grounds that it was submitted late.", "source": "Cambridge Dictionary"},
            {"text": "He opposed the policy on the grounds that it violated civil liberties.", "source": "The Guardian, 2023"},
        ],
        "level": "CET-6 / IELTS 7.0+",
    },
    "give rise to": {
        "definition": "cause or bring about",
        "chinese": "引起，导致",
        "examples": [
            {"text": "The new regulations may give rise to unintended consequences.", "source": "The Economist, 2023"},
            {"text": "Rapid urbanisation has given rise to a host of social problems.", "source": "UN Habitat Report, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "hinge on": {
        "definition": "depend entirely on",
        "chinese": "取决于",
        "examples": [
            {"text": "The success of the negotiations hinges on both sides making concessions.", "source": "Foreign Affairs, 2023"},
            {"text": "The election outcome hinges on voter turnout in swing states.", "source": "The New York Times, 2024"},
        ],
        "level": "CET-6 / IELTS 7.0+",
    },
    "fall short of": {
        "definition": "fail to reach (a standard or required amount)",
        "chinese": "未达到，不足",
        "examples": [
            {"text": "The company's earnings fell short of analysts' expectations.", "source": "Financial Times, 2023"},
            {"text": "The agreement falls short of what environmentalists had hoped for.", "source": "The Guardian, 2023"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "set the stage for": {
        "definition": "create the conditions for a particular event or development",
        "chinese": "为……做准备/铺垫",
        "examples": [
            {"text": "The reforms set the stage for a decade of economic growth.", "source": "The Economist, 2022"},
            {"text": "Recent diplomatic moves have set the stage for a historic summit.", "source": "BBC News, 2023"},
        ],
        "level": "CET-6 / IELTS 7.0+",
    },
    "hold sway": {
        "definition": "have great power or influence over a particular person, place, or domain",
        "chinese": "有影响力，占支配地位",
        "examples": [
            {"text": "Traditional values still hold sway in many rural communities.", "source": "The New Yorker, 2022"},
            {"text": "The ideology that has held sway for decades is now being questioned.", "source": "Foreign Affairs, 2023"},
        ],
        "level": "TEM-8 / IELTS 7.5+",
    },
    "run counter to": {
        "definition": "go against; conflict with",
        "chinese": "与……相悖/背道而驰",
        "examples": [
            {"text": "The policy runs counter to the principles of free trade.", "source": "The Economist, 2023"},
            {"text": "His actions run counter to his stated beliefs.", "source": "Oxford Advanced Learner's Dictionary"},
        ],
        "level": "CET-6 / IELTS 7.0+",
    },
    "bear the brunt of": {
        "definition": "suffer the worst part of something unpleasant",
        "chinese": "首当其冲，承受最大压力",
        "examples": [
            {"text": "Low-income families bear the brunt of rising food prices.", "source": "The Guardian, 2023"},
            {"text": "Coastal regions bore the brunt of the hurricane's fury.", "source": "The New York Times, 2022"},
        ],
        "level": "CET-6 / IELTS 7.0+",
    },
    "in tandem with": {
        "definition": "together with; in conjunction with",
        "chinese": "与……一起/同步",
        "examples": [
            {"text": "Economic reform must proceed in tandem with political reform.", "source": "Foreign Affairs, 2022"},
            {"text": "Technology is evolving in tandem with changing consumer expectations.", "source": "Harvard Business Review, 2023"},
        ],
        "level": "IELTS 7.0+ / TEM-8",
    },
    "a far cry from": {
        "definition": "very different from",
        "chinese": "与……相去甚远",
        "examples": [
            {"text": "The current state of affairs is a far cry from what was promised.", "source": "The Economist, 2023"},
            {"text": "Life in the city is a far cry from the rural upbringing she was accustomed to.", "source": "Cambridge Dictionary"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "shed light on": {
        "definition": "make free from confusion or ambiguity; clarify",
        "chinese": "阐明，揭示",
        "examples": [
            {"text": "The investigation shed light on the extent of corporate fraud.", "source": "The New York Times, 2022"},
            {"text": "New research sheds light on the mechanisms of memory formation.", "source": "Nature, 2023"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
}

# ─── Notable Sentence Patterns ────────────────────────────────────

SENTENCE_PATTERNS = [
    {
        "pattern": "Not only ... but also ...",
        "regex": r"[Nn]ot only .{10,80} but (?:also )?",
        "description": "并列强调结构，用于同时突出两个方面",
        "chinese": "不仅……而且……",
        "example": "Not only has the policy failed to reduce inequality, but it has also widened the gap between rich and poor.",
        "usage": "常用于议论文写作中强调双重影响或特征",
    },
    {
        "pattern": "It is ... that ... (强调句)",
        "regex": r"[Ii]t (?:is|was) .{3,50} that ",
        "description": "强调句型，通过 it is/was ... that 结构突出某个成分",
        "chinese": "正是……（强调）",
        "example": "It is precisely this kind of short-sighted thinking that has led to the current crisis.",
        "usage": "用于学术写作和社论中强调关键观点",
    },
    {
        "pattern": "倒装句 (Never/Rarely/Seldom ...)",
        "regex": r"(?:Never|Rarely|Seldom|Hardly|Scarcely|Not until|Not only|Little|No sooner) (?:has|had|did|does|do|was|were|will|would|can|could|should) ",
        "description": "否定词前置引起的部分倒装，增强语气",
        "chinese": "从不/很少……（倒装强调）",
        "example": "Rarely has a single policy decision provoked such widespread public outcry.",
        "usage": "常见于正式文体和社论评论中，增强表达力度",
    },
    {
        "pattern": "独立主格结构",
        "regex": r", (?:with|its|their|his|her) \w+ (?:ing|ed|en) ",
        "description": "独立主格结构，用于补充说明伴随状态或原因",
        "chinese": "伴随状态/原因（独立主格）",
        "example": "With inflation spiralling out of control, the central bank had no choice but to raise interest rates.",
        "usage": "用于丰富句子层次，在写作中展示语言功底",
    },
    {
        "pattern": "虚拟语气 (were to / should ...)",
        "regex": r"(?:[Ww]ere .{1,20} to |[Ss]hould .{1,20} (?:fail|prove|decide|choose|happen))",
        "description": "虚拟语气，表示假设或不太可能发生的情况",
        "chinese": "假如/万一……",
        "example": "Were the government to implement these reforms, the economy could see a significant recovery.",
        "usage": "用于学术写作和政策讨论中表达假设情景",
    },
    {
        "pattern": "让步状语从句 (While/Although/Despite ...)",
        "regex": r"(?:While|Although|Despite|Notwithstanding|Much as|However much) .{10,100},",
        "description": "让步结构，先承认一个事实再转折",
        "chinese": "虽然/尽管……",
        "example": "While the government has made some progress in reducing emissions, much more needs to be done.",
        "usage": "议论文必备句型，展示思维的全面性",
    },
]


class ReadingAnalyzer:
    """Analyzes text for intensive reading study."""

    def analyze(self, text, title=""):
        """
        Perform intensive reading analysis on the given text.
        Returns vocabulary, phrases, sentence patterns, and study notes.
        """
        text_lower = text.lower()
        words = re.findall(r"\b[a-zA-Z]{3,}\b", text_lower)
        word_freq = Counter(words)

        result = {
            "title": title,
            "word_count": len(words),
            "unique_words": len(set(words)),
            "vocabulary": self._extract_vocabulary(text, text_lower, word_freq),
            "phrases": self._extract_phrases(text, text_lower),
            "sentence_patterns": self._extract_patterns(text),
            "difficulty_assessment": self._assess_difficulty(words, word_freq),
        }

        return result

    def _extract_vocabulary(self, text, text_lower, word_freq):
        """Find advanced vocabulary present in the text."""
        found = []
        for word, info in ADVANCED_VOCAB.items():
            # Check for word and its common forms
            forms = [word]
            if word.endswith("e"):
                forms.append(word + "d")
                forms.append(word + "s")
                forms.append(word[:-1] + "ing")
            else:
                forms.append(word + "ed")
                forms.append(word + "s")
                forms.append(word + "ing")

            for form in forms:
                if form in text_lower:
                    context = self._find_context(text, form)
                    found.append({
                        "word": word,
                        "form_found": form,
                        "pos": info["pos"],
                        "definition": info["definition"],
                        "chinese": info["chinese"],
                        "phonetic": info.get("phonetic", ""),
                        "examples": info["examples"],
                        "collocations": info.get("collocations", []),
                        "level": info["level"],
                        "context_in_article": context,
                    })
                    break

        return found

    def _extract_phrases(self, text, text_lower):
        """Find useful phrases present in the text."""
        found = []
        for phrase, info in USEFUL_PHRASES.items():
            if phrase.lower() in text_lower:
                context = self._find_context(text, phrase)
                found.append({
                    "phrase": phrase,
                    "definition": info["definition"],
                    "chinese": info["chinese"],
                    "examples": info["examples"],
                    "level": info["level"],
                    "context_in_article": context,
                })

        return found

    def _extract_patterns(self, text):
        """Find notable sentence patterns in the text."""
        found = []
        sentences = re.split(r"[.!?]+", text)

        for pattern_info in SENTENCE_PATTERNS:
            for sentence in sentences:
                sentence = sentence.strip()
                if len(sentence) < 15:
                    continue
                if re.search(pattern_info["regex"], sentence):
                    found.append({
                        "pattern": pattern_info["pattern"],
                        "description": pattern_info["description"],
                        "chinese": pattern_info["chinese"],
                        "found_sentence": sentence.strip()[:200] + ("..." if len(sentence) > 200 else ""),
                        "model_example": pattern_info["example"],
                        "usage_tip": pattern_info["usage"],
                    })
                    break

        return found

    def _find_context(self, text, target):
        """Find the sentence containing the target word/phrase."""
        sentences = re.split(r"(?<=[.!?])\s+", text)
        target_lower = target.lower()
        for sentence in sentences:
            if target_lower in sentence.lower():
                return sentence.strip()[:300]
        return ""

    def _assess_difficulty(self, words, word_freq):
        """Assess the overall difficulty level of the text."""
        total = len(words)
        unique = len(set(words))
        avg_word_len = sum(len(w) for w in words) / max(total, 1)

        # Lexical diversity (type-token ratio)
        ttr = unique / max(total, 1)

        if avg_word_len > 6 and ttr > 0.6:
            level = "Advanced (专八/雅思7.5+)"
        elif avg_word_len > 5.2 and ttr > 0.5:
            level = "Upper-Intermediate (六级/雅思6.5-7.0)"
        elif avg_word_len > 4.5:
            level = "Intermediate (四级/雅思5.5-6.0)"
        else:
            level = "Pre-Intermediate (四级以下)"

        return {
            "level": level,
            "total_words": total,
            "unique_words": unique,
            "avg_word_length": round(avg_word_len, 1),
            "lexical_diversity": round(ttr, 3),
        }
