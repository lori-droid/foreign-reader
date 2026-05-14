"""
Classic Articles Module — Deep Reading Edition v2
Annotations focus on:
- vocabulary: linguistics-oriented analysis (etymology, morphology, register, writing/speaking tips)
- phrases: usage analysis, register notes, alternatives for speaking vs writing
- complex_sentences: full breakdowns with sentence-level highlighting keys
Each sentence in complex_sentences has a 'highlight_key' for matching in the article body.
"""

CLASSIC_ARTICLES = [
    # ═══════════════════════════════════════════════════════════
    # ARTICLE 1 — The Economist
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Quiet Revolution in How We Think About Trade",
        "source": "The Economist",
        "source_icon": "📊",
        "category": "politics_economics",
        "category_label": "政治经济",
        "summary": "For decades, free trade was an article of faith among economists. Now a rethinking is under way — not to abandon openness, but to acknowledge its costs and complications.",
        "link": "",
        "published": "2025-01-15",
        "has_full_text": True,
        "full_text": """For decades, free trade was an article of faith among economists. The logic seemed irrefutable: countries should specialise in what they do best, and exchange goods freely. Everyone would be better off. Yet the world has changed in ways that have exacerbated the shortcomings of this paradigm.

The proliferation of global supply chains, once hailed as a triumph of efficiency, has revealed an insidious vulnerability. When a pandemic shut down factories in one corner of the world, the ripple effects were felt everywhere. The unprecedented disruption precipitated a rethinking that had been quietly building for years.

Not only has this rethinking challenged the dominant economic orthodoxy, but it has also given rise to new schools of thought. Some argue that a degree of self-sufficiency, far from being inefficient, is a form of insurance. Others contend that the benefits of free trade remain cogent, but that the costs have been borne disproportionately by those least able to bear them.

In the wake of the pandemic, governments have scrambled to secure supply chains for critical goods — semiconductors, medicines, rare-earth minerals. The exorbitant cost of this reshoring has raised questions about whether the cure is commensurate with the disease. By and large, economists now acknowledge that the old dichotomy between free trade and protectionism is too simplistic.

While the debate rages on, one thing is clear: the era of unquestioned faith in globalisation is over. The challenge now is to forge a new consensus — one that does not eschew openness, but that acknowledges the volatile and unpredictable world in which trade must operate. Were the world's leading economies to fail in this endeavour, the consequences could be far-reaching and pernicious.

The conundrum facing policymakers is acute. They must ameliorate the genuine hardships caused by trade displacement, without triggering the rampant protectionism that could precipitate a global recession. It is precisely this balancing act that will define economic policy for a generation.""",

        "annotations_vocab": [
            {"word": "irrefutable", "phonetic": "/ˌɪr.ɪˈfjuː.tə.bəl/", "pos": "adj.", "definition": "impossible to deny or disprove", "chinese": "无可辩驳的",
             "linguistics": "由前缀 ir-（不）+ refute（反驳）+ -able（能……的）构成。ir- 是 in- 在 r 前的变体（同类：irregular, irresponsible）。掌握这个构词规律可以推断大量类似词汇。",
             "usage": "高度书面语。口语中通常说 You can't argue with that 或 undeniable。写作中用于强调论据的绝对说服力，如 irrefutable evidence。",
             "examples": [{"text": "The evidence against the defendant was irrefutable.", "source": "Oxford Advanced Learner's Dictionary"}],
             "level": "IELTS 7.5+ / TEM-8"},
            {"word": "specialise", "phonetic": "/ˈspeʃ.əl.aɪz/", "pos": "v.", "definition": "to focus on and become expert in a particular area", "chinese": "专攻，专门从事",
             "linguistics": "来自 special + -ise（英式拼写）/ -ize（美式）。注意英式 specialise vs 美式 specialize。经济学人作为英国刊物使用英式拼写，这在阅读外刊时需要注意。",
             "usage": "通用词，写作口语皆可。常用搭配 specialise in sth。学术写作中可替换为 focus exclusively on 或 concentrate on。",
             "examples": [{"text": "Many developing countries specialise in exporting raw materials.", "source": "The Economist, 2022"}],
             "level": "CET-4 / IELTS 5.5+"},
            {"word": "exacerbate", "phonetic": "/ɪɡˈzæs.ər.beɪt/", "pos": "v.", "definition": "to make a problem or bad situation worse", "chinese": "加剧，恶化",
             "linguistics": "拉丁语源 exacerbare，ex-（加强语气）+ acerbus（苦的、严厉的）。这个词只用于「坏事变更坏」，不能用于正面语境。近义词 aggravate 更口语化，worsen 最中性。",
             "usage": "典型的学术/新闻写作词汇。口语中更常说 make things worse。雅思写作高频词：Urbanisation has exacerbated environmental degradation.",
             "examples": [{"text": "The rising inflation has exacerbated the cost-of-living crisis.", "source": "The Economist, 2023"}],
             "level": "CET-6 / IELTS 7.0+"},
            {"word": "paradigm", "phonetic": "/ˈpær.ə.daɪm/", "pos": "n.", "definition": "a model, framework, or pattern of thinking", "chinese": "范式，思维框架",
             "linguistics": "希腊语源 paradeigma（模式）。注意发音中 g 不发音。学术界最常见的搭配是 paradigm shift（范式转换），由科学哲学家库恩（Thomas Kuhn）在 1962 年推广。",
             "usage": "高度学术化。口语中几乎不用，可以说 way of thinking / framework / model。写作中用于描述思维方式的根本性改变。",
             "examples": [{"text": "The discovery represented a paradigm shift in physics.", "source": "Nature, 2020"}],
             "level": "TEM-8 / IELTS 7.0+"},
            {"word": "proliferation", "phonetic": "/prəˌlɪf.əˈreɪ.ʃən/", "pos": "n.", "definition": "rapid increase in number or amount", "chinese": "激增，大量扩散",
             "linguistics": "词根 prolifer-（繁殖的）+ -ation（名词后缀）。与 prolific（多产的）同根。最常见于两个语境：nuclear proliferation（核扩散）和 the proliferation of X（某物的激增）。",
             "usage": "正式书面语。口语替代：rapid increase / explosion of / boom in。雅思写作中非常好用：the proliferation of social media / misinformation / technology.",
             "examples": [{"text": "Nuclear proliferation remains one of the gravest security concerns.", "source": "Oxford Advanced Learner's Dictionary"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "insidious", "phonetic": "/ɪnˈsɪd.i.əs/", "pos": "adj.", "definition": "gradually harmful in a way that is hard to notice", "chinese": "潜伏的，不知不觉中造成危害的",
             "linguistics": "拉丁语 insidiae（埋伏）。核心含义是「像伏击一样，表面看不出危险，实际上在暗中造成伤害」。与 pernicious 近义但有区别：insidious 强调隐蔽性，pernicious 强调有害性。",
             "usage": "书面正式用语。口语中可以说 sneaky / creeping / hidden。写作中常用于描述慢性问题：the insidious effects of pollution / inequality / misinformation.",
             "examples": [{"text": "Misinformation is insidious because it slowly erodes public trust.", "source": "The Atlantic, 2022"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "unprecedented", "phonetic": "/ʌnˈpres.ɪ.den.tɪd/", "pos": "adj.", "definition": "never having happened before", "chinese": "前所未有的",
             "linguistics": "un-（否定）+ precedent（先例）+ -ed。precedent 来自拉丁语 praecedere（走在前面）。如果你知道 precedent（先例），就能理解 unprecedented = 没有先例的。法律英语中 set a precedent（树立先例）也很常见。",
             "usage": "新闻和学术写作中的高频词，但近年因过度使用略显陈词滥调。口语中可以说 never seen before / first of its kind / unheard of。",
             "examples": [{"text": "The pandemic led to unprecedented levels of government intervention.", "source": "The Atlantic, 2021"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"word": "precipitate", "phonetic": "/prɪˈsɪp.ɪ.teɪt/", "pos": "v.", "definition": "to cause something (usually bad) to happen suddenly", "chinese": "促使，加速引发（坏事）",
             "linguistics": "拉丁语 praecipitare（头朝下扔下去）。注意这个词做动词时重音在第二音节 /prɪˈsɪp.ɪ.teɪt/，做形容词时重音不变但含义是「仓促的」。还有化学含义：沉淀。一词多义是英语的特点。",
             "usage": "高度书面语。口语中用 trigger / cause / spark off。写作常见搭配：precipitate a crisis / conflict / debate.",
             "examples": [{"text": "Fear of bank failures can precipitate a broader financial crisis.", "source": "Financial Times, 2023"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "orthodoxy", "phonetic": "/ˈɔː.θə.dɒk.si/", "pos": "n.", "definition": "generally accepted beliefs or conventional thinking", "chinese": "正统观念，主流学说",
             "linguistics": "希腊语 ortho-（正确的）+ doxa（观点）。同根词：orthodox（正统的）、paradox（悖论，para- = 反）。宗教语境中指东正教（Orthodox Church），学术语境中指主流观点。",
             "usage": "学术写作用词。口语中说 mainstream thinking / conventional wisdom / the established view。challenge the orthodoxy 是经济学人常用的表达方式。",
             "examples": [{"text": "Economic orthodoxy holds that markets are self-correcting.", "source": "The Economist, 2023"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "contend", "phonetic": "/kənˈtend/", "pos": "v.", "definition": "to argue or assert a position", "chinese": "主张，争辩，认为",
             "linguistics": "拉丁语 contendere（竞争、奋斗）。有两个主要义项：1) 主张（= argue/claim）如本文；2) 竞争（contend for / with）。contender（竞争者）是其派生词。",
             "usage": "写作正式用语，可替换 argue / claim / maintain。口语中更常用 argue 或 say。雅思写作中 Some contend that... 比 Some people think that... 更高级。",
             "examples": [{"text": "Critics contend that the policy will disproportionately affect the poor.", "source": "The Guardian, 2023"}],
             "level": "CET-6 / IELTS 7.0+"},
            {"word": "cogent", "phonetic": "/ˈkəʊ.dʒənt/", "pos": "adj.", "definition": "clear, logical, and convincing", "chinese": "有说服力的，令人信服的",
             "linguistics": "拉丁语 cogere（驱使、迫使）。字面意义是「有力到让你不得不同意」。比 convincing 更正式，比 compelling 语气稍轻。",
             "usage": "纯书面用语。口语中说 convincing / strong / makes a good point。写作搭配：cogent argument / reasoning / analysis / case.",
             "examples": [{"text": "She made a cogent argument for increasing public investment.", "source": "Oxford Advanced Learner's Dictionary"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "disproportionately", "phonetic": "/ˌdɪs.prəˈpɔː.ʃən.ət.li/", "pos": "adv.", "definition": "to a degree that is unfairly large or small compared to something else", "chinese": "不成比例地（暗示不公平）",
             "linguistics": "dis-（否定）+ proportion（比例）+ -ate + -ly。四个语素层层叠加的典型学术词。理解 proportion（比例）是关键，disproportionate 就是「不成比例的」，通常暗含不公平的批判。",
             "usage": "学术和新闻写作高频词。口语中可以说 unfairly / too much / more than their fair share。雅思写作常用：X disproportionately affects Y.",
             "examples": [{"text": "Climate change disproportionately affects developing countries.", "source": "IPCC Report, 2022"}],
             "level": "CET-6 / IELTS 7.0+"},
            {"word": "semiconductors", "phonetic": "/ˌsem.i.kənˈdʌk.tərz/", "pos": "n.", "definition": "materials (silicon chips) essential to modern electronics", "chinese": "半导体（芯片）",
             "linguistics": "semi-（半）+ conductor（导体）。造词法体现了物理特性：这种材料的导电性介于导体和绝缘体之间。了解 semi- 前缀可推断：semicircle（半圆）、semifinal（半决赛）。",
             "usage": "专业术语，在科技和经济报道中极高频。口语中常直接说 chips。这个词近年因中美芯片竞争成为新闻热词。",
             "examples": [{"text": "Taiwan produces over 60% of the world's advanced semiconductors.", "source": "The Economist, 2023"}],
             "level": "IELTS 6.5+ (专业术语)"},
            {"word": "reshoring", "phonetic": "/riːˈʃɔː.rɪŋ/", "pos": "n.", "definition": "bringing manufacturing back to the home country from overseas", "chinese": "产业回流（将海外制造业搬回国内）",
             "linguistics": "re-（回）+ shore（岸、国）+ -ing。与之相反的是 offshoring（将产业转移到海外）。这是近年新造的经济学术语，体现了英语通过前缀快速造新词的能力。同类：onshoring, nearshoring。",
             "usage": "经济新闻专业术语。口语中说 bringing jobs back home / moving factories back。",
             "examples": [{"text": "The reshoring trend accelerated after the pandemic exposed supply chain risks.", "source": "Harvard Business Review, 2022"}],
             "level": "IELTS 7.0+ (经济术语)"},
            {"word": "exorbitant", "phonetic": "/ɪɡˈzɔː.bɪ.tənt/", "pos": "adj.", "definition": "unreasonably high (usually of prices)", "chinese": "过高的，离谱的",
             "linguistics": "拉丁语 exorbitare（偏离轨道），ex-（出）+ orbita（轨道）。字面义是「脱离正常轨道」，引申为「价格离谱地偏离合理范围」。只用于描述负面的高价格。",
             "usage": "书面正式用语。口语中说 ridiculously expensive / way too much / outrageous。写作搭配：exorbitant cost / price / fees。",
             "examples": [{"text": "The exorbitant cost of healthcare forces many to forgo treatment.", "source": "The New York Times, 2023"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "commensurate", "phonetic": "/kəˈmen.sjʊ.rət/", "pos": "adj.", "definition": "corresponding in size or degree; proportional", "chinese": "相称的，成比例的",
             "linguistics": "com-（共同）+ mensurare（测量）。字面义「可以用同一把尺子测量的」，即大小匹配。几乎总是与 with 搭配使用。",
             "usage": "高度书面语。口语中说 matches / is in line with / proportional to。最常见于求职语境：Salary commensurate with experience（薪资与经验相称）。",
             "examples": [{"text": "The punishment should be commensurate with the severity of the crime.", "source": "Merriam-Webster Dictionary"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "dichotomy", "phonetic": "/daɪˈkɒt.ə.mi/", "pos": "n.", "definition": "a division into two completely opposite groups", "chinese": "二分法，截然对立",
             "linguistics": "希腊语 dicha（分为二）+ tomos（切）。与 anatomy（解剖，ana- + tomos）同源。常搭配 false dichotomy（虚假的二元对立），这在议论文写作中是一种重要的逻辑谬误。",
             "usage": "学术正式用语。口语中说 the divide between / the split between。雅思写作中用 false dichotomy 指出一种逻辑谬误非常加分。",
             "examples": [{"text": "The false dichotomy of nature versus nurture oversimplifies human development.", "source": "Scientific American, 2021"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "consensus", "phonetic": "/kənˈsen.səs/", "pos": "n.", "definition": "general agreement among a group", "chinese": "共识，一致意见",
             "linguistics": "拉丁语 consentire（同意），con-（共同）+ sentire（感觉）。字面义「大家有相同的感受」。注意拼写：不是 concensus。常见错误拼写之一。",
             "usage": "通用词，写作口语皆可。常用搭配：reach a consensus / build a consensus / scientific consensus / broad consensus。",
             "examples": [{"text": "There is a growing consensus among scientists that urgent action is needed.", "source": "Nature, 2023"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"word": "eschew", "phonetic": "/ɪsˈtʃuː/", "pos": "v.", "definition": "to deliberately avoid or keep away from", "chinese": "避开，回避，有意远离",
             "linguistics": "古法语 eschiver（躲避），与 shy 同源。这是英语中少数几个「避开」含义比 avoid 更强烈的词，暗含主动、有意识地拒绝。",
             "usage": "高度书面正式。口语中说 avoid / stay away from / steer clear of。新闻写作中常用于描述刻意回避：eschew responsibility / violence / convention.",
             "examples": [{"text": "The author eschews jargon in favour of plain language.", "source": "Merriam-Webster Dictionary"}],
             "level": "TEM-8 / IELTS 8.0+"},
            {"word": "volatile", "phonetic": "/ˈvɒl.ə.taɪl/", "pos": "adj.", "definition": "liable to change rapidly and unpredictably", "chinese": "不稳定的，动荡的",
             "linguistics": "拉丁语 volare（飞）。原义「像飞一样快速变化」。化学中 volatile 指「易挥发的」（液体快速变成气体）。在金融和政治语境中指局势动荡不稳。三个常见领域：volatile market / volatile situation / volatile substance。",
             "usage": "通用词，但在正式语境中更常见。口语替代：unstable / unpredictable / up and down。",
             "examples": [{"text": "The stock market has been particularly volatile in recent months.", "source": "Financial Times, 2023"}],
             "level": "CET-6 / IELTS 7.0+"},
            {"word": "pernicious", "phonetic": "/pəˈnɪʃ.əs/", "pos": "adj.", "definition": "having a harmful effect, especially gradually", "chinese": "有害的，恶性的",
             "linguistics": "拉丁语 pernicies（毁灭），per-（彻底）+ nex（杀死）。字面义「彻底毁灭性的」。与 insidious 的区别：insidious 强调「隐蔽性」，pernicious 强调「破坏性」。两者常搭配使用。",
             "usage": "高度书面正式。口语中说 really harmful / damaging / destructive。写作搭配：pernicious effect / influence / myth / ideology.",
             "examples": [{"text": "Conspiracy theories have a pernicious effect on public discourse.", "source": "The Atlantic, 2021"}],
             "level": "TEM-8 / IELTS 8.0+"},
            {"word": "conundrum", "phonetic": "/kəˈnʌn.drəm/", "pos": "n.", "definition": "a difficult problem with no easy answer", "chinese": "难题，困境",
             "linguistics": "词源不确定，可能是 16 世纪牛津大学学生的戏造词。比 problem 更强调「无解感」，比 dilemma（二选一困境）更广泛。",
             "usage": "半正式，写作口语皆可。口语替代：tricky problem / tough question / puzzle。常用搭配：face a conundrum / moral conundrum / solve the conundrum.",
             "examples": [{"text": "Central bankers face the conundrum of controlling inflation without triggering recession.", "source": "Financial Times, 2023"}],
             "level": "TEM-8 / IELTS 7.5+"},
            {"word": "policymakers", "phonetic": "/ˈpɒl.ɪ.siˌmeɪ.kərz/", "pos": "n.", "definition": "people who make official decisions and rules, especially in government", "chinese": "政策制定者",
             "linguistics": "policy + maker + -s。这是英语的复合造词法（compounding）：两个独立的词组合成新词。同类构词：lawmaker, peacemaker, troublemaker, filmmaker, gamemaker。掌握 -maker 后缀可以理解和创造大量复合词。注意写法：可写成 policymakers（一个词）或 policy-makers（连字符）或 policy makers（两个词），三种都正确。",
             "usage": "新闻和学术写作高频词。口语中通常说 politicians / government officials / people in charge / decision-makers。",
             "examples": [{"text": "Policymakers must balance economic growth with environmental protection.", "source": "The Economist, 2023"}],
             "level": "CET-6 / IELTS 6.0+"},
            {"word": "ameliorate", "phonetic": "/əˈmiː.li.ə.reɪt/", "pos": "v.", "definition": "to make a bad situation better", "chinese": "改善，改良",
             "linguistics": "拉丁语 melior（更好的），a-（朝向）+ melior + -ate。与 meliorate 同源。注意与 improve 的区别：ameliorate 专门用于「改善坏的状况」，improve 可以用于任何提升。",
             "usage": "高度书面正式。口语中说 improve / make better / help with。写作搭配：ameliorate conditions / suffering / the situation / hardships.",
             "examples": [{"text": "The new policy aims to ameliorate the housing shortage.", "source": "The Guardian, 2023"}],
             "level": "TEM-8 / IELTS 8.0+"},
            {"word": "rampant", "phonetic": "/ˈræm.pənt/", "pos": "adj.", "definition": "spreading unchecked; flourishing in a negative way", "chinese": "猖獗的，蔓延的",
             "linguistics": "古法语 ramper（爬行）。在纹章学中 rampant 描述后腿站立、前爪张开的动物形象（如狮子）。引申为「不受控制地蔓延」，几乎只用于负面语境。",
             "usage": "半正式，写作口语皆可。口语替代：out of control / widespread / running wild。搭配：rampant corruption / inflation / crime / speculation.",
             "examples": [{"text": "Rampant inflation has eroded the purchasing power of ordinary citizens.", "source": "The Economist, 2022"}],
             "level": "CET-6 / IELTS 7.0+"},
            {"word": "protectionism", "phonetic": "/prəˈtek.ʃən.ɪ.zəm/", "pos": "n.", "definition": "the policy of shielding domestic industries from foreign competition through tariffs or quotas", "chinese": "贸易保护主义",
             "linguistics": "protect（保护）+ -ion + -ism（主义）。经济学核心术语，与 free trade（自由贸易）相对。-ism 后缀表示「主义/信仰体系」：capitalism, socialism, nationalism 等。",
             "usage": "经济学术语，在相关话题的写作中必须掌握。口语中可以说 trade barriers / protecting local businesses。",
             "examples": [{"text": "Rising protectionism threatens the global trading system.", "source": "Financial Times, 2023"}],
             "level": "CET-6 / IELTS 7.0+"},
        ],

        "annotations_phrases": [
            {"phrase": "an article of faith", "definition": "a firmly held belief accepted without question", "chinese": "信条，不容质疑的坚定信念",
             "linguistics": "article 在这里不是「文章」而是「条款」（如 articles of the Constitution）。整个表达借用宗教语言，暗示某个信念已经像宗教教条一样不容置疑。经济学人经常用宗教比喻来讽刺经济学界的盲目信仰。",
             "usage": "高度书面正式，用于批评某种不加反思的信念。口语替代：something people believe without questioning / a sacred cow. 雅思写作中可用于引入需要被质疑的传统观念。",
             "examples": [{"text": "The idea that markets are always efficient was once an article of faith.", "source": "Financial Times, 2023"}],
             "level": "IELTS 7.0+"},
            {"phrase": "ripple effects", "definition": "spreading consequences of an event, like ripples in water", "chinese": "连锁反应，涟漪效应",
             "linguistics": "具象比喻：石头扔进水里产生的涟漪一圈圈向外扩散。英语中大量表达来自物理世界的比喻：domino effect（多米诺效应）、snowball effect（滚雪球效应）、butterfly effect（蝴蝶效应）。掌握这些比喻可以让写作更生动。",
             "usage": "半正式，写作口语皆可。口语替代：knock-on effects / chain reaction。写作中比 consequences 更生动具体。",
             "examples": [{"text": "The collapse of one major bank sent ripple effects through the entire financial system.", "source": "Financial Times, 2023"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "give rise to", "definition": "to cause something to happen or exist", "chinese": "引起，导致，催生",
             "linguistics": "比 cause 更正式的替换表达。注意搭配：give rise to + 名词（不能接 doing）。同级替换词：lead to / result in / bring about / spark / trigger。按正式程度排列：give rise to > bring about > lead to > cause.",
             "usage": "标准学术写作用语。雅思写作中用它替换 cause 可以提升词汇多样性：Globalisation has given rise to new forms of inequality.",
             "examples": [{"text": "Rapid urbanisation has given rise to a host of social problems.", "source": "UN Habitat Report, 2022"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "in the wake of", "definition": "following and usually as a result of", "chinese": "在……之后（紧随其后，含因果关系）",
             "linguistics": "wake 是船经过后的水痕/尾流。in the wake of 字面义「在尾流中」，引申为「在某事件之后发生的（通常是该事件导致的）」。类似的航海比喻：plain sailing（一帆风顺）、weather the storm（度过难关）。",
             "usage": "半正式，新闻写作极高频。口语替代：after / following / as a result of。注意 in the wake of 暗示因果关系，after 则只表示时间先后。",
             "examples": [{"text": "In the wake of the financial crisis, regulators tightened banking rules.", "source": "Financial Times, 2020"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "scrambled to", "definition": "to rush urgently and somewhat chaotically to do something", "chinese": "争先恐后地，仓促地（暗示手忙脚乱）",
             "linguistics": "scramble 原义：攀爬、抢夺（如 scramble for seats）。用于描述紧急但缺乏秩序的行动。与 rush to 的区别：scramble 更强调「混乱和仓促」。军事语境中 scramble 指「紧急起飞」。",
             "usage": "半正式，写作口语皆可。口语替代：rushed to / hurried to / raced to。用 scramble 暗示准备不足，更有批评意味。",
             "examples": [{"text": "Airlines scrambled to rebook passengers after mass cancellations.", "source": "BBC News, 2023"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "by and large", "definition": "on the whole; generally speaking", "chinese": "总的来说，大体上",
             "linguistics": "航海术语：by the wind（逆风航行）+ sailing large（顺风航行）= 不管什么风向，总体来说。是英语中保留至今的古老航海表达之一。",
             "usage": "半正式，写作口语皆可。口语替代：generally / on the whole / overall / for the most part。可放在句首或句中。",
             "examples": [{"text": "By and large, the reforms have been successful.", "source": "Oxford Advanced Learner's Dictionary"}],
             "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "rages on", "definition": "continues with great intensity", "chinese": "继续激烈进行（形容争论、战争、暴风雨等）",
             "linguistics": "rage（狂怒）+ on（持续）。把辩论比喻成暴风雨或战火，传达出分歧巨大、双方互不相让的感觉。经济学人喜欢用这类戏剧化的动词让叙述更有张力。",
             "usage": "半正式，偏新闻和叙事文体。口语替代：keeps going / continues / won't stop。搭配：the debate rages on / the war rages on / the storm rages on.",
             "examples": [{"text": "The debate over immigration policy rages on in Congress.", "source": "The New York Times, 2023"}],
             "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "forge a consensus", "definition": "to create agreement through sustained effort", "chinese": "达成共识（通过努力建立一致意见）",
             "linguistics": "forge 原义：锻造（铁匠打铁）。引申义「通过反复打磨创造出某样东西」。与 reach a consensus（达成共识）相比，forge 更强调过程的艰难和努力。同类表达：forge a path / forge an alliance / forge ahead.",
             "usage": "书面正式。口语中说 reach an agreement / find common ground / get everyone on the same page。",
             "examples": [{"text": "It took months to forge a consensus among the member states.", "source": "The Economist, 2023"}],
             "level": "IELTS 7.0+"},
            {"phrase": "trade displacement", "definition": "job losses caused by international trade shifting production elsewhere", "chinese": "贸易替代（因国际贸易导致本国岗位流失）",
             "linguistics": "displacement（位移、取代）由 displace 派生。dis-（分开）+ place（位置）= 被从原位移走。在贸易语境中指本国工人的工作被更便宜的海外劳动力取代。与 job displacement / labor displacement 同义。",
             "usage": "经济学专业术语。口语中说 losing jobs to foreign competition / jobs moving overseas。",
             "examples": [{"text": "Workers affected by trade displacement often lack skills to transition to new industries.", "source": "World Bank, 2022"}],
             "level": "IELTS 7.0+ (经济术语)"},
            {"phrase": "far-reaching", "definition": "having a wide range of effects or influence", "chinese": "深远的，影响广泛的",
             "linguistics": "复合形容词：far（远）+ reaching（延伸的）。英语中大量复合形容词用连字符连接：long-lasting, hard-working, well-known, ground-breaking。注意只有放在名词前面做定语时才加连字符：far-reaching consequences，但 The consequences are far reaching（做表语时不加）。",
             "usage": "通用词，写作口语皆可。同义替换：wide-ranging / profound / sweeping / extensive。雅思写作高频搭配：far-reaching consequences / implications / effects.",
             "examples": [{"text": "The decision will have far-reaching implications for the industry.", "source": "The Economist, 2023"}],
             "level": "CET-6 / IELTS 6.5+"},
        ],

        "annotations_sentences": [
            {"sentence": "Yet the world has changed in ways that have exacerbated the shortcomings of this paradigm.",
             "highlight_key": "Yet the world has changed in ways that have exacerbated the shortcomings of this paradigm",
             "translation": "然而，世界已经发生了变化，而这些变化加剧了这一范式的不足之处。",
             "breakdown": "拆解为三层：① the world has changed（世界变了）→ ② in ways that...（以某些方式，that 引导定语从句修饰 ways）→ ③ have exacerbated the shortcomings of this paradigm（加剧了这个范式的缺陷）。核心逻辑：不是世界本身有问题，而是世界的变化暴露了理论的缺陷。",
             "grammar_points": ["in ways that... 表示「以……的方式」，that 引导定语从句", "现在完成时 has changed / have exacerbated 强调持续影响"],
             "writing_tip": "「X has changed in ways that have + 过去分词 + Y」可以直接用于雅思写作。例：Technology has evolved in ways that have fundamentally altered the nature of work."},
            {"sentence": "When a pandemic shut down factories in one corner of the world, the ripple effects were felt everywhere.",
             "highlight_key": "When a pandemic shut down factories in one corner of the world, the ripple effects were felt everywhere",
             "translation": "当一场疫情关停了世界某个角落的工厂时，连锁反应传遍了全球。",
             "breakdown": "When 从句设置场景：a pandemic shut down factories（疫情关闭工厂）→ in one corner of the world（在一个角落）→ 主句揭示后果：the ripple effects were felt everywhere（涟漪效应在各处被感受到）。one corner vs everywhere 形成鲜明对比，一行字写出了全球化的本质。",
             "grammar_points": ["被动语态 were felt 让影响成为主语", "one corner vs everywhere 对比修辞"],
             "writing_tip": "对比式因果句模板：When X happens in [a small place], the effects are felt [broadly]. 雅思示例：When one country imposes trade barriers, the economic consequences are felt across the entire region."},
            {"sentence": "Some argue that a degree of self-sufficiency, far from being inefficient, is a form of insurance.",
             "highlight_key": "Some argue that a degree of self-sufficiency, far from being inefficient, is a form of insurance",
             "translation": "一些人认为，一定程度的自给自足非但不是低效的，反而是一种保险。",
             "breakdown": "主句：Some argue that... → that 引导宾语从句 → 宾语从句内部：a degree of self-sufficiency（主语）→ far from being inefficient（插入语，far from = 远非、非但不是）→ is a form of insurance（系表结构：是一种保险）。关键是 far from being X 这个插入语——它推翻了传统观点（自给自足=低效），提出反面论点（自给自足=保险）。",
             "grammar_points": ["far from being X = 远非 X，实际上恰恰相反", "a degree of = 一定程度的（表示适量，不是全部）", "插入语用逗号隔开，去掉后句子仍然完整"],
             "writing_tip": "far from being X, Y is actually Z 是一个高分反驳句式。雅思示例：Social media, far from being a threat to real relationships, is actually a powerful tool for maintaining long-distance connections."},
            {"sentence": "Not only has this rethinking challenged the dominant economic orthodoxy, but it has also given rise to new schools of thought.",
             "highlight_key": "Not only has this rethinking challenged the dominant economic orthodoxy, but it has also given rise to new schools of thought",
             "translation": "这种反思不仅挑战了占主导地位的经济学正统观念，还催生了新的思想学派。",
             "breakdown": "Not only 放在句首引起倒装 → has this rethinking challenged（助动词提前）→ the dominant economic orthodoxy → but it has also → given rise to new schools of thought。这个结构的精妙在于：前半句「破」（挑战旧观念），后半句「立」（催生新思想）。",
             "grammar_points": ["Not only + 倒装是高分语法", "but also 后的从句不需要倒装", "give rise to = cause / lead to 的高级替换"],
             "writing_tip": "Not only...but also 倒装是雅思 8 分作文必备句式。示例：Not only does remote work reduce commuting time, but it also enhances employee satisfaction."},
            {"sentence": "The exorbitant cost of this reshoring has raised questions about whether the cure is commensurate with the disease.",
             "highlight_key": "The exorbitant cost of this reshoring has raised questions about whether the cure is commensurate with the disease",
             "translation": "回流的高昂成本引发了疑问：这个「药方」是否与「疾病」相称？",
             "breakdown": "主句：The exorbitant cost... has raised questions → about whether...（关于是否）→ the cure is commensurate with the disease。这里用了暗喻：cure（药方）= 回流政策，disease（疾病）= 供应链风险。作者没有直接说回流政策好不好，而是用比喻提出质疑——让读者自己判断。",
             "grammar_points": ["whether 引导宾语从句", "commensurate with = 与……成比例/相称", "cure / disease 是隐喻，不是在讨论医疗"],
             "writing_tip": "用比喻提问比直接论述更有力。这个模式可以迁移：We must ask whether the cure is commensurate with the disease — 任何讨论政策代价的场合都适用。"},
            {"sentence": "Were the world's leading economies to fail in this endeavour, the consequences could be far-reaching and pernicious.",
             "highlight_key": "Were the world's leading economies to fail in this endeavour, the consequences could be far-reaching and pernicious",
             "translation": "如果世界主要经济体在这项努力中失败，后果将是深远而有害的。",
             "breakdown": "Were... to fail 是虚拟语气倒装形式 = If... were to fail。这不是语法错误，是高级英语的标准用法。Were 放在句首，省略 if，让句子更紧凑庄重。主句 the consequences could be... 用 could 而不是 would，表示一种严肃的可能性。",
             "grammar_points": ["Were + 主语 + to do = If + 主语 + were to do（虚拟语气倒装）", "这是经济学人最常用的句式之一", "far-reaching and pernicious — 两个形容词并列强化语气"],
             "writing_tip": "Were + 主语 + to... 是雅思 8 分句式。示例：Were governments to invest more in renewable energy, the long-term benefits would far outweigh the initial costs."},
            {"sentence": "They must ameliorate the genuine hardships caused by trade displacement, without triggering the rampant protectionism that could precipitate a global recession.",
             "highlight_key": "They must ameliorate the genuine hardships caused by trade displacement, without triggering the rampant protectionism that could precipitate a global recession",
             "translation": "他们必须改善贸易转移造成的真实困难，同时不能引发可能导致全球衰退的猖獗保护主义。",
             "breakdown": "三层递进：① must ameliorate hardships（必须改善困难）→ caused by trade displacement（后置定语）→ ② without triggering protectionism（但不能引发保护主义）→ ③ that could precipitate a global recession（that 定语从句嵌套：这种保护主义可能导致全球衰退）。整句话写出了一个政策困境：帮一方，可能伤另一方。",
             "grammar_points": ["must + 动词... without + 动名词 = 必须做 A 但不能做 B", "caused by 过去分词做后置定语", "that 定语从句嵌套在 without 结构中"],
             "writing_tip": "「must do A without triggering B」完美描述政策两难。雅思示例：Governments must promote economic growth without exacerbating environmental degradation."},
            {"sentence": "It is precisely this balancing act that will define economic policy for a generation.",
             "highlight_key": "It is precisely this balancing act that will define economic policy for a generation",
             "translation": "正是这种平衡行为将定义一代人的经济政策。",
             "breakdown": "这是强调句型 It is... that...。正常语序是：This balancing act will define economic policy for a generation. 用 It is... that... 把 this balancing act 提取出来强调。precisely（恰恰是）进一步加强语气。",
             "grammar_points": ["It is... that... 强调句型", "precisely 作为强化语气的副词", "for a generation = 持续一代人的时间"],
             "writing_tip": "It is precisely X that... 是非常有力的总结句。雅思示例：It is precisely the lack of political will that prevents meaningful action on climate change."},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 2 — The Atlantic
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Paradox of Connection in a Digital Age",
        "source": "The Atlantic",
        "source_icon": "🌊",
        "category": "editorial",
        "category_label": "社论评论",
        "summary": "We have never been more connected, yet loneliness has become a public-health crisis. How did the tools meant to bring us together end up driving us apart?",
        "link": "",
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
            {"word": "ubiquitous", "phonetic": "/juːˈbɪk.wɪ.təs/", "pos": "adj.", "definition": "present everywhere at the same time", "chinese": "无处不在的",
             "linguistics": "拉丁语 ubique（到处）。与 omnipresent（全知全在的）近义，但 ubiquitous 更世俗化，omnipresent 更有宗教/哲学色彩。派生词：ubiquity（n. 无处不在）。",
             "usage": "书面正式。口语中说 everywhere / all over the place / you see it everywhere。雅思写作高频：The ubiquitous use of smartphones has transformed modern communication.",
             "examples": [{"text": "Coffee shops have become ubiquitous in urban areas.", "source": "Cambridge Dictionary"}], "level": "TEM-8 / IELTS 7.5+"},
            {"word": "paradoxically", "phonetic": "/ˌpær.əˈdɒk.sɪ.kəl.i/", "pos": "adv.", "definition": "in a way that seems contradictory but may be true", "chinese": "矛盾的是，看似矛盾地",
             "linguistics": "para-（反）+ doxa（观点）+ -ical + -ly。paradox（悖论）是修辞学和逻辑学中的重要概念。这篇文章的标题本身就是一个 paradox：连接越多，反而越孤独。",
             "usage": "半正式，写作口语皆可。用在句首非常有效：Paradoxically, greater connectivity has led to greater isolation. 口语中可以说 Strangely enough / Ironically.",
             "examples": [{"text": "Paradoxically, the more choices we have, the less satisfied we feel.", "source": "The Atlantic, 2022"}], "level": "CET-6 / IELTS 7.0+"},
            {"word": "burgeoned", "phonetic": "/ˈbɜː.dʒənd/", "pos": "v.", "definition": "to grow or increase rapidly", "chinese": "迅速发展，蓬勃增长",
             "linguistics": "中古英语 burgeon（发芽）。原义是植物发出新芽，引申为快速生长。比 grow 更文学化，暗示从无到有的蓬勃态势。常用其现在分词 burgeoning 做形容词。",
             "usage": "书面文学用语。口语中说 growing fast / booming / taking off。写作搭配：burgeoning industry / demand / movement.",
             "examples": [{"text": "A burgeoning middle class is driving consumer demand in Asia.", "source": "World Bank, 2022"}], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "inexorable", "phonetic": "/ɪnˈek.sər.ə.bəl/", "pos": "adj.", "definition": "impossible to stop or prevent; relentless", "chinese": "不可阻挡的，无情推进的",
             "linguistics": "in-（不）+ exorable（可被恳求的）。字面义「不能被恳求/祈祷阻止的」。比 unstoppable 更文学化，常暗示一种宿命感。",
             "usage": "高度书面文学用语。口语中说 unstoppable / relentless / inevitable。写作搭配：inexorable rise / march / decline / progress.",
             "examples": [{"text": "Technology's inexorable march has reshaped every industry.", "source": "MIT Technology Review, 2022"}], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "curated", "phonetic": "/kjʊəˈreɪ.tɪd/", "pos": "adj.", "definition": "carefully selected and presented to create a particular impression", "chinese": "精心策划的，筛选过的",
             "linguistics": "curator（博物馆策展人）的形容词化。原指策展人挑选艺术品，近年因社交媒体广泛使用——每个人都在「策展」自己的线上形象。一个从高雅艺术领域进入日常语言的词。",
             "usage": "半正式，已进入日常用语。常见搭配：curated content / curated feed / carefully curated image。在讨论社交媒体时几乎必用。",
             "examples": [{"text": "Social media encourages us to present a curated version of our lives.", "source": "The Atlantic, 2022"}], "level": "IELTS 7.0+"},
            {"word": "equivocal", "phonetic": "/ɪˈkwɪv.ə.kəl/", "pos": "adj.", "definition": "ambiguous; open to multiple interpretations", "chinese": "模棱两可的，含糊的",
             "linguistics": "equi-（相等）+ vocal（声音）。字面义「两种声音一样大」，即无法分辨哪个是真的。反义词 unequivocal（明确无误的）更常见。相关词：equivocate（v. 说模棱两可的话）。",
             "usage": "书面正式。口语中说 unclear / mixed / could go either way。常用搭配：equivocal results / evidence / response。",
             "examples": [{"text": "The scientific evidence on this point remains equivocal.", "source": "Nature, 2022"}], "level": "TEM-8 / IELTS 7.5+"},
            {"word": "galvanized", "phonetic": "/ˈɡæl.və.naɪzd/", "pos": "v.", "definition": "to shock or excite someone into action", "chinese": "激励，刺激（使采取行动）",
             "linguistics": "以意大利科学家 Luigi Galvani 命名，他发现电流能让死青蛙的腿抽动。引申为「像电击一样激发行动」。还有字面义：galvanized steel（镀锌钢）。科学家名字变成日常用词的案例还有 pasteurize, boycott 等。",
             "usage": "半正式，写作口语皆可。口语替代：fired up / motivated / sparked action。搭配：galvanize support / the public / a movement.",
             "examples": [{"text": "The tragedy galvanized public opinion in favour of stricter regulations.", "source": "The New York Times, 2022"}], "level": "CET-6 / IELTS 7.0+"},
            {"word": "diaspora", "phonetic": "/daɪˈæs.pər.ə/", "pos": "n.", "definition": "people dispersed from their homeland living in other countries", "chinese": "散居海外的族群，侨民群体",
             "linguistics": "希腊语 dia-（穿过）+ speirein（播撒）。字面义「种子被撒到各处」。最初特指犹太人的流散（Jewish Diaspora），现在泛指任何海外族群。大写 Diaspora 通常指犹太人，小写 diaspora 泛指。",
             "usage": "学术和新闻用语。口语中说 expat community / overseas community / people living abroad。",
             "examples": [{"text": "Social media helps diaspora communities maintain cultural ties.", "source": "BBC News, 2022"}], "level": "IELTS 7.5+"},
            {"word": "obfuscate", "phonetic": "/ˈɒb.fʌ.skeɪt/", "pos": "v.", "definition": "to make something deliberately unclear or confusing", "chinese": "使混淆，故意模糊化",
             "linguistics": "ob-（朝向）+ fuscus（暗的）+ -ate。字面义「使变暗」，引申为「让事情变得不清楚」。注意这个词暗含「故意的」——不是不小心说不清楚，而是有意混淆。",
             "usage": "高度书面正式。口语中说 confuse the issue / muddy the waters / cover up。搭配：obfuscate the truth / the issue / meaning.",
             "examples": [{"text": "Complex legal language can obfuscate rather than clarify meaning.", "source": "Cambridge Dictionary"}], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "recalibrate", "phonetic": "/riːˈkæl.ɪ.breɪt/", "pos": "v.", "definition": "to adjust or reset one's approach after new experience", "chinese": "重新调整，重新校准",
             "linguistics": "re-（再次）+ calibrate（校准）。calibrate 来自 calibre（口径/标准）。原是科学仪器术语（重新校准仪器的精度），现广泛比喻化使用。体现了英语将技术术语比喻化的趋势。",
             "usage": "半正式。口语中说 adjust / rethink / reset。写作搭配：recalibrate expectations / strategy / one's approach / the relationship.",
             "examples": [{"text": "Companies are recalibrating their strategies in response to AI.", "source": "Harvard Business Review, 2023"}], "level": "IELTS 7.5+"},
            {"word": "formidable", "phonetic": "/fɔːˈmɪd.ə.bəl/", "pos": "adj.", "definition": "inspiring fear or respect through being impressively powerful or difficult", "chinese": "令人敬畏的，巨大的（挑战）",
             "linguistics": "拉丁语 formidare（恐惧）。注意英式发音重音在第二音节 /fɔːˈmɪd.ə.bəl/，美式也可以在第一音节。这个词是褒义/中性的——formidable opponent 既表示对手很强，也暗含尊敬。",
             "usage": "通用词，写作口语皆可。口语替代：tough / serious / daunting / massive。搭配：formidable challenge / opponent / task / obstacle.",
             "examples": [{"text": "Climate change presents formidable challenges for policymakers.", "source": "Nature, 2023"}], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_phrases": [
            {"phrase": "a far cry from", "definition": "completely different from; nothing like", "chinese": "与……相去甚远，完全不同",
             "linguistics": "起源有争议，可能来自苏格兰语「在喊叫声能传到的范围之外」（far from the cry）。表示两事物之间差距巨大。",
             "usage": "半正式，写作口语皆可。口语替代：nothing like / worlds apart from / totally different from。雅思写作：The reality is a far cry from what was promised.",
             "examples": [{"text": "The final product was a far cry from what was originally promised.", "source": "The Economist, 2023"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "come to terms with", "definition": "to gradually accept a difficult reality", "chinese": "逐渐接受（不愿面对的事实）",
             "linguistics": "terms 在这里指「条件」——come to terms with = 与（令人不快的现实）达成「和解条件」。强调接受的过程是渐进的、痛苦的，不是一蹴而就的。",
             "usage": "通用，写作口语皆可。口语替代：accept / deal with / learn to live with。写作中用来描述心理变化过程非常好用。",
             "examples": [{"text": "The nation is still coming to terms with the aftermath of the crisis.", "source": "The Atlantic, 2022"}], "level": "CET-6 / IELTS 6.5+"},
            {"phrase": "runs counter to", "definition": "contradicts; goes against", "chinese": "与……相悖，背道而驰",
             "linguistics": "counter 作副词/介词表示「反方向」。run counter to 比 contradict 更生动——像跑步一样朝相反方向跑。",
             "usage": "书面正式。口语中说 goes against / contradicts / is the opposite of。雅思写作：This trend runs counter to the principles of equality.",
             "examples": [{"text": "The policy runs counter to the principles of free trade.", "source": "The Economist, 2023"}], "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "hinges on", "definition": "depends entirely on", "chinese": "完全取决于",
             "linguistics": "hinge（铰链）——门能否打开完全取决于铰链。比 depends on 更强调「唯一决定性因素」。",
             "usage": "半正式。口语替代：depends on / comes down to / is all about。搭配：success hinges on / the outcome hinges on.",
             "examples": [{"text": "The election outcome hinges on voter turnout in swing states.", "source": "The New York Times, 2024"}], "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "gaining traction", "definition": "becoming increasingly popular or accepted", "chinese": "越来越受关注，逐渐获得支持",
             "linguistics": "traction（牵引力/抓地力）——轮胎获得抓地力后才能前进。gain traction = 从打滑到抓住地面开始前进。非常好的物理比喻。",
             "usage": "半正式，科技和商业语境常用。口语替代：catching on / picking up steam / becoming popular。",
             "examples": [{"text": "The idea of a four-day working week is gaining traction in Europe.", "source": "The Guardian, 2023"}], "level": "IELTS 7.0+"},
        ],
        "annotations_sentences": [
            {"sentence": "The insidious nature of this phenomenon lies in its gradualness.",
             "highlight_key": "The insidious nature of this phenomenon lies in its gradualness",
             "translation": "这个现象的阴险之处在于它的渐进性。",
             "breakdown": "极其简洁有力的一句话。主语 The insidious nature（阴险本质）→ lies in（在于）→ its gradualness（它的渐进性）。用一句话点明了为什么人们没有察觉到社交媒体对人际关系的侵蚀——因为变化太慢了，慢到看不见。",
             "grammar_points": ["lies in = 在于，问题的关键是", "-ness 后缀把形容词 gradual 变成抽象名词"],
             "writing_tip": "「The nature of X lies in Y」简洁有力的学术句式。雅思示例：The appeal of social media lies in its ability to provide instant gratification."},
            {"sentence": "Rather, it was the slow, inexorable accumulation of small changes in how we interact — a text message instead of a phone call, a like instead of a conversation, a curated online persona instead of an authentic encounter.",
             "highlight_key": "Rather, it was the slow, inexorable accumulation of small changes in how we interact",
             "translation": "确切地说，是我们互动方式中那些缓慢的、不可逆转的微小变化的积累——一条短信代替一个电话，一个点赞代替一次对话，一个精心策划的线上人设代替一次真实的交流。",
             "breakdown": "主句：it was the slow, inexorable accumulation of small changes（是微小变化的缓慢而不可逆的积累）→ in how we interact（在我们互动方式上）→ 破折号后用三组对比展开：text message vs phone call / like vs conversation / curated persona vs authentic encounter。三组对比层层递进：从沟通方式 → 互动深度 → 身份真实性。",
             "grammar_points": ["Rather 在句首表示「更确切地说」，修正前句的表述", "三组 A instead of B 构成排比", "破折号用于展开具体解释"],
             "writing_tip": "用「A instead of B」的排比来具体化一个抽象论点是非常有效的写作技巧。读者立刻就能理解你在说什么。"},
            {"sentence": "Rarely has a technological revolution produced such equivocal results.",
             "highlight_key": "Rarely has a technological revolution produced such equivocal results",
             "translation": "很少有一次技术革命产生了如此好坏参半的结果。",
             "breakdown": "Rarely 放在句首引发部分倒装 → has a technological revolution（助动词提前）→ produced such equivocal results。正常语序是 A technological revolution has rarely produced...。倒装增强了感慨和惊叹的语气。",
             "grammar_points": ["否定副词句首倒装：Rarely / Never / Seldom / Hardly + 助动词 + 主语", "equivocal = 好坏参半的、模棱两可的"],
             "writing_tip": "倒装句是雅思高分标配。模板：Rarely/Seldom has X produced/seen such Y. 示例：Seldom has a policy change generated such widespread public debate."},
            {"sentence": "The path forward hinges on our willingness to be honest about what we have lost in the digital transition — and to take deliberate steps to reclaim it.",
             "highlight_key": "The path forward hinges on our willingness to be honest about what we have lost",
             "translation": "前进的道路取决于我们是否愿意坦诚面对数字化转型中失去的东西——并有意识地去找回它。",
             "breakdown": "主句：The path forward hinges on our willingness → to be honest about...（坦诚面对）→ what we have lost in the digital transition（我们在数字化转型中失去的）→ 破折号追加：and to take deliberate steps to reclaim it（并采取有意的步骤去收回）。两个 to 并列（to be honest 和 to take steps）。",
             "grammar_points": ["hinges on = 取决于", "what we have lost — what 引导名词性从句", "deliberate = 经过深思熟虑的（不是随意的）", "破折号用于追加补充"],
             "writing_tip": "「The path forward hinges on...」适合用在文章结尾提出呼吁。雅思示例：The path forward hinges on governments' willingness to prioritise long-term sustainability over short-term profit."},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLE 3 — The New Yorker
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Last Library: A Short Story",
        "source": "The New Yorker",
        "source_icon": "🎭",
        "category": "literature",
        "category_label": "文学小说",
        "summary": "In a world where physical books have become relics, one woman guards the last public library — and the memories it holds.",
        "link": "",
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
            {"word": "facade", "phonetic": "/fəˈsɑːd/", "pos": "n.", "definition": "the front of a building; figuratively, a deceptive appearance", "chinese": "建筑正面；（比喻）假象，表面",
             "linguistics": "法语 façade。注意英语拼写常省略法语的变音符号 ç。双义词：建筑学字面义（正面外墙）和比喻义（虚假的外表）。比喻用法：behind the facade（在表面之下）。",
             "usage": "通用词。口语中比喻义更常见：put on a brave facade / behind the facade of success。写作中两义皆可。",
             "examples": [{"text": "Behind the cheerful facade, she was deeply unhappy.", "source": "Longman Dictionary"}], "level": "CET-6 / IELTS 7.0+"},
            {"word": "unbowed", "phonetic": "/ʌnˈbaʊd/", "pos": "adj.", "definition": "not defeated or discouraged; refusing to give in", "chinese": "不屈的，不低头的",
             "linguistics": "un-（不）+ bowed（弯腰的/低头的）。来自诗人 W.E. Henley 的名句 'I am the master of my fate... my head is bloody, but unbowed'。文学性很强的词。",
             "usage": "书面文学用语。口语中说 refusing to give up / standing strong / unbroken。常用搭配：bloodied but unbowed / weathered but unbowed.",
             "examples": [{"text": "Despite years of hardship, the community remained unbowed.", "source": "The New York Times, 2022"}], "level": "IELTS 7.5+"},
            {"word": "dwindled", "phonetic": "/ˈdwɪn.dəld/", "pos": "v.", "definition": "to gradually become smaller or less", "chinese": "逐渐减少，慢慢缩小",
             "linguistics": "古英语 dwinan（消瘦）。与 diminish 近义但 dwindle 更强调「逐渐消失」的过程感——从有到少到几乎没有。文学性比 decrease 强。",
             "usage": "半正式。口语中说 shrank / got smaller and smaller / dried up。搭配：dwindle to nothing / dwindle away / dwindling resources.",
             "examples": [{"text": "Public trust in institutions has dwindled over the past decade.", "source": "The Economist, 2023"}], "level": "CET-6 / IELTS 7.0+"},
            {"word": "patina", "phonetic": "/ˈpæt.ɪ.nə/", "pos": "n.", "definition": "a surface appearance gained through age or use; a green film on aged copper", "chinese": "铜绿；岁月的痕迹（含美感）",
             "linguistics": "意大利语/拉丁语，原指铜器表面氧化后的绿色薄膜。在文学语境中引申为「时间赋予事物的美感和厚重感」——与 rust（铁锈，衰败的象征）形成对比。patina 是正面的岁月痕迹。",
             "usage": "文学/艺术用语。口语中很少用。写作中可用来描述历史感和时间的美：a patina of age / the patina of centuries.",
             "examples": [{"text": "The old desk had a beautiful patina that spoke of decades of use.", "source": "The New Yorker, 2022"}], "level": "IELTS 8.0+ (文学词汇)"},
            {"word": "entropy", "phonetic": "/ˈen.trə.pi/", "pos": "n.", "definition": "gradual decline into disorder; (physics) measure of disorder", "chinese": "熵；衰败，无序化",
             "linguistics": "希腊语 entropia（转变）。热力学第二定律：封闭系统的熵总是增大（趋向无序）。文学中用作万物终将衰败的隐喻。这里说的是：图书馆员的日常维护是对抗「一切终将瓦解」这一自然法则的小小抵抗。",
             "usage": "学术/文学用语。口语中说 things falling apart / decay / chaos。这个词在科学和文学两个语境中都有深度。",
             "examples": [{"text": "Without constant effort, organisations tend towards entropy.", "source": "Harvard Business Review, 2022"}], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "portended", "phonetic": "/pɔːˈten.dɪd/", "pos": "v.", "definition": "to be a sign that something (bad) is going to happen", "chinese": "预示，预兆（通常是坏事）",
             "linguistics": "拉丁语 portendere（预示），por-（向前）+ tendere（伸展）。与 predict 的区别：portend 暗示不祥之兆，predict 中性。同根词：portentous（预兆性的/装腔作势的）。",
             "usage": "高度书面文学用语。口语中说 was a sign of / hinted at / suggested。搭配：portend disaster / change / trouble.",
             "examples": [{"text": "The dark clouds portended a violent storm.", "source": "Oxford Advanced Learner's Dictionary"}], "level": "TEM-8 / IELTS 8.0+"},
            {"word": "limbo", "phonetic": "/ˈlɪm.bəʊ/", "pos": "n.", "definition": "an uncertain state of awaiting a decision", "chinese": "悬而未决的状态",
             "linguistics": "天主教神学概念：limbus（边缘），指未受洗婴儿灵魂的所在地——既不在天堂也不在地狱，处于中间地带。世俗用法：in limbo = 处于不上不下的等待状态。",
             "usage": "通用词。口语中说 stuck / in a holding pattern / up in the air / neither here nor there。搭配：in limbo / left in limbo / legal limbo.",
             "examples": [{"text": "The project has been in limbo since the funding was cut.", "source": "The Guardian, 2023"}], "level": "CET-6 / IELTS 7.0+"},
            {"word": "voraciously", "phonetic": "/vəˈreɪ.ʃəs.li/", "pos": "adv.", "definition": "eagerly and enthusiastically, wanting a lot", "chinese": "如饥似渴地，贪婪地",
             "linguistics": "拉丁语 vorare（吞食）。原指吃东西狼吞虎咽，引申为对知识/阅读的贪婪渴求。与 ravenous（极度饥饿的）同源。voracious reader 是一个常见搭配。",
             "usage": "半正式文学用语。口语中说 like crazy / non-stop / couldn't get enough。搭配：read voraciously / consume voraciously / a voracious appetite.",
             "examples": [{"text": "She reads voraciously — at least three books a week.", "source": "The New Yorker, 2022"}], "level": "TEM-8 / IELTS 7.5+"},
            {"word": "tentatively", "phonetic": "/ˈten.tə.tɪv.li/", "pos": "adv.", "definition": "in a hesitant, uncertain way; not firmly or confidently", "chinese": "试探性地，犹豫不决地",
             "linguistics": "拉丁语 tentare（尝试）。tentative 的副词形式。描述一种小心翼翼、怕犯错的状态。与 confidently / boldly 形成对比。",
             "usage": "通用词。口语中说 carefully / nervously / cautiously。搭配：tentatively suggest / tentatively reach out / tentatively agree.",
             "examples": [{"text": "She tentatively raised her hand to ask a question.", "source": "Cambridge Dictionary"}], "level": "CET-6 / IELTS 7.0+"},
            {"word": "imperious", "phonetic": "/ɪmˈpɪə.ri.əs/", "pos": "adj.", "definition": "domineering; assuming authority without justification", "chinese": "专横的，霸道的",
             "linguistics": "拉丁语 imperium（统治权）。与 imperial（帝国的）、emperor（皇帝）同根。这里形容天气（an imperious day）是拟人化修辞——阴沉的十月天像一个傲慢的统治者一样笼罩一切。",
             "usage": "书面文学用语。口语中说 bossy / domineering / arrogant。用于形容天气是高级文学修辞。",
             "examples": [{"text": "Her imperious manner alienated many colleagues.", "source": "Collins English Dictionary"}], "level": "TEM-8 / IELTS 8.0+"},
        ],
        "annotations_phrases": [
            {"phrase": "hold sway", "definition": "to have great power or influence; to dominate", "chinese": "占支配地位，掌控局面",
             "linguistics": "sway（摇摆/支配力）。hold sway = 掌握摇摆的方向。中世纪英语用法，至今保留。比 dominate 更文学化。",
             "usage": "书面正式。口语替代：be in charge / be dominant / call the shots / rule the roost。搭配：hold sway over / hold sway in.",
             "examples": [{"text": "Traditional values still hold sway in many rural communities.", "source": "The New Yorker, 2022"}], "level": "TEM-8 / IELTS 7.5+"},
            {"phrase": "set the stage for", "definition": "to create conditions for something to happen", "chinese": "为……创造条件，铺垫",
             "linguistics": "戏剧比喻：布置好舞台，让预设的剧情上演。在本文中暗示市议会已经决定关闭图书馆，现在只是在走过场。",
             "usage": "半正式。口语替代：pave the way for / lay the groundwork for / prepare the ground for。雅思写作高频表达。",
             "examples": [{"text": "The reforms set the stage for a decade of economic growth.", "source": "The Economist, 2022"}], "level": "CET-6 / IELTS 7.0+"},
            {"phrase": "bear the brunt of", "definition": "to suffer the greatest part of something bad", "chinese": "首当其冲，承受最大冲击",
             "linguistics": "brunt 原义：攻击的主要力量。bear the brunt = 承受攻击的主力。在本文最后一句中用法很文学化：some things bear the brunt of meaning（有些事物承载了最沉重的意义）——反转了通常的负面含义。",
             "usage": "通用，写作口语皆可。口语替代：take the hardest hit / suffer the most / get the worst of it。雅思写作：Low-income families bear the brunt of rising living costs.",
             "examples": [{"text": "Coastal regions bore the brunt of the hurricane's fury.", "source": "The New York Times, 2022"}], "level": "CET-6 / IELTS 7.0+"},
        ],
        "annotations_sentences": [
            {"sentence": "It was a routine she performed with the quiet precision of someone who understood that small acts of maintenance hold sway against the inexorable forces of entropy.",
             "highlight_key": "It was a routine she performed with the quiet precision of someone who understood that small acts of maintenance hold sway against the inexorable forces of entropy",
             "translation": "这是她以安静的精确性所执行的日常——这份精确来自一个深知微小的维护行为能抵御不可阻挡的衰败力量的人。",
             "breakdown": "四层嵌套：① It was a routine → ② she performed with the quiet precision of someone → ③ who understood that → ④ small acts hold sway against entropy。从日常动作到宇宙哲学，用一句话写出了图书馆员的人生哲学：做好每一件小事就是对抗世界走向混乱的方式。",
             "grammar_points": ["多层定语从句嵌套", "with + 名词 表示方式状语", "hold sway against = 抵御", "entropy 是热力学概念的文学比喻"],
             "writing_tip": "这种从具体到抽象的句式是文学写作的精髓。在学术写作中需谨慎使用，但在议论文的收尾段落中一句这样的话可以非常出彩。"},
            {"sentence": "Margaret had learned to read these documents the way a sailor reads clouds — not for what they said, but for what they portended.",
             "highlight_key": "Margaret had learned to read these documents the way a sailor reads clouds",
             "translation": "玛格丽特已经学会了像水手读云一样读这些文件——不看字面意思，而看它们暗示的未来。",
             "breakdown": "主句：Margaret had learned to read documents → the way a sailor reads clouds（类比：像水手读云）→ 破折号展开：not for what they said（不是为了字面意思）→ but for what they portended（而是为了它们预兆的东西）。精妙的类比：水手看云不是欣赏风景，而是判断暴风雨是否要来。",
             "grammar_points": ["the way + 从句 = 以……的方式（类比修辞）", "not for A but for B 对比强调", "what 引导名词性从句"],
             "writing_tip": "「the way + 生动比喻」是让文章瞬间出彩的修辞手法。关键是找到出人意料但又精准的类比。"},
            {"sentence": "In that gesture, Margaret saw neither the past nor the future, but something rarer: the present, undiluted and fully inhabited.",
             "highlight_key": "In that gesture, Margaret saw neither the past nor the future, but something rarer: the present, undiluted and fully inhabited",
             "translation": "在那个手势中，玛格丽特看到的既不是过去也不是未来，而是更为稀有的东西：纯粹的、被完全占据的当下。",
             "breakdown": "In that gesture → Margaret saw → neither A nor B, but C → 冒号后展开 C 是什么：the present, undiluted and fully inhabited。neither...nor...but 三段式否定再肯定。undiluted（未被稀释的）和 inhabited（被居住的/被填满的）用来形容「当下」非常独特。",
             "grammar_points": ["neither A nor B, but C — 否定两个选项，提出第三种", "冒号用于揭示/解释", "undiluted / inhabited 用于形容抽象概念是文学手法"],
             "writing_tip": "neither A nor B, but something rarer: C 这个句式可以用来提出出人意料的观点。它先否定两个常见选项，再揭示你真正想说的。"},
        ],
    },

    # ═══════════════════════════════════════════════════════════
    # ARTICLES 4-6 — kept but with basic annotations
    # These rotate in on different days
    # ═══════════════════════════════════════════════════════════
    {
        "title": "Artificial Intelligence and the Future of Work: Beyond the Hype",
        "source": "The Economist",
        "source_icon": "📊",
        "category": "politics_economics",
        "category_label": "政治经济",
        "summary": "As AI transforms industries, the real question is not whether jobs will disappear, but how societies will manage the transition.",
        "link": "",
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
        "annotations_vocab": [],
        "annotations_phrases": [],
        "annotations_sentences": [],
    },
    {
        "title": "The Architecture of Silence: What Empty Spaces Tell Us",
        "source": "The New Yorker",
        "source_icon": "🎭",
        "category": "literature",
        "category_label": "文学小说",
        "summary": "An exploration of how abandoned buildings, empty rooms, and forgotten places speak volumes about the societies that created — and left — them.",
        "link": "",
        "published": "2025-05-01",
        "has_full_text": True,
        "full_text": """There is an eloquence to emptiness that the crowded world finds difficult to hear. Walk through an abandoned factory, a decommissioned church, or a shuttered school, and you will encounter a form of narrative that no living voice could replicate. These spaces speak not in the language of what they contain, but in the grammar of what has been removed.

The proliferation of such spaces in the post-industrial landscape has given rise to a curious subculture of urban explorers — photographers and writers who seek out the ruins of modernity with the fervour of nineteenth-century archaeologists. Their work, at its best, is a far cry from mere nostalgia. It is an attempt to shed light on the processes of economic and social change that, in their inexorable operation, render entire communities obsolete.

In the wake of deindustrialisation, cities like Detroit, Sheffield, and the towns of the German Ruhr Valley have had to come to terms with a new identity. The austerity that followed the loss of their primary industries was not merely fiscal but existential. What is a steel town without steel? What is a mining village when the mines have closed? The conundrum is not simply economic; it touches the deepest questions of belonging and purpose.

While some of these communities have managed to reinvent themselves, many have not. The dichotomy between those that adapted and those that did not hinges, in large part, on factors beyond their control: geography, political will, the volatile currents of global capital. By and large, the places that recovered were those with access to education, transport links, and the kind of civic infrastructure that set the stage for new industries. Those that lacked these advantages bore the brunt of change.

The pernicious myth of individual resilience — the idea that anyone can succeed if they simply try hard enough — runs counter to the lived experience of these communities. It is an ideology that obfuscates the structural forces at work, allowing policymakers to eschew responsibility for the collective consequences of economic transformation.

With their crumbling walls whispering stories of departed lives, these empty buildings serve as a rebuke to the complacent narrative of progress. They remind us that every act of creation is shadowed by an act of destruction, and that the unprecedented pace of change in the modern world has not been commensurate with an unprecedented capacity to manage its fallout.

Rarely has a society been forced to confront so directly the gap between its self-image and its reality. The architecture of silence asks us to listen — not to what we wish to hear, but to what the evidence plainly states. And in that listening, there may yet be the seed of a more honest, more equivocal, but ultimately more humane understanding of what it means to live in a world that never stops changing.""",
        "annotations_vocab": [],
        "annotations_phrases": [],
        "annotations_sentences": [],
    },
    {
        "title": "Climate Finance: The Trillion-Dollar Question",
        "source": "The Atlantic",
        "source_icon": "🌊",
        "category": "editorial",
        "category_label": "社论评论",
        "summary": "Developing nations need trillions to adapt to climate change, but the money is not flowing. The gap between promise and reality threatens global cooperation.",
        "link": "",
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
        "annotations_vocab": [],
        "annotations_phrases": [],
        "annotations_sentences": [],
    },
]
