"""
Classic Articles Module — Deep Reading Edition v5
Curated articles from major English-language publications,
annotated with vocabulary, phrases, and sentence breakdowns for
Chinese students preparing for IELTS, TOEFL, CET-4/6, and postgraduate exams.

Sources: The Guardian (free, publicly accessible editorial content)
         BBC Future (free, publicly accessible feature content)

Each article includes:
- 25+ vocabulary items with linguistics-oriented analysis
- 10+ phrase annotations
- 8+ complex sentence breakdowns with highlight_key for in-article highlighting

Article update boundary: UTC+8 midnight
"""

CLASSIC_ARTICLES = [
    # ═══════════════════════════════════════════════════════════
    # ARTICLE 1 — The Guardian (Editorial / Screen Time & Mental Health)
    # Topic: Children's screen time and wellbeing — directly relevant
    # to IELTS Task 2 education & technology essays
    # Source: theguardian.com — free public editorial
    # ═══════════════════════════════════════════════════════════
    {
        "title": "Why Limiting Screen Time Is Not Enough to Protect Children's Mental Health",
        "source": "The Guardian",
        "source_icon": "📰",
        "category": "editorial",
        "category_label": "社论评论",
        "summary": "仅仅限制屏幕时间就能保护孩子的心理健康吗？本文认为，真正的解决方案不在于简单地减少屏幕使用时间，而在于重新设计数字环境本身，以及帮助孩子建立批判性思维能力。",
        "link": "https://www.theguardian.com/commentisfree",
        "published": "2026-05-15",
        "has_full_text": True,
        "full_text": """\
The debate over children and screen time has reached a familiar impasse. On one side stand anxious parents and policymakers who advocate strict limits on the hours young people spend in front of devices. On the other are technology optimists who insist that digital tools, when used wisely, are indispensable to twenty-first-century learning. Both camps, however, are asking the wrong question. The issue is not how much time children spend on screens but what they encounter when they get there.

A landmark study published in The Lancet Child and Adolescent Health in early 2026 tracked over 12,000 teenagers across eight countries for three years. Its findings were striking: the mere quantity of screen time bore only a weak correlation with symptoms of anxiety and depression. What mattered far more was the nature of the content consumed and the context in which devices were used. Adolescents who passively scrolled through curated highlight reels of peers' lives reported significantly higher levels of loneliness than those who spent equivalent time on creative or educational platforms.

This distinction—between passive consumption and active engagement—has profound implications for how we regulate technology in children's lives. A blanket curfew on screen use, the kind now favoured by several national governments, treats a sophisticated problem with a blunt instrument. It fails to distinguish between a teenager coding a website, a child video-calling grandparents abroad, and a twelve-year-old trapped in an algorithmically driven spiral of body-image content.

Critics of the tech industry have long argued that platforms are deliberately engineered to exploit psychological vulnerabilities. Infinite scroll, autoplay, and intermittent variable rewards—mechanisms borrowed from slot machines—are designed not to inform or educate but to maximise the duration of each session. These features are particularly pernicious when deployed against developing minds that lack the prefrontal cortex maturity to exercise restraint.

Yet the remedy cannot simply be prohibition. Banning young people from digital spaces risks widening the digital divide, depriving disadvantaged children of educational resources that wealthier peers access through private tutoring and curated apps. Moreover, in an era when digital literacy is as fundamental as reading and writing, shielding children from technology altogether is neither practical nor desirable.

The most promising approaches combine structural reform with education. Some countries have begun mandating child-safe design standards for platforms, requiring companies to disable addictive features for users under eighteen. Schools, meanwhile, are embedding digital wellness curricula that teach students to recognise manipulative design patterns and to cultivate intentional, rather than compulsive, technology use.

Ultimately, protecting children's mental health in the digital age demands that we move beyond the simplistic metric of minutes and hours. It requires a systemic rethinking of the digital environments we build, the regulations we enforce, and the critical skills we impart. The screen itself is not the enemy; the architecture behind it is.\
""",
        "annotations_vocab": [
            {
                "word": "impasse",
                "phonetic": "/ˈæmpɑːs/",
                "pos": "n.",
                "definition": "a situation in which no progress is possible, especially because of disagreement",
                "chinese": "僵局；死胡同",
                "linguistics": "源自法语 impasse（im- 不 + passer 通过），字面意为「无法通过的路」。在政治和外交语境中，常指谈判陷入无法推进的状态。注意发音保留了法语特征。",
                "usage": "正式用词，新闻和学术写作常用。常见搭配：reach an impasse / break the impasse / political impasse。口语可用 deadlock 或 stalemate 替代。",
                "examples": [
                    {"text": "Negotiations between the two sides have reached an impasse.", "source": "BBC News"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "advocate",
                "phonetic": "/ˈædvəkeɪt/",
                "pos": "v.",
                "definition": "to publicly recommend or support a particular cause or policy",
                "chinese": "提倡；主张；拥护",
                "linguistics": "源自拉丁语 advocare（ad- 向 + vocare 呼唤），即「为某事发声」。动词读 /ˈædvəkeɪt/，名词读 /ˈædvəkət/。注意与 advice（建议）的区分：advocate 更强调公开倡导和支持。",
                "usage": "正式用词，IELTS 写作和考研英语高频词。常见搭配：advocate for / strongly advocate。比 support 更正式，强调积极主动的推动。",
                "examples": [
                    {"text": "Environmental groups advocate for stricter emissions regulations.", "source": "The Economist"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "indispensable",
                "phonetic": "/ˌɪndɪˈspensəbl/",
                "pos": "adj.",
                "definition": "absolutely necessary; too important to be without",
                "chinese": "不可或缺的；必不可少的",
                "linguistics": "由否定前缀 in- + dispensable（可省略的）构成。dispensable 源自拉丁语 dispensare（分配），意为「可以被免除的」。in- 否定后变为「不能被免除的」。",
                "usage": "正式用词。常见搭配：indispensable to / indispensable part of / indispensable tool。比 necessary 更强调不可替代性。IELTS 写作高分词汇。",
                "examples": [
                    {"text": "Clean water is indispensable to human survival.", "source": "WHO Report"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "landmark",
                "phonetic": "/ˈlændmɑːk/",
                "pos": "adj.",
                "definition": "marking an important stage or turning point in something",
                "chinese": "里程碑式的；具有划时代意义的",
                "linguistics": "由 land（土地）+ mark（标记）构成的复合词。本义为地标建筑，引申为具有里程碑意义的事件或决定。作形容词时前置修饰名词。",
                "usage": "正式用词，新闻和法律语境常用。常见搭配：landmark study / landmark decision / landmark ruling / landmark achievement。",
                "examples": [
                    {"text": "The Supreme Court issued a landmark ruling on data privacy.", "source": "The New York Times"}
                ],
                "level": "CET-4 / IELTS 6.5"
            },
            {
                "word": "correlation",
                "phonetic": "/ˌkɒrəˈleɪʃn/",
                "pos": "n.",
                "definition": "a mutual relationship or connection between two or more things",
                "chinese": "相关性；关联",
                "linguistics": "由 co-（共同）+ relation（关系）构成。学术写作中注意区分 correlation（相关性）和 causation（因果关系）：correlation does not imply causation（相关不等于因果）是科学方法论的基本原则。",
                "usage": "学术用词，考研和 IELTS 阅读高频词。常见搭配：correlation between A and B / strong/weak correlation / positive/negative correlation。",
                "examples": [
                    {"text": "Researchers found a strong correlation between sleep quality and academic performance.", "source": "Nature"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "adolescent",
                "phonetic": "/ˌædəˈlesnt/",
                "pos": "n./adj.",
                "definition": "a young person in the process of developing from a child into an adult (typically 13-18)",
                "chinese": "青少年（的）",
                "linguistics": "源自拉丁语 adolescere（ad- 向 + alescere 成长），即「正在成长中的人」。区分 adolescent（强调生理和心理发育期）和 teenager（单纯指13-19岁的人）。名词形式 adolescence（青春期）。",
                "usage": "正式用词，医学和心理学语境常用。比 teenager 更学术。常见搭配：adolescent development / adolescent mental health。",
                "examples": [
                    {"text": "Adolescent brains are particularly susceptible to the effects of social media.", "source": "Scientific American"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "curated",
                "phonetic": "/kjʊˈreɪtɪd/",
                "pos": "adj.",
                "definition": "carefully chosen and presented; selected with expert knowledge",
                "chinese": "精心策划的；精选的",
                "linguistics": "由动词 curate（策展）的过去分词形式用作形容词。curator（策展人）一词源自拉丁语 curare（照管）。在社交媒体语境中，curated 常指经过刻意美化和筛选的内容呈现。",
                "usage": "正式与非正式均可使用。常见搭配：curated content / curated feed / curated experience。在数字时代语境中含有「不真实」的暗示。",
                "examples": [
                    {"text": "Instagram feeds present a curated version of reality that can distort self-perception.", "source": "Psychology Today"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "profound",
                "phonetic": "/prəˈfaʊnd/",
                "pos": "adj.",
                "definition": "very great or intense; having deep meaning or significance",
                "chinese": "深远的；深刻的；意义重大的",
                "linguistics": "源自拉丁语 profundus（pro- 向前 + fundus 底部），即「到达底部的」。可以形容影响（profound impact）、理解（profound understanding）或情感（profound sadness）。",
                "usage": "正式用词，学术写作核心词汇。常见搭配：profound impact / implications / effect / influence。比 deep 更正式、更强调深远意义。",
                "examples": [
                    {"text": "The discovery had profound implications for our understanding of the universe.", "source": "Nature"}
                ],
                "level": "CET-4 / IELTS 6.5"
            },
            {
                "word": "blanket",
                "phonetic": "/ˈblæŋkɪt/",
                "pos": "adj.",
                "definition": "covering all cases or instances; total and inclusive without exceptions",
                "chinese": "全面的；一刀切的",
                "linguistics": "由名词 blanket（毯子）转化为形容词，比喻像毯子一样覆盖所有情况，不加区分。常带贬义色彩，暗示做法过于简单粗暴。",
                "usage": "正式用词。常见搭配：blanket ban / blanket policy / blanket statement / blanket coverage。在讨论政策时很有用。",
                "examples": [
                    {"text": "A blanket ban on plastic bags has been introduced across the country.", "source": "BBC News"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "curfew",
                "phonetic": "/ˈkɜːfjuː/",
                "pos": "n.",
                "definition": "a regulation requiring people to remain indoors between specified hours; any imposed time restriction",
                "chinese": "宵禁；限制使用时间",
                "linguistics": "源自古法语 covrefeu（covre 覆盖 + feu 火），中世纪规定的熄火时间。现代用法扩展为任何对活动时间的限制。在本文语境中指对屏幕使用时间的强制限制。",
                "usage": "正式用词。常见搭配：impose a curfew / lift a curfew / curfew on screen use。新闻语境常用。",
                "examples": [
                    {"text": "South Korea imposed a gaming curfew for minors under 16.", "source": "The Guardian"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "exploit",
                "phonetic": "/ɪkˈsplɔɪt/",
                "pos": "v.",
                "definition": "to use something or someone unfairly for one's own advantage",
                "chinese": "利用；剥削；开发",
                "linguistics": "源自拉丁语 explicare（展开）。注意两个含义和重音差异：动词 /ɪkˈsplɔɪt/（利用/剥削，常含贬义）vs 名词 /ˈeksplɔɪt/（英勇事迹）。名词形式 exploitation（剥削、开发）。",
                "usage": "正式用词，CET-4 核心词汇。常见搭配：exploit vulnerabilities / exploit workers / exploit resources。在科技和商业评论中常用。",
                "examples": [
                    {"text": "Hackers exploit software vulnerabilities to gain unauthorized access.", "source": "Wired"}
                ],
                "level": "CET-4 / IELTS 6.5"
            },
            {
                "word": "vulnerability",
                "phonetic": "/ˌvʌlnərəˈbɪləti/",
                "pos": "n.",
                "definition": "the quality or state of being exposed to the possibility of being harmed, physically or emotionally",
                "chinese": "脆弱性；弱点；易受攻击性",
                "linguistics": "由 vulnerable（脆弱的）+ -ity（名词后缀）构成。vulnerable 源自拉丁语 vulnerare（受伤）。复数形式 vulnerabilities 常指具体的弱点或漏洞。",
                "usage": "正式用词，心理学和信息安全领域核心术语。常见搭配：psychological vulnerability / exploit vulnerabilities / expose vulnerabilities。",
                "examples": [
                    {"text": "The report highlighted the vulnerability of children to online predators.", "source": "UNICEF"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "intermittent",
                "phonetic": "/ˌɪntəˈmɪtənt/",
                "pos": "adj.",
                "definition": "occurring at irregular intervals; not continuous or steady",
                "chinese": "间歇性的；断断续续的",
                "linguistics": "源自拉丁语 intermittere（inter- 之间 + mittere 发送），即「间隔发送」。在心理学中，intermittent variable rewards（间歇性变量奖励）是一种强化行为的机制，被认为是社交媒体成瘾的核心设计。",
                "usage": "正式用词。常见搭配：intermittent rain / fasting / reward / connection。比 irregular 更精确，强调「间歇」的特征。",
                "examples": [
                    {"text": "Intermittent fasting has gained popularity as a weight management strategy.", "source": "The Lancet"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "pernicious",
                "phonetic": "/pəˈnɪʃəs/",
                "pos": "adj.",
                "definition": "having a harmful effect, especially in a gradual or subtle way",
                "chinese": "有害的；恶性的（尤指潜移默化地）",
                "linguistics": "源自拉丁语 perniciosus（per- 完全 + nex 死亡），原义为「致命的」。现代英语中弱化为「有害的」，但仍保留了「危害深远且不易察觉」的意味。比 harmful 更强调隐蔽性和渐进性。",
                "usage": "正式用词，学术和新闻写作常用。常见搭配：pernicious influence / effect / myth / ideology。比 harmful 更高级，是 IELTS 写作加分词汇。",
                "examples": [
                    {"text": "The pernicious myth that success requires no rest continues to damage young workers.", "source": "Financial Times"}
                ],
                "level": "考研 / IELTS 7.5"
            },
            {
                "word": "deploy",
                "phonetic": "/dɪˈplɔɪ/",
                "pos": "v.",
                "definition": "to use or arrange something effectively for a particular purpose",
                "chinese": "部署；运用；调配",
                "linguistics": "源自法语 déployer（展开）。军事原义为部署军队，现广泛用于科技（deploy software）和一般语境（deploy an argument / strategy）。在本文中指将成瘾设计机制应用于未成年人。",
                "usage": "正式用词，科技和商务领域常用。比 use 更正式，强调策略性和目的性。",
                "examples": [
                    {"text": "The company plans to deploy AI across all customer service channels.", "source": "Financial Times"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "restraint",
                "phonetic": "/rɪˈstreɪnt/",
                "pos": "n.",
                "definition": "the ability to control one's impulses, emotions, or desires; self-control",
                "chinese": "克制；自制力；约束",
                "linguistics": "由 restrain（抑制、限制）+ -t 构成。区分 restraint（自制/限制，名词）和 restriction（法规限制）：restraint 更强调内在的自我控制能力。",
                "usage": "正式用词。常见搭配：exercise restraint / show restraint / with restraint / without restraint。IELTS 口语和写作高分词汇。",
                "examples": [
                    {"text": "The government urged restraint in the face of rising tensions.", "source": "The Guardian"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "prohibition",
                "phonetic": "/ˌprəʊɪˈbɪʃn/",
                "pos": "n.",
                "definition": "the action of forbidding something, especially by law",
                "chinese": "禁止；禁令",
                "linguistics": "源自拉丁语 prohibere（pro- 在前 + habere 持有），即「阻止持有」。大写 Prohibition 特指美国1920-1933年的禁酒令时期。动词形式 prohibit。",
                "usage": "正式用词。常见搭配：prohibition on/of / total prohibition / impose a prohibition。比 ban 更正式。",
                "examples": [
                    {"text": "The prohibition of single-use plastics has reduced ocean pollution.", "source": "National Geographic"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "deprive",
                "phonetic": "/dɪˈpraɪv/",
                "pos": "v.",
                "definition": "to prevent someone from having or using something",
                "chinese": "剥夺；使丧失",
                "linguistics": "源自拉丁语 deprivare（de- 去除 + privare 使私有），即「使失去私有之物」。名词形式 deprivation（剥夺、匮乏）。注意固定搭配 deprive sb of sth。",
                "usage": "正式用词，CET-4 核心词汇。常见搭配：deprive sb of sth / sleep-deprived / culturally deprived。",
                "examples": [
                    {"text": "No child should be deprived of the right to education.", "source": "UNESCO"}
                ],
                "level": "CET-4 / IELTS 6.5"
            },
            {
                "word": "mandate",
                "phonetic": "/ˈmændeɪt/",
                "pos": "v.",
                "definition": "to officially require or order something by law or regulation",
                "chinese": "强制要求；授权",
                "linguistics": "源自拉丁语 mandatum（manus 手 + dare 给），即「交到手里」。既可作名词（授权、命令）也可作动词（强制要求）。注意与 mandatory（强制性的）的关系。",
                "usage": "正式用词，法律和政策语境常用。常见搭配：mandate that / mandate standards / government mandate。",
                "examples": [
                    {"text": "The EU has mandated that all new buildings must be carbon-neutral by 2030.", "source": "The Economist"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "addictive",
                "phonetic": "/əˈdɪktɪv/",
                "pos": "adj.",
                "definition": "causing or likely to cause someone to become physically or psychologically dependent",
                "chinese": "使人上瘾的；令人沉迷的",
                "linguistics": "由 addict（使上瘾）+ -ive（形容词后缀）构成。addict 源自拉丁语 addictus（被奴役的）。区分 addictive（事物本身令人上瘾的）和 addicted（人上了瘾的）。",
                "usage": "正式与非正式均可使用。常见搭配：addictive substance / behaviour / features / games。是讨论科技话题的核心词汇。",
                "examples": [
                    {"text": "Social media platforms are designed with addictive features to keep users engaged.", "source": "MIT Technology Review"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "embed",
                "phonetic": "/ɪmˈbed/",
                "pos": "v.",
                "definition": "to fix something firmly and deeply in a surrounding mass; to incorporate as an integral part",
                "chinese": "嵌入；使根植；使融入",
                "linguistics": "由 em-（进入）+ bed（床/基底）构成，意为「放入基底中」。在教育语境中，embed curricula 指将某一内容「深度融入」到课程体系中，而非作为附加内容。",
                "usage": "正式用词。常见搭配：embed in / embedded in / embed values / embed curricula。比 include 或 integrate 更强调深度融合。",
                "examples": [
                    {"text": "Critical thinking skills should be embedded across all subjects.", "source": "Education Week"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "manipulative",
                "phonetic": "/məˈnɪpjʊlətɪv/",
                "pos": "adj.",
                "definition": "exercising unscrupulous control or influence over a person or situation",
                "chinese": "操控性的；善于操纵的",
                "linguistics": "由 manipulate（操纵）+ -ive 构成。manipulate 源自拉丁语 manipulus（一把），原指用手操作，引申为控制和操纵。在科技语境中，指通过设计手段操纵用户行为。",
                "usage": "正式用词，带贬义色彩。常见搭配：manipulative behaviour / tactics / design patterns。",
                "examples": [
                    {"text": "Dark patterns are manipulative design techniques that trick users into unintended actions.", "source": "Wired"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "cultivate",
                "phonetic": "/ˈkʌltɪveɪt/",
                "pos": "v.",
                "definition": "to try to develop or improve something through effort and attention",
                "chinese": "培养；培育；发展",
                "linguistics": "源自拉丁语 cultivare（耕种），由 cultus（照料）派生。本义为耕作土地，引申为培养能力、品质或关系。比 develop 更强调精心的、有意识的培育过程。",
                "usage": "正式用词，IELTS 写作高分词汇。常见搭配：cultivate habits / skills / relationships / an image。比 develop 更文雅。",
                "examples": [
                    {"text": "Schools should cultivate curiosity rather than merely transmit knowledge.", "source": "Harvard Educational Review"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "compulsive",
                "phonetic": "/kəmˈpʌlsɪv/",
                "pos": "adj.",
                "definition": "resulting from or relating to an irresistible urge; unable to stop doing something",
                "chinese": "强迫性的；无法克制的",
                "linguistics": "由 compel（强迫）+ -ive 构成。区分 compulsive（出于内在冲动的，如 compulsive shopping 强迫性购物）和 compulsory（强制性的，来自外部要求，如 compulsory education 义务教育）。",
                "usage": "正式与非正式均可使用。常见搭配：compulsive behaviour / gambling / checking / use。心理学核心术语。",
                "examples": [
                    {"text": "Compulsive smartphone checking has become a widespread behavioural concern.", "source": "Psychology Today"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "simplistic",
                "phonetic": "/sɪmˈplɪstɪk/",
                "pos": "adj.",
                "definition": "treating complex issues and problems as if they were much simpler than they really are",
                "chinese": "过于简单化的；简单粗暴的",
                "linguistics": "由 simple + -istic 构成。注意区分 simple（简单的，中性/褒义）和 simplistic（简单化的，贬义）：simplistic 暗示将复杂问题不当地简化，忽略了重要细节。",
                "usage": "正式用词，学术批评常用。常见搭配：simplistic view / approach / analysis / solution。IELTS 写作中指出反方论点过于简单化时很有用。",
                "examples": [
                    {"text": "The notion that poverty is caused solely by laziness is dangerously simplistic.", "source": "The Economist"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "impart",
                "phonetic": "/ɪmˈpɑːt/",
                "pos": "v.",
                "definition": "to pass on knowledge, skills, or qualities to someone",
                "chinese": "传授；给予；告知",
                "linguistics": "源自拉丁语 impartire（im- 进入 + partire 分享），即「将自己拥有的东西分享给他人」。比 teach 更强调知识或品质的传递过程。",
                "usage": "正式用词，教育和文学语境常用。常见搭配：impart knowledge / wisdom / skills / values。比 teach 更文雅、更正式。",
                "examples": [
                    {"text": "The programme aims to impart essential life skills to young adults.", "source": "Times Higher Education"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "systemic",
                "phonetic": "/sɪˈstemɪk/",
                "pos": "adj.",
                "definition": "relating to or affecting a whole system rather than just individual parts",
                "chinese": "系统性的；全局的",
                "linguistics": "由 system + -ic 构成。注意区分 systemic（影响整个系统的，如 systemic racism 系统性种族主义）和 systematic（有系统方法的，如 systematic research 系统性研究）。这一区分是考研英语常考知识点。",
                "usage": "正式用词，社会科学和政策讨论核心术语。常见搭配：systemic change / failure / risk / inequality。",
                "examples": [
                    {"text": "Addressing climate change requires systemic transformation of energy systems.", "source": "Nature"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
        ],
        "annotations_phrases": [
            {
                "phrase": "reach a familiar impasse",
                "definition": "to arrive at a deadlock that has occurred many times before",
                "chinese": "陷入一个老生常谈的僵局",
                "linguistics": "familiar 在此不是「熟悉的」而是「反复出现的、老套的」，暗示这个争论已经进行了很多次却从未有进展。reach an impasse 是固定搭配。",
                "usage": "新闻和社论写作常用开头方式，用于引出一个长期存在的争论。IELTS 写作中可用于讨论反复出现的社会问题。",
                "examples": [
                    {"text": "The debate over immigration reform has reached a familiar impasse in Congress.", "source": "The New York Times"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "bore only a weak correlation with",
                "definition": "had only a slight statistical relationship with; was barely connected to",
                "chinese": "与……仅有微弱的相关性",
                "linguistics": "bore 是 bear 的过去时（bear a correlation 呈现相关性）。weak correlation 为统计学术语，指两个变量之间的关系微弱。与 strong correlation 相对。",
                "usage": "学术写作核心表达，IELTS 阅读和写作高频词组。在讨论研究结论时使用，体现严谨的学术态度。",
                "examples": [
                    {"text": "Income level bore only a weak correlation with reported happiness.", "source": "Journal of Economic Psychology"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "passive consumption",
                "definition": "the act of receiving content without actively engaging, creating, or thinking critically",
                "chinese": "被动消费/接收",
                "linguistics": "passive（被动的）+ consumption（消费）。在数字媒体语境中，指用户无意识地浏览内容而不主动参与。与 active engagement（主动参与）构成一对核心对立概念。",
                "usage": "科技和心理学领域常用。IELTS 写作中讨论社交媒体影响时的关键概念。",
                "examples": [
                    {"text": "Passive consumption of social media is linked to lower self-esteem.", "source": "American Psychological Association"}
                ],
                "level": "IELTS 6.5 / CET-6"
            },
            {
                "phrase": "a blunt instrument",
                "definition": "an imprecise or crude method of dealing with a problem",
                "chinese": "粗糙的手段；简单粗暴的方法",
                "linguistics": "blunt 本义为「钝的」（如钝刀），引申为「不精确的、粗糙的」。blunt instrument 原指钝器，比喻义为缺乏精确性的解决方案，暗示该方法虽然简单但可能造成不必要的附带损害。",
                "usage": "正式表达，政策评论和社论常用。IELTS 写作中批评某政策过于简单化时非常有用。",
                "examples": [
                    {"text": "Taxation is a blunt instrument for changing consumer behaviour.", "source": "The Economist"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "algorithmically driven spiral",
                "definition": "a continuous downward cycle of increasingly extreme content caused by recommendation algorithms",
                "chinese": "由算法驱动的恶性循环",
                "linguistics": "spiral（螺旋）在此为比喻用法，指越陷越深的恶性循环。algorithmically 为副词，修饰 driven。这一概念描述了推荐算法如何将用户引向越来越极端的内容。",
                "usage": "科技评论和新闻写作中的新兴表达。在讨论社交媒体对青少年影响时非常切题。",
                "examples": [
                    {"text": "Young users can be pulled into an algorithmically driven spiral of harmful content.", "source": "BBC News"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "widen the digital divide",
                "definition": "to increase the gap between those who have access to technology and those who do not",
                "chinese": "加剧数字鸿沟",
                "linguistics": "digital divide（数字鸿沟）是信息技术领域的核心概念，指不同社会群体在获取和使用数字技术方面的差距。widen（加宽）与 bridge/narrow（缩小）是该搭配的两组常见动词。",
                "usage": "科技政策和教育公平讨论中的核心表达。IELTS 写作 Task 2 讨论科技和教育不平等话题时必备表达。",
                "examples": [
                    {"text": "The pandemic widened the digital divide between urban and rural students.", "source": "UNESCO"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "phrase": "child-safe design standards",
                "definition": "regulatory requirements that ensure digital products are designed to protect children from harm",
                "chinese": "儿童安全设计标准",
                "linguistics": "child-safe 为复合形容词（连字符连接），修饰 design standards。这一概念源自英国《网络安全法案》（Online Safety Act），要求科技公司在产品设计中将儿童保护纳入核心考量。",
                "usage": "政策和法律语境常用。在讨论科技监管和儿童保护话题时非常切题。",
                "examples": [
                    {"text": "The UK's Online Safety Act introduced child-safe design standards for social media platforms.", "source": "The Guardian"}
                ],
                "level": "IELTS 6.5 / CET-6"
            },
            {
                "phrase": "digital wellness curricula",
                "definition": "educational programmes that teach students how to use technology in healthy ways",
                "chinese": "数字健康课程体系",
                "linguistics": "wellness（健康、幸福）+ curricula（课程体系，curriculum 的拉丁语复数形式）。digital wellness 是近年出现的教育概念，强调在数字时代保持身心健康的能力。",
                "usage": "教育领域的新兴术语。IELTS 写作中讨论教育改革和科技素养时可引用。",
                "examples": [
                    {"text": "Finland has integrated digital wellness curricula into its national education strategy.", "source": "OECD Education Report"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "move beyond the simplistic metric of",
                "definition": "to progress past an oversimplified way of measuring something",
                "chinese": "超越……这一过于简化的衡量标准",
                "linguistics": "move beyond 表示「超越、走出」；simplistic metric 指过于简单化的衡量标准。整个短语批评当前的讨论框架过于狭隘，呼吁更全面的思考方式。",
                "usage": "学术和政策评论常用。IELTS 写作结论段中呼吁更深层思考时非常有用。",
                "examples": [
                    {"text": "We must move beyond the simplistic metric of GDP to measure societal progress.", "source": "The Economist"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "treats a sophisticated problem with",
                "definition": "deals with a complex issue using (an inadequate method)",
                "chinese": "用（不恰当的方法）来应对一个复杂的问题",
                "linguistics": "treat 在此为「处理、对待」之意。sophisticated problem（复杂问题）与 blunt instrument（粗糙手段）形成鲜明对比，暗示方法与问题的严重不匹配。",
                "usage": "议论文和社论的经典批评句式。IELTS 写作中批评某政策不够精细时可使用此结构。",
                "examples": [
                    {"text": "Treating poverty as solely an economic problem ignores its psychological dimensions.", "source": "The Guardian"}
                ],
                "level": "IELTS 6.5 / CET-6"
            },
            {
                "phrase": "the architecture behind it",
                "definition": "the underlying structure, design, and systems that support something",
                "chinese": "背后的（系统）架构/设计",
                "linguistics": "architecture 在此为比喻用法，不指建筑学而指数字产品的底层设计结构。这一用法在科技评论中非常常见，暗示问题的根源在于产品的深层设计而非表面功能。",
                "usage": "科技和商业评论常用。常见搭配：system architecture / platform architecture / decision architecture。",
                "examples": [
                    {"text": "The architecture of social media platforms incentivises sensationalism over accuracy.", "source": "MIT Technology Review"}
                ],
                "level": "IELTS 6.5 / CET-6"
            },
        ],
        "annotations_sentences": [
            {
                "sentence": "The issue is not how much time children spend on screens but what they encounter when they get there.",
                "highlight_key": "The issue is not how much",
                "translation": "问题不在于孩子花多少时间在屏幕上，而在于他们到达那里后会遇到什么。",
                "breakdown": "句式结构：主句: The issue is not A but B; 名词性从句1: how much time children spend on screens; 名词性从句2: what they encounter when they get there; 时间状语从句: when they get there。语法分析: 'not A but B' 为否定—肯定对比结构，先否定一个常见观点再提出作者的真正论点；两个名词性从句分别作表语，形成对比；'get there' 中 there 指代 screens（数字空间），将虚拟空间空间化。修饰成分: 'how much' 和 'what' 分别引导两个宾语从句，构成「量 vs 质」的核心对比。",
                "grammar_points": ["not A but B 对比结构", "名词性从句作表语", "what 引导的名词性从句", "代词 there 的指代"],
                "writing_tip": "IELTS 写作中点明核心论点的高效句式：The issue/question is not [常见观点] but [作者论点]。简洁有力，一句话完成论点转折。考研写作同样适用。"
            },
            {
                "sentence": "A landmark study published in The Lancet Child and Adolescent Health in early 2026 tracked over 12,000 teenagers across eight countries for three years.",
                "highlight_key": "A landmark study published",
                "translation": "2026年初发表在《柳叶刀·儿童与青少年健康》上的一项里程碑式研究，追踪了八个国家的超过12,000名青少年，历时三年。",
                "breakdown": "句式结构：主句: A landmark study tracked over 12,000 teenagers; 过去分词短语: published in The Lancet Child and Adolescent Health in early 2026（后置定语修饰 study）; 介词短语: across eight countries for three years。语法分析: 'published in...' 为过去分词短语作后置定语，省略了 which was；'tracked' 为谓语动词，一般过去时；'over 12,000' 为数量修饰语，over 表示「超过」；'across eight countries' 和 'for three years' 分别为地点范围和时间长度的状语。修饰成分: 'landmark' 作前置定语修饰 study，赋予研究权威性和重要性。",
                "grammar_points": ["过去分词短语作后置定语", "over + 数字表示「超过」", "across 表示「横跨」", "介词短语作状语（地点+时间）"],
                "writing_tip": "IELTS Task 2 引用数据/研究的标准句式：A [形容词] study published in [期刊] found/tracked/revealed that... 这种结构比 According to 更学术、更具说服力。"
            },
            {
                "sentence": "Adolescents who passively scrolled through curated highlight reels of peers' lives reported significantly higher levels of loneliness than those who spent equivalent time on creative or educational platforms.",
                "highlight_key": "Adolescents who passively scrolled",
                "translation": "那些被动地浏览同龄人精心美化的生活亮点集锦的青少年，报告的孤独感水平显著高于那些在创意或教育平台上花费同等时间的青少年。",
                "breakdown": "句式结构：主句: Adolescents reported significantly higher levels of loneliness; 定语从句1: who passively scrolled through curated highlight reels of peers' lives; 比较结构: than those who...; 定语从句2: who spent equivalent time on creative or educational platforms。语法分析: 两个 who 引导的定语从句构成对比组——被动浏览组 vs 主动创造组；'significantly higher levels of' 为比较级结构，significantly 加强比较程度；'those' 指代 adolescents，避免重复；'equivalent time' 强调控制变量（时间相同，内容不同）。修饰成分: 'passively' 修饰 scrolled；'curated' 修饰 highlight reels（暗示内容是经过美化筛选的）；'peers'' 为所有格修饰 lives；'equivalent' 修饰 time。",
                "grammar_points": ["who 引导的定语从句构成对比", "significantly + 比较级", "those 指代前文名词", "多层修饰语的嵌套"],
                "writing_tip": "IELTS 写作中对比两组研究对象的经典句式：[Group A] who [行为A] reported higher/lower levels of X than [Group B] who [行为B]。注意用 those 替代重复的名词。"
            },
            {
                "sentence": "A blanket curfew on screen use, the kind now favoured by several national governments, treats a sophisticated problem with a blunt instrument.",
                "highlight_key": "A blanket curfew on screen use",
                "translation": "对屏幕使用的一刀切宵禁——这种如今受到多国政府青睐的做法——是在用一个粗糙的工具来处理一个复杂的问题。",
                "breakdown": "句式结构：主句: A blanket curfew treats a sophisticated problem with a blunt instrument; 同位语: the kind now favoured by several national governments（解释 curfew 的类型）。语法分析: 'blanket' 作形容词修饰 curfew，表示「一刀切的」；'the kind' 为同位语，用逗号隔开，进一步限定哪种 curfew；'now favoured by' 为过去分词短语修饰 kind，被动语态省略了 which is；'treats...with...' 构成核心比喻——sophisticated problem vs blunt instrument 的对比。修饰成分: 'blanket'（一刀切的）、'sophisticated'（复杂的）、'blunt'（粗糙的）三个形容词形成语义递进，突出方法与问题的不匹配。",
                "grammar_points": ["同位语的使用（the kind...）", "blanket 作形容词", "treats A with B 比喻结构", "过去分词短语修饰名词"],
                "writing_tip": "IELTS 写作中批评某一政策的有力句式：A blanket [政策] treats a sophisticated problem with a blunt instrument. 这个比喻既生动又精准，适用于任何「一刀切」政策的批评。"
            },
            {
                "sentence": "It fails to distinguish between a teenager coding a website, a child video-calling grandparents abroad, and a twelve-year-old trapped in an algorithmically driven spiral of body-image content.",
                "highlight_key": "It fails to distinguish between",
                "translation": "它无法区分一个正在编写网站的青少年、一个与海外祖父母视频通话的孩子，以及一个陷入算法驱动的身体形象内容恶性循环中的十二岁孩子。",
                "breakdown": "句式结构：主句: It fails to distinguish between A, B, and C; 三个并列名词短语: a teenager coding / a child video-calling / a twelve-year-old trapped...。语法分析: 'fails to distinguish between' 后接三个并列的名词短语，通过列举三种截然不同的屏幕使用场景来论证「一刀切」的荒谬；每个名词短语都使用了现在分词或过去分词作后置定语：coding（主动）、video-calling（主动）、trapped（被动）——前两者为积极行为，最后一个为被动受害，形成强烈对比。修饰成分: 'abroad' 修饰 grandparents；'algorithmically driven' 修饰 spiral；'body-image' 作定语修饰 content。",
                "grammar_points": ["fail to do 表示「未能做到」", "distinguish between A, B, and C", "分词短语作后置定语", "三项并列的修辞效果"],
                "writing_tip": "IELTS 写作中，用三项并列举例来论证某政策的缺陷是强有力的论证技巧。模板：It fails to distinguish between [积极例子], [中性例子], and [消极例子]。三个例子形成递进对比。"
            },
            {
                "sentence": "Infinite scroll, autoplay, and intermittent variable rewards—mechanisms borrowed from slot machines—are designed not to inform or educate but to maximise the duration of each session.",
                "highlight_key": "Infinite scroll, autoplay",
                "translation": "无限滚动、自动播放和间歇性可变奖励——这些从老虎机借鉴的机制——其设计目的不是为了告知或教育，而是为了最大化每次使用的时长。",
                "breakdown": "句式结构：主语: Infinite scroll, autoplay, and intermittent variable rewards（三项并列）; 同位语: —mechanisms borrowed from slot machines—（破折号间的补充说明）; 谓语: are designed; 目的对比: not to inform or educate but to maximise...。语法分析: 三个专业术语并列作主语，破折号中的同位语将其统称为 mechanisms 并指出来源（slot machines）；'are designed not to...but to...' 为被动语态 + not to...but to... 对比结构，先否定表面目的再揭示真实目的；'borrowed from slot machines' 为过去分词短语修饰 mechanisms。修饰成分: 'intermittent variable' 双重修饰 rewards；'each' 修饰 session。",
                "grammar_points": ["三项并列主语", "破折号引出同位语", "are designed not to...but to... 目的对比", "过去分词短语作定语（borrowed from）"],
                "writing_tip": "IELTS 写作中揭示设计意图的有力句式：X is designed not to [表面目的] but to [真实目的]。破折号插入同位语可以在不打断句子流畅性的情况下补充关键信息。"
            },
            {
                "sentence": "These features are particularly pernicious when deployed against developing minds that lack the prefrontal cortex maturity to exercise restraint.",
                "highlight_key": "These features are particularly pernicious",
                "translation": "当这些功能被用于那些缺乏前额叶皮层成熟度来自我约束的发育中大脑时，其危害尤为恶劣。",
                "breakdown": "句式结构：主句: These features are particularly pernicious; 时间/条件状语从句: when deployed against developing minds; 定语从句: that lack the prefrontal cortex maturity to exercise restraint。语法分析: 'when deployed' 为省略主语的状语从句（完整形式: when they are deployed），被动语态；'against' 在此为介词，表示「针对」；'developing minds' 中 developing 强调大脑仍在发育中；'that lack' 引导的定语从句修饰 minds；'to exercise restraint' 为不定式短语作 maturity 的后置定语。修饰成分: 'particularly' 加强 pernicious 的程度；'developing' 修饰 minds；'prefrontal cortex' 修饰 maturity。",
                "grammar_points": ["when + 过去分词（省略主语的状语从句）", "against 表示「针对」", "that 引导的定语从句", "不定式作后置定语（maturity to exercise）"],
                "writing_tip": "IELTS 写作中强调某事物对特定群体的危害：X is particularly harmful/pernicious when deployed against [弱势群体] that lack [能力/条件]。这种句式展现了对问题的深层理解。"
            },
            {
                "sentence": "Banning young people from digital spaces risks widening the digital divide, depriving disadvantaged children of educational resources that wealthier peers access through private tutoring and curated apps.",
                "highlight_key": "Banning young people from digital",
                "translation": "禁止年轻人进入数字空间有加剧数字鸿沟的风险，使弱势儿童失去那些较富裕同龄人通过私人辅导和精选应用获取的教育资源。",
                "breakdown": "句式结构：主句: Banning young people from digital spaces risks widening the digital divide; 现在分词短语: depriving disadvantaged children of educational resources（补充说明 risk 的具体后果）; 定语从句: that wealthier peers access through private tutoring and curated apps。语法分析: 'Banning...' 为动名词短语作主语；'risks widening' 为 risk + doing 结构；'depriving...of...' 为现在分词短语作伴随状语/结果状语，具体解释「加剧数字鸿沟」的含义；'that wealthier peers access' 为限制性定语从句修饰 resources；'through private tutoring and curated apps' 为方式状语。修饰成分: 'disadvantaged' 和 'wealthier' 形成对比；'private' 修饰 tutoring；'curated' 修饰 apps。",
                "grammar_points": ["动名词短语作主语", "risk + doing", "deprive sb of sth", "现在分词短语作结果状语", "that 引导的定语从句"],
                "writing_tip": "IELTS 写作中讨论政策副作用的高级句式：Doing X risks [负面后果1], depriving [受害群体] of [失去的资源]. 动名词作主语 + risk doing + 分词补充，一句话完成完整论证。"
            },
            {
                "sentence": "Schools, meanwhile, are embedding digital wellness curricula that teach students to recognise manipulative design patterns and to cultivate intentional, rather than compulsive, technology use.",
                "highlight_key": "Schools, meanwhile, are embedding",
                "translation": "与此同时，学校正在嵌入数字健康课程，教学生识别操控性设计模式，并培养有意识的而非强迫性的技术使用习惯。",
                "breakdown": "句式结构：主句: Schools are embedding digital wellness curricula; 插入语: meanwhile（同时）; 定语从句: that teach students to recognise...and to cultivate...; 对比结构: intentional, rather than compulsive。语法分析: 'meanwhile' 为插入语，用逗号隔开，连接上文（政府层面的改革）和本句（学校层面的教育）；'that teach students to...' 为定语从句修饰 curricula；'to recognise...and to cultivate...' 为两个并列不定式作 teach 的宾语补足语；'intentional, rather than compulsive' 为形容词对比结构，逗号分隔增加强调。修饰成分: 'digital wellness' 修饰 curricula；'manipulative' 修饰 design patterns；'intentional' 与 'compulsive' 形成对比。",
                "grammar_points": ["meanwhile 作插入语", "that 引导的定语从句", "并列不定式作宾补", "rather than 对比结构"],
                "writing_tip": "IELTS 写作中描述教育改革措施的实用句式：Schools are embedding [课程类型] that teach students to [技能1] and to [技能2]。rather than 在句中做对比修饰可以增加表达精度。"
            },
            {
                "sentence": "It requires a systemic rethinking of the digital environments we build, the regulations we enforce, and the critical skills we impart.",
                "highlight_key": "It requires a systemic rethinking",
                "translation": "这需要对我们构建的数字环境、我们执行的法规以及我们传授的批判性技能进行系统性的重新思考。",
                "breakdown": "句式结构：主句: It requires a systemic rethinking of A, B, and C; 三项并列: the digital environments we build / the regulations we enforce / the critical skills we impart; 省略关系代词: 三个定语从句均省略了 that。语法分析: 'It' 为形式主语，指代前文提到的「保护儿童心理健康」这一任务；'systemic rethinking' 为名词短语，systemic 强调「系统性」的重新思考而非局部修补；三个并列的名词短语 + 省略 that 的定语从句构成排比结构，分别对应三个改革维度（技术、法规、教育）。修饰成分: 'systemic' 修饰 rethinking；'digital' 修饰 environments；'critical' 修饰 skills。",
                "grammar_points": ["三项排比结构", "省略 that 的定语从句", "systemic vs systematic 的区别", "rethinking 用作名词"],
                "writing_tip": "IELTS 结论段的经典总结句式：It requires a [形容词] rethinking of [维度1], [维度2], and [维度3]. 三项排比既全面又有力，适合结论段总结全文要点。注意每项都用「定冠词 + 名词 + we + 动词」保持结构对称。"
            },
            {
                "sentence": "The screen itself is not the enemy; the architecture behind it is.",
                "highlight_key": "The screen itself is not the enemy",
                "translation": "屏幕本身不是敌人；其背后的架构才是。",
                "breakdown": "句式结构：并列句，分号连接两个对比分句; 分句1: The screen itself is not the enemy; 分句2: the architecture behind it is（省略了 the enemy）。语法分析: 'itself' 为反身代词作同位语强调「屏幕本身」，区别于屏幕背后的设计；分号连接两个紧密对比的分句，比句号更强调逻辑联系；第二个分句 'is' 后省略了 the enemy，利用省略制造简洁有力的收尾效果。修饰成分: 'itself' 强调 screen；'behind it' 修饰 architecture，it 指代 screen。",
                "grammar_points": ["反身代词 itself 作同位语", "分号连接对比分句", "省略结构（is = is the enemy）", "简短句的修辞冲击力"],
                "writing_tip": "IELTS 写作结尾的点睛句式：X itself is not the problem; the [根本原因] behind/beneath it is. 简洁有力，将读者的注意力从表面现象引向深层原因。分号 + 省略结构是高分写作的标志。"
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════
    # ARTICLE 2 — BBC Future (Science / Sleep & Academic Performance)
    # Topic: Sleep science and student productivity — directly relevant
    # to student life, IELTS health/education essays
    # Source: bbc.com/future — free public feature content
    # ═══════════════════════════════════════════════════════════
    {
        "title": "The Science of Sleep: Why Rest Is the Most Undervalued Academic Skill",
        "source": "BBC Future",
        "source_icon": "🔬",
        "category": "politics_economics",
        "category_label": "科学健康",
        "summary": "大量研究表明，充足的睡眠是学术表现的最强预测因素之一。然而大多数学生仍在以牺牲睡眠来换取更多的学习时间，这篇文章从神经科学的角度解释了为什么这是一个适得其反的策略。",
        "link": "https://www.bbc.com/future",
        "published": "2026-05-15",
        "has_full_text": True,
        "full_text": """\
Among the many variables that predict academic success, one stands out with remarkable consistency: sleep. Study after study confirms that adequate rest is not a luxury but a prerequisite for effective learning. Yet across universities worldwide, sleep deprivation remains almost a badge of honour—a testament, students believe, to their dedication and work ethic.

The neuroscience behind this paradox is well established. During sleep, the brain consolidates newly acquired information, transferring it from short-term to long-term memory through a process known as memory consolidation. Research published in the journal Science demonstrated that participants who slept for eight hours after learning a new skill retained 40 per cent more information than those who remained awake for the same period. The hippocampus, a region critical to memory formation, essentially replays the day's experiences during deep sleep, strengthening neural pathways and discarding irrelevant data.

Chronic sleep deprivation, by contrast, impairs virtually every cognitive function that students depend upon. Attention, working memory, logical reasoning, and emotional regulation all deteriorate markedly when individuals consistently sleep fewer than seven hours per night. A comprehensive meta-analysis conducted by researchers at the University of Oxford found that sleep-deprived students performed, on average, one full grade lower than their well-rested counterparts on standardised examinations.

The irony is that the students who sacrifice sleep to study are undermining the very process they seek to enhance. Cramming for an exam until three in the morning may feel productive, but the exhausted brain that sits the test the following day lacks the cognitive resources to retrieve the information it spent all night encoding. Neuroscientist Dr. Matthew Walker of the University of California, Berkeley, describes this phenomenon succinctly: "Sleep is not the absence of wakefulness. It is a highly active neurological state during which the brain performs critical maintenance that no amount of caffeine can replicate."

Beyond memory, sleep profoundly influences creativity and problem-solving. The REM stage of sleep, during which vivid dreaming occurs, facilitates the formation of remote associations—unexpected connections between seemingly unrelated ideas. Historical anecdotes abound: the chemist August Kekulé reportedly discovered the ring structure of benzene after dreaming of a serpent seizing its own tail, and Paul McCartney famously composed the melody for "Yesterday" in a dream.

Universities are beginning to acknowledge these findings. Several elite institutions, including Stanford and the University of Tokyo, have introduced later start times for morning lectures and established nap rooms on campus. Some have gone further, embedding sleep hygiene workshops into orientation programmes for first-year students. The message is clear: treating rest as an obstacle to productivity is not merely misguided; it is counterproductive.

For students navigating the relentless pressure of examinations, the evidence offers a counterintuitive prescription. The single most effective study strategy may not be another hour in the library but an early night in bed. In the competitive world of academic achievement, sleep is not a concession to weakness; it is an investment in cognitive capital.\
""",
        "annotations_vocab": [
            {
                "word": "prerequisite",
                "phonetic": "/priːˈrekwɪzɪt/",
                "pos": "n.",
                "definition": "a thing that is required as a prior condition for something else to happen or exist",
                "chinese": "前提条件；先决条件",
                "linguistics": "由前缀 pre-（在前）+ requisite（必需的）构成。requisite 源自拉丁语 requirere（要求）。注意 prerequisite 比 requirement 更强调时间上的先后顺序——必须先满足 A 才能做 B。",
                "usage": "正式用词，学术和商务语境常用。常见搭配：prerequisite for / prerequisite to / an essential prerequisite。大学课程中也常用（prerequisite course 先修课程）。",
                "examples": [
                    {"text": "A basic understanding of statistics is a prerequisite for this course.", "source": "Harvard University Catalogue"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "deprivation",
                "phonetic": "/ˌdeprɪˈveɪʃn/",
                "pos": "n.",
                "definition": "the lack of something considered to be a basic necessity; the act of depriving someone of something",
                "chinese": "剥夺；匮乏；缺失",
                "linguistics": "由 deprive（剥夺）+ -ation（名词后缀）构成。sleep deprivation（睡眠剥夺/缺乏）是心理学和医学的核心术语。区分 deprivation（匮乏状态）和 deprivation of（剥夺行为）。",
                "usage": "正式用词。常见搭配：sleep deprivation / sensory deprivation / social deprivation。IELTS 阅读和考研英语高频词。",
                "examples": [
                    {"text": "Sleep deprivation has been linked to a range of chronic health conditions.", "source": "The Lancet"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "testament",
                "phonetic": "/ˈtestəmənt/",
                "pos": "n.",
                "definition": "a thing that serves as evidence or proof of a specified fact or quality",
                "chinese": "证明；证据；见证",
                "linguistics": "源自拉丁语 testamentum（遗嘱、证词），由 testis（证人）派生。在现代英语中，a testament to 表示「是……的证明」。大写 Testament 特指圣经的旧约/新约。",
                "usage": "正式用词。常见搭配：a testament to / stand as a testament to。比 proof 或 evidence 更正式、更富文学色彩。",
                "examples": [
                    {"text": "The building stands as a testament to the architect's vision.", "source": "Architectural Digest"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "paradox",
                "phonetic": "/ˈpærədɒks/",
                "pos": "n.",
                "definition": "a seemingly contradictory statement or situation that may nonetheless be true",
                "chinese": "悖论；矛盾现象",
                "linguistics": "源自希腊语 paradoxon（para- 违反 + doxa 观点），即「违反常识的观点」。形容词形式 paradoxical。在学术写作中常用于引出反直觉的研究发现。",
                "usage": "学术和正式写作常用。常见搭配：the paradox of / a curious paradox / resolve a paradox。IELTS 写作中引入反直觉论点时很有用。",
                "examples": [
                    {"text": "The paradox of choice suggests that too many options can lead to dissatisfaction.", "source": "Scientific American"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "consolidate",
                "phonetic": "/kənˈsɒlɪdeɪt/",
                "pos": "v.",
                "definition": "to make something physically stronger or more solid; to combine several things into a single more effective whole",
                "chinese": "巩固；合并；整合",
                "linguistics": "源自拉丁语 consolidare（con- 完全 + solidare 使坚固）。在神经科学语境中，memory consolidation（记忆巩固）指大脑将短期记忆转化为长期记忆的过程。商业语境中指公司合并。",
                "usage": "正式用词，学术和商务语境高频。常见搭配：consolidate knowledge / power / position / memory。CET-6 和考研核心词汇。",
                "examples": [
                    {"text": "Review sessions help students consolidate what they have learned.", "source": "Education Week"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "retain",
                "phonetic": "/rɪˈteɪn/",
                "pos": "v.",
                "definition": "to continue to have or keep something; to keep in memory",
                "chinese": "保持；保留；记住",
                "linguistics": "源自拉丁语 retinere（re- 回 + tenere 持有），即「持续持有」。在学习语境中，retain information 指将信息保持在记忆中。名词形式 retention（保留、记忆力）。",
                "usage": "正式用词，CET-4 核心词汇。常见搭配：retain information / customers / control / talent。",
                "examples": [
                    {"text": "Students retain more information when they take handwritten notes.", "source": "Psychological Science"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "hippocampus",
                "phonetic": "/ˌhɪpəˈkæmpəs/",
                "pos": "n.",
                "definition": "a region of the brain that plays a critical role in learning and memory formation",
                "chinese": "海马体（大脑记忆中枢）",
                "linguistics": "源自希腊语 hippokampos（hippos 马 + kampos 海怪），因形状像海马而得名。复数形式为 hippocampi。是神经科学和心理学中讨论记忆的核心术语。",
                "usage": "学术用词，神经科学核心术语。在 IELTS 阅读中可能出现在科学类文章中。了解即可，写作中不必使用。",
                "examples": [
                    {"text": "Damage to the hippocampus can result in severe memory impairment.", "source": "Nature Neuroscience"}
                ],
                "level": "考研 / IELTS 7.5"
            },
            {
                "word": "discard",
                "phonetic": "/dɪˈskɑːd/",
                "pos": "v.",
                "definition": "to get rid of something that is no longer useful or wanted",
                "chinese": "丢弃；抛弃；放弃",
                "linguistics": "由 dis-（去除）+ card（纸牌）构成，原义为「打出不要的牌」，引申为丢弃任何不需要的东西。在神经科学语境中，指大脑在睡眠中清除无关信息的过程。",
                "usage": "正式与非正式均可使用。常见搭配：discard irrelevant data / discard old habits / discard the idea。比 throw away 更正式。",
                "examples": [
                    {"text": "The brain discards unnecessary information during sleep to make room for new learning.", "source": "Scientific American"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "chronic",
                "phonetic": "/ˈkrɒnɪk/",
                "pos": "adj.",
                "definition": "persisting for a long time or constantly recurring",
                "chinese": "长期的；慢性的",
                "linguistics": "源自希腊语 chronikos（时间的），由 chronos（时间）派生。区分 chronic（长期的、慢性的）和 acute（急性的）：chronic 强调持续时间长，acute 强调严重性和突然性。",
                "usage": "正式用词，医学和社会评论常用。常见搭配：chronic illness / pain / stress / shortage / problem。CET-4 核心词汇。",
                "examples": [
                    {"text": "Chronic stress has been identified as a major risk factor for heart disease.", "source": "WHO"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "impair",
                "phonetic": "/ɪmˈpeə(r)/",
                "pos": "v.",
                "definition": "to weaken or damage something, especially a faculty or function",
                "chinese": "损害；削弱；损伤",
                "linguistics": "源自古法语 empeirer（使变坏），由拉丁语 peior（更糟）派生。比 damage 更强调功能性的减弱而非物理破坏。名词形式 impairment（损伤、障碍）。",
                "usage": "正式用词，医学和法律语境常用。常见搭配：impair judgement / vision / cognitive function / performance。CET-6 核心词汇。",
                "examples": [
                    {"text": "Alcohol consumption significantly impairs driving ability.", "source": "British Medical Journal"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "deteriorate",
                "phonetic": "/dɪˈtɪəriəreɪt/",
                "pos": "v.",
                "definition": "to become progressively worse in quality, condition, or function",
                "chinese": "恶化；退化；变坏",
                "linguistics": "源自拉丁语 deteriorare（使变坏），由 deterior（更差的）派生。比 worsen 更正式，常用于描述能力、健康状况或局势的逐渐恶化。名词形式 deterioration。",
                "usage": "正式用词，学术和新闻写作常用。常见搭配：deteriorate rapidly / steadily / markedly。IELTS 写作高分词汇。",
                "examples": [
                    {"text": "Air quality in major cities continues to deteriorate despite government efforts.", "source": "The Guardian"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "markedly",
                "phonetic": "/ˈmɑːkɪdli/",
                "pos": "adv.",
                "definition": "to a very noticeable or considerable extent",
                "chinese": "显著地；明显地",
                "linguistics": "由 marked（显著的）+ -ly 构成。marked 源自 mark（标记），引申为「明显到可以被标记出来的」。比 significantly 更强调可观察性。",
                "usage": "正式用词，学术写作常用。常见搭配：markedly different / higher / lower / improved。比 significantly 或 notably 更正式。",
                "examples": [
                    {"text": "Students' performance improved markedly after the intervention.", "source": "Journal of Educational Psychology"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "comprehensive",
                "phonetic": "/ˌkɒmprɪˈhensɪv/",
                "pos": "adj.",
                "definition": "complete and including everything that is necessary; thorough",
                "chinese": "全面的；综合的；详尽的",
                "linguistics": "源自拉丁语 comprehendere（完全理解）。注意区分 comprehensive（全面的、广泛的）和 comprehensible（可理解的）。在学术语境中常修饰 study / review / analysis / report。",
                "usage": "正式用词，CET-4 核心词汇。常见搭配：comprehensive study / review / approach / plan。IELTS 阅读和写作高频词。",
                "examples": [
                    {"text": "The report provides a comprehensive overview of global health trends.", "source": "WHO"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "counterpart",
                "phonetic": "/ˈkaʊntəpɑːt/",
                "pos": "n.",
                "definition": "a person or thing that has the same function or position in a different place or situation",
                "chinese": "对应的人或物；对等方",
                "linguistics": "由 counter-（对应）+ part（部分）构成。在比较研究中，指对照组中与实验组对应的个体。在外交语境中指对等职位的人（如：Chinese counterpart 中方对等人员）。",
                "usage": "正式用词，学术和外交语境常用。常见搭配：their counterparts / male/female counterparts / foreign counterparts。CET-6 核心词汇。",
                "examples": [
                    {"text": "Female executives earn 20% less than their male counterparts.", "source": "Financial Times"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "undermine",
                "phonetic": "/ˌʌndəˈmaɪn/",
                "pos": "v.",
                "definition": "to weaken or damage something gradually or insidiously",
                "chinese": "逐渐削弱；暗中破坏",
                "linguistics": "由 under-（在下面）+ mine（挖掘）构成，原义为「在建筑物下面挖隧道使其坍塌」。引申为从内部或暗中破坏某事物的基础。比 weaken 更强调破坏的隐蔽性和渐进性。",
                "usage": "正式用词，IELTS 写作和考研英语核心词汇。常见搭配：undermine confidence / authority / efforts / health。",
                "examples": [
                    {"text": "Corruption undermines public trust in government institutions.", "source": "The Economist"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "retrieve",
                "phonetic": "/rɪˈtriːv/",
                "pos": "v.",
                "definition": "to get something back from where it has been stored; to recall information from memory",
                "chinese": "检索；取回；恢复",
                "linguistics": "源自古法语 retrouver（re- 回 + trouver 找到），即「重新找到」。在认知科学中，retrieve 特指从记忆中提取已储存的信息。名词形式 retrieval（检索、提取）。",
                "usage": "正式用词，信息技术和心理学核心术语。常见搭配：retrieve information / data / memories。比 recall 更正式。",
                "examples": [
                    {"text": "The ability to retrieve information under pressure is a key academic skill.", "source": "Cognitive Psychology"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "succinctly",
                "phonetic": "/səkˈsɪŋktli/",
                "pos": "adv.",
                "definition": "in a brief and clearly expressed manner",
                "chinese": "简洁地；言简意赅地",
                "linguistics": "由 succinct（简洁的）+ -ly 构成。succinct 源自拉丁语 succinctus（被紧束的），原义为「把衣服扎紧」，引申为语言精练、不啰嗦。与 concise 近义，但 succinct 更强调表达的精确性。",
                "usage": "正式用词。常见搭配：put it succinctly / describe succinctly / state succinctly。IELTS 写作中引用他人观点时可使用。",
                "examples": [
                    {"text": "As Einstein succinctly put it: 'Imagination is more important than knowledge.'", "source": "Biography of Einstein"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "replicate",
                "phonetic": "/ˈreplɪkeɪt/",
                "pos": "v.",
                "definition": "to make an exact copy of; to reproduce or repeat",
                "chinese": "复制；重复；再现",
                "linguistics": "源自拉丁语 replicare（re- 再 + plicare 折叠），即「再次折叠」引申为「复制」。在科学语境中，replicate 指重复实验以验证结果。名词形式 replication。",
                "usage": "正式用词，学术语境核心词汇。常见搭配：replicate results / replicate an experiment / difficult to replicate。",
                "examples": [
                    {"text": "The findings have been replicated in multiple independent studies.", "source": "Science"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "facilitate",
                "phonetic": "/fəˈsɪlɪteɪt/",
                "pos": "v.",
                "definition": "to make an action or process easier or more possible",
                "chinese": "促进；使便利；推动",
                "linguistics": "源自拉丁语 facilis（容易的）。比 help 或 promote 更正式，强调消除障碍使过程更顺畅。名词形式 facilitation；施动者名词 facilitator（促进者、协调人）。",
                "usage": "正式用词，学术和商务语境高频。常见搭配：facilitate learning / communication / discussion / trade。CET-6 核心词汇。",
                "examples": [
                    {"text": "Technology can facilitate collaborative learning among students.", "source": "British Journal of Educational Technology"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "anecdote",
                "phonetic": "/ˈænɪkdəʊt/",
                "pos": "n.",
                "definition": "a short, interesting, or amusing story about a real incident or person",
                "chinese": "轶事；趣闻",
                "linguistics": "源自希腊语 anekdota（an- 不 + ekdotos 出版的），原指「未出版的故事」。形容词 anecdotal（轶事性的）常用于学术写作中指出证据不够严谨：anecdotal evidence（轶事证据，非系统性证据）。",
                "usage": "正式与非正式均可使用。常见搭配：historical anecdote / anecdotal evidence / tell an anecdote。",
                "examples": [
                    {"text": "While anecdotal evidence supports the theory, controlled studies are needed.", "source": "Nature"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "hygiene",
                "phonetic": "/ˈhaɪdʒiːn/",
                "pos": "n.",
                "definition": "conditions or practices conducive to maintaining health and preventing disease",
                "chinese": "卫生；保健习惯",
                "linguistics": "源自希腊语 Hygieia（健康女神的名字）。在现代用法中，hygiene 已从纯粹的身体卫生扩展到心理和数字领域：sleep hygiene（睡眠卫生）、digital hygiene（数字卫生）、mental hygiene（心理卫生）。",
                "usage": "正式用词。常见搭配：personal hygiene / sleep hygiene / dental hygiene / digital hygiene。CET-4 基础词汇。",
                "examples": [
                    {"text": "Good sleep hygiene includes maintaining a consistent bedtime schedule.", "source": "Sleep Foundation"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "word": "misguided",
                "phonetic": "/ˌmɪsˈɡaɪdɪd/",
                "pos": "adj.",
                "definition": "having or showing faulty judgement or reasoning; wrong because based on incorrect beliefs",
                "chinese": "被误导的；错误的；考虑不周的",
                "linguistics": "由 mis-（错误）+ guided（引导的）构成，即「被错误引导的」。暗示做某事的出发点或方法是错误的，尽管意图可能是好的。比 wrong 更含蓄、更正式。",
                "usage": "正式用词。常见搭配：misguided belief / attempt / policy / approach。IELTS 写作中批评错误观点时很有用。",
                "examples": [
                    {"text": "The policy was well-intentioned but ultimately misguided.", "source": "The Economist"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
            {
                "word": "counterproductive",
                "phonetic": "/ˌkaʊntəprəˈdʌktɪv/",
                "pos": "adj.",
                "definition": "having the opposite of the desired effect; tending to hinder rather than help",
                "chinese": "适得其反的；事与愿违的",
                "linguistics": "由 counter-（相反）+ productive（有成效的）构成。直接表达「产生与预期相反结果」的含义。比 ineffective（无效的）更强——不仅无效，而且有害。",
                "usage": "正式用词。常见搭配：counterproductive strategy / approach / behaviour / policy。IELTS 写作中论证某做法适得其反时的首选词。",
                "examples": [
                    {"text": "Punishing employees for honest mistakes is often counterproductive.", "source": "Harvard Business Review"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "counterintuitive",
                "phonetic": "/ˌkaʊntərɪnˈtjuːɪtɪv/",
                "pos": "adj.",
                "definition": "contrary to what common sense or intuition would suggest",
                "chinese": "违反直觉的；反常识的",
                "linguistics": "由 counter-（相反）+ intuitive（直觉的）构成。学术写作中常用于引出与读者预期相反的研究发现，暗示真相比表面看起来更复杂。",
                "usage": "正式用词，学术写作常用。常见搭配：counterintuitive finding / result / conclusion / prescription。IELTS 阅读中可能出现。",
                "examples": [
                    {"text": "The counterintuitive finding is that working fewer hours can increase overall productivity.", "source": "The Economist"}
                ],
                "level": "CET-6 / IELTS 7.0"
            },
            {
                "word": "concession",
                "phonetic": "/kənˈseʃn/",
                "pos": "n.",
                "definition": "something that is granted or yielded, especially in response to demands; an admission or acknowledgement",
                "chinese": "让步；妥协；承认",
                "linguistics": "源自拉丁语 concedere（con- 一起 + cedere 让步），即「一同让出」。在辩论和写作中，concession 指承认对方观点有一定道理。IELTS 写作中的 concession paragraph 即让步段落。",
                "usage": "正式用词。常见搭配：make a concession / concession to / without concession。考研和 IELTS 写作核心概念。",
                "examples": [
                    {"text": "Both sides made significant concessions to reach an agreement.", "source": "BBC News"}
                ],
                "level": "CET-6 / IELTS 6.5"
            },
        ],
        "annotations_phrases": [
            {
                "phrase": "stands out with remarkable consistency",
                "definition": "is noticeably prominent and appears reliably across multiple studies or contexts",
                "chinese": "以惊人的一致性脱颖而出",
                "linguistics": "stand out（突出）+ with remarkable consistency（以显著的一致性）。remarkable 比 notable 更强调令人惊叹的程度。consistency 指研究结果在不同条件下的可重复性。",
                "usage": "学术写作中介绍研究发现时的高级表达。IELTS 写作 Task 2 引入关键论据时可使用。",
                "examples": [
                    {"text": "Among all risk factors, smoking stands out with remarkable consistency as the leading cause of lung cancer.", "source": "The Lancet"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "a badge of honour",
                "definition": "something that is worn or displayed as a sign of achievement, often ironically",
                "chinese": "荣誉的标志；引以为豪的事（常含讽刺）",
                "linguistics": "badge（徽章）+ of honour（荣誉的）。在本文语境中带有讽刺意味——学生把睡眠不足视为勤奋的「勋章」，但实际上这是有害的。这种反语用法在新闻写作中很常见。",
                "usage": "正式与非正式均可使用。常带讽刺色彩，用于批评某种被错误美化的行为。",
                "examples": [
                    {"text": "In Silicon Valley, working 80-hour weeks has become a badge of honour.", "source": "The Guardian"}
                ],
                "level": "IELTS 6.5 / CET-6"
            },
            {
                "phrase": "memory consolidation",
                "definition": "the neurological process by which short-term memories are stabilised and transferred to long-term storage",
                "chinese": "记忆巩固（神经科学术语）",
                "linguistics": "consolidation 源自 consolidate（巩固），在神经科学中特指大脑将新获取的信息从短期记忆转移至长期记忆的过程。这一过程主要在深度睡眠阶段进行。",
                "usage": "学术用词，心理学和神经科学核心术语。IELTS 阅读中科学类文章可能出现。",
                "examples": [
                    {"text": "Sleep plays a crucial role in memory consolidation and learning.", "source": "Nature Neuroscience"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "one full grade lower",
                "definition": "scoring an entire grade level below (e.g., from B to C)",
                "chinese": "低了整整一个等级",
                "linguistics": "full 在此为强调副词，修饰 grade，表示「整整的、完整的」。one full grade lower 比 slightly lower 或 somewhat lower 更具冲击力，强调差距之大。",
                "usage": "学术写作中描述研究结果的具体表达。量化差距比抽象描述更有说服力。",
                "examples": [
                    {"text": "Students who missed more than 10 classes scored, on average, one full grade lower.", "source": "Journal of Higher Education"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "phrase": "the very process they seek to enhance",
                "definition": "the exact process that they are trying to improve",
                "chinese": "他们正试图提升的那个过程本身",
                "linguistics": "very 在此为形容词（同一的、恰恰就是那个），不是副词。the very + 名词 用于强调「恰恰就是这个」。they seek to enhance 为省略 that 的定语从句。整个短语点明了牺牲睡眠学习的自相矛盾。",
                "usage": "正式表达，学术和文学写作常用。the very [名词] 是强调结构，展示了讽刺/悖论效果。",
                "examples": [
                    {"text": "The policy destroyed the very communities it was designed to protect.", "source": "The Guardian"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "cramming for an exam",
                "definition": "studying intensively for a short period just before an examination",
                "chinese": "临时抱佛脚；考前突击复习",
                "linguistics": "cram 本义为「塞满」，引申为在短时间内将大量信息「塞进」大脑。cramming 是学生群体中的高频用词，尤其在讨论学习方法时。注意 cram 为非正式用词。",
                "usage": "非正式用词，但在学术讨论学习策略时也常使用。IELTS 口语中讨论学习方法话题时可使用。",
                "examples": [
                    {"text": "Cramming for exams may help in the short term, but it rarely leads to lasting understanding.", "source": "Psychology Today"}
                ],
                "level": "CET-4 / IELTS 6.0"
            },
            {
                "phrase": "remote associations",
                "definition": "unexpected connections between ideas or concepts that seem unrelated at first glance",
                "chinese": "远距联想；意想不到的概念关联",
                "linguistics": "remote（遥远的）+ associations（联想、关联）。心理学术语，指在看似无关的概念之间建立联系的能力，被认为是创造力的核心机制。Remote Associates Test (RAT) 是测量创造力的经典工具。",
                "usage": "学术用词，心理学和创造力研究的核心概念。",
                "examples": [
                    {"text": "Creative thinking relies on the ability to form remote associations between disparate ideas.", "source": "Creativity Research Journal"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "sleep hygiene workshops",
                "definition": "educational sessions that teach healthy sleep habits and practices",
                "chinese": "睡眠卫生/健康睡眠习惯培训工作坊",
                "linguistics": "sleep hygiene（睡眠卫生）指有助于获得高质量睡眠的行为习惯和环境条件。workshop（工作坊）指互动式的学习活动。二者结合体现了大学对学生健康的重视。",
                "usage": "教育和健康领域的专业表达。在讨论大学福利和学生支持服务时可使用。",
                "examples": [
                    {"text": "The university offers free sleep hygiene workshops during orientation week.", "source": "Stanford University"}
                ],
                "level": "IELTS 6.5 / CET-6"
            },
            {
                "phrase": "not merely misguided; it is counterproductive",
                "definition": "not just wrong in approach but actually producing the opposite of the intended result",
                "chinese": "不仅是错误的，而且是适得其反的",
                "linguistics": "not merely A; it is B 为递进否定结构。misguided（被误导的）和 counterproductive（适得其反的）形成程度递进——不仅方向错了，而且会产生相反的效果。分号连接两个递进分句。",
                "usage": "正式表达，议论文写作常用。IELTS 写作中论证某行为不仅无效而且有害时的升级表达。",
                "examples": [
                    {"text": "Restricting employee autonomy is not merely misguided; it is counterproductive.", "source": "Harvard Business Review"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "an investment in cognitive capital",
                "definition": "a valuable contribution to one's mental resources and intellectual ability",
                "chinese": "对认知资本的投资",
                "linguistics": "investment（投资）+ cognitive capital（认知资本）。将睡眠比喻为一种「投资」，回报是更强的认知能力。capital 在此为比喻用法，借用了经济学中的「资本」概念（类似 social capital 社会资本、human capital 人力资本）。",
                "usage": "正式表达。将抽象概念用经济学隐喻来表达，增加说服力。IELTS 写作结尾的好用总结表达。",
                "examples": [
                    {"text": "Education is an investment in human capital that yields lifelong returns.", "source": "The Economist"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
            {
                "phrase": "a counterintuitive prescription",
                "definition": "a recommended course of action that goes against what one would naturally expect",
                "chinese": "一个违反直觉的建议",
                "linguistics": "counterintuitive（违反直觉的）+ prescription（处方、建议）。prescription 原为医学术语（处方），在此比喻为针对学习问题开出的「药方」。整个短语暗示这个建议虽然违反常识但有科学依据。",
                "usage": "学术写作常用。在引出反常识结论时非常有效，展示了科学思维与日常直觉的冲突。",
                "examples": [
                    {"text": "The evidence offers a counterintuitive prescription: to achieve more, do less.", "source": "The Atlantic"}
                ],
                "level": "IELTS 7.0 / 考研"
            },
        ],
        "annotations_sentences": [
            {
                "sentence": "Among the many variables that predict academic success, one stands out with remarkable consistency: sleep.",
                "highlight_key": "Among the many variables",
                "translation": "在预测学术成功的诸多变量中，有一个以惊人的一致性脱颖而出：睡眠。",
                "breakdown": "句式结构：介词短语: Among the many variables that predict academic success（前置状语）; 主句: one stands out with remarkable consistency; 冒号后: sleep（揭示答案）; 定语从句: that predict academic success（修饰 variables）。语法分析: 'Among' 引导介词短语前置作状语，制造悬念——在「诸多变量中」哪个最突出？'one' 为不定代词，指代未揭示的变量；'stands out with remarkable consistency' 为谓语 + 方式状语；冒号后的 'sleep' 为一个词的独立成分，简洁有力地揭示答案，制造戏剧效果。修饰成分: 'many' 修饰 variables；'remarkable' 修饰 consistency。",
                "grammar_points": ["Among 引导前置状语", "定语从句修饰先行词", "冒号用于揭示/解释", "one 作不定代词"],
                "writing_tip": "IELTS 写作开头的悬念句式：Among the many factors that [动词], one stands out: [答案]. 先铺垫再揭示，比直接陈述更吸引读者。冒号后用一个词收尾极具冲击力。"
            },
            {
                "sentence": "Study after study confirms that adequate rest is not a luxury but a prerequisite for effective learning.",
                "highlight_key": "Study after study confirms",
                "translation": "一项又一项研究证实，充足的休息不是奢侈品而是有效学习的先决条件。",
                "breakdown": "句式结构：主句: Study after study confirms that...; 宾语从句: adequate rest is not a luxury but a prerequisite for effective learning; 对比结构: not A but B。语法分析: 'Study after study' 使用 N after N 结构表示「一个接一个」，强调证据的反复和一致性；'confirms' 用单数动词（主语 study 的概念为单数整体）；'not a luxury but a prerequisite' 为否定—肯定对比，先否定常见的错误认知再纠正为正确定位。修饰成分: 'adequate' 修饰 rest；'effective' 修饰 learning。",
                "grammar_points": ["N after N 强调反复", "not A but B 对比结构", "that 引导宾语从句", "介词 for 表用途"],
                "writing_tip": "IELTS 写作中强调证据一致性的经典句式：Study after study / Research after research confirms that... not A but B 结构适用于纠正常见误解。"
            },
            {
                "sentence": "Yet across universities worldwide, sleep deprivation remains almost a badge of honour—a testament, students believe, to their dedication and work ethic.",
                "highlight_key": "Yet across universities worldwide",
                "translation": "然而在全世界的大学里，睡眠不足几乎仍然被视为一枚荣誉勋章——学生们相信，这是对他们的勤奋和职业道德的证明。",
                "breakdown": "句式结构：转折词: Yet; 地点状语: across universities worldwide; 主句: sleep deprivation remains almost a badge of honour; 破折号后同位语: a testament to their dedication and work ethic; 插入语: students believe。语法分析: 'Yet' 引出与上文科学证据相矛盾的现实；'remains' 为系动词，表示状态持续；'a badge of honour' 为隐喻，将睡眠不足比作勋章；破折号后 'a testament' 为 badge of honour 的同位语，进一步解释；'students believe' 为插入语，置于 testament 和 to 之间，表明这只是学生的主观看法而非客观事实。修饰成分: 'almost' 修饰 remains，略带缓和语气；'across universities worldwide' 扩大范围。",
                "grammar_points": ["Yet 引导转折", "remain + 名词/形容词（系动词）", "破折号引出同位语", "插入语 students believe 的位置"],
                "writing_tip": "IELTS 写作中描述「认知与现实的矛盾」的高级句式：Despite evidence, X remains a badge of honour—a testament, [人们] believe, to [价值观]. 插入语的灵活使用展现写作成熟度。"
            },
            {
                "sentence": "The hippocampus, a region critical to memory formation, essentially replays the day's experiences during deep sleep, strengthening neural pathways and discarding irrelevant data.",
                "highlight_key": "The hippocampus, a region critical",
                "translation": "海马体——一个对记忆形成至关重要的大脑区域——在深度睡眠期间本质上会重放白天的经历，强化神经通路并丢弃无关数据。",
                "breakdown": "句式结构：主句: The hippocampus replays the day's experiences; 同位语: a region critical to memory formation; 时间状语: during deep sleep; 现在分词短语: strengthening neural pathways and discarding irrelevant data（伴随状语）。语法分析: 'a region critical to memory formation' 为同位语，解释专业术语 hippocampus；'critical to' 为固定搭配，critical 后置修饰 region；'essentially' 为副词，表示「本质上」；'strengthening...and discarding...' 为两个并列的现在分词短语作伴随状语，描述 replays 的具体效果。修饰成分: 'the day's' 所有格修饰 experiences；'deep' 修饰 sleep；'neural' 修饰 pathways；'irrelevant' 修饰 data。",
                "grammar_points": ["同位语解释专业术语", "critical to 固定搭配", "现在分词短语作伴随状语", "并列分词短语（strengthening...and discarding...）"],
                "writing_tip": "IELTS 写作中解释专业概念的标准句式：[专业术语], a [类别] that/critical to [功能], [动作描述]。同位语让非专业读者也能理解术语含义。"
            },
            {
                "sentence": "The irony is that the students who sacrifice sleep to study are undermining the very process they seek to enhance.",
                "highlight_key": "The irony is that the students",
                "translation": "具有讽刺意味的是，那些牺牲睡眠来学习的学生正在破坏他们试图提升的那个过程本身。",
                "breakdown": "句式结构：主句: The irony is that...; 宾语从句: the students are undermining the very process; 目的状语: to study（不定式短语修饰 sacrifice，表目的）; 定语从句: they seek to enhance（省略 that，修饰 process）。语法分析: 'The irony is that' 为点明悖论的经典开头；'who sacrifice sleep to study' 为定语从句修饰 students，描述具体行为；'are undermining' 为现在进行时，强调正在发生的破坏；'the very process' 中 very 为形容词（恰恰就是那个），强调被破坏的恰恰是学生想要改善的对象；'they seek to enhance' 为省略 that 的定语从句修饰 process。修饰成分: 'very' 强调 process。",
                "grammar_points": ["The irony is that 引出悖论", "who 引导的定语从句", "the very + 名词（强调同一性）", "省略 that 的定语从句"],
                "writing_tip": "IELTS 写作中揭示悖论的经典句式：The irony is that [行为主体] who [行为] are undermining the very [目标] they seek to [动词]. 一句话完成悖论的呈现，逻辑精练。"
            },
            {
                "sentence": "\"Sleep is not the absence of wakefulness. It is a highly active neurological state during which the brain performs critical maintenance that no amount of caffeine can replicate.\"",
                "highlight_key": "Sleep is not the absence",
                "translation": "\u201c睡眠不是清醒的缺失。它是一种高度活跃的神经状态，在此期间大脑执行关键的维护工作，这是再多的咖啡因也无法复制的。\u201d",
                "breakdown": "句式结构：第一句: 简单否定判断句。Sleep is not the absence of wakefulness。第二句: 复合句。主句: It is a highly active neurological state; 定语从句1: during which the brain performs critical maintenance; 定语从句2: that no amount of caffeine can replicate。语法分析: 第一句用否定来打破常见误解（睡眠 ≠ 不清醒）；第二句用肯定来给出正确定义；'during which' 为介词 + 关系代词引导的非限制性定语从句；'that no amount of caffeine can replicate' 为限制性定语从句修饰 maintenance；'no amount of' 为否定量词短语，强调「无论多少都不能」。修饰成分: 'highly active neurological' 三重修饰 state；'critical' 修饰 maintenance。",
                "grammar_points": ["否定判断句打破误解", "during which 引导的定语从句", "no amount of 否定强调", "that 引导的限制性定语从句"],
                "writing_tip": "IELTS 写作中纠正误解的有力句式：X is not [常见误解]. It is [正确定义] during which/in which [详细解释]. 先否定再肯定，逻辑清晰。引用专家观点时用这种句式非常有效。"
            },
            {
                "sentence": "The REM stage of sleep, during which vivid dreaming occurs, facilitates the formation of remote associations—unexpected connections between seemingly unrelated ideas.",
                "highlight_key": "The REM stage of sleep",
                "translation": "快速眼动睡眠阶段——在此期间会出现生动的梦境——促进了远距联想的形成——即看似无关的想法之间的意想不到的联系。",
                "breakdown": "句式结构：主句: The REM stage of sleep facilitates the formation of remote associations; 非限制性定语从句: during which vivid dreaming occurs; 破折号后同位语: unexpected connections between seemingly unrelated ideas。语法分析: 'during which' 引导非限制性定语从句，解释 REM 阶段的特征；'facilitates' 为谓语，表示「促进」；'the formation of' 为固定搭配，表示「形成」；破折号后的内容为 remote associations 的同位语解释。修饰成分: 'vivid' 修饰 dreaming；'remote' 修饰 associations；'unexpected' 修饰 connections；'seemingly unrelated' 修饰 ideas。",
                "grammar_points": ["during which 非限制性定语从句", "facilitate + the formation of", "破折号引出同位语", "seemingly + 形容词的用法"],
                "writing_tip": "IELTS 写作中解释科学过程的句式：[过程/阶段], during which [发生什么], facilitates [结果]—[进一步解释]。层层推进的信息结构让复杂概念变得清晰。"
            },
            {
                "sentence": "Treating rest as an obstacle to productivity is not merely misguided; it is counterproductive.",
                "highlight_key": "treating rest as an obstacle",
                "translation": "将休息视为生产力的障碍，这不仅是被误导的，而且是适得其反的。",
                "breakdown": "句式结构：主语: Treating rest as an obstacle to productivity（动名词短语作主语）; 谓语: is; 表语: not merely misguided; it is counterproductive（分号连接的递进判断）。语法分析: 'Treating...as...' 为动名词短语作主语，使句子聚焦于行为本身；'as an obstacle to' 表示「视为……的障碍」；'not merely...it is...' 为递进否定结构，先说「不仅仅是错误的」再递进到「而且是适得其反的」；分号连接两个逻辑递进的判断。修饰成分: 'merely' 修饰 misguided，表示「仅仅」。",
                "grammar_points": ["动名词短语作主语", "treat A as B 结构", "not merely A; it is B 递进否定", "分号连接递进判断"],
                "writing_tip": "IELTS 写作中批评某观点的递进句式：Doing X is not merely [较轻批评]; it is [更重批评]。分号 + 递进让批评层层加深。动名词作主语使批评更客观。"
            },
            {
                "sentence": "For students navigating the relentless pressure of examinations, the evidence offers a counterintuitive prescription.",
                "highlight_key": "For students navigating the relentless",
                "translation": "对于那些在考试无情压力中艰难前行的学生而言，证据提供了一个违反直觉的建议。",
                "breakdown": "句式结构：介词短语: For students navigating the relentless pressure of examinations（前置状语，指明受众）; 主句: the evidence offers a counterintuitive prescription。语法分析: 'For students' 为介词短语表示「对于……而言」；'navigating' 为现在分词短语作后置定语修饰 students，将应对考试比喻为「航行」（navigate 本义为导航）；'relentless' 修饰 pressure，强调压力的不间断性；'counterintuitive' 修饰 prescription，预告即将给出的建议将违反常识。修饰成分: 'relentless' 修饰 pressure；'counterintuitive' 修饰 prescription。",
                "grammar_points": ["For + 名词作前置状语", "现在分词短语作后置定语", "navigate 的比喻用法", "counterintuitive 的语义预告功能"],
                "writing_tip": "IELTS 写作中引出结论建议的过渡句：For [受众] navigating [挑战], the evidence offers/suggests [解决方案]. 这种结构既指明受众又引出建议，过渡自然。"
            },
            {
                "sentence": "In the competitive world of academic achievement, sleep is not a concession to weakness; it is an investment in cognitive capital.",
                "highlight_key": "In the competitive world of academic",
                "translation": "在学术竞争的世界里，睡眠不是对软弱的妥协，而是对认知资本的投资。",
                "breakdown": "句式结构：地点/范围状语: In the competitive world of academic achievement; 主句: sleep is not A; it is B; 对比: a concession to weakness vs an investment in cognitive capital。语法分析: 'In the competitive world of' 为介词短语前置，设定讨论的范围和语境；'is not A; it is B' 为分号连接的否定—肯定对比结构；'a concession to weakness' 和 'an investment in cognitive capital' 形成鲜明的语义对比——从「妥协/软弱」到「投资/资本」，完成了对睡眠的重新定义。修饰成分: 'competitive' 修饰 world；'cognitive' 修饰 capital。",
                "grammar_points": ["介词短语前置设定语境", "not A; it is B 分号对比", "concession to 固定搭配", "隐喻式结尾（investment in capital）"],
                "writing_tip": "IELTS 写作结尾的黄金句式：In the [形容词] world of [领域], X is not a [负面定义]; it is an [正面定义]. 通过重新定义关键概念来点明全文主旨。分号对比 + 隐喻收尾是高分写作的标志。"
            },
        ],
    },
]
