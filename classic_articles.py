"""
Classic Articles Module — Deep Reading Edition
Each article includes embedded intensive reading annotations:
- vocabulary: all difficult words and domain-specific terms
- phrases: all important expressions, collocations, idioms
- complex_sentences: long/difficult sentence breakdowns with grammar, translation, writing tips
"""

CLASSIC_ARTICLES = [
    # ═══════════════════════════════════════════════════════════
    # ARTICLE 1 — The Economist (Politics & Economics)
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Quiet Revolution in How We Think About Trade",
        "source": "The Economist",
        "source_icon": "📊",
        "category": "politics_economics",
        "category_label": "政治经济",
        "summary": "For decades, free trade was an article of faith among economists. Now a rethinking is under way — not to abandon openness, but to acknowledge its costs and complications.",
        "link": "https://www.economist.com/leaders/",
        "published": "2025-01-15",
        "has_full_text": True,
        "full_text": """For decades, free trade was an article of faith among economists. The logic seemed irrefutable: countries should specialise in what they do best, and exchange goods freely. Everyone would be better off. Yet the world has changed in ways that have exacerbated the shortcomings of this paradigm.

The proliferation of global supply chains, once hailed as a triumph of efficiency, has revealed an insidious vulnerability. When a pandemic shut down factories in one corner of the world, the ripple effects were felt everywhere. The unprecedented disruption precipitated a rethinking that had been quietly building for years.

Not only has this rethinking challenged the dominant economic orthodoxy, but it has also given rise to new schools of thought. Some argue that a degree of self-sufficiency, far from being inefficient, is a form of insurance. Others contend that the benefits of free trade remain cogent, but that the costs have been borne disproportionately by those least able to bear them.

In the wake of the pandemic, governments have scrambled to secure supply chains for critical goods — semiconductors, medicines, rare-earth minerals. The exorbitant cost of this reshoring has raised questions about whether the cure is commensurate with the disease. By and large, economists now acknowledge that the old dichotomy between free trade and protectionism is too simplistic.

While the debate rages on, one thing is clear: the era of unquestioned faith in globalisation is over. The challenge now is to forge a new consensus — one that does not eschew openness, but that acknowledges the volatile and unpredictable world in which trade must operate. Were the world's leading economies to fail in this endeavour, the consequences could be far-reaching and pernicious.

The conundrum facing policymakers is acute. They must ameliorate the genuine hardships caused by trade displacement, without triggering the rampant protectionism that could precipitate a global recession. It is precisely this balancing act that will define economic policy for a generation.""",

        # ─── DEEP READING: VOCABULARY ────────────────────────────
        "annotations_vocab": [
            {
                "word": "irrefutable",
                "phonetic": "/ˌɪr.ɪˈfjuː.tə.bəl/",
                "pos": "adj.",
                "definition": "impossible to deny or disprove; undeniable",
                "chinese": "无可辩驳的，不可反驳的",
                "context": "The logic seemed irrefutable",
                "examples": [
                    {"text": "The evidence against the defendant was irrefutable.", "source": "Oxford Advanced Learner's Dictionary"},
                    {"text": "He presented irrefutable proof that the policy had failed.", "source": "The Guardian, 2023"},
                ],
                "collocations": ["irrefutable evidence", "irrefutable logic", "irrefutable proof"],
                "level": "IELTS 7.5+ / TEM-8",
            },
            {
                "word": "specialise",
                "phonetic": "/ˈspeʃ.əl.aɪz/",
                "pos": "v.",
                "definition": "to concentrate on and become expert in a particular subject or skill",
                "chinese": "专攻，专门从事",
                "context": "countries should specialise in what they do best",
                "examples": [
                    {"text": "The firm specialises in corporate law.", "source": "Cambridge Dictionary"},
                    {"text": "Many developing countries specialise in exporting raw materials.", "source": "The Economist, 2022"},
                ],
                "collocations": ["specialise in", "highly specialised", "specialised knowledge"],
                "level": "CET-6 / IELTS 6.0+",
            },
            {
                "word": "exacerbate",
                "phonetic": "/ɪɡˈzæs.ər.beɪt/",
                "pos": "v.",
                "definition": "to make a problem, bad situation, or negative feeling worse",
                "chinese": "加剧，恶化",
                "context": "the world has changed in ways that have exacerbated the shortcomings",
                "examples": [
                    {"text": "The rising inflation has exacerbated the cost-of-living crisis for millions.", "source": "The Economist, 2023"},
                    {"text": "Drought conditions were exacerbated by climate change.", "source": "IPCC Report, 2022"},
                ],
                "collocations": ["exacerbate the problem", "exacerbate tensions", "exacerbate inequality"],
                "level": "CET-6 / IELTS 7.0+",
            },
            {
                "word": "paradigm",
                "phonetic": "/ˈpær.ə.daɪm/",
                "pos": "n.",
                "definition": "a typical example, pattern, or model of something; a framework of thinking",
                "chinese": "范式，典范；思维框架",
                "context": "exacerbated the shortcomings of this paradigm",
                "examples": [
                    {"text": "The discovery represented a paradigm shift in our understanding of physics.", "source": "Nature, 2020"},
                    {"text": "The old economic paradigm is being challenged by new realities.", "source": "Harvard Business Review, 2023"},
                ],
                "collocations": ["paradigm shift", "dominant paradigm", "new paradigm"],
                "level": "TEM-8 / IELTS 7.0+",
            },
            {
                "word": "proliferation",
                "phonetic": "/prəˌlɪf.əˈreɪ.ʃən/",
                "pos": "n.",
                "definition": "rapid increase in the number or amount of something",
                "chinese": "激增，大量扩散",
                "context": "The proliferation of global supply chains",
                "examples": [
                    {"text": "The proliferation of misinformation on social media threatens democracy.", "source": "The New Yorker, 2022"},
                    {"text": "Nuclear proliferation remains one of the gravest security concerns.", "source": "Oxford Advanced Learner's Dictionary"},
                ],
                "collocations": ["nuclear proliferation", "proliferation of weapons", "rapid proliferation"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "insidious",
                "phonetic": "/ɪnˈsɪd.i.əs/",
                "pos": "adj.",
                "definition": "proceeding in a gradual, subtle way, but with harmful effects",
                "chinese": "潜伏的，不知不觉中起破坏作用的",
                "context": "has revealed an insidious vulnerability",
                "examples": [
                    {"text": "The insidious effects of air pollution take years to manifest.", "source": "The Lancet, 2021"},
                    {"text": "Misinformation is insidious because it slowly erodes trust.", "source": "The Atlantic, 2022"},
                ],
                "collocations": ["insidious threat", "insidious influence", "insidious nature"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "unprecedented",
                "phonetic": "/ʌnˈpres.ɪ.den.tɪd/",
                "pos": "adj.",
                "definition": "never having happened or existed before",
                "chinese": "前所未有的，史无前例的",
                "context": "The unprecedented disruption",
                "examples": [
                    {"text": "The pandemic led to unprecedented levels of government intervention.", "source": "The Atlantic, 2021"},
                    {"text": "We face challenges of unprecedented scale.", "source": "UN Secretary-General, 2023"},
                ],
                "collocations": ["unprecedented scale", "unprecedented challenge", "unprecedented growth"],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "word": "precipitate",
                "phonetic": "/prɪˈsɪp.ɪ.teɪt/",
                "pos": "v.",
                "definition": "to cause something to happen suddenly or sooner than expected (usually something bad)",
                "chinese": "促使，加速引发（通常指坏事）",
                "context": "precipitated a rethinking",
                "examples": [
                    {"text": "The assassination precipitated a full-scale military conflict.", "source": "Oxford Advanced Learner's Dictionary"},
                    {"text": "Fear of bank failures can precipitate a broader financial crisis.", "source": "Financial Times, 2023"},
                ],
                "collocations": ["precipitate a crisis", "precipitate change", "precipitate a decline"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "orthodoxy",
                "phonetic": "/ˈɔː.θə.dɒk.si/",
                "pos": "n.",
                "definition": "a generally accepted theory, doctrine, or practice; conventional thinking",
                "chinese": "正统观念，主流学说",
                "context": "challenged the dominant economic orthodoxy",
                "examples": [
                    {"text": "The new findings challenged prevailing scientific orthodoxy.", "source": "Nature, 2022"},
                    {"text": "Economic orthodoxy holds that markets are self-correcting.", "source": "The Economist, 2023"},
                ],
                "collocations": ["economic orthodoxy", "challenge the orthodoxy", "prevailing orthodoxy"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "contend",
                "phonetic": "/kənˈtend/",
                "pos": "v.",
                "definition": "to assert something as a position in an argument; to argue",
                "chinese": "主张，争辩，认为",
                "context": "Others contend that the benefits of free trade remain cogent",
                "examples": [
                    {"text": "Critics contend that the policy will disproportionately affect the poor.", "source": "The Guardian, 2023"},
                    {"text": "Some scientists contend that the data has been misinterpreted.", "source": "Scientific American, 2022"},
                ],
                "collocations": ["contend that", "contend with", "fiercely contend"],
                "level": "CET-6 / IELTS 7.0+",
            },
            {
                "word": "cogent",
                "phonetic": "/ˈkəʊ.dʒənt/",
                "pos": "adj.",
                "definition": "(of an argument or case) clear, logical, and convincing",
                "chinese": "有说服力的，令人信服的",
                "context": "the benefits of free trade remain cogent",
                "examples": [
                    {"text": "She made a cogent argument for increasing public investment.", "source": "Oxford Advanced Learner's Dictionary"},
                    {"text": "The report presents a cogent analysis of the crisis.", "source": "The Economist, 2023"},
                ],
                "collocations": ["cogent argument", "cogent reasoning", "cogent analysis"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "disproportionately",
                "phonetic": "/ˌdɪs.prəˈpɔː.ʃən.ət.li/",
                "pos": "adv.",
                "definition": "to a degree that is too large or too small in comparison with something else",
                "chinese": "不成比例地（通常暗示不公平）",
                "context": "costs have been borne disproportionately by those least able to bear them",
                "examples": [
                    {"text": "Climate change disproportionately affects developing countries.", "source": "IPCC Report, 2022"},
                    {"text": "Minorities are disproportionately represented in the prison population.", "source": "The New York Times, 2023"},
                ],
                "collocations": ["disproportionately affected", "disproportionately high", "disproportionately represented"],
                "level": "CET-6 / IELTS 7.0+",
            },
            {
                "word": "semiconductors",
                "phonetic": "/ˌsem.i.kənˈdʌk.tərz/",
                "pos": "n.",
                "definition": "materials (like silicon chips) that conduct electricity under certain conditions; the chips essential to modern electronics",
                "chinese": "半导体（芯片），现代电子产品的核心元件",
                "context": "secure supply chains for critical goods — semiconductors, medicines, rare-earth minerals",
                "examples": [
                    {"text": "The global shortage of semiconductors disrupted car manufacturing worldwide.", "source": "Financial Times, 2022"},
                    {"text": "Taiwan produces over 60% of the world's advanced semiconductors.", "source": "The Economist, 2023"},
                ],
                "collocations": ["semiconductor shortage", "semiconductor industry", "advanced semiconductors"],
                "level": "IELTS 6.5+ (专业术语)",
            },
            {
                "word": "reshoring",
                "phonetic": "/riːˈʃɔː.rɪŋ/",
                "pos": "n.",
                "definition": "the practice of bringing manufacturing or services back to the home country from overseas",
                "chinese": "回流/回迁（将制造业从海外搬回国内）",
                "context": "The exorbitant cost of this reshoring",
                "examples": [
                    {"text": "Reshoring of chip manufacturing has become a national security priority.", "source": "The New York Times, 2023"},
                    {"text": "The reshoring trend accelerated after the pandemic exposed supply chain risks.", "source": "Harvard Business Review, 2022"},
                ],
                "collocations": ["reshoring trend", "reshoring of manufacturing", "reshoring jobs"],
                "level": "IELTS 7.0+ (经济专业术语)",
            },
            {
                "word": "exorbitant",
                "phonetic": "/ɪɡˈzɔː.bɪ.tənt/",
                "pos": "adj.",
                "definition": "(of a price or amount) unreasonably high; extortionate",
                "chinese": "过高的，离谱的（通常形容价格）",
                "context": "The exorbitant cost of this reshoring",
                "examples": [
                    {"text": "The exorbitant cost of healthcare forces many to forgo treatment.", "source": "The New York Times, 2023"},
                    {"text": "Tourists are often charged exorbitant prices in popular destinations.", "source": "Longman Dictionary"},
                ],
                "collocations": ["exorbitant price", "exorbitant cost", "exorbitant fees"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "commensurate",
                "phonetic": "/kəˈmen.sjʊ.rət/",
                "pos": "adj.",
                "definition": "corresponding in size, extent, or degree; proportional",
                "chinese": "相称的，相当的，成比例的",
                "context": "whether the cure is commensurate with the disease",
                "examples": [
                    {"text": "Salary will be commensurate with experience.", "source": "Oxford Advanced Learner's Dictionary"},
                    {"text": "The punishment should be commensurate with the severity of the crime.", "source": "Merriam-Webster Dictionary"},
                ],
                "collocations": ["commensurate with", "commensurate increase", "commensurate level"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "dichotomy",
                "phonetic": "/daɪˈkɒt.ə.mi/",
                "pos": "n.",
                "definition": "a division into two completely opposite groups or things",
                "chinese": "二分法，截然对立",
                "context": "the old dichotomy between free trade and protectionism",
                "examples": [
                    {"text": "The false dichotomy of nature versus nurture oversimplifies human development.", "source": "Scientific American, 2021"},
                    {"text": "The dichotomy between rich and poor continues to widen.", "source": "The Economist, 2023"},
                ],
                "collocations": ["false dichotomy", "sharp dichotomy", "dichotomy between"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "consensus",
                "phonetic": "/kənˈsen.səs/",
                "pos": "n.",
                "definition": "a general agreement among a group of people",
                "chinese": "共识，一致意见",
                "context": "forge a new consensus",
                "examples": [
                    {"text": "There is a growing consensus among scientists that action is needed.", "source": "Nature, 2023"},
                    {"text": "The committee failed to reach a consensus on the issue.", "source": "Cambridge Dictionary"},
                ],
                "collocations": ["reach a consensus", "broad consensus", "scientific consensus"],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "word": "eschew",
                "phonetic": "/ɪsˈtʃuː/",
                "pos": "v.",
                "definition": "to deliberately avoid or keep away from something",
                "chinese": "避开，回避，有意远离",
                "context": "one that does not eschew openness",
                "examples": [
                    {"text": "The author eschews jargon in favour of plain language.", "source": "Merriam-Webster Dictionary"},
                    {"text": "Many young professionals eschew traditional career paths.", "source": "The Economist, 2023"},
                ],
                "collocations": ["eschew violence", "eschew convention", "eschew responsibility"],
                "level": "TEM-8 / IELTS 8.0+",
            },
            {
                "word": "volatile",
                "phonetic": "/ˈvɒl.ə.taɪl/",
                "pos": "adj.",
                "definition": "liable to change rapidly and unpredictably, especially for the worse",
                "chinese": "不稳定的，动荡的，变化无常的",
                "context": "the volatile and unpredictable world",
                "examples": [
                    {"text": "The stock market has been particularly volatile in recent months.", "source": "Financial Times, 2023"},
                    {"text": "The political situation in the region remains volatile.", "source": "BBC News, 2023"},
                ],
                "collocations": ["volatile market", "volatile situation", "highly volatile"],
                "level": "CET-6 / IELTS 7.0+",
            },
            {
                "word": "pernicious",
                "phonetic": "/pəˈnɪʃ.əs/",
                "pos": "adj.",
                "definition": "having a harmful effect, especially in a gradual or subtle way",
                "chinese": "有害的，恶性的（尤指慢慢起作用的）",
                "context": "the consequences could be far-reaching and pernicious",
                "examples": [
                    {"text": "The pernicious influence of lobbying on democratic governance is well documented.", "source": "Foreign Affairs, 2022"},
                    {"text": "Conspiracy theories have a pernicious effect on public discourse.", "source": "The Atlantic, 2021"},
                ],
                "collocations": ["pernicious effect", "pernicious influence", "pernicious myth"],
                "level": "TEM-8 / IELTS 8.0+",
            },
            {
                "word": "conundrum",
                "phonetic": "/kəˈnʌn.drəm/",
                "pos": "n.",
                "definition": "a confusing and difficult problem or question with no easy answer",
                "chinese": "难题，困境（没有简单解决方案的问题）",
                "context": "The conundrum facing policymakers is acute",
                "examples": [
                    {"text": "The ethical conundrum of AI development has no easy solution.", "source": "MIT Technology Review, 2023"},
                    {"text": "Central bankers face the conundrum of controlling inflation without triggering recession.", "source": "Financial Times, 2023"},
                ],
                "collocations": ["moral conundrum", "face a conundrum", "solve the conundrum"],
                "level": "TEM-8 / IELTS 7.5+",
            },
            {
                "word": "ameliorate",
                "phonetic": "/əˈmiː.li.ə.reɪt/",
                "pos": "v.",
                "definition": "to make a bad or unsatisfactory situation better",
                "chinese": "改善，改良（不好的状况）",
                "context": "ameliorate the genuine hardships",
                "examples": [
                    {"text": "The new policy aims to ameliorate the housing shortage.", "source": "The Guardian, 2023"},
                    {"text": "Technology alone cannot ameliorate deep-rooted social inequalities.", "source": "The New Yorker, 2022"},
                ],
                "collocations": ["ameliorate conditions", "ameliorate the situation", "ameliorate suffering"],
                "level": "TEM-8 / IELTS 8.0+",
            },
            {
                "word": "rampant",
                "phonetic": "/ˈræm.pənt/",
                "pos": "adj.",
                "definition": "(of something unwelcome) flourishing or spreading unchecked",
                "chinese": "猖獗的，蔓延的，不受控制的",
                "context": "rampant protectionism",
                "examples": [
                    {"text": "Corruption remains rampant in many developing nations.", "source": "Transparency International, 2023"},
                    {"text": "Rampant inflation has eroded the purchasing power of ordinary citizens.", "source": "The Economist, 2022"},
                ],
                "collocations": ["rampant corruption", "rampant inflation", "run rampant"],
                "level": "CET-6 / IELTS 7.0+",
            },
        ],

        # ─── DEEP READING: PHRASES ────────────────────────────────
        "annotations_phrases": [
            {
                "phrase": "an article of faith",
                "definition": "a firmly held belief that is accepted without question, almost like religious belief",
                "chinese": "信条，坚定不移的信念（像宗教信仰一样不容质疑的观点）",
                "context": "free trade was an article of faith among economists",
                "explanation": "这里把自由贸易比作「信条」，暗示经济学家们几乎把它当作宗教信仰一样不容置疑，但下文马上就要挑战这个「信仰」了。",
                "examples": [
                    {"text": "For many environmentalists, renewable energy is an article of faith.", "source": "The Guardian, 2022"},
                    {"text": "The idea that markets are always efficient was once an article of faith in economics.", "source": "Financial Times, 2023"},
                ],
                "level": "IELTS 7.0+",
            },
            {
                "phrase": "specialise in",
                "definition": "to focus on and become expert in a particular area or activity",
                "chinese": "专注于，专门从事",
                "context": "countries should specialise in what they do best",
                "explanation": "这是国际贸易理论中「比较优势」(comparative advantage) 的核心概念：每个国家应该做自己最擅长的事情。",
                "examples": [
                    {"text": "Japan specialises in advanced manufacturing and robotics.", "source": "The Economist, 2022"},
                    {"text": "Our company specialises in providing cybersecurity solutions.", "source": "Harvard Business Review, 2023"},
                ],
                "level": "CET-4 / IELTS 5.5+",
            },
            {
                "phrase": "ripple effects",
                "definition": "the continuing and spreading results of an event or action, like ripples in water",
                "chinese": "连锁反应，涟漪效应（像水中涟漪一样不断扩散的影响）",
                "context": "the ripple effects were felt everywhere",
                "explanation": "非常生动的比喻：就像石头扔进水里，涟漪一圈一圈向外扩散。疫情让一个地方的工厂关闭，影响像涟漪一样传遍全球。",
                "examples": [
                    {"text": "The collapse of one major bank sent ripple effects through the entire financial system.", "source": "Financial Times, 2023"},
                    {"text": "The trade war has had ripple effects far beyond the two countries involved.", "source": "The Economist, 2022"},
                ],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "phrase": "give rise to",
                "definition": "to cause something to happen or exist",
                "chinese": "引起，导致，催生",
                "context": "it has also given rise to new schools of thought",
                "explanation": "比 cause 更正式的表达，常用于学术写作。在雅思写作中可以替代 lead to / result in。",
                "examples": [
                    {"text": "The new regulations may give rise to unintended consequences.", "source": "The Economist, 2023"},
                    {"text": "Rapid urbanisation has given rise to a host of social problems.", "source": "UN Habitat Report, 2022"},
                ],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "phrase": "in the wake of",
                "definition": "as a result of; happening after and usually because of",
                "chinese": "在……之后（紧随其后，通常是因果关系）",
                "context": "In the wake of the pandemic",
                "explanation": "wake 原意是船经过后留下的水痕。in the wake of 就像「在（某事件的）尾流中」，强调事件的后续影响。",
                "examples": [
                    {"text": "In the wake of the financial crisis, regulators tightened banking rules.", "source": "Financial Times, 2020"},
                    {"text": "In the wake of the scandal, several executives resigned.", "source": "The Guardian, 2022"},
                ],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "phrase": "scrambled to",
                "definition": "to rush or struggle to do something urgently and in a disorganized way",
                "chinese": "争先恐后地，仓促地（暗示紧急且手忙脚乱）",
                "context": "governments have scrambled to secure supply chains",
                "explanation": "scramble 原意是攀爬、争抢。这里形容各国政府在疫情后手忙脚乱地确保供应链安全，暗示之前缺乏准备。",
                "examples": [
                    {"text": "Airlines scrambled to rebook passengers after the flight cancellations.", "source": "BBC News, 2023"},
                    {"text": "Companies scrambled to find alternative suppliers when trade routes were disrupted.", "source": "The Economist, 2022"},
                ],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "phrase": "by and large",
                "definition": "on the whole; generally speaking; everything considered",
                "chinese": "总的来说，大体上",
                "context": "By and large, economists now acknowledge",
                "explanation": "这个表达来自航海术语，意思是「不管风从哪个方向吹」。在写作中用来引出一个总结性的观点。",
                "examples": [
                    {"text": "By and large, the reforms have been successful.", "source": "Oxford Advanced Learner's Dictionary"},
                    {"text": "The project, by and large, met its objectives.", "source": "Harvard Business Review, 2022"},
                ],
                "level": "CET-6 / IELTS 6.5+",
            },
            {
                "phrase": "rages on",
                "definition": "continues with great force or intensity (used for arguments, battles, storms, etc.)",
                "chinese": "继续激烈地进行着（形容争论、战争、暴风雨等）",
                "context": "While the debate rages on",
                "explanation": "rage 原意是「狂怒」。debate rages on 把辩论比喻成一场不停歇的风暴，说明分歧很大、争论很激烈。",
                "examples": [
                    {"text": "The debate over immigration policy rages on in Congress.", "source": "The New York Times, 2023"},
                    {"text": "As the war rages on, the humanitarian crisis deepens.", "source": "BBC News, 2023"},
                ],
                "level": "CET-6 / IELTS 7.0+",
            },
            {
                "phrase": "forge a consensus",
                "definition": "to create or build an agreement through effort and negotiation",
                "chinese": "达成共识（通过努力和谈判建立一致意见）",
                "context": "The challenge now is to forge a new consensus",
                "explanation": "forge 原意是「锻造」（铁匠打铁）。forge a consensus 暗示达成共识像打铁一样需要反复敲打和不懈努力。",
                "examples": [
                    {"text": "The two parties must forge a consensus on climate policy.", "source": "Foreign Affairs, 2023"},
                    {"text": "It took months to forge a consensus among the member states.", "source": "The Economist, 2023"},
                ],
                "level": "IELTS 7.0+ / TEM-8",
            },
            {
                "phrase": "trade displacement",
                "definition": "the loss of jobs or economic activity in one area caused by international trade shifting production elsewhere",
                "chinese": "贸易替代/贸易转移（因为国际贸易导致某些地方的工作岗位或产业流失）",
                "context": "ameliorate the genuine hardships caused by trade displacement",
                "explanation": "贸易经济学核心概念。自由贸易让一些国家获益，但也会导致另一些国家的工人失业——这就是 trade displacement。",
                "examples": [
                    {"text": "Workers affected by trade displacement often lack the skills to transition to new industries.", "source": "World Bank Report, 2022"},
                    {"text": "Government programmes to address trade displacement have been underfunded.", "source": "The Economist, 2023"},
                ],
                "level": "IELTS 7.0+ (经济专业术语)",
            },
        ],

        # ─── DEEP READING: COMPLEX SENTENCES ──────────────────────
        "annotations_sentences": [
            {
                "sentence": "Yet the world has changed in ways that have exacerbated the shortcomings of this paradigm.",
                "translation": "然而，世界已经发生了变化，而这些变化加剧了这一范式（即自由贸易理论）的不足之处。",
                "breakdown": "主句：the world has changed（世界已经改变）→ in ways that...（以某些方式）→ that 引导定语从句修饰 ways → have exacerbated the shortcomings（加剧了不足）→ of this paradigm（这个范式的）。核心逻辑：世界的变化暴露了自由贸易理论的缺陷。",
                "grammar_points": [
                    "in ways that... 表示「以……的方式」，that 引导定语从句",
                    "现在完成时 has changed / have exacerbated 强调过去的变化对现在仍有影响",
                    "this paradigm 指代前文的「自由贸易信条」",
                ],
                "writing_tip": "这个句式「X has changed in ways that have + 过去分词」非常实用。雅思写作例句：Technology has evolved in ways that have transformed the nature of work. （技术以改变工作本质的方式不断演变。）",
            },
            {
                "sentence": "When a pandemic shut down factories in one corner of the world, the ripple effects were felt everywhere.",
                "translation": "当一场疫情关停了世界某个角落的工厂时，连锁反应传遍了全球各地。",
                "breakdown": "When 引导时间状语从句 → a pandemic shut down factories（疫情关停了工厂）→ in one corner of the world（在世界的某个角落）→ 主句：the ripple effects were felt everywhere（涟漪效应在任何地方都能感受到）。被动语态 were felt 强调的是全球都受到了影响。",
                "grammar_points": [
                    "in one corner of the world 与 everywhere 形成对比，一个角落 vs 全世界",
                    "被动语态 were felt 让「涟漪效应」成为主语，突出影响的广泛性",
                    "ripple effects 是一个生动的比喻（水波涟漪效应）",
                ],
                "writing_tip": "这是一个非常好的「对比式因果句」模板：When X happened in [a small/specific place], the effects were felt [broadly/everywhere]. 雅思写作可用：When one country imposes trade barriers, the economic consequences are felt across the entire region.",
            },
            {
                "sentence": "Not only has this rethinking challenged the dominant economic orthodoxy, but it has also given rise to new schools of thought.",
                "translation": "这种重新思考不仅挑战了占主导地位的经济学正统观念，还催生了新的学派。",
                "breakdown": "Not only...but also... 强调结构 → Not only 放在句首导致部分倒装（has this rethinking，助动词提前）→ 第一层：challenged the dominant economic orthodoxy → 第二层：given rise to new schools of thought。逻辑：不仅「破」了旧的，还「立」了新的。",
                "grammar_points": [
                    "Not only + 倒装：Not only 放在句首时，主句必须用倒装语序（has this... 而不是 this has...）",
                    "but also 后面的从句不需要倒装",
                    "give rise to = cause / lead to（更正式的替换词）",
                ],
                "writing_tip": "Not only...but also + 倒装是雅思高分句式。注意 not only 放在句首才倒装。示例：Not only does social media connect people across borders, but it also provides a platform for misinformation.",
            },
            {
                "sentence": "The exorbitant cost of this reshoring has raised questions about whether the cure is commensurate with the disease.",
                "translation": "这种回流的高昂成本引发了疑问：这种「药方」是否与「疾病」相称？（即代价是否值得）",
                "breakdown": "主句：The exorbitant cost... has raised questions → about whether...（关于是否……）→ the cure is commensurate with the disease（治疗方法与疾病相当）。这里用了一个巧妙的比喻：把回流政策比作「药」（cure），把供应链风险比作「病」（disease）。",
                "grammar_points": [
                    "about whether 引导宾语从句，表示「关于是否」",
                    "commensurate with = 与……相称/成比例",
                    "the cure / the disease 是隐喻，不是真的在讨论医疗",
                ],
                "writing_tip": "「whether the cure is commensurate with the disease」这个比喻可以广泛使用在讨论政策代价的文章中。雅思写作：When evaluating any policy, we must ask whether the cure is commensurate with the disease — that is, whether the costs of intervention outweigh the problem itself.",
            },
            {
                "sentence": "Were the world's leading economies to fail in this endeavour, the consequences could be far-reaching and pernicious.",
                "translation": "如果世界主要经济体在这项努力中失败，后果将是深远而有害的。",
                "breakdown": "这是虚拟语气的倒装形式 → Were... to fail = If... were to fail（如果……失败的话）→ the consequences could be...（后果可能是……）。省略 if，用 Were 开头倒装，是非常正式的书面英语。",
                "grammar_points": [
                    "Were + 主语 + to do = If + 主语 + were to do（虚拟语气的正式倒装写法）",
                    "这不是语法错误！这是高级英语的标准用法，经济学人等严肃刊物经常使用",
                    "could be 表示虚拟的可能性",
                    "far-reaching and pernicious 两个形容词并列，加强语气",
                ],
                "writing_tip": "Were + 主语 + to... 是雅思写作中展示语法功底的高分句式。示例：Were governments to invest more in renewable energy, the long-term benefits would far outweigh the initial costs.",
            },
            {
                "sentence": "They must ameliorate the genuine hardships caused by trade displacement, without triggering the rampant protectionism that could precipitate a global recession.",
                "translation": "他们必须改善贸易转移造成的实实在在的困难，同时又不能引发可能导致全球衰退的猖獗的贸易保护主义。",
                "breakdown": "主干：They must ameliorate... hardships → caused by trade displacement（后置定语，修饰 hardships）→ without triggering...（不能引发……）→ the rampant protectionism → that could precipitate...（that 引导定语从句，修饰 protectionism）→ a global recession。核心矛盾：要帮助受害者，但不能过度保护。",
                "grammar_points": [
                    "must ameliorate... without triggering...：must + 动词... without + 动名词，表示「必须做 A，但不能做 B」",
                    "caused by 过去分词作后置定语",
                    "that could precipitate 定语从句嵌套在 without 短语中",
                    "三层递进：ameliorate hardships → without triggering protectionism → that could precipitate recession",
                ],
                "writing_tip": "「must do A without triggering B」这个结构非常适合讨论政策的两难困境。雅思写作：Governments must stimulate economic growth without exacerbating environmental degradation.",
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 2 — The Atlantic (Editorial)
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Paradox of Connection in a Digital Age",
        "source": "The Atlantic",
        "source_icon": "🌊",
        "category": "editorial",
        "category_label": "社论评论",
        "summary": "We have never been more connected, yet loneliness has become a public-health crisis. How did the tools meant to bring us together end up driving us apart?",
        "link": "https://www.theatlantic.com/ideas/",
        "published": "2025-02-10",
        "has_full_text": True,
        "full_text": """We live in an age of ubiquitous connectivity. Smartphones, social media, and instant messaging have made it possible to reach anyone, anywhere, at any time. Yet paradoxically, loneliness has burgeoned into what some researchers call a modern epidemic. The tools designed to bring us together have, in many cases, driven us further apart.

The insidious nature of this phenomenon lies in its gradualness. No single app or platform precipitated the crisis. Rather, it was the slow, inexorable accumulation of small changes in how we interact — a text message instead of a phone call, a like instead of a conversation, a curated online persona instead of an authentic encounter.

Rarely has a technological revolution produced such equivocal results. On the one hand, social media has galvanized political movements, connected diaspora communities, and given voice to the marginalised. On the other, it has given rise to a culture of comparison and performance that runs counter to genuine human connection.

The dichotomy between online and offline life is, in many ways, a false one. Our digital interactions shape our real-world relationships, and vice versa. With anxiety and depression spiralling among young people, the question of how technology affects mental health has become impossible to obfuscate.

Some researchers argue that the solution is not to eschew technology altogether but to use it more intentionally. This means coming to terms with the fact that a social media feed is a far cry from genuine social connection. It means recognising that the proliferation of communication channels has not been commensurate with an increase in meaningful communication.

Despite the pernicious effects that have been documented, there are grounds for optimism. A burgeoning movement of digital minimalism is gaining traction, particularly among younger users who have grown up with these technologies and understand their limitations. By and large, people are beginning to recalibrate their relationship with their devices.

The path forward hinges on our willingness to be honest about what we have lost in the digital transition — and to take deliberate steps to reclaim it. Although the challenges are formidable, the human need for authentic connection remains as powerful as ever.""",
        "annotations_vocab": [
            {"word": "ubiquitous", "phonetic": "/juːˈbɪk.wɪ.təs/", "pos": "adj.", "definition": "present, appearing, or found everywhere", "chinese": "无处不在的", "context": "an age of ubiquitous connectivity", "examples": [{"text": "Smartphones have become ubiquitous in modern society.", "source": "Cambridge Dictionary"}, {"text": "The ubiquitous surveillance cameras raised privacy concerns.", "source": "The Atlantic, 2022"}], "collocations": ["ubiquitous presence", "increasingly ubiquitous", "ubiquitous technology"], "level": "TEM-8 / IELTS 7.5+"},
            {"word": "burgeoned", "phonetic": "/ˈbɜː.dʒənd/", "pos": "v.", "definition": "to grow or increase rapidly; to flourish", "chinese": "迅速发展，蓬勃增长", "context": "loneliness has burgeoned into what some researchers call a modern epidemic", "examples": [{"text": "The tech sector has burgeoned over the past decade.", "source": "The Economist, 2023"}, {"text": "Online learning burgeoned during the pandemic.", "source": "Harvard Business Review, 2021"}], "collocations": ["burgeoning industry", "burgeoning demand", "burgeoning population"], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "inexorable", "phonetic": "/ɪnˈek.sər.ə.bəl/", "pos": "adj.", "definition": "impossible to stop or prevent; relentless", "chinese": "不可阻挡的，无法改变的", "context": "the slow, inexorable accumulation of small changes", "examples": [{"text": "The inexorable rise of sea levels threatens coastal communities.", "source": "IPCC Report, 2023"}, {"text": "Technology's inexorable march has reshaped every industry.", "source": "MIT Technology Review, 2022"}], "collocations": ["inexorable rise", "inexorable decline", "inexorable march"], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "curated", "phonetic": "/kjʊəˈreɪ.tɪd/", "pos": "adj.", "definition": "carefully chosen and presented; selected to create a particular impression", "chinese": "精心策划的，筛选过的", "context": "a curated online persona", "examples": [{"text": "Social media encourages us to present a curated version of our lives.", "source": "The Atlantic, 2022"}, {"text": "The museum's curated collection spans three centuries.", "source": "The New York Times, 2023"}], "collocations": ["curated content", "carefully curated", "curated experience"], "level": "IELTS 7.0+"},
            {"word": "equivocal", "phonetic": "/ɪˈkwɪv.ə.kəl/", "pos": "adj.", "definition": "open to more than one interpretation; ambiguous; uncertain", "chinese": "模棱两可的，含糊的", "context": "produced such equivocal results", "examples": [{"text": "The minister gave an equivocal response, satisfying neither side.", "source": "The Guardian, 2023"}, {"text": "The scientific evidence remains equivocal on this point.", "source": "Nature, 2022"}], "collocations": ["equivocal answer", "equivocal evidence", "equivocal results"], "level": "TEM-8 / IELTS 7.5+"},
            {"word": "galvanized", "phonetic": "/ˈɡæl.və.naɪzd/", "pos": "v.", "definition": "to shock or excite someone into taking action", "chinese": "激励，刺激（某人采取行动）", "context": "social media has galvanized political movements", "examples": [{"text": "The tragedy galvanized public opinion in favour of stricter gun laws.", "source": "The New York Times, 2022"}, {"text": "The speech galvanized the crowd into action.", "source": "Longman Dictionary"}], "collocations": ["galvanize support", "galvanize action", "galvanize the public"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "diaspora", "phonetic": "/daɪˈæs.pər.ə/", "pos": "n.", "definition": "people who have spread or been dispersed from their homeland", "chinese": "侨民，散居海外的族群", "context": "connected diaspora communities", "examples": [{"text": "The Chinese diaspora plays a significant role in Southeast Asian economies.", "source": "The Economist, 2023"}, {"text": "Social media helps diaspora communities maintain cultural ties.", "source": "BBC News, 2022"}], "collocations": ["the diaspora", "diaspora communities", "diaspora networks"], "level": "IELTS 7.5+"},
            {"word": "obfuscate", "phonetic": "/ˈɒb.fʌ.skeɪt/", "pos": "v.", "definition": "to make something unclear, confusing, or hard to understand", "chinese": "使模糊，使混淆", "context": "has become impossible to obfuscate", "examples": [{"text": "Politicians often obfuscate the issue with misleading statistics.", "source": "The New York Times, 2022"}, {"text": "Complex legal language can obfuscate rather than clarify meaning.", "source": "Cambridge Dictionary"}], "collocations": ["obfuscate the truth", "obfuscate the issue", "deliberately obfuscate"], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "recalibrate", "phonetic": "/riːˈkæl.ɪ.breɪt/", "pos": "v.", "definition": "to adjust or change one's approach, especially after new information or experience", "chinese": "重新调整，重新校准", "context": "people are beginning to recalibrate their relationship with their devices", "examples": [{"text": "Companies are recalibrating their strategies in response to changing consumer behaviour.", "source": "Harvard Business Review, 2023"}, {"text": "We need to recalibrate our expectations about economic growth.", "source": "The Economist, 2023"}], "collocations": ["recalibrate expectations", "recalibrate strategy", "recalibrate one's approach"], "level": "IELTS 7.5+"},
            {"word": "formidable", "phonetic": "/fɔːˈmɪd.ə.bəl/", "pos": "adj.", "definition": "inspiring fear or respect through being impressively large, powerful, or difficult", "chinese": "令人敬畏的，巨大的（挑战），难以对付的", "context": "Although the challenges are formidable", "examples": [{"text": "The team faces a formidable opponent in the final.", "source": "BBC Sport, 2023"}, {"text": "Climate change presents formidable challenges for policymakers.", "source": "Nature, 2023"}], "collocations": ["formidable challenge", "formidable opponent", "formidable task"], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_phrases": [
            {"phrase": "a far cry from", "definition": "very different from; nothing like", "chinese": "与……相去甚远，完全不同", "context": "a social media feed is a far cry from genuine social connection", "explanation": "强调两者之间的巨大差距。社交媒体上的互动和真正的人际连接完全不是一回事。", "examples": [{"text": "The final product was a far cry from what was originally promised.", "source": "The Economist, 2023"}, {"text": "Life in the city is a far cry from rural tranquillity.", "source": "Cambridge Dictionary"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "come to terms with", "definition": "to gradually accept a difficult or unpleasant situation", "chinese": "接受，学会面对（困难的事实）", "context": "coming to terms with the fact that", "explanation": "不是突然接受，而是经历一个心理过程后逐渐承认事实。", "examples": [{"text": "The nation is still coming to terms with the aftermath of the crisis.", "source": "The Atlantic, 2022"}, {"text": "She has finally come to terms with her diagnosis.", "source": "Longman Dictionary"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "runs counter to", "definition": "goes against; is in conflict with", "chinese": "与……相悖，背道而驰", "context": "a culture of comparison and performance that runs counter to genuine human connection", "explanation": "比 contradicts 更正式和生动的表达。", "examples": [{"text": "The policy runs counter to the principles of free trade.", "source": "The Economist, 2023"}, {"text": "His actions run counter to his stated beliefs.", "source": "Oxford Advanced Learner's Dictionary"}], "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "hinges on", "definition": "depends entirely on; is determined by", "chinese": "取决于，关键在于", "context": "The path forward hinges on our willingness", "explanation": "hinge 是门的铰链，门能否打开完全取决于铰链。hinges on 就是「完全取决于」。", "examples": [{"text": "The success of the negotiations hinges on both sides making concessions.", "source": "Foreign Affairs, 2023"}, {"text": "The election outcome hinges on voter turnout.", "source": "The New York Times, 2024"}], "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "gaining traction", "definition": "becoming increasingly popular or accepted; building momentum", "chinese": "越来越受欢迎，逐渐获得关注和支持", "context": "A burgeoning movement of digital minimalism is gaining traction", "explanation": "traction 原意是「牵引力、抓地力」。gaining traction 就像轮胎获得抓地力，开始前进。", "examples": [{"text": "The idea of a four-day working week is gaining traction in Europe.", "source": "The Guardian, 2023"}, {"text": "Electric vehicles are gaining traction in developing markets.", "source": "Financial Times, 2023"}], "level": "IELTS 7.0+"},
        ],
        "annotations_sentences": [
            {"sentence": "The insidious nature of this phenomenon lies in its gradualness.", "translation": "这个现象的阴险之处在于它的渐进性。", "breakdown": "主语：The insidious nature（阴险本质）→ of this phenomenon（这个现象的）→ 谓语：lies in（在于）→ its gradualness（它的渐进性）。简洁有力的一句话，点出了为什么人们没有察觉社交媒体对人际关系的侵蚀——因为它是慢慢发生的。", "grammar_points": ["lies in = 在于，关键是", "insidious 强调「不知不觉中造成伤害」", "gradualness 由 gradual + ness 构成的抽象名词"], "writing_tip": "「The nature of X lies in Y」是一个很好的学术写作句式。雅思范例：The appeal of social media lies in its ability to provide instant gratification."},
            {"sentence": "Rarely has a technological revolution produced such equivocal results.", "translation": "很少有一次技术革命产生了如此模棱两可的结果。", "breakdown": "Rarely 放在句首引发部分倒装 → has a technological revolution（助动词提前）→ produced such equivocal results。正常语序是 A technological revolution has rarely produced... 倒装让语气更强。", "grammar_points": ["否定副词 Rarely 放句首，主句必须倒装", "equivocal results = 好坏参半的结果", "such 加强语气"], "writing_tip": "否定副词 + 倒装是高分句式。可用的否定副词：Never, Rarely, Seldom, Hardly, Not only。雅思范例：Seldom has a policy change generated such widespread debate."},
            {"sentence": "The path forward hinges on our willingness to be honest about what we have lost in the digital transition — and to take deliberate steps to reclaim it.", "translation": "前进的道路取决于我们是否愿意坦诚面对在数字化转型中所失去的东西——并采取有意识的步骤去重新夺回它。", "breakdown": "主句：The path forward hinges on our willingness → to be honest about what we have lost（坦诚面对失去的）→ in the digital transition → 破折号引出第二层：and to take deliberate steps to reclaim it（并有意识地去找回）。两个 to 并列：to be honest 和 to take steps。", "grammar_points": ["hinges on + 名词/动名词 = 取决于", "what we have lost — what 引导名词性从句", "deliberate steps = 经过深思熟虑的步骤（不是随意的）", "破折号用于追加补充信息"], "writing_tip": "「The path forward hinges on...」可以用在任何需要指出关键因素的场合。雅思范例：The path forward hinges on governments' willingness to prioritise long-term sustainability over short-term economic gains."},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 3 — The New Yorker (Literature)
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Last Library: A Short Story",
        "source": "The New Yorker",
        "source_icon": "🎭",
        "category": "literature",
        "category_label": "文学小说",
        "summary": "In a world where physical books have become relics, one woman guards the last public library — and the memories it holds.",
        "link": "https://www.newyorker.com/fiction",
        "published": "2025-03-05",
        "has_full_text": True,
        "full_text": """The library stood at the corner of Maple and Fifth, its limestone facade weathered but unbowed, a relic of an era that had passed so gradually that few had noticed its departure. Margaret Chen had been its sole librarian for eleven years, and in that time, the number of daily visitors had dwindled from a modest stream to a barely perceptible trickle.

She arrived each morning at precisely seven forty-five, unlocking the heavy oak doors with a brass key that bore the patina of a century of use. The ritual was unchanged: lights on, heating adjusted, the overnight returns — there were seldom any — checked and reshelved. It was a routine she performed with the quiet precision of someone who understood that small acts of maintenance hold sway against the inexorable forces of entropy.

The city council had been making noises about the building for years. Not hostile noises, exactly, but the kind of equivocal murmuring that, in the language of bureaucracy, set the stage for a predetermined conclusion. "Underutilised asset" was the phrase that appeared with rampant frequency in their reports. Margaret had learned to read these documents the way a sailor reads clouds — not for what they said, but for what they portended.

With its shelves of unread volumes standing like sentinels, the library had become something of a conundrum for the authorities. Closing it would precipitate accusations of cultural vandalism. Keeping it open was an exorbitant indulgence in an era of austerity. And so it persisted in a kind of administrative limbo, its funding cut but never quite severed, its future perpetually uncertain.

It was on a Tuesday in late October — the kind of grey, imperious day that makes the idea of a warm room full of books seem less like nostalgia and more like necessity — that the boy appeared. He was perhaps twelve, thin and watchful, with the wary bearing of someone accustomed to navigating spaces where he was not entirely welcome. He stood in the doorway for a long moment, taking in the high ceilings, the oak reading tables, the amber light filtering through tall windows.

"Is this really a library?" he asked. "With actual books?"

Margaret smiled. It was not the first time she had encountered this particular species of wonder, but it never failed to galvanize something in her — a reminder of why she remained.

"It is," she said. "Would you like to see?"

He stepped inside, his footsteps echoing in the vast, quiet space. She watched as he reached out and touched the spine of a book — tentatively, the way one might touch something fragile and precious. In that gesture, Margaret saw neither the past nor the future, but something rarer: the present, undiluted and fully inhabited.

The boy came back the next day, and the day after that. He read voraciously, indiscriminately — novels, histories, atlases, volumes of poetry. He did not eschew any genre or period. It was as though he were trying to consume the entire accumulated knowledge of the printed word before some unspoken deadline.

Margaret never asked his name. To name him would have been to fix him in time, and she preferred to let him exist, as the library itself did, in a space slightly apart from the ordinary reckoning of things. She understood, in a way she could not have articulated, that some things bear the brunt of meaning precisely because they remain unnamed.""",
        "annotations_vocab": [
            {"word": "facade", "phonetic": "/fəˈsɑːd/", "pos": "n.", "definition": "the front of a building; also figuratively, a deceptive outward appearance", "chinese": "建筑正面，外墙；（比喻）表面，假象", "context": "its limestone facade weathered but unbowed", "examples": [{"text": "Behind the cheerful facade, she was deeply unhappy.", "source": "Longman Dictionary"}, {"text": "The grand facade of the cathedral dates back to the 14th century.", "source": "The Guardian, 2022"}], "collocations": ["behind the facade", "put on a facade", "facade of normality"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "unbowed", "phonetic": "/ʌnˈbaʊd/", "pos": "adj.", "definition": "not having given in to pressure; not defeated or discouraged", "chinese": "不屈的，不低头的", "context": "weathered but unbowed", "examples": [{"text": "Despite years of hardship, the community remained unbowed.", "source": "The New York Times, 2022"}, {"text": "Bloodied but unbowed, she continued her fight for justice.", "source": "The Guardian, 2023"}], "collocations": ["bloodied but unbowed", "remain unbowed", "unbowed spirit"], "level": "IELTS 7.5+"},
            {"word": "dwindled", "phonetic": "/ˈdwɪn.dəld/", "pos": "v.", "definition": "to gradually become less or smaller over time", "chinese": "逐渐减少，慢慢缩小", "context": "the number of daily visitors had dwindled", "examples": [{"text": "The population of the village has dwindled to just a few hundred.", "source": "BBC News, 2022"}, {"text": "Public trust in institutions has dwindled over the past decade.", "source": "The Economist, 2023"}], "collocations": ["dwindle away", "dwindle to", "dwindling resources"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "patina", "phonetic": "/ˈpæt.ɪ.nə/", "pos": "n.", "definition": "a surface appearance of something grown beautiful with age or use; a green film on copper or bronze", "chinese": "铜绿；岁月留下的痕迹（带有美感的）", "context": "a brass key that bore the patina of a century of use", "examples": [{"text": "The old desk had a beautiful patina that spoke of decades of use.", "source": "The New Yorker, 2022"}, {"text": "The bronze statue had acquired a green patina over the years.", "source": "Merriam-Webster Dictionary"}], "collocations": ["patina of age", "develop a patina", "rich patina"], "level": "IELTS 8.0+ (文学词汇)"},
            {"word": "entropy", "phonetic": "/ˈen.trə.pi/", "pos": "n.", "definition": "a gradual decline into disorder; (physics) a measure of disorder in a system", "chinese": "熵；（比喻）衰败，无序化", "context": "the inexorable forces of entropy", "examples": [{"text": "Without constant effort, organisations tend towards entropy.", "source": "Harvard Business Review, 2022"}, {"text": "The second law of thermodynamics states that entropy always increases.", "source": "Nature, 2021"}], "collocations": ["forces of entropy", "increase in entropy", "fight against entropy"], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "portended", "phonetic": "/pɔːˈten.dɪd/", "pos": "v.", "definition": "to be a sign or warning that something (usually bad) is going to happen", "chinese": "预示，预兆（通常是坏事）", "context": "not for what they said, but for what they portended", "examples": [{"text": "The dark clouds portended a violent storm.", "source": "Oxford Advanced Learner's Dictionary"}, {"text": "The economic indicators portended a recession.", "source": "Financial Times, 2023"}], "collocations": ["portend disaster", "portend change", "what it portends"], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "sentinels", "phonetic": "/ˈsen.tɪ.nəlz/", "pos": "n.", "definition": "soldiers or guards whose job is to stand and keep watch; anything that stands watch", "chinese": "哨兵，守卫者", "context": "shelves of unread volumes standing like sentinels", "examples": [{"text": "The ancient oaks stood like sentinels along the avenue.", "source": "The New Yorker, 2022"}, {"text": "Lighthouses serve as sentinels along the coast.", "source": "Collins English Dictionary"}], "collocations": ["stand like sentinels", "silent sentinels", "serve as sentinels"], "level": "IELTS 7.5+ (文学词汇)"},
            {"word": "limbo", "phonetic": "/ˈlɪm.bəʊ/", "pos": "n.", "definition": "an uncertain period of awaiting a decision or resolution; an intermediate state", "chinese": "悬而未决的状态，不确定的等待期", "context": "persisted in a kind of administrative limbo", "examples": [{"text": "The project has been in limbo since the funding was cut.", "source": "The Guardian, 2023"}, {"text": "Thousands of refugees remain in legal limbo.", "source": "BBC News, 2023"}], "collocations": ["in limbo", "left in limbo", "political limbo"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "voraciously", "phonetic": "/vəˈreɪ.ʃəs.li/", "pos": "adv.", "definition": "in an eager and enthusiastic way, wanting a lot (especially of reading or eating)", "chinese": "如饥似渴地，贪婪地", "context": "He read voraciously, indiscriminately", "examples": [{"text": "She reads voraciously — at least three books a week.", "source": "The New Yorker, 2022"}, {"text": "The child consumed information voraciously.", "source": "Cambridge Dictionary"}], "collocations": ["read voraciously", "consume voraciously", "voracious reader"], "level": "TEM-8 / IELTS 7.5+"},
        ],
        "annotations_phrases": [
            {"phrase": "hold sway", "definition": "to have great power or influence; to dominate", "chinese": "有影响力，占支配地位", "context": "small acts of maintenance hold sway against the inexorable forces of entropy", "explanation": "sway 是摇摆。hold sway 就是「掌握摇摆的方向」，即掌控局面。这里说的是：微小的日常维护工作能够对抗衰败的力量。", "examples": [{"text": "Traditional values still hold sway in many rural communities.", "source": "The New Yorker, 2022"}, {"text": "The old guard continues to hold sway over the party.", "source": "The Economist, 2023"}], "level": "TEM-8 / IELTS 7.5+"},
            {"phrase": "set the stage for", "definition": "to create the conditions for something to happen", "chinese": "为……创造条件，为……铺垫", "context": "set the stage for a predetermined conclusion", "explanation": "像戏剧一样——先布置好舞台，戏就会按预设的方向上演。这里暗示市议会已经决定要关闭图书馆，现在只是在走过场。", "examples": [{"text": "The reforms set the stage for a decade of economic growth.", "source": "The Economist, 2022"}, {"text": "Recent events have set the stage for a dramatic confrontation.", "source": "Foreign Affairs, 2023"}], "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "bear the brunt of", "definition": "to suffer the worst part of something unpleasant", "chinese": "首当其冲，承受最大的压力或伤害", "context": "some things bear the brunt of meaning precisely because they remain unnamed", "explanation": "这里用法很文学化。通常 bear the brunt of 指承受损害，但作者反转了用法——有些事物之所以承载最深的意义，恰恰因为它们没有被命名。", "examples": [{"text": "Low-income families bear the brunt of rising food prices.", "source": "The Guardian, 2023"}, {"text": "Coastal regions bore the brunt of the hurricane.", "source": "The New York Times, 2022"}], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_sentences": [
            {"sentence": "It was a routine she performed with the quiet precision of someone who understood that small acts of maintenance hold sway against the inexorable forces of entropy.", "translation": "这是她以一种安静的精确性所执行的日常，这种精确性来自于一个深知微小的维护行为能够抵御不可阻挡的衰败力量的人。", "breakdown": "主句：It was a routine → she performed（定语从句修饰 routine）→ with the quiet precision of someone → who understood that...（who 引导定语从句修饰 someone）→ small acts of maintenance hold sway against the inexorable forces of entropy（that 引导宾语从句）。三层嵌套：routine → precision of someone → who understood that...。", "grammar_points": ["多层定语从句嵌套", "with + 名词 表示「以……的方式」", "hold sway against = 对抗，抵御", "entropy（熵）在此是文学比喻，指一切趋向衰败的自然力量"], "writing_tip": "这种多层嵌套的长句是文学写作的典型特征。在学术写作中要适度使用，确保读者能跟上逻辑。"},
            {"sentence": "Margaret had learned to read these documents the way a sailor reads clouds — not for what they said, but for what they portended.", "translation": "玛格丽特已经学会了像水手读云一样读这些文件——不是看它们说了什么，而是看它们预示着什么。", "breakdown": "主句：Margaret had learned to read these documents → the way a sailor reads clouds（比喻，方式状语从句）→ 破折号后解释：not for what they said（不是为了字面意思）→ but for what they portended（而是为了它们暗示的东西）。", "grammar_points": ["the way + 从句 = 以……的方式", "not for... but for... 对比强调", "what they portended — what 引导名词性从句", "这个比喻精妙：水手看云不是欣赏风景，而是判断暴风雨是否要来"], "writing_tip": "「the way + 比喻」是非常有力的修辞手法。在写作中可以用来让抽象概念变得生动。"},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 4 — The Economist (Politics & Economics)
    # ═══════════════════════════════════════════════════════════
    {
        "title": "Artificial Intelligence and the Future of Work: Beyond the Hype",
        "source": "The Economist",
        "source_icon": "📊",
        "category": "politics_economics",
        "category_label": "政治经济",
        "summary": "As AI transforms industries, the real question is not whether jobs will disappear, but how societies will manage the transition.",
        "link": "https://www.economist.com/leaders/",
        "published": "2025-04-20",
        "has_full_text": True,
        "full_text": """The proliferation of artificial intelligence in the workplace has precipitated a debate that, by and large, generates more heat than light. Apocalyptic predictions of mass unemployment vie with utopian visions of a leisure society. The truth, as is often the case, is more nuanced — and more interesting — than either extreme.

What is unprecedented about the current wave of automation is not its scale but its scope. Previous technological revolutions displaced manual labour; AI threatens to displace cognitive labour as well. Lawyers, radiologists, financial analysts — professions once considered immune to automation — now find themselves in the crosshairs. The paradigm of "safe" careers is being fundamentally challenged.

Not only does this raise practical questions about retraining and social safety nets, but it also gives rise to deeper philosophical questions about the nature of work itself. If machines can perform cognitive tasks with greater speed and accuracy, what is the distinctive human contribution? The answer may hinge on qualities that are difficult to automate: creativity, empathy, ethical judgment, and the ability to navigate ambiguity.

The insidious danger lies not in AI itself but in the intransigent refusal to prepare for its consequences. History offers a cogent warning: the Industrial Revolution, while ultimately beneficial, precipitated decades of social upheaval because institutions failed to adapt at the pace of technological change. We are in danger of repeating this pattern.

In the wake of each new AI breakthrough, governments have scrambled to respond. Yet their efforts have often fallen short of what is needed. The exorbitant cost of comprehensive retraining programmes has led many to settle for half-measures — a far cry from the systemic transformation that the situation demands.

While some argue that the market will naturally ameliorate the disruption, this view runs counter to the evidence. The volatile nature of technological change means that the benefits and costs will not be evenly distributed. Those who bear the brunt of displacement will be, disproportionately, workers in routine cognitive and manual roles — precisely those with the fewest resources to adapt.

Were policymakers to take the long view, they would recognise that the conundrum of AI and employment is not primarily a technological problem but a political one. It is the question of how a society chooses to distribute the gains from increased productivity. The ubiquitous presence of AI in our daily lives makes this question not merely academic but urgently practical.

Despite these challenges, there are reasons for cautious optimism. A burgeoning ecosystem of human-AI collaboration is emerging, one in which artificial intelligence augments rather than replaces human capabilities. The key is to ensure that this collaboration is commensurate with broad social benefit, rather than concentrated among a narrow elite. The stakes, quite simply, could not be higher.""",
        "annotations_vocab": [
            {"word": "apocalyptic", "phonetic": "/əˌpɒk.əˈlɪp.tɪk/", "pos": "adj.", "definition": "describing or prophesying the complete destruction of the world; extremely catastrophic", "chinese": "世界末日般的，灾难性的", "context": "Apocalyptic predictions of mass unemployment", "examples": [{"text": "The report painted an apocalyptic picture of environmental collapse.", "source": "The Guardian, 2023"}, {"text": "His apocalyptic warnings proved exaggerated.", "source": "The Economist, 2022"}], "collocations": ["apocalyptic scenario", "apocalyptic vision", "apocalyptic warning"], "level": "IELTS 7.5+"},
            {"word": "vie", "phonetic": "/vaɪ/", "pos": "v.", "definition": "to compete eagerly with others for something", "chinese": "竞争，争夺", "context": "Apocalyptic predictions... vie with utopian visions", "examples": [{"text": "Several companies are vying for the contract.", "source": "Cambridge Dictionary"}, {"text": "The two candidates are vying for the presidency.", "source": "The New York Times, 2024"}], "collocations": ["vie for", "vie with", "vie for attention"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "nuanced", "phonetic": "/ˈnjuː.ɑːnst/", "pos": "adj.", "definition": "characterized by subtle differences or distinctions; not simplistic", "chinese": "细致入微的，有层次的", "context": "The truth is more nuanced", "examples": [{"text": "The issue requires a more nuanced approach.", "source": "Foreign Affairs, 2023"}, {"text": "His understanding of the problem is remarkably nuanced.", "source": "The Atlantic, 2022"}], "collocations": ["nuanced understanding", "nuanced approach", "more nuanced"], "level": "IELTS 7.0+"},
            {"word": "intransigent", "phonetic": "/ɪnˈtræn.sɪ.dʒənt/", "pos": "adj.", "definition": "unwilling to change one's views or to agree; stubbornly inflexible", "chinese": "不妥协的，固执的，顽固不化的", "context": "the intransigent refusal to prepare", "examples": [{"text": "The intransigent stance of both parties made negotiations impossible.", "source": "The Economist, 2023"}, {"text": "Government intransigence on reform has frustrated voters.", "source": "BBC News, 2022"}], "collocations": ["intransigent position", "intransigent attitude", "remain intransigent"], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "upheaval", "phonetic": "/ʌpˈhiː.vəl/", "pos": "n.", "definition": "a violent or sudden change or disruption to something", "chinese": "剧变，动荡，大动乱", "context": "precipitated decades of social upheaval", "examples": [{"text": "The country experienced political upheaval following the contested election.", "source": "BBC News, 2023"}, {"text": "Technological upheaval has reshaped entire industries.", "source": "Harvard Business Review, 2022"}], "collocations": ["social upheaval", "political upheaval", "economic upheaval"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "augments", "phonetic": "/ɔːɡˈments/", "pos": "v.", "definition": "to make something greater by adding to it; to enhance", "chinese": "增强，扩大，补充", "context": "artificial intelligence augments rather than replaces human capabilities", "examples": [{"text": "Technology should augment human decision-making, not replace it.", "source": "MIT Technology Review, 2023"}, {"text": "The new evidence augments our understanding of the disease.", "source": "Nature, 2022"}], "collocations": ["augment capabilities", "augment income", "augment reality"], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_phrases": [
            {"phrase": "more heat than light", "definition": "producing more anger/controversy than useful understanding", "chinese": "争论多于实质（产生的愤怒和争议多于有用的见解）", "context": "a debate that generates more heat than light", "explanation": "绝妙的比喻：辩论像火一样产生了很多「热量」（激烈的争吵），却没产生多少「光」（有价值的认识）。", "examples": [{"text": "The parliamentary debate generated more heat than light.", "source": "The Economist, 2023"}, {"text": "Social media discussions often produce more heat than light.", "source": "The Atlantic, 2022"}], "level": "IELTS 7.0+"},
            {"phrase": "in the crosshairs", "definition": "being targeted; at risk of being affected or attacked", "chinese": "成为目标，处于危险之中（原意是枪的瞄准器中心）", "context": "now find themselves in the crosshairs", "explanation": "crosshairs 是步枪瞄准镜中的十字线。处于 crosshairs 中就是被瞄准了，暗示这些职业正面临被 AI 取代的威胁。", "examples": [{"text": "The tech industry now finds itself in the crosshairs of regulators.", "source": "Financial Times, 2023"}, {"text": "Middle-class jobs are increasingly in the crosshairs of automation.", "source": "The Economist, 2023"}], "level": "IELTS 7.5+"},
            {"phrase": "fallen short of", "definition": "failed to reach or achieve a required or expected standard", "chinese": "未达到，不够，没有达到预期", "context": "their efforts have often fallen short of what is needed", "explanation": "fall short 像跳远一样——跳了，但没到标线。", "examples": [{"text": "The company's earnings fell short of analysts' expectations.", "source": "Financial Times, 2023"}, {"text": "The agreement falls short of what environmentalists had hoped for.", "source": "The Guardian, 2023"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "settle for half-measures", "definition": "to accept an inadequate or incomplete solution instead of a proper one", "chinese": "退而求其次，接受不够彻底的方案", "context": "has led many to settle for half-measures", "explanation": "half-measures = 只做了一半的措施。settle for = 勉强接受。整个表达暗示政府因为成本太高，只做了些不到位的事。", "examples": [{"text": "We cannot afford to settle for half-measures on climate change.", "source": "The Guardian, 2023"}, {"text": "The reform was dismissed as a half-measure that would change nothing.", "source": "The Economist, 2022"}], "level": "IELTS 7.0+"},
        ],
        "annotations_sentences": [
            {"sentence": "The proliferation of artificial intelligence in the workplace has precipitated a debate that, by and large, generates more heat than light.", "translation": "人工智能在职场中的激增引发了一场总体上争论多于实质的辩论。", "breakdown": "主句：The proliferation... has precipitated a debate → that 引导定语从句修饰 debate → by and large（插入语，总体上）→ generates more heat than light（比喻：产生的争议多于有价值的见解）。", "grammar_points": ["that 引导定语从句", "by and large 作插入语，用逗号隔开", "more heat than light 是固定比喻表达"], "writing_tip": "「X has precipitated a debate that...」是讨论争议话题的好开头。雅思范例：The rapid development of AI has precipitated a debate that divides experts across disciplines."},
            {"sentence": "What is unprecedented about the current wave of automation is not its scale but its scope.", "translation": "当前这波自动化浪潮前所未有的地方不在于它的规模，而在于它的范围。", "breakdown": "What 引导主语从句 → What is unprecedented about...（关于……前所未有的是）→ is（系动词）→ not... but...（不是……而是……）→ not its scale but its scope。用 not A but B 的对比结构点出关键区别。", "grammar_points": ["What 引导名词性从句做主语", "not A but B 对比强调结构", "scale（规模）vs scope（范围/广度）的精确区分"], "writing_tip": "「What is X about Y is not A but B」是一个很有力的论证开头。雅思范例：What is concerning about social media is not its existence but its pervasive influence on young minds."},
            {"sentence": "Were policymakers to take the long view, they would recognise that the conundrum of AI and employment is not primarily a technological problem but a political one.", "translation": "如果决策者能够有长远眼光的话，他们就会认识到，AI与就业的难题主要不是一个技术问题，而是一个政治问题。", "breakdown": "Were... to take（虚拟语气倒装 = If policymakers were to take）→ the long view（长远视角）→ they would recognise that...（他们就会认识到）→ the conundrum is not primarily... but...（这个难题主要不是……而是……）。", "grammar_points": ["Were + 主语 + to do = If + 主语 + were to do（虚拟语气倒装）", "take the long view = 从长远角度看", "not primarily A but B = 主要不是A而是B"], "writing_tip": "Were + 主语 + to... 在雅思8分作文中非常出彩。练习：Were educators to embrace AI as a teaching tool, the quality of personalised learning could improve dramatically."},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 5 — The New Yorker (Literature)
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Architecture of Silence: What Empty Spaces Tell Us",
        "source": "The New Yorker",
        "source_icon": "🎭",
        "category": "literature",
        "category_label": "文学小说",
        "summary": "An exploration of how abandoned buildings, empty rooms, and forgotten places speak volumes about the societies that created — and left — them.",
        "link": "https://www.newyorker.com/culture",
        "published": "2025-05-01",
        "has_full_text": True,
        "full_text": """There is an eloquence to emptiness that the crowded world finds difficult to hear. Walk through an abandoned factory, a decommissioned church, or a shuttered school, and you will encounter a form of narrative that no living voice could replicate. These spaces speak not in the language of what they contain, but in the grammar of what has been removed.

The proliferation of such spaces in the post-industrial landscape has given rise to a curious subculture of urban explorers — photographers and writers who seek out the ruins of modernity with the fervour of nineteenth-century archaeologists. Their work, at its best, is a far cry from mere nostalgia. It is an attempt to shed light on the processes of economic and social change that, in their inexorable operation, render entire communities obsolete.

In the wake of deindustrialisation, cities like Detroit, Sheffield, and the towns of the German Ruhr Valley have had to come to terms with a new identity. The austerity that followed the loss of their primary industries was not merely fiscal but existential. What is a steel town without steel? What is a mining village when the mines have closed? The conundrum is not simply economic; it touches the deepest questions of belonging and purpose.

While some of these communities have managed to reinvent themselves, many have not. The dichotomy between those that adapted and those that did not hinges, in large part, on factors beyond their control: geography, political will, the volatile currents of global capital. By and large, the places that recovered were those with access to education, transport links, and the kind of civic infrastructure that set the stage for new industries. Those that lacked these advantages bore the brunt of change.

The pernicious myth of individual resilience — the idea that anyone can succeed if they simply try hard enough — runs counter to the lived experience of these communities. It is an ideology that obfuscates the structural forces at work, allowing policymakers to eschew responsibility for the collective consequences of economic transformation.

With their crumbling walls whispering stories of departed lives, these empty buildings serve as a rebuke to the complacent narrative of progress. They remind us that every act of creation is shadowed by an act of destruction, and that the unprecedented pace of change in the modern world has not been commensurate with an unprecedented capacity to manage its fallout.

Rarely has a society been forced to confront so directly the gap between its self-image and its reality. The architecture of silence asks us to listen — not to what we wish to hear, but to what the evidence plainly states. And in that listening, there may yet be the seed of a more honest, more equivocal, but ultimately more humane understanding of what it means to live in a world that never stops changing.""",
        "annotations_vocab": [
            {"word": "eloquence", "phonetic": "/ˈel.ə.kwəns/", "pos": "n.", "definition": "the art of using language in a fluent and persuasive way; expressive power", "chinese": "雄辩，口才；表现力", "context": "There is an eloquence to emptiness", "examples": [{"text": "The eloquence of her speech moved the audience to tears.", "source": "The Guardian, 2022"}, {"text": "His writing has an eloquence that few can match.", "source": "The New Yorker, 2023"}], "collocations": ["natural eloquence", "quiet eloquence", "eloquence of silence"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "decommissioned", "phonetic": "/ˌdiː.kəˈmɪʃ.ənd/", "pos": "adj.", "definition": "withdrawn from active service; shut down (of a facility, ship, or nuclear plant)", "chinese": "退役的，停用的", "context": "a decommissioned church", "examples": [{"text": "The decommissioned power plant is now a museum.", "source": "BBC News, 2022"}, {"text": "Several decommissioned military bases have been converted into housing.", "source": "The Guardian, 2023"}], "collocations": ["decommissioned plant", "decommissioned facility", "decommissioned ship"], "level": "IELTS 7.0+"},
            {"word": "obsolete", "phonetic": "/ˌɒb.səˈliːt/", "pos": "adj.", "definition": "no longer produced or used; outdated; made unnecessary", "chinese": "过时的，被淘汰的", "context": "render entire communities obsolete", "examples": [{"text": "New technology has made many traditional skills obsolete.", "source": "The Economist, 2023"}, {"text": "The factory became obsolete when production moved overseas.", "source": "Financial Times, 2022"}], "collocations": ["become obsolete", "render obsolete", "technologically obsolete"], "level": "CET-6 / IELTS 6.5+"},
            {"word": "deindustrialisation", "phonetic": "/diːɪnˌdʌs.tri.əl.aɪˈzeɪ.ʃən/", "pos": "n.", "definition": "the reduction of industrial activity in a region, especially heavy industry", "chinese": "去工业化（某个地区的工业活动减少或消失）", "context": "In the wake of deindustrialisation", "examples": [{"text": "Deindustrialisation left many communities without a source of livelihood.", "source": "The Economist, 2022"}, {"text": "The social costs of deindustrialisation are still being felt today.", "source": "The Guardian, 2023"}], "collocations": ["post-industrial", "deindustrialisation of", "effects of deindustrialisation"], "level": "IELTS 7.5+ (社会学术语)"},
            {"word": "complacent", "phonetic": "/kəmˈpleɪ.sənt/", "pos": "adj.", "definition": "showing smug or uncritical satisfaction with oneself or one's achievements; self-satisfied", "chinese": "自满的，沾沾自喜的", "context": "a rebuke to the complacent narrative of progress", "examples": [{"text": "We must not become complacent about the threat of climate change.", "source": "The Guardian, 2023"}, {"text": "Success can make companies dangerously complacent.", "source": "Harvard Business Review, 2022"}], "collocations": ["become complacent", "dangerously complacent", "complacent attitude"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "rebuke", "phonetic": "/rɪˈbjuːk/", "pos": "n.", "definition": "an expression of sharp disapproval or criticism", "chinese": "指责，批评，谴责", "context": "serve as a rebuke to the complacent narrative", "examples": [{"text": "The court's ruling was a rebuke to the government's policy.", "source": "The New York Times, 2023"}, {"text": "His resignation served as a public rebuke to the leadership.", "source": "BBC News, 2022"}], "collocations": ["sharp rebuke", "public rebuke", "serve as a rebuke"], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_phrases": [
            {"phrase": "shed light on", "definition": "to make something clearer or easier to understand; to reveal", "chinese": "阐明，揭示，使更清楚", "context": "an attempt to shed light on the processes of economic and social change", "explanation": "字面意思是「照一束光」，比喻让黑暗中的事物变得可见。", "examples": [{"text": "The investigation shed light on the extent of corporate fraud.", "source": "The New York Times, 2022"}, {"text": "New research sheds light on the mechanisms of memory formation.", "source": "Nature, 2023"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "come to terms with", "definition": "to gradually accept a difficult or painful reality", "chinese": "逐渐接受（困难的现实）", "context": "have had to come to terms with a new identity", "explanation": "这些城市不得不接受一个痛苦的事实：它们曾经引以为傲的工业身份已经消失了。", "examples": [{"text": "The nation is still coming to terms with the aftermath of the crisis.", "source": "The Atlantic, 2022"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "the lived experience", "definition": "personal, first-hand experience as opposed to theory or statistics", "chinese": "亲身经历，切实的生活体验（与理论或数据相对）", "context": "runs counter to the lived experience of these communities", "explanation": "学术和新闻写作中的高频表达。强调真实的个人体验，而非纸上谈兵。", "examples": [{"text": "Policy must be informed by the lived experience of those it affects.", "source": "The Guardian, 2023"}, {"text": "The lived experience of poverty cannot be captured by statistics alone.", "source": "The Atlantic, 2022"}], "level": "IELTS 7.0+"},
        ],
        "annotations_sentences": [
            {"sentence": "These spaces speak not in the language of what they contain, but in the grammar of what has been removed.", "translation": "这些空间不是用它们所包含的东西来说话，而是用被移除的东西的「语法」来表达。", "breakdown": "主句：These spaces speak → not in... but in...（不是以……而是以……的方式）→ the language of what they contain（它们所包含的东西的语言）→ the grammar of what has been removed（被移除的东西的语法）。language 和 grammar 构成比喻的平行：空间像语言一样「说话」，但它说的不是「有什么」，而是「失去了什么」。", "grammar_points": ["not A but B 对比结构", "what they contain / what has been removed — what 引导名词性从句", "language 和 grammar 的比喻用法——把空间拟人化为会说话的叙述者"], "writing_tip": "「speak not in the language of A, but in the grammar of B」这种修辞可以用来描述任何通过「缺失」来传达信息的事物。"},
            {"sentence": "Rarely has a society been forced to confront so directly the gap between its self-image and its reality.", "translation": "一个社会很少被迫如此直接地面对自身形象与现实之间的差距。", "breakdown": "Rarely 引发倒装 → has a society been forced → to confront（面对）→ so directly（如此直接地）→ the gap between its self-image and its reality（自我形象与现实的差距）。", "grammar_points": ["Rarely + 倒装（has a society been forced 而非 a society has been forced）", "the gap between A and B 表示差距", "self-image vs reality 构成核心矛盾"], "writing_tip": "雅思写作中可以用这个结构讨论社会议题：Rarely has a generation been forced to confront so directly the consequences of environmental neglect."},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 6 — The Atlantic (Editorial)
    # ═══════════════════════════════════════════════════════════
    {
        "title": "Climate Finance: The Trillion-Dollar Question",
        "source": "The Atlantic",
        "source_icon": "🌊",
        "category": "editorial",
        "category_label": "社论评论",
        "summary": "Developing nations need trillions to adapt to climate change, but the money is not flowing. The gap between promise and reality threatens global cooperation.",
        "link": "https://www.theatlantic.com/science/",
        "published": "2025-03-28",
        "has_full_text": True,
        "full_text": """At the expense of their own development, the world's poorest nations are being asked to bear the brunt of a crisis they did little to create. The exorbitant cost of adapting to climate change — estimated at trillions of dollars — falls disproportionately on countries with the fewest resources to meet it. This is not merely an injustice; it is a conundrum that threatens the entire architecture of international climate cooperation.

The proliferation of climate pledges at successive COP summits has created an impressive edifice of ambition. Yet the gap between promise and delivery remains a far cry from what is needed. Rich nations pledged $100 billion annually in climate finance — a figure that, even if fully met, would fall short of the actual need by an order of magnitude. The reality is more equivocal still: much of what counts as "climate finance" consists of loans rather than grants, adding to the debt burden of nations already in fiscal distress.

Not only has this shortfall exacerbated tensions between the Global North and South, but it has also given rise to a deeper crisis of trust. Developing nations, having witnessed decades of unkept promises, have become increasingly intransigent in negotiations. On what grounds should they commit to ambitious emissions reductions when the financial support they were promised has not materialised?

The insidious logic of climate delay is that each year of inaction makes the eventual cost of adaptation higher. Coastal cities that could have been protected with modest investment a decade ago now require exorbitant infrastructure projects. Agricultural systems that could have been gradually adapted must now undergo unprecedented transformation. The volatile weather patterns that climate change has precipitated wait for no budget cycle.

While the political challenges are formidable, the financial mechanisms exist. Green bonds, carbon markets, debt-for-nature swaps — a burgeoning array of instruments could, in principle, channel capital where it is most needed. The paradigm shift required is not financial but political: a recognition that climate adaptation in vulnerable nations is not charity but enlightened self-interest.

Were the international community to fail in mobilising climate finance at the necessary scale, the consequences would be pernicious and far-reaching. Climate migration, resource conflicts, and the collapse of fragile states would impose costs on wealthy nations that dwarf the investment required to prevent them. The cogent case for climate finance is not altruistic — it is strategic.

In tandem with increased public finance, the private sector must be galvanized into action. The ubiquitous rhetoric of corporate sustainability must be matched by commensurate investment. This will require regulatory frameworks that set the stage for long-term thinking, rather than the short-termism that continues to hold sway in financial markets.

The rampant inequality that characterises the global response to climate change is not inevitable. It is the product of political choices — choices that can, and must, be remade. History will not judge kindly a generation that had the knowledge, the resources, and the technology to act, but that chose to eschew its responsibilities at the expense of those least able to protect themselves.""",
        "annotations_vocab": [
            {"word": "edifice", "phonetic": "/ˈed.ɪ.fɪs/", "pos": "n.", "definition": "a large, imposing building; or a complex system of beliefs or ideas", "chinese": "（宏伟的）建筑；（比喻）体系，大厦", "context": "an impressive edifice of ambition", "examples": [{"text": "The entire edifice of international law rests on this principle.", "source": "Foreign Affairs, 2023"}, {"text": "The Gothic edifice dominated the city skyline.", "source": "The Guardian, 2022"}], "collocations": ["impressive edifice", "crumbling edifice", "legal edifice"], "level": "TEM-8 / IELTS 7.5+"},
            {"word": "materialised", "phonetic": "/məˈtɪə.ri.ə.laɪzd/", "pos": "v.", "definition": "to become actual fact; to happen or appear", "chinese": "实现，成为现实；出现", "context": "the financial support they were promised has not materialised", "examples": [{"text": "The promised investment never materialised.", "source": "Financial Times, 2023"}, {"text": "Hopes for a quick recovery have not materialised.", "source": "The Economist, 2022"}], "collocations": ["failed to materialise", "never materialised", "hopes materialised"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "altruistic", "phonetic": "/ˌæl.truˈɪs.tɪk/", "pos": "adj.", "definition": "showing a selfless concern for the well-being of others; unselfish", "chinese": "利他的，无私的", "context": "The cogent case for climate finance is not altruistic — it is strategic", "examples": [{"text": "His motives were not entirely altruistic.", "source": "Cambridge Dictionary"}, {"text": "Altruistic behaviour can be found across many animal species.", "source": "Nature, 2022"}], "collocations": ["altruistic motives", "purely altruistic", "altruistic behaviour"], "level": "CET-6 / IELTS 7.0+"},
            {"word": "dwarf", "phonetic": "/dwɔːf/", "pos": "v.", "definition": "to make something seem small or insignificant by comparison", "chinese": "使相形见绌，使显得很小", "context": "would impose costs... that dwarf the investment required", "examples": [{"text": "The new skyscraper dwarfs all the surrounding buildings.", "source": "The New York Times, 2023"}, {"text": "The cost of inaction dwarfs the cost of prevention.", "source": "The Economist, 2023"}], "collocations": ["dwarf by comparison", "dwarf the cost", "dwarf everything else"], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_phrases": [
            {"phrase": "at the expense of", "definition": "so as to cause harm to or neglect of something else", "chinese": "以……为代价，牺牲……", "context": "At the expense of their own development", "explanation": "开篇第一句就点明核心矛盾：穷国为了应对气候变化，牺牲了自身的发展。", "examples": [{"text": "Economic growth should not come at the expense of environmental protection.", "source": "The Economist, 2023"}, {"text": "He pursued his career at the expense of his family relationships.", "source": "Cambridge Dictionary"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "an order of magnitude", "definition": "approximately ten times; a level of size or scale used for comparison", "chinese": "一个数量级（大约10倍的差距）", "context": "would fall short of the actual need by an order of magnitude", "explanation": "用来强调差距极大。$1000亿 vs 实际需要的万亿级别，差距不是一点点，而是10倍级别的。", "examples": [{"text": "The actual cost exceeded the estimate by an order of magnitude.", "source": "Nature, 2022"}, {"text": "Computing power has increased by several orders of magnitude.", "source": "MIT Technology Review, 2023"}], "level": "IELTS 7.0+"},
            {"phrase": "in tandem with", "definition": "together with; at the same time and in coordination with", "chinese": "与……同步，与……协同", "context": "In tandem with increased public finance", "explanation": "tandem 原意是两人共骑的自行车。in tandem with 就是两者像骑双人车一样同步前进。", "examples": [{"text": "Economic reform must proceed in tandem with political reform.", "source": "Foreign Affairs, 2022"}, {"text": "Technology evolves in tandem with consumer expectations.", "source": "Harvard Business Review, 2023"}], "level": "IELTS 7.0+ / TEM-8"},
            {"phrase": "debt-for-nature swaps", "definition": "agreements where a portion of a developing nation's debt is forgiven in exchange for environmental protection commitments", "chinese": "债务换自然（用减免发展中国家债务来换取其对环境保护的承诺）", "context": "Green bonds, carbon markets, debt-for-nature swaps", "explanation": "一种创新性的气候融资机制。例如：发达国家免除穷国的100亿美元债务，条件是穷国用这笔钱保护雨林。", "examples": [{"text": "Ecuador completed a landmark debt-for-nature swap to protect the Galápagos Islands.", "source": "The New York Times, 2023"}, {"text": "Debt-for-nature swaps are gaining momentum as a climate finance tool.", "source": "The Economist, 2023"}], "level": "IELTS 7.5+ (环境经济学术语)"},
        ],
        "annotations_sentences": [
            {"sentence": "At the expense of their own development, the world's poorest nations are being asked to bear the brunt of a crisis they did little to create.", "translation": "以牺牲自身发展为代价，世界上最贫穷的国家被要求承受一场他们几乎没有造成的危机的最大冲击。", "breakdown": "At the expense of...（介词短语前置，强调代价）→ the world's poorest nations → are being asked（被动语态，暗示不公平）→ to bear the brunt of a crisis → they did little to create（定语从句，说明这些国家对危机的责任很小）。", "grammar_points": ["介词短语前置作状语，增强句子力度", "are being asked — 被动进行时，暗示正在发生的不公正", "bear the brunt of = 首当其冲", "they did little to create — 「几乎没有」的委婉表达"], "writing_tip": "这种「At the expense of X, Y is being asked to Z」的句式非常适合讨论不公平现象。雅思范例：At the expense of their childhood, millions of children are being forced to work in hazardous conditions."},
            {"sentence": "History will not judge kindly a generation that had the knowledge, the resources, and the technology to act, but that chose to eschew its responsibilities at the expense of those least able to protect themselves.", "translation": "历史不会善待这样一代人：他们拥有行动所需的知识、资源和技术，却选择逃避责任，牺牲那些最无力保护自己的人。", "breakdown": "主句：History will not judge kindly a generation → that had... to act（第一个 that 定语从句：有能力行动）→ but that chose to eschew...（第二个 that 定语从句，转折：却选择逃避）→ at the expense of those → least able to protect themselves（最没有能力自我保护的人）。两个 that 从句形成强烈对比：有能力 vs 不行动。", "grammar_points": ["两个 that 定语从句并列（had... but chose...），形成讽刺性对比", "the knowledge, the resources, and the technology — 三词并列，排比增强气势", "eschew = 回避（非常正式的用词）", "those least able to... = those who are least able to...（省略了 who are）"], "writing_tip": "这个结尾句式在议论文中可用于道德呼吁。三元素排比（knowledge, resources, technology）+ 转折（but chose to...）的结构非常有力。"},
        ],
    },
]
