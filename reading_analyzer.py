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
    # ── CET-4/6 & IELTS 5.5–7.5: Common in everyday articles ──
    "crucial": {
        "pos": "adj.",
        "definition": "of great importance; critical",
        "chinese": "至关重要的",
        "phonetic": "/ˈkruː.ʃəl/",
        "examples": [
            {"text": "Early childhood education plays a crucial role in long-term development.", "source": "UNICEF Report, 2022"},
            {"text": "It is crucial that governments invest in renewable energy sources.", "source": "The Guardian, 2023"},
        ],
        "collocations": ["crucial role", "crucial factor", "crucial importance"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "significant": {
        "pos": "adj.",
        "definition": "sufficiently great or important to be worthy of attention",
        "chinese": "重大的，有意义的",
        "phonetic": "/sɪɡˈnɪf.ɪ.kənt/",
        "examples": [
            {"text": "The study found a significant correlation between sleep quality and productivity.", "source": "Nature, 2022"},
            {"text": "There has been a significant increase in online learning since 2020.", "source": "The Economist, 2021"},
        ],
        "collocations": ["significant impact", "significant difference", "significant improvement"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "demonstrate": {
        "pos": "v.",
        "definition": "clearly show the existence or truth of something by giving proof or evidence",
        "chinese": "证明，展示",
        "phonetic": "/ˈdem.ən.streɪt/",
        "examples": [
            {"text": "The experiment demonstrated that the new drug was effective.", "source": "The Lancet, 2023"},
            {"text": "These results demonstrate the need for further research.", "source": "Scientific American, 2022"},
        ],
        "collocations": ["clearly demonstrate", "demonstrate the ability", "demonstrate a link"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "substantial": {
        "pos": "adj.",
        "definition": "of considerable importance, size, or worth",
        "chinese": "大量的，实质性的",
        "phonetic": "/səbˈstæn.ʃəl/",
        "examples": [
            {"text": "The company made a substantial investment in artificial intelligence.", "source": "Financial Times, 2023"},
            {"text": "There is substantial evidence linking air pollution to respiratory disease.", "source": "The Lancet, 2022"},
        ],
        "collocations": ["substantial amount", "substantial evidence", "substantial growth"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "perceive": {
        "pos": "v.",
        "definition": "become aware or conscious of something; interpret or regard in a particular way",
        "chinese": "感知，认为",
        "phonetic": "/pəˈsiːv/",
        "examples": [
            {"text": "Many consumers perceive organic food as healthier, though evidence is mixed.", "source": "The New York Times, 2022"},
            {"text": "The policy was perceived as unfair by a large segment of the population.", "source": "BBC News, 2023"},
        ],
        "collocations": ["perceive as", "widely perceived", "perceive a threat"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "facilitate": {
        "pos": "v.",
        "definition": "make an action or process easy or easier",
        "chinese": "促进，使便利",
        "phonetic": "/fəˈsɪl.ɪ.teɪt/",
        "examples": [
            {"text": "Technology can facilitate communication between people across the globe.", "source": "Cambridge Dictionary"},
            {"text": "The new platform facilitates collaboration among remote teams.", "source": "Harvard Business Review, 2023"},
        ],
        "collocations": ["facilitate learning", "facilitate communication", "facilitate the process"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "comprehend": {
        "pos": "v.",
        "definition": "grasp mentally; understand",
        "chinese": "理解，领悟",
        "phonetic": "/ˌkɒm.prɪˈhend/",
        "examples": [
            {"text": "It is difficult to comprehend the scale of the environmental crisis.", "source": "The Guardian, 2023"},
            {"text": "Students need time to fully comprehend complex scientific concepts.", "source": "Nature, 2021"},
        ],
        "collocations": ["fully comprehend", "fail to comprehend", "difficult to comprehend"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "elaborate": {
        "pos": "v. / adj.",
        "definition": "(v.) develop or present in detail; (adj.) involving many carefully arranged parts; detailed and complicated",
        "chinese": "（动）详细阐述；（形）精心制作的，复杂的",
        "phonetic": "/ɪˈlæb.ər.ət/",
        "examples": [
            {"text": "Could you elaborate on your proposal for improving the system?", "source": "Cambridge Dictionary"},
            {"text": "The company devised an elaborate plan to restructure its operations.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["elaborate on", "elaborate plan", "elaborate system"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "controversy": {
        "pos": "n.",
        "definition": "prolonged public disagreement or heated discussion",
        "chinese": "争议，争论",
        "phonetic": "/ˈkɒn.trə.vɜː.si/",
        "examples": [
            {"text": "The new policy has sparked considerable controversy among educators.", "source": "The New York Times, 2023"},
            {"text": "The controversy surrounding data privacy shows no signs of abating.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["spark controversy", "controversy surrounding", "political controversy"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "phenomenon": {
        "pos": "n.",
        "definition": "a fact or situation that is observed to exist or happen, especially one whose cause is in question",
        "chinese": "现象",
        "phonetic": "/fɪˈnɒm.ɪ.nən/",
        "examples": [
            {"text": "Social media addiction is a growing phenomenon among teenagers.", "source": "The Atlantic, 2023"},
            {"text": "Scientists are still trying to explain this mysterious phenomenon.", "source": "Nature, 2022"},
        ],
        "collocations": ["natural phenomenon", "cultural phenomenon", "global phenomenon"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "ambiguous": {
        "pos": "adj.",
        "definition": "open to more than one interpretation; not having one obvious meaning",
        "chinese": "模糊的，有歧义的",
        "phonetic": "/æmˈbɪɡ.ju.əs/",
        "examples": [
            {"text": "The regulations are ambiguous and open to different interpretations.", "source": "The Economist, 2023"},
            {"text": "His response was deliberately ambiguous, leaving room for manoeuvre.", "source": "BBC News, 2022"},
        ],
        "collocations": ["ambiguous language", "morally ambiguous", "ambiguous results"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "inevitable": {
        "pos": "adj.",
        "definition": "certain to happen; unavoidable",
        "chinese": "不可避免的",
        "phonetic": "/ɪnˈev.ɪ.tə.bəl/",
        "examples": [
            {"text": "Some experts believe that a recession is inevitable given current trends.", "source": "Financial Times, 2023"},
            {"text": "Technological disruption of traditional industries is inevitable.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["inevitable consequence", "inevitable result", "seem inevitable"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "profound": {
        "pos": "adj.",
        "definition": "very great or intense; having deep meaning",
        "chinese": "深刻的，深远的",
        "phonetic": "/prəˈfaʊnd/",
        "examples": [
            {"text": "The internet has had a profound impact on how we access information.", "source": "The Economist, 2022"},
            {"text": "The loss of biodiversity could have profound consequences for ecosystems.", "source": "Nature, 2023"},
        ],
        "collocations": ["profound impact", "profound effect", "profound change"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "sustain": {
        "pos": "v.",
        "definition": "cause to continue for an extended period; maintain",
        "chinese": "维持，持续",
        "phonetic": "/səˈsteɪn/",
        "examples": [
            {"text": "It is difficult to sustain economic growth without investing in education.", "source": "World Bank Report, 2023"},
            {"text": "The charity relies on donations to sustain its programmes.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["sustain growth", "sustain development", "sustain interest"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "accumulate": {
        "pos": "v.",
        "definition": "gather together or acquire an increasing number or quantity of",
        "chinese": "积累，积聚",
        "phonetic": "/əˈkjuː.mjə.leɪt/",
        "examples": [
            {"text": "Over time, small habits accumulate into significant lifestyle changes.", "source": "Harvard Business Review, 2022"},
            {"text": "Plastic waste continues to accumulate in the world's oceans.", "source": "National Geographic, 2023"},
        ],
        "collocations": ["accumulate wealth", "accumulate evidence", "accumulate over time"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "integrate": {
        "pos": "v.",
        "definition": "combine one thing with another so that they become a whole",
        "chinese": "整合，融合",
        "phonetic": "/ˈɪn.tɪ.ɡreɪt/",
        "examples": [
            {"text": "Schools are finding new ways to integrate technology into the classroom.", "source": "The New York Times, 2023"},
            {"text": "The company plans to integrate the two platforms into a single system.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["integrate into", "fully integrate", "integrate with"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "exploit": {
        "pos": "v.",
        "definition": "make full use of a resource; use a situation unfairly for one's own advantage",
        "chinese": "利用，剥削",
        "phonetic": "/ɪkˈsplɔɪt/",
        "examples": [
            {"text": "Companies must not exploit workers in pursuit of higher profits.", "source": "The Guardian, 2023"},
            {"text": "Hackers can exploit software vulnerabilities to gain access to personal data.", "source": "MIT Technology Review, 2022"},
        ],
        "collocations": ["exploit resources", "exploit vulnerabilities", "exploit workers"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "allocate": {
        "pos": "v.",
        "definition": "distribute resources or duties for a particular purpose",
        "chinese": "分配，拨款",
        "phonetic": "/ˈæl.ə.keɪt/",
        "examples": [
            {"text": "The government has allocated additional funding for healthcare.", "source": "BBC News, 2023"},
            {"text": "Teams need to allocate time for both planning and execution.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["allocate resources", "allocate funds", "allocate time"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "implement": {
        "pos": "v.",
        "definition": "put a decision, plan, or agreement into effect",
        "chinese": "实施，执行",
        "phonetic": "/ˈɪm.plɪ.ment/",
        "examples": [
            {"text": "Several countries have implemented strict data protection laws.", "source": "The Economist, 2023"},
            {"text": "The school plans to implement a new curriculum next year.", "source": "BBC News, 2022"},
        ],
        "collocations": ["implement a policy", "implement changes", "implement a plan"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "undermine": {
        "pos": "v.",
        "definition": "lessen the effectiveness, power, or ability of, especially gradually or insidiously",
        "chinese": "破坏，削弱",
        "phonetic": "/ˌʌn.dəˈmaɪn/",
        "examples": [
            {"text": "Misinformation can undermine public trust in science.", "source": "Nature, 2022"},
            {"text": "Corruption undermines economic development and social stability.", "source": "World Bank Report, 2023"},
        ],
        "collocations": ["undermine confidence", "undermine trust", "undermine authority"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "stimulate": {
        "pos": "v.",
        "definition": "encourage or arouse interest or enthusiasm in; cause development or increased activity",
        "chinese": "刺激，促进",
        "phonetic": "/ˈstɪm.jə.leɪt/",
        "examples": [
            {"text": "Tax cuts are often used to stimulate economic growth.", "source": "The Economist, 2023"},
            {"text": "Reading widely can stimulate creativity and critical thinking.", "source": "Scientific American, 2022"},
        ],
        "collocations": ["stimulate growth", "stimulate demand", "stimulate innovation"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "distort": {
        "pos": "v.",
        "definition": "give a misleading or false account of; twist out of shape",
        "chinese": "歪曲，扭曲",
        "phonetic": "/dɪˈstɔːt/",
        "examples": [
            {"text": "Social media algorithms can distort our perception of reality.", "source": "The Atlantic, 2023"},
            {"text": "The report accused the media of distorting the facts.", "source": "BBC News, 2022"},
        ],
        "collocations": ["distort the truth", "distort reality", "distort the facts"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "acknowledge": {
        "pos": "v.",
        "definition": "accept or admit the existence or truth of",
        "chinese": "承认，认可",
        "phonetic": "/əkˈnɒl.ɪdʒ/",
        "examples": [
            {"text": "The company acknowledged that it had failed to protect customer data.", "source": "The Guardian, 2023"},
            {"text": "Scientists acknowledge that more research is needed in this area.", "source": "Nature, 2022"},
        ],
        "collocations": ["widely acknowledged", "acknowledge the fact", "acknowledge a problem"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "advocate": {
        "pos": "v. / n.",
        "definition": "(v.) publicly recommend or support; (n.) a person who publicly supports a particular cause",
        "chinese": "（动）提倡，主张；（名）倡导者",
        "phonetic": "/ˈæd.və.keɪt/",
        "examples": [
            {"text": "Health experts advocate regular exercise as a way to prevent chronic disease.", "source": "The Lancet, 2022"},
            {"text": "She is a strong advocate for equal access to education.", "source": "The New York Times, 2023"},
        ],
        "collocations": ["advocate for", "strongly advocate", "advocate a policy"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "enormous": {
        "pos": "adj.",
        "definition": "very large in size, quantity, or extent",
        "chinese": "巨大的，庞大的",
        "phonetic": "/ɪˈnɔː.məs/",
        "examples": [
            {"text": "The project required an enormous amount of investment and coordination.", "source": "Financial Times, 2023"},
            {"text": "Social media has had an enormous influence on political campaigns.", "source": "The Atlantic, 2022"},
        ],
        "collocations": ["enormous amount", "enormous pressure", "enormous potential"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "fundamental": {
        "pos": "adj.",
        "definition": "forming a necessary base or core; of central importance",
        "chinese": "基本的，根本的",
        "phonetic": "/ˌfʌn.dəˈmen.təl/",
        "examples": [
            {"text": "Access to clean water is a fundamental human right.", "source": "United Nations, 2022"},
            {"text": "There is a fundamental difference between correlation and causation.", "source": "Scientific American, 2023"},
        ],
        "collocations": ["fundamental change", "fundamental right", "fundamental question"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "perspective": {
        "pos": "n.",
        "definition": "a particular attitude toward or way of regarding something; a point of view",
        "chinese": "观点，视角",
        "phonetic": "/pəˈspek.tɪv/",
        "examples": [
            {"text": "Travelling broadens your perspective and challenges your assumptions.", "source": "The New York Times, 2022"},
            {"text": "From a historical perspective, this period was one of rapid transformation.", "source": "The Economist, 2023"},
        ],
        "collocations": ["from the perspective of", "global perspective", "new perspective"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "transparent": {
        "pos": "adj.",
        "definition": "easy to perceive or detect; open and honest, without secrets",
        "chinese": "透明的，公开的",
        "phonetic": "/trænsˈpær.ənt/",
        "examples": [
            {"text": "Governments must be transparent about how they use public funds.", "source": "The Guardian, 2023"},
            {"text": "The company pledged to be more transparent about its data collection practices.", "source": "BBC News, 2022"},
        ],
        "collocations": ["transparent process", "fully transparent", "transparent governance"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "vulnerable": {
        "pos": "adj.",
        "definition": "exposed to the possibility of being attacked or harmed, either physically or emotionally",
        "chinese": "脆弱的，易受伤的",
        "phonetic": "/ˈvʌl.nər.ə.bəl/",
        "examples": [
            {"text": "Children and the elderly are particularly vulnerable to the effects of heatwaves.", "source": "The Lancet, 2023"},
            {"text": "Small businesses are especially vulnerable during economic downturns.", "source": "The Economist, 2022"},
        ],
        "collocations": ["vulnerable to", "vulnerable groups", "particularly vulnerable"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "trivial": {
        "pos": "adj.",
        "definition": "of little value or importance",
        "chinese": "琐碎的，不重要的",
        "phonetic": "/ˈtrɪv.i.əl/",
        "examples": [
            {"text": "What may seem trivial to adults can be deeply important to children.", "source": "Scientific American, 2022"},
            {"text": "The issue is far from trivial—it affects millions of people.", "source": "The Guardian, 2023"},
        ],
        "collocations": ["trivial matter", "far from trivial", "trivial detail"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "skeptical": {
        "pos": "adj.",
        "definition": "not easily convinced; having doubts or reservations",
        "chinese": "怀疑的",
        "phonetic": "/ˈskep.tɪ.kəl/",
        "examples": [
            {"text": "Many scientists remain skeptical about the claims made in the study.", "source": "Nature, 2023"},
            {"text": "Voters are increasingly skeptical of politicians' promises.", "source": "The Economist, 2022"},
        ],
        "collocations": ["remain skeptical", "deeply skeptical", "skeptical about"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "resilient": {
        "pos": "adj.",
        "definition": "able to withstand or recover quickly from difficult conditions",
        "chinese": "有弹性的，适应力强的",
        "phonetic": "/rɪˈzɪl.i.ənt/",
        "examples": [
            {"text": "Communities that invest in infrastructure tend to be more resilient to natural disasters.", "source": "World Bank Report, 2023"},
            {"text": "The economy has proved remarkably resilient despite global headwinds.", "source": "Financial Times, 2023"},
        ],
        "collocations": ["resilient economy", "resilient communities", "highly resilient"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "innovative": {
        "pos": "adj.",
        "definition": "featuring new methods; advanced and original",
        "chinese": "创新的",
        "phonetic": "/ˈɪn.ə.veɪ.tɪv/",
        "examples": [
            {"text": "The company is known for its innovative approach to product design.", "source": "Harvard Business Review, 2023"},
            {"text": "Innovative teaching methods can dramatically improve student engagement.", "source": "The New York Times, 2022"},
        ],
        "collocations": ["innovative approach", "innovative solution", "innovative technology"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "collaborate": {
        "pos": "v.",
        "definition": "work jointly on an activity or project",
        "chinese": "合作，协作",
        "phonetic": "/kəˈlæb.ə.reɪt/",
        "examples": [
            {"text": "Researchers from different countries collaborated on the vaccine development.", "source": "The Lancet, 2021"},
            {"text": "The two companies will collaborate to develop new renewable energy solutions.", "source": "Financial Times, 2023"},
        ],
        "collocations": ["collaborate with", "collaborate on", "collaborate closely"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "authentic": {
        "pos": "adj.",
        "definition": "of undisputed origin; genuine; true to one's own personality or character",
        "chinese": "真实的，可靠的",
        "phonetic": "/ɔːˈθen.tɪk/",
        "examples": [
            {"text": "Consumers increasingly value authentic brands that align with their beliefs.", "source": "Harvard Business Review, 2023"},
            {"text": "The museum displays authentic artefacts from the ancient civilisation.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["authentic experience", "authentic voice", "authentic leadership"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "autonomous": {
        "pos": "adj.",
        "definition": "having the freedom to act independently; self-governing",
        "chinese": "自治的，自主的",
        "phonetic": "/ɔːˈtɒn.ə.məs/",
        "examples": [
            {"text": "Autonomous vehicles could revolutionise the transportation industry.", "source": "MIT Technology Review, 2023"},
            {"text": "The university operates as an autonomous institution free from government control.", "source": "The Economist, 2022"},
        ],
        "collocations": ["autonomous vehicle", "autonomous region", "fully autonomous"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "indispensable": {
        "pos": "adj.",
        "definition": "absolutely necessary; essential",
        "chinese": "不可或缺的",
        "phonetic": "/ˌɪn.dɪˈspen.sə.bəl/",
        "examples": [
            {"text": "The internet has become an indispensable tool for education and commerce.", "source": "The Economist, 2023"},
            {"text": "Good communication skills are indispensable in the modern workplace.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["indispensable part", "indispensable tool", "absolutely indispensable"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "deteriorate": {
        "pos": "v.",
        "definition": "become progressively worse",
        "chinese": "恶化，变坏",
        "phonetic": "/dɪˈtɪə.ri.ə.reɪt/",
        "examples": [
            {"text": "Air quality in major cities continues to deteriorate at an alarming rate.", "source": "The Guardian, 2023"},
            {"text": "Relations between the two countries have deteriorated sharply.", "source": "Foreign Affairs, 2022"},
        ],
        "collocations": ["deteriorate rapidly", "deteriorate further", "conditions deteriorate"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "flourish": {
        "pos": "v.",
        "definition": "grow or develop in a healthy or vigorous way; thrive",
        "chinese": "繁荣，茂盛",
        "phonetic": "/ˈflʌr.ɪʃ/",
        "examples": [
            {"text": "Small businesses flourish when given access to affordable credit.", "source": "The Economist, 2023"},
            {"text": "Arts and culture flourished during the Renaissance period.", "source": "Oxford Advanced Learner's Dictionary"},
        ],
        "collocations": ["flourish in", "continue to flourish", "flourish under"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "encompass": {
        "pos": "v.",
        "definition": "surround and have or hold within; include comprehensively",
        "chinese": "包含，涵盖",
        "phonetic": "/ɪnˈkʌm.pəs/",
        "examples": [
            {"text": "The curriculum encompasses subjects ranging from science to the humanities.", "source": "The New York Times, 2022"},
            {"text": "The report encompasses data from over 50 countries.", "source": "World Bank Report, 2023"},
        ],
        "collocations": ["encompass a range of", "encompass all aspects", "encompass both"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "supplement": {
        "pos": "v. / n.",
        "definition": "(v.) add an extra element to; (n.) something added to complete or enhance",
        "chinese": "（动）补充；（名）补充物",
        "phonetic": "/ˈsʌp.lɪ.ment/",
        "examples": [
            {"text": "Many teachers supplement textbooks with online resources.", "source": "BBC News, 2023"},
            {"text": "Dietary supplements are a multi-billion-dollar industry.", "source": "The New York Times, 2022"},
        ],
        "collocations": ["supplement income", "dietary supplement", "supplement with"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "erode": {
        "pos": "v.",
        "definition": "gradually destroy or diminish",
        "chinese": "侵蚀，逐渐削弱",
        "phonetic": "/ɪˈrəʊd/",
        "examples": [
            {"text": "Public trust in institutions has been steadily eroded by scandals.", "source": "The Atlantic, 2023"},
            {"text": "Inflation erodes the purchasing power of savings.", "source": "The Economist, 2022"},
        ],
        "collocations": ["erode trust", "erode confidence", "gradually erode"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "mitigate": {
        "pos": "v.",
        "definition": "make less severe, serious, or painful",
        "chinese": "减轻，缓和",
        "phonetic": "/ˈmɪt.ɪ.ɡeɪt/",
        "examples": [
            {"text": "Governments must take action to mitigate the effects of climate change.", "source": "IPCC Report, 2023"},
            {"text": "Early intervention can help mitigate the impact of learning disabilities.", "source": "The Lancet, 2022"},
        ],
        "collocations": ["mitigate risk", "mitigate the effects", "mitigate the impact"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "prioritize": {
        "pos": "v.",
        "definition": "designate or treat something as more important than other things",
        "chinese": "优先处理",
        "phonetic": "/praɪˈɒr.ɪ.taɪz/",
        "examples": [
            {"text": "Companies need to prioritize employee well-being alongside productivity.", "source": "Harvard Business Review, 2023"},
            {"text": "Schools should prioritize critical thinking over rote memorisation.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["prioritize safety", "prioritize education", "prioritize over"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "scrutinize": {
        "pos": "v.",
        "definition": "examine or inspect closely and thoroughly",
        "chinese": "仔细检查，审视",
        "phonetic": "/ˈskruː.tɪ.naɪz/",
        "examples": [
            {"text": "Regulators are scrutinizing the tech industry's data practices.", "source": "The New York Times, 2023"},
            {"text": "Every detail of the proposal was carefully scrutinized by the committee.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["closely scrutinize", "scrutinize data", "scrutinize the details"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "navigate": {
        "pos": "v.",
        "definition": "find one's way through a complex situation or environment",
        "chinese": "导航，驾驭（复杂局面）",
        "phonetic": "/ˈnæv.ɪ.ɡeɪt/",
        "examples": [
            {"text": "Young people must learn to navigate the challenges of the digital age.", "source": "The Atlantic, 2023"},
            {"text": "Businesses are navigating an increasingly complex regulatory landscape.", "source": "Financial Times, 2023"},
        ],
        "collocations": ["navigate challenges", "navigate through", "navigate the complexities"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "enhance": {
        "pos": "v.",
        "definition": "intensify, increase, or further improve the quality, value, or extent of",
        "chinese": "提高，增强",
        "phonetic": "/ɪnˈhɑːns/",
        "examples": [
            {"text": "Technology can enhance the learning experience for students of all ages.", "source": "The Guardian, 2023"},
            {"text": "Regular exercise has been shown to enhance cognitive function.", "source": "The Lancet, 2022"},
        ],
        "collocations": ["enhance performance", "enhance quality", "enhance the experience"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "transform": {
        "pos": "v.",
        "definition": "make a thorough or dramatic change in the form, appearance, or character of",
        "chinese": "转变，改造",
        "phonetic": "/trænsˈfɔːm/",
        "examples": [
            {"text": "Artificial intelligence is transforming industries from healthcare to finance.", "source": "MIT Technology Review, 2023"},
            {"text": "The industrial revolution transformed the way people lived and worked.", "source": "The Economist, 2022"},
        ],
        "collocations": ["transform into", "transform the way", "fundamentally transform"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "diminish": {
        "pos": "v.",
        "definition": "make or become less; reduce",
        "chinese": "减少，降低",
        "phonetic": "/dɪˈmɪn.ɪʃ/",
        "examples": [
            {"text": "The scandal did little to diminish her popularity among voters.", "source": "The New York Times, 2023"},
            {"text": "Our natural resources are diminishing at an alarming rate.", "source": "National Geographic, 2022"},
        ],
        "collocations": ["diminish in value", "diminish over time", "greatly diminish"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "prevalent": {
        "pos": "adj.",
        "definition": "widespread in a particular area or at a particular time",
        "chinese": "流行的，普遍的",
        "phonetic": "/ˈprev.əl.ənt/",
        "examples": [
            {"text": "Anxiety disorders are increasingly prevalent among university students.", "source": "The Lancet, 2023"},
            {"text": "The attitude that technology solves all problems is still prevalent in Silicon Valley.", "source": "The Atlantic, 2022"},
        ],
        "collocations": ["most prevalent", "increasingly prevalent", "prevalent in"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "compelling": {
        "pos": "adj.",
        "definition": "evoking interest, attention, or admiration in a powerfully irresistible way",
        "chinese": "令人信服的，引人注目的",
        "phonetic": "/kəmˈpel.ɪŋ/",
        "examples": [
            {"text": "The documentary presents a compelling case for ocean conservation.", "source": "National Geographic, 2023"},
            {"text": "She gave a compelling speech that moved the entire audience.", "source": "The New York Times, 2022"},
        ],
        "collocations": ["compelling evidence", "compelling argument", "compelling reason"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "constraint": {
        "pos": "n.",
        "definition": "a limitation or restriction",
        "chinese": "限制，约束",
        "phonetic": "/kənˈstreɪnt/",
        "examples": [
            {"text": "Budget constraints forced the school to cut several programmes.", "source": "BBC News, 2023"},
            {"text": "Time constraints make it difficult to cover the entire syllabus.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["budget constraint", "time constraint", "impose constraints"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "inherent": {
        "pos": "adj.",
        "definition": "existing in something as a permanent, essential, or characteristic attribute",
        "chinese": "固有的，内在的",
        "phonetic": "/ɪnˈhɪə.rənt/",
        "examples": [
            {"text": "There are inherent risks in any investment strategy.", "source": "Financial Times, 2023"},
            {"text": "The system has inherent flaws that need to be addressed.", "source": "The Economist, 2022"},
        ],
        "collocations": ["inherent risk", "inherent in", "inherent weakness"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "aggregate": {
        "pos": "v. / adj. / n.",
        "definition": "(v.) combine into a whole; (adj./n.) formed by combining several elements; the total",
        "chinese": "（动）聚集，汇总；（形/名）总计的，总量",
        "phonetic": "/ˈæɡ.rɪ.ɡeɪt/",
        "examples": [
            {"text": "The platform aggregates news from hundreds of different sources.", "source": "MIT Technology Review, 2023"},
            {"text": "In aggregate, these small changes add up to a major shift.", "source": "The Economist, 2022"},
        ],
        "collocations": ["in aggregate", "aggregate data", "aggregate demand"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "coherent": {
        "pos": "adj.",
        "definition": "logical and consistent; forming a unified whole",
        "chinese": "连贯的，一致的",
        "phonetic": "/kəʊˈhɪə.rənt/",
        "examples": [
            {"text": "The government needs a more coherent strategy on climate policy.", "source": "The Guardian, 2023"},
            {"text": "Her essay was well-structured and coherent throughout.", "source": "Cambridge Dictionary"},
        ],
        "collocations": ["coherent strategy", "coherent argument", "coherent plan"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "pragmatic": {
        "pos": "adj.",
        "definition": "dealing with things sensibly and realistically; practical rather than idealistic",
        "chinese": "务实的，实用主义的",
        "phonetic": "/præɡˈmæt.ɪk/",
        "examples": [
            {"text": "We need a pragmatic approach to solving the housing crisis.", "source": "The Economist, 2023"},
            {"text": "The new leader is known for her pragmatic style of governance.", "source": "Foreign Affairs, 2022"},
        ],
        "collocations": ["pragmatic approach", "pragmatic solution", "pragmatic decision"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "plausible": {
        "pos": "adj.",
        "definition": "seeming reasonable or probable; appearing worthy of belief",
        "chinese": "貌似合理的，可信的",
        "phonetic": "/ˈplɔː.zɪ.bəl/",
        "examples": [
            {"text": "His explanation sounded plausible, but further investigation proved otherwise.", "source": "BBC News, 2023"},
            {"text": "There are several plausible explanations for this phenomenon.", "source": "Nature, 2022"},
        ],
        "collocations": ["plausible explanation", "plausible scenario", "seem plausible"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "elicit": {
        "pos": "v.",
        "definition": "evoke or draw out a reaction, answer, or fact from someone",
        "chinese": "引出，引起",
        "phonetic": "/ɪˈlɪs.ɪt/",
        "examples": [
            {"text": "The survey was designed to elicit honest responses from participants.", "source": "Scientific American, 2022"},
            {"text": "Her comment elicited a strong reaction from the audience.", "source": "The New York Times, 2023"},
        ],
        "collocations": ["elicit a response", "elicit information", "elicit support"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "curb": {
        "pos": "v. / n.",
        "definition": "(v.) restrain or keep in check; (n.) a check or restraint on something",
        "chinese": "（动）抑制，遏制；（名）限制",
        "phonetic": "/kɜːb/",
        "examples": [
            {"text": "The government introduced new measures to curb air pollution.", "source": "The Guardian, 2023"},
            {"text": "Efforts to curb spending have had mixed results.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["curb emissions", "curb spending", "curb inflation"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "exert": {
        "pos": "v.",
        "definition": "apply or bring to bear (a force, influence, or quality)",
        "chinese": "施加，运用",
        "phonetic": "/ɪɡˈzɜːt/",
        "examples": [
            {"text": "Social media platforms exert a powerful influence on public opinion.", "source": "The Atlantic, 2023"},
            {"text": "Parents continue to exert significant control over their children's career choices.", "source": "The Economist, 2022"},
        ],
        "collocations": ["exert influence", "exert pressure", "exert control"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "bolster": {
        "pos": "v.",
        "definition": "support or strengthen",
        "chinese": "支持，加强",
        "phonetic": "/ˈbəʊl.stər/",
        "examples": [
            {"text": "The new evidence bolsters the case for stronger environmental regulations.", "source": "Nature, 2023"},
            {"text": "The central bank cut interest rates to bolster economic growth.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["bolster confidence", "bolster support", "bolster the economy"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "disparity": {
        "pos": "n.",
        "definition": "a great difference; inequality",
        "chinese": "差距，不平等",
        "phonetic": "/dɪˈspær.ə.ti/",
        "examples": [
            {"text": "The disparity in income between the richest and poorest continues to grow.", "source": "The Economist, 2023"},
            {"text": "There is a significant disparity in healthcare access between urban and rural areas.", "source": "The Lancet, 2022"},
        ],
        "collocations": ["income disparity", "gender disparity", "growing disparity"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "conducive": {
        "pos": "adj.",
        "definition": "making a certain situation or outcome likely or possible; favourable",
        "chinese": "有利于……的，有助于……的",
        "phonetic": "/kənˈdjuː.sɪv/",
        "examples": [
            {"text": "A quiet environment is more conducive to focused study.", "source": "Cambridge Dictionary"},
            {"text": "Policies that are conducive to innovation will drive economic growth.", "source": "Harvard Business Review, 2023"},
        ],
        "collocations": ["conducive to", "conducive environment", "conducive conditions"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "viable": {
        "pos": "adj.",
        "definition": "capable of working successfully; feasible",
        "chinese": "可行的，切实可行的",
        "phonetic": "/ˈvaɪ.ə.bəl/",
        "examples": [
            {"text": "Solar energy is now a commercially viable alternative to fossil fuels.", "source": "The Economist, 2023"},
            {"text": "The plan is ambitious, but is it financially viable?", "source": "Financial Times, 2022"},
        ],
        "collocations": ["viable alternative", "viable option", "commercially viable"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "depict": {
        "pos": "v.",
        "definition": "represent or show something in a picture, story, or description",
        "chinese": "描绘，描述",
        "phonetic": "/dɪˈpɪkt/",
        "examples": [
            {"text": "The film depicts the struggles of immigrants in a new country.", "source": "The New York Times, 2023"},
            {"text": "Media often depicts scientists in a stereotypical manner.", "source": "Scientific American, 2022"},
        ],
        "collocations": ["accurately depict", "depict as", "vividly depict"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "hinder": {
        "pos": "v.",
        "definition": "make it difficult for someone to do something or for something to happen",
        "chinese": "阻碍，妨碍",
        "phonetic": "/ˈhɪn.dər/",
        "examples": [
            {"text": "Bureaucratic red tape can hinder economic development.", "source": "The Economist, 2023"},
            {"text": "Poor infrastructure hinders access to education in rural areas.", "source": "World Bank Report, 2022"},
        ],
        "collocations": ["hinder progress", "hinder development", "hinder growth"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "surge": {
        "pos": "v. / n.",
        "definition": "(v.) increase suddenly and powerfully; (n.) a sudden powerful forward movement or increase",
        "chinese": "（动）激增；（名）浪涌，激增",
        "phonetic": "/sɜːdʒ/",
        "examples": [
            {"text": "Online shopping surged during the pandemic lockdowns.", "source": "The Economist, 2021"},
            {"text": "There has been a surge in demand for electric vehicles.", "source": "Financial Times, 2023"},
        ],
        "collocations": ["surge in demand", "power surge", "surge forward"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "foster": {
        "pos": "v.",
        "definition": "encourage the development of something; promote",
        "chinese": "培养，促进",
        "phonetic": "/ˈfɒs.tər/",
        "examples": [
            {"text": "Schools should foster creativity rather than just academic performance.", "source": "The Guardian, 2023"},
            {"text": "The programme aims to foster cooperation between nations.", "source": "United Nations, 2022"},
        ],
        "collocations": ["foster growth", "foster innovation", "foster a sense of"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "implicit": {
        "pos": "adj.",
        "definition": "suggested though not directly expressed; inherent",
        "chinese": "含蓄的，隐含的",
        "phonetic": "/ɪmˈplɪs.ɪt/",
        "examples": [
            {"text": "There was an implicit assumption that everyone agreed with the plan.", "source": "The Economist, 2023"},
            {"text": "The policy contains an implicit bias against smaller firms.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["implicit assumption", "implicit bias", "implicit in"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "notion": {
        "pos": "n.",
        "definition": "a conception of or belief about something; an idea",
        "chinese": "概念，观念",
        "phonetic": "/ˈnəʊ.ʃən/",
        "examples": [
            {"text": "The notion that hard work always leads to success is being challenged.", "source": "The Atlantic, 2023"},
            {"text": "He rejected the notion that technology is inherently dangerous.", "source": "MIT Technology Review, 2022"},
        ],
        "collocations": ["the notion that", "reject the notion", "popular notion"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "pertinent": {
        "pos": "adj.",
        "definition": "relevant or applicable to a particular matter",
        "chinese": "相关的，中肯的",
        "phonetic": "/ˈpɜː.tɪ.nənt/",
        "examples": [
            {"text": "The question is particularly pertinent in the context of rising inequality.", "source": "The Economist, 2023"},
            {"text": "She raised several pertinent points during the discussion.", "source": "Cambridge Dictionary"},
        ],
        "collocations": ["pertinent question", "pertinent to", "particularly pertinent"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "detrimental": {
        "pos": "adj.",
        "definition": "tending to cause harm",
        "chinese": "有害的，不利的",
        "phonetic": "/ˌdet.rɪˈmen.təl/",
        "examples": [
            {"text": "Excessive screen time can be detrimental to children's development.", "source": "The Lancet, 2023"},
            {"text": "The policy had a detrimental effect on small businesses.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["detrimental effect", "detrimental to", "detrimental impact"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "robust": {
        "pos": "adj.",
        "definition": "strong and healthy; vigorous; sturdy and effective",
        "chinese": "强健的，稳健的",
        "phonetic": "/rəʊˈbʌst/",
        "examples": [
            {"text": "The country needs a more robust healthcare system.", "source": "The Economist, 2023"},
            {"text": "The study provides robust evidence for the effectiveness of the treatment.", "source": "Nature, 2022"},
        ],
        "collocations": ["robust economy", "robust evidence", "robust system"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "alleviate": {
        "pos": "v.",
        "definition": "make suffering, deficiency, or a problem less severe",
        "chinese": "减轻，缓解",
        "phonetic": "/əˈliː.vi.eɪt/",
        "examples": [
            {"text": "The new policy aims to alleviate poverty in the most deprived regions.", "source": "World Bank Report, 2023"},
            {"text": "Medication can help alleviate the symptoms, but it does not cure the disease.", "source": "The Lancet, 2022"},
        ],
        "collocations": ["alleviate poverty", "alleviate suffering", "alleviate pressure"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "feasible": {
        "pos": "adj.",
        "definition": "possible and practical to do easily or conveniently",
        "chinese": "可行的，行得通的",
        "phonetic": "/ˈfiː.zɪ.bəl/",
        "examples": [
            {"text": "Renewable energy at scale is now technically and economically feasible.", "source": "The Economist, 2023"},
            {"text": "We need to determine whether the plan is feasible within the current budget.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["economically feasible", "technically feasible", "feasible solution"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "rigorous": {
        "pos": "adj.",
        "definition": "extremely thorough and careful; demanding strict attention to rules",
        "chinese": "严格的，严谨的",
        "phonetic": "/ˈrɪɡ.ər.əs/",
        "examples": [
            {"text": "The study was conducted using rigorous scientific methods.", "source": "Nature, 2023"},
            {"text": "Universities should maintain rigorous academic standards.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["rigorous analysis", "rigorous standards", "rigorous testing"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "predominantly": {
        "pos": "adv.",
        "definition": "mainly; for the most part",
        "chinese": "主要地，占主导地位地",
        "phonetic": "/prɪˈdɒm.ɪ.nənt.li/",
        "examples": [
            {"text": "The workforce in this industry is predominantly male.", "source": "The Economist, 2023"},
            {"text": "The disease predominantly affects older adults.", "source": "The Lancet, 2022"},
        ],
        "collocations": ["predominantly male", "predominantly used", "predominantly found"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "consensus": {
        "pos": "n.",
        "definition": "a general agreement among a group of people",
        "chinese": "共识，一致意见",
        "phonetic": "/kənˈsen.səs/",
        "examples": [
            {"text": "There is a growing consensus among scientists that urgent action is needed.", "source": "Nature, 2023"},
            {"text": "The committee failed to reach a consensus on the proposed changes.", "source": "The Economist, 2022"},
        ],
        "collocations": ["reach a consensus", "scientific consensus", "general consensus"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "articulate": {
        "pos": "v. / adj.",
        "definition": "(v.) express an idea or feeling fluently and coherently; (adj.) having or showing the ability to speak fluently",
        "chinese": "（动）清楚表达；（形）表达清晰的",
        "phonetic": "/ɑːˈtɪk.jə.leɪt/",
        "examples": [
            {"text": "She was able to articulate her vision for the company clearly.", "source": "Harvard Business Review, 2023"},
            {"text": "The report articulates the challenges facing the education system.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["articulate a vision", "clearly articulate", "articulate the need"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "implications": {
        "pos": "n.",
        "definition": "the possible effects or results of an action or decision",
        "chinese": "影响，含义",
        "phonetic": "/ˌɪm.plɪˈkeɪ.ʃənz/",
        "examples": [
            {"text": "The ethical implications of gene editing are still being debated.", "source": "Nature, 2023"},
            {"text": "The policy change has far-reaching implications for the entire industry.", "source": "The Economist, 2022"},
        ],
        "collocations": ["far-reaching implications", "policy implications", "implications for"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "correlate": {
        "pos": "v.",
        "definition": "have a mutual relationship or connection in which one thing affects or depends on another",
        "chinese": "相关，关联",
        "phonetic": "/ˈkɒr.ə.leɪt/",
        "examples": [
            {"text": "Studies show that income level correlates strongly with life expectancy.", "source": "The Lancet, 2022"},
            {"text": "Higher education levels tend to correlate with greater civic engagement.", "source": "Scientific American, 2023"},
        ],
        "collocations": ["correlate with", "positively correlate", "strongly correlate"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "incentive": {
        "pos": "n.",
        "definition": "a thing that motivates or encourages someone to do something",
        "chinese": "激励，动机",
        "phonetic": "/ɪnˈsen.tɪv/",
        "examples": [
            {"text": "Tax incentives can encourage companies to invest in green technology.", "source": "The Economist, 2023"},
            {"text": "There is little incentive for employees to work harder without fair compensation.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["financial incentive", "provide an incentive", "incentive to"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "comprehensive": {
        "pos": "adj.",
        "definition": "including or dealing with all or nearly all elements or aspects of something",
        "chinese": "全面的，综合的",
        "phonetic": "/ˌkɒm.prɪˈhen.sɪv/",
        "examples": [
            {"text": "The report provides a comprehensive overview of the current situation.", "source": "World Bank Report, 2023"},
            {"text": "Students need a comprehensive understanding of the subject matter.", "source": "The Guardian, 2022"},
        ],
        "collocations": ["comprehensive review", "comprehensive plan", "comprehensive approach"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "anticipate": {
        "pos": "v.",
        "definition": "regard as probable; expect or predict",
        "chinese": "预期，期望",
        "phonetic": "/ænˈtɪs.ɪ.peɪt/",
        "examples": [
            {"text": "Analysts anticipate a slowdown in economic growth next quarter.", "source": "Financial Times, 2023"},
            {"text": "The company failed to anticipate the shift in consumer preferences.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["widely anticipated", "anticipate a change", "anticipate the need"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "exaggerate": {
        "pos": "v.",
        "definition": "represent something as being larger, better, or worse than it really is",
        "chinese": "夸大，夸张",
        "phonetic": "/ɪɡˈzædʒ.ə.reɪt/",
        "examples": [
            {"text": "The media tends to exaggerate the risks associated with new technologies.", "source": "Scientific American, 2023"},
            {"text": "It would be difficult to exaggerate the importance of this discovery.", "source": "Nature, 2022"},
        ],
        "collocations": ["greatly exaggerated", "exaggerate the risk", "tend to exaggerate"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "underestimate": {
        "pos": "v.",
        "definition": "estimate something to be smaller or less important than it actually is",
        "chinese": "低估",
        "phonetic": "/ˌʌn.dərˈes.tɪ.meɪt/",
        "examples": [
            {"text": "We should not underestimate the impact of social media on young people.", "source": "The Atlantic, 2023"},
            {"text": "The complexity of the task was significantly underestimated.", "source": "The Economist, 2022"},
        ],
        "collocations": ["underestimate the importance", "seriously underestimate", "underestimate the impact"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "overlook": {
        "pos": "v.",
        "definition": "fail to notice or consider something",
        "chinese": "忽视，忽略",
        "phonetic": "/ˌəʊ.vəˈlʊk/",
        "examples": [
            {"text": "The report overlooks the role of cultural factors in economic development.", "source": "The Economist, 2023"},
            {"text": "Important details are often overlooked in the rush to meet deadlines.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["easily overlooked", "overlook the fact", "often overlooked"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "adequate": {
        "pos": "adj.",
        "definition": "satisfactory or acceptable in quality or quantity",
        "chinese": "足够的，充分的",
        "phonetic": "/ˈæd.ɪ.kwət/",
        "examples": [
            {"text": "Many schools lack adequate resources for special needs education.", "source": "The Guardian, 2023"},
            {"text": "Without adequate preparation, the project is unlikely to succeed.", "source": "Cambridge Dictionary"},
        ],
        "collocations": ["adequate resources", "adequate funding", "adequate preparation"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "diverse": {
        "pos": "adj.",
        "definition": "showing a great deal of variety; very different",
        "chinese": "多样的，多元的",
        "phonetic": "/daɪˈvɜːs/",
        "examples": [
            {"text": "The city is home to a diverse population from many different backgrounds.", "source": "The New York Times, 2023"},
            {"text": "A diverse workforce brings a wider range of perspectives and ideas.", "source": "Harvard Business Review, 2022"},
        ],
        "collocations": ["diverse range", "diverse population", "culturally diverse"],
        "level": "CET-4 / IELTS 5.5+",
    },
    "impose": {
        "pos": "v.",
        "definition": "force something unwelcome to be accepted or put in place",
        "chinese": "强加，施加",
        "phonetic": "/ɪmˈpəʊz/",
        "examples": [
            {"text": "The government imposed strict regulations on carbon emissions.", "source": "The Guardian, 2023"},
            {"text": "New tariffs were imposed on imported goods.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["impose restrictions", "impose sanctions", "impose a ban"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "legitimate": {
        "pos": "adj.",
        "definition": "conforming to the law or to rules; justifiable",
        "chinese": "合法的，正当的",
        "phonetic": "/lɪˈdʒɪt.ɪ.mət/",
        "examples": [
            {"text": "Citizens have a legitimate right to know how their data is being used.", "source": "The Economist, 2023"},
            {"text": "The company has raised legitimate concerns about the new regulations.", "source": "Financial Times, 2022"},
        ],
        "collocations": ["legitimate concern", "legitimate reason", "legitimate interest"],
        "level": "CET-6 / IELTS 6.5+",
    },
    "reluctant": {
        "pos": "adj.",
        "definition": "unwilling and hesitant; disinclined",
        "chinese": "不情愿的，勉强的",
        "phonetic": "/rɪˈlʌk.tənt/",
        "examples": [
            {"text": "Many companies are reluctant to adopt new technologies without clear evidence of ROI.", "source": "Harvard Business Review, 2023"},
            {"text": "He was reluctant to discuss his plans publicly.", "source": "BBC News, 2022"},
        ],
        "collocations": ["reluctant to", "seem reluctant", "reluctant acceptance"],
        "level": "CET-4 / IELTS 6.0+",
    },
    "paradox": {
        "pos": "n.",
        "definition": "a seemingly absurd or contradictory statement or situation that may nonetheless be true",
        "chinese": "悖论，矛盾",
        "phonetic": "/ˈpær.ə.dɒks/",
        "examples": [
            {"text": "The paradox of choice suggests that too many options can lead to less satisfaction.", "source": "Scientific American, 2022"},
            {"text": "It is a paradox that economic growth can sometimes increase poverty.", "source": "The Economist, 2023"},
        ],
        "collocations": ["paradox of", "apparent paradox", "resolve the paradox"],
        "level": "CET-6 / IELTS 7.0+",
    },
    "endeavor": {
        "pos": "v. / n.",
        "definition": "(v.) try hard to do or achieve something; (n.) an attempt to achieve a goal",
        "chinese": "（动）努力，尝试；（名）努力，事业",
        "phonetic": "/ɪnˈdev.ər/",
        "examples": [
            {"text": "Scientists continue to endeavor to find a cure for the disease.", "source": "The Lancet, 2023"},
            {"text": "The space programme represents humanity's greatest scientific endeavor.", "source": "Nature, 2022"},
        ],
        "collocations": ["human endeavor", "creative endeavor", "endeavor to"],
        "level": "CET-6 / IELTS 7.0+",
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
    # ── Newly added common phrases ──
    "on the other hand": {
        "definition": "used to present an alternative or contrasting point of view",
        "chinese": "另一方面",
        "examples": [
            {"text": "Remote work offers flexibility; on the other hand, it can lead to isolation.", "source": "Harvard Business Review, 2023"},
            {"text": "The plan is ambitious. On the other hand, it may be exactly what we need.", "source": "The Economist, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "in terms of": {
        "definition": "with regard to the particular aspect specified",
        "chinese": "在……方面，就……而言",
        "examples": [
            {"text": "In terms of cost, the new system is far more efficient.", "source": "Financial Times, 2023"},
            {"text": "The country ranks highly in terms of educational attainment.", "source": "World Bank Report, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "as a matter of fact": {
        "definition": "in reality; actually (used to emphasise a statement)",
        "chinese": "事实上",
        "examples": [
            {"text": "As a matter of fact, the data tells a very different story.", "source": "The Economist, 2023"},
            {"text": "He claims to be an expert, but as a matter of fact, he has very little experience.", "source": "Cambridge Dictionary"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "to a certain extent": {
        "definition": "partly but not entirely",
        "chinese": "在一定程度上",
        "examples": [
            {"text": "To a certain extent, economic growth depends on government policy.", "source": "The Economist, 2023"},
            {"text": "The criticism is valid to a certain extent, but it overlooks key factors.", "source": "The Guardian, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "as opposed to": {
        "definition": "in contrast with",
        "chinese": "与……相对，而不是",
        "examples": [
            {"text": "The company focuses on long-term value, as opposed to short-term profits.", "source": "Harvard Business Review, 2023"},
            {"text": "Online learning, as opposed to traditional classroom teaching, offers greater flexibility.", "source": "The Guardian, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "in contrast to": {
        "definition": "when compared with; unlike",
        "chinese": "与……形成对比",
        "examples": [
            {"text": "In contrast to previous years, this year's growth has been modest.", "source": "Financial Times, 2023"},
            {"text": "In contrast to popular belief, the study found no significant link.", "source": "Nature, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "regardless of": {
        "definition": "without being affected or influenced by",
        "chinese": "不管，不顾",
        "examples": [
            {"text": "All students should have access to quality education, regardless of their background.", "source": "UNICEF Report, 2023"},
            {"text": "The policy applies to all employees, regardless of their position.", "source": "The Economist, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "with respect to": {
        "definition": "in relation to; concerning",
        "chinese": "关于，就……而言",
        "examples": [
            {"text": "With respect to data privacy, the new regulations set a higher standard.", "source": "The Guardian, 2023"},
            {"text": "The two countries have very different policies with respect to immigration.", "source": "Foreign Affairs, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "for the sake of": {
        "definition": "in order to achieve or preserve something",
        "chinese": "为了……的缘故",
        "examples": [
            {"text": "We should not sacrifice quality for the sake of speed.", "source": "Harvard Business Review, 2022"},
            {"text": "For the sake of clarity, let us define the key terms first.", "source": "Cambridge Dictionary"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "in light of": {
        "definition": "taking something into consideration; because of",
        "chinese": "鉴于，根据",
        "examples": [
            {"text": "In light of recent events, the company has revised its security protocols.", "source": "Financial Times, 2023"},
            {"text": "In light of the evidence, the committee decided to approve the proposal.", "source": "The Economist, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "take into account": {
        "definition": "consider something along with other factors before making a decision",
        "chinese": "考虑到，将……纳入考量",
        "examples": [
            {"text": "The report takes into account the views of all stakeholders.", "source": "World Bank Report, 2023"},
            {"text": "We must take into account the long-term environmental impact.", "source": "The Guardian, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "boil down to": {
        "definition": "be essentially a matter of; amount to",
        "chinese": "归结为",
        "examples": [
            {"text": "The debate ultimately boils down to a question of priorities.", "source": "The Economist, 2023"},
            {"text": "Success often boils down to consistency and hard work.", "source": "Harvard Business Review, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "bring about": {
        "definition": "cause something to happen",
        "chinese": "引起，导致",
        "examples": [
            {"text": "The invention of the internet brought about a revolution in communication.", "source": "The Atlantic, 2022"},
            {"text": "Effective leadership can bring about lasting organisational change.", "source": "Harvard Business Review, 2023"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "keep pace with": {
        "definition": "move, develop, or progress at the same speed as",
        "chinese": "跟上……的步伐",
        "examples": [
            {"text": "Education systems must keep pace with technological change.", "source": "The Economist, 2023"},
            {"text": "Wages have failed to keep pace with the rising cost of living.", "source": "The Guardian, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "lose sight of": {
        "definition": "fail to consider or be aware of something",
        "chinese": "忽视，忘记",
        "examples": [
            {"text": "In the pursuit of profit, companies must not lose sight of their social responsibilities.", "source": "The Economist, 2023"},
            {"text": "It is easy to lose sight of the bigger picture when dealing with daily pressures.", "source": "Harvard Business Review, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "stem from": {
        "definition": "originate from or be caused by",
        "chinese": "源于，起因于",
        "examples": [
            {"text": "Many of these problems stem from a lack of adequate funding.", "source": "The Guardian, 2023"},
            {"text": "The conflict stems from deep-rooted historical grievances.", "source": "Foreign Affairs, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "account for": {
        "definition": "provide an explanation for; represent a specified proportion of",
        "chinese": "解释；占（比例）",
        "examples": [
            {"text": "Renewable energy now accounts for over 30% of electricity generation.", "source": "The Economist, 2023"},
            {"text": "This theory does not fully account for the observed results.", "source": "Nature, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "pave the way for": {
        "definition": "create the circumstances to enable something to happen",
        "chinese": "为……铺平道路",
        "examples": [
            {"text": "The agreement paves the way for closer economic cooperation.", "source": "Financial Times, 2023"},
            {"text": "Early research in this field paved the way for modern computing.", "source": "MIT Technology Review, 2022"},
        ],
        "level": "CET-6 / IELTS 6.5+",
    },
    "in the long run": {
        "definition": "over a long period of time; eventually",
        "chinese": "从长远来看",
        "examples": [
            {"text": "Investing in education pays off in the long run.", "source": "The Economist, 2023"},
            {"text": "In the long run, sustainable practices will prove more profitable.", "source": "Harvard Business Review, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "play a role in": {
        "definition": "contribute to or be involved in",
        "chinese": "在……中起作用",
        "examples": [
            {"text": "Social media plays an increasingly important role in shaping public opinion.", "source": "The Atlantic, 2023"},
            {"text": "Genetics plays a role in determining susceptibility to certain diseases.", "source": "The Lancet, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "draw attention to": {
        "definition": "make people notice or be aware of something",
        "chinese": "引起对……的注意",
        "examples": [
            {"text": "The report draws attention to the growing gap between rich and poor.", "source": "World Bank Report, 2023"},
            {"text": "Activists have drawn attention to the environmental damage caused by mining.", "source": "The Guardian, 2022"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "on the whole": {
        "definition": "in general; considering everything",
        "chinese": "总体来说",
        "examples": [
            {"text": "On the whole, the results have been positive.", "source": "The Economist, 2023"},
            {"text": "The programme, on the whole, has achieved its intended goals.", "source": "BBC News, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "with regard to": {
        "definition": "concerning; in connection with",
        "chinese": "关于，至于",
        "examples": [
            {"text": "With regard to your question, I would like to offer a different perspective.", "source": "Cambridge Dictionary"},
            {"text": "Significant progress has been made with regard to reducing emissions.", "source": "IPCC Report, 2023"},
        ],
        "level": "CET-4 / IELTS 6.0+",
    },
    "make up for": {
        "definition": "compensate for something lost, missed, or deficient",
        "chinese": "弥补，补偿",
        "examples": [
            {"text": "The company is trying to make up for lost time after the delays.", "source": "Financial Times, 2023"},
            {"text": "Quality can sometimes make up for a lack of quantity.", "source": "Harvard Business Review, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "result in": {
        "definition": "cause a particular outcome to happen",
        "chinese": "导致，造成",
        "examples": [
            {"text": "The policy changes resulted in a significant reduction in carbon emissions.", "source": "The Guardian, 2023"},
            {"text": "Poor planning can result in costly delays.", "source": "Harvard Business Review, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
    },
    "contribute to": {
        "definition": "help to cause or bring about",
        "chinese": "促成，有助于",
        "examples": [
            {"text": "Several factors contributed to the company's rapid growth.", "source": "Financial Times, 2023"},
            {"text": "Regular exercise contributes to better mental health.", "source": "The Lancet, 2022"},
        ],
        "level": "CET-4 / IELTS 5.5+",
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
