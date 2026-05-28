/**
 * Foreign Journal Reader — 外刊精读 v3
 * With star bookmarks, dictionary audio, deploy-ready
 */

// ═══ STATE ═══
let currentView = 'home';
let previousView = 'home';
let currentArticles = [];
let currentAnalysis = null;
let currentArticleText = '';
let tooltipWord = '';

// ═══ INIT ═══
document.addEventListener('DOMContentLoaded', () => {
  setTodayDate();
  loadDailyArticles();
  document.addEventListener('click', handleGlobalClick);
  window.addEventListener('scroll', updateReadingProgress);
  initDblclickLookup();
});

function setTodayDate() {
  const el = document.getElementById('today-date');
  // Display in CST (Asia/Shanghai)
  const now = new Date();
  const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', timeZone: 'Asia/Shanghai' };
  el.textContent = now.toLocaleDateString('en-US', options);
}

// ═══ NAVIGATION ═══
function showView(viewName) {
  previousView = currentView;
  currentView = viewName;

  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  document.getElementById('view-' + viewName).classList.add('active');

  document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.view === viewName);
  });

  if (viewName === 'vocabulary') loadVocabulary();
  if (viewName === 'history') loadHistory();
  if (viewName === 'starred') loadStarred();

  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function goBack() { showView(previousView || 'home'); }

// ═══ DAILY ARTICLES ═══
async function loadDailyArticles() {
  const grid = document.getElementById('articles-grid');
  try {
    const res = await fetch('/api/daily-articles');
    const data = await res.json();
    if (data.success && data.articles.length > 0) {
      currentArticles = data.articles;
      renderArticles(data.articles);
    } else {
      grid.innerHTML = '<div class="empty-state"><p>暂无文章，请稍后再试</p></div>';
    }
  } catch (err) {
    grid.innerHTML = '<div class="empty-state"><p>加载失败，请检查网络连接</p></div>';
  }
}

function renderArticles(articles) {
  const grid = document.getElementById('articles-grid');
  grid.innerHTML = '';
  if (!articles.length) {
    grid.innerHTML = '<div class="empty-state"><p>暂无精读文章</p><p class="empty-hint">在 Cowork 中粘贴外刊原文,我会生成精读 JSON 写入 articles/ 目录,git push 后即可上线</p></div>';
    return;
  }

  // 按日期分组(降序)
  const byDate = {};
  articles.forEach((a, idx) => {
    a._origIdx = idx;
    const d = a.published || '未标注日期';
    (byDate[d] = byDate[d] || []).push(a);
  });
  const sortedDates = Object.keys(byDate).sort().reverse();

  const todayStr = new Date().toLocaleDateString('sv-SE', { timeZone: 'Asia/Shanghai' });

  sortedDates.forEach(dateStr => {
    const group = document.createElement('div');
    group.className = 'date-group';
    let dateLabel = dateStr;
    if (dateStr !== '未标注日期') {
      const d = new Date(dateStr + 'T00:00:00+08:00');
      dateLabel = d.toLocaleDateString('zh-CN', {
        year: 'numeric', month: 'long', day: 'numeric', weekday: 'long', timeZone: 'Asia/Shanghai'
      });
    }
    const isToday = dateStr === todayStr;
    group.innerHTML = `<div class="date-group-header"><span class="date-group-dot"></span>${dateLabel}${isToday ? ' · 今天' : ''}</div><div class="date-group-cards"></div>`;
    const cardsWrap = group.querySelector('.date-group-cards');

    byDate[dateStr].forEach(article => {
      const idx = article._origIdx;
      const card = document.createElement('div');
      card.className = 'article-card';
      const categoryClass = 'cat-' + (article.category || 'editorial');
      const starClass = article.starred ? 'star-active' : '';
      card.innerHTML = `
        <button class="card-star ${starClass}" onclick="event.stopPropagation(); toggleStar(this, ${idx})" title="收藏">&#9733;</button>
        <div class="card-source">
          <span>${article.source_icon || ''}</span>
          <span>${article.source || ''}</span>
          <span class="card-category ${categoryClass}">${article.category_label || ''}</span>
        </div>
        <h3 class="card-title">${escapeHtml(article.title)}</h3>
        <p class="card-summary">${escapeHtml(article.summary || '')}</p>
        <div class="card-footer">
          <span class="card-type type-classic">精读</span>
          <span class="card-action">开始精读 &rarr;</span>
        </div>
      `;
      card.onclick = () => openArticle(article, idx);
      cardsWrap.appendChild(card);
    });
    grid.appendChild(group);
  });
}

// ═══ STAR / UNSTAR ═══
async function toggleStar(btnEl, articleIdx) {
  const article = currentArticles[articleIdx];
  if (!article) return;
  try {
    const res = await fetch('/api/starred', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(article)
    });
    const data = await res.json();
    if (data.success) {
      article.starred = data.starred;
      btnEl.classList.toggle('star-active', data.starred);
      notify(data.starred ? '已收藏' : '已取消收藏', 'success');
    }
  } catch (err) { notify('操作失败', 'error'); }
}

// ═══ STARRED VIEW ═══
async function loadStarred() {
  const container = document.getElementById('starred-list');
  try {
    const res = await fetch('/api/starred');
    const data = await res.json();
    if (data.success && data.starred.length > 0) {
      container.innerHTML = '';
      data.starred.forEach(article => {
        const item = document.createElement('div');
        item.className = 'history-article-item';
        item.onclick = () => openHistoryArticle(article);
        const catClass = 'cat-' + (article.category || 'editorial');
        item.innerHTML = `
          <span class="history-article-icon">${article.source_icon || ''}</span>
          <div class="history-article-info">
            <div class="history-article-title">${escapeHtml(article.title)}</div>
            <div class="history-article-meta">${article.source || ''} &middot; <span class="card-category ${catClass}" style="font-size:0.65rem">${article.category_label || ''}</span></div>
          </div>
        `;
        container.appendChild(item);
      });
    } else {
      container.innerHTML = '<div class="empty-state"><p class="empty-icon">&#9733;</p><p>还没有收藏的文章</p><p class="empty-hint">在今日推荐页面，点击文章右上角的星标即可收藏</p></div>';
    }
  } catch (err) {
    container.innerHTML = '<div class="empty-state"><p>加载失败</p></div>';
  }
}

// ═══ HISTORY ═══
async function loadHistory() {
  const container = document.getElementById('history-list');
  try {
    const res = await fetch('/api/history');
    const data = await res.json();
    if (data.success && Object.keys(data.history).length > 0) {
      renderHistory(data.history);
    } else {
      container.innerHTML = '<div class="empty-state"><p class="empty-icon">&#9201;</p><p>暂无历史记录</p><p class="empty-hint">每天访问「今日推荐」，文章会自动归档到这里</p></div>';
    }
  } catch (err) {
    container.innerHTML = '<div class="empty-state"><p>加载失败</p></div>';
  }
}

function renderHistory(history) {
  const container = document.getElementById('history-list');
  container.innerHTML = '';
  const todayStr = new Date().toLocaleDateString('sv-SE', { timeZone: 'Asia/Shanghai' }); // YYYY-MM-DD
  for (const [dateStr, articles] of Object.entries(history)) {
    const group = document.createElement('div');
    group.className = 'history-date-group';
    const d = new Date(dateStr + 'T00:00:00+08:00');
    const dateLabel = d.toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long', timeZone: 'Asia/Shanghai' });
    const isToday = dateStr === todayStr;
    group.innerHTML = `<div class="history-date-header"><span class="history-date-dot"></span>${dateLabel}${isToday ? ' (今天)' : ''}</div>`;
    articles.forEach(article => {
      const item = document.createElement('div');
      item.className = 'history-article-item';
      item.onclick = () => openHistoryArticle(article);
      const catClass = 'cat-' + (article.category || 'editorial');
      item.innerHTML = `
        <span class="history-article-icon">${article.source_icon || ''}</span>
        <div class="history-article-info">
          <div class="history-article-title">${escapeHtml(article.title)}</div>
          <div class="history-article-meta">${article.source || ''} &middot; <span class="card-category ${catClass}" style="font-size:0.65rem">${article.category_label || ''}</span></div>
        </div>
      `;
      group.appendChild(item);
    });
    container.appendChild(group);
  }
}

function openHistoryArticle(article) {
  const aid = article.article_id || article.article_index;
  if (aid !== null && aid !== undefined) {
    fetch(`/api/article/${aid}`)
      .then(r => r.json())
      .then(data => {
        if (data.success && data.article.full_text) {
          const a = data.article;
          a._id = a._id || aid;
          openArticle(a);
        } else { notify('无法加载该文章', 'error'); }
      })
      .catch(() => notify('加载失败', 'error'));
  } else {
    notify('该文章为 RSS 摘要，请使用「粘贴精读」功能', 'info');
  }
}

// ═══ OPEN & ANALYZE ARTICLE ═══
async function openArticle(article) {
  if (!article.has_full_text || !article.full_text) {
    notify('该文章暂无全文内容', 'error');
    return;
  }
  showView('reader');
  currentArticleText = article.full_text;
  document.getElementById('reader-source').textContent = article.source || '';
  document.getElementById('reader-title').textContent = article.title;
  document.getElementById('reader-body').innerHTML = '<div class="loading-state"><div class="loader"></div><p>正在分析文章...</p></div>';
  document.getElementById('reader-meta').innerHTML = '';
  clearTabs();

  try {
    const res = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: article.full_text, title: article.title, article_id: article._id })
    });
    const data = await res.json();
    if (data.success) {
      currentAnalysis = data.analysis;
      renderReader(article, data.analysis);
    } else {
      document.getElementById('reader-body').innerHTML = '<div class="empty-state"><p>分析失败</p></div>';
    }
  } catch (err) {
    document.getElementById('reader-body').innerHTML = '<div class="empty-state"><p>分析失败，请重试</p></div>';
  }
}

function clearTabs() {
  ['vocab', 'phrases', 'patterns'].forEach(t => {
    document.getElementById('tab-' + t).innerHTML = '<div class="analysis-empty">分析中...</div>';
  });
}

// ═══ RENDER READER ═══
function renderReader(article, analysis) {
  const da = analysis.difficulty_assessment;
  const complexSentences = analysis.complex_sentences || analysis.sentence_patterns || [];
  const articleLink = analysis.article_link || article.link || '';

  document.getElementById('reader-meta').innerHTML = `
    <span class="meta-badge difficulty">${da.level}</span>
    <span class="meta-badge words">${da.total_words} 词 &middot; 平均词长 ${da.avg_word_length}</span>
    <span class="meta-badge vocab-count">${analysis.vocabulary.length} 个核心词汇 &middot; ${analysis.phrases.length} 个高级词组 &middot; ${complexSentences.length} 个长难句</span>
    ${articleLink ? `<a class="meta-badge" href="${articleLink}" target="_blank" style="text-decoration:none;background:var(--blue-soft);color:var(--blue)">原文链接 &rarr;</a>` : ''}
  `;
  document.getElementById('count-vocab').textContent = analysis.vocabulary.length;
  document.getElementById('count-phrases').textContent = analysis.phrases.length;
  document.getElementById('count-patterns').textContent = complexSentences.length;

  // Collect vocab words for highlighting — support both form_found (old) and word (new)
  const vocabWords = (analysis.vocabulary || []).map(v => v.form_found || v.word);
  const phrases = (analysis.phrases || []).map(p => p.phrase);

  const bodyEl = document.getElementById('reader-body');
  const paragraphs = (article.full_text || '').split(/\n{2,}/).filter(p => p.trim());

  // Collect sentence highlight keys
  const sentenceKeys = complexSentences
    .filter(s => s.highlight_key)
    .map(s => ({ key: s.highlight_key, idx: complexSentences.indexOf(s) }));

  let html = '';
  paragraphs.forEach((para, idx) => {
    let p = escapeHtml(para.trim());

    // 1. Highlight complex sentences first (longest first to avoid partial matches)
    sentenceKeys.sort((a, b) => b.key.length - a.key.length).forEach(({ key, idx: sIdx }) => {
      const escaped = escapeHtml(key);
      // Use a longer prefix for more accurate matching
      const matchPrefix = escaped.substring(0, Math.min(120, escaped.length));
      if (p.toLowerCase().includes(matchPrefix.substring(0, 40).toLowerCase())) {
        // Find and wrap the sentence — match from the key prefix to the end of the sentence
        const regexStr = escapeRegExp(matchPrefix) + (escaped.length > 120 ? '[^<]*?' : '');
        const sentenceRegex = new RegExp('(' + regexStr + ')', 'i');
        p = p.replace(sentenceRegex, '<span class="highlight-sentence" data-sentence-idx="' + sIdx + '">$1</span>');
      }
    });

    // 2. Highlight phrases (longest first) — only in text nodes, skip inside HTML tags
    const sortedPhrases = [...phrases].sort((a, b) => b.length - a.length);
    sortedPhrases.forEach(phrase => {
      p = highlightInTextNodes(p, phrase, (match) =>
        '<span class="highlight-phrase" data-phrase="' + match.toLowerCase() + '">' + match + '</span>'
      );
    });

    // 3. Highlight vocab words — only in text nodes, skip inside HTML tags
    vocabWords.forEach(word => {
      p = highlightInTextNodes(p, word, (match) =>
        '<span class="highlight-vocab" data-word="' + word.toLowerCase() + '">' + match + '</span>',
        true /* word boundary */
      );
    });

    html += `<div class="para-wrapper"><span class="para-number">${idx + 1}</span><p>${p}</p></div>`;
  });
  bodyEl.innerHTML = html;

  // 按原文出现顺序排序卡片(否则按 JSON 中的顺序)
  const fullTextLower = (article.full_text || '').toLowerCase();
  const sortByAppearance = (items, keyFn) => items.slice().sort((a, b) => {
    const ka = (keyFn(a) || '').toLowerCase();
    const kb = (keyFn(b) || '').toLowerCase();
    const ia = ka ? fullTextLower.indexOf(ka) : -1;
    const ib = kb ? fullTextLower.indexOf(kb) : -1;
    return (ia === -1 ? Infinity : ia) - (ib === -1 ? Infinity : ib);
  });

  const sortedVocab = sortByAppearance(analysis.vocabulary || [], v => v.form_found || v.word);
  const sortedPhrases = sortByAppearance(analysis.phrases || [], p => p.phrase);
  const sortedSentences = sortByAppearance(complexSentences, s => s.highlight_key || s.sentence);

  renderVocabTab(sortedVocab);
  renderPhrasesTab(sortedPhrases);
  renderSentencesTab(sortedSentences);
  switchTab('vocab');
  bindHighlightClicks();
  bindCardClicks();
}

// ═══ 右侧卡片点击 → 左侧原文滚动 + 闪烁 ═══
function bindCardClicks() {
  document.querySelectorAll('.vocab-card').forEach(card => {
    card.addEventListener('click', (e) => {
      // 避免点击内部按钮(收藏/朗读)触发跳转
      if (e.target.closest('button')) return;
      scrollOriginalTo('vocab', card.dataset.key);
    });
  });
  document.querySelectorAll('.phrase-card').forEach(card => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('button')) return;
      scrollOriginalTo('phrase', card.dataset.key);
    });
  });
  document.querySelectorAll('.pattern-card[id^="sentence-card-"]').forEach(card => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('button')) return;
      const sIdx = card.id.replace('sentence-card-', '');
      scrollOriginalTo('sentence', sIdx);
    });
  });
}

function scrollOriginalTo(type, key) {
  let target = null;
  if (type === 'vocab') {
    target = document.querySelector(`.highlight-vocab[data-word="${(key || '').toLowerCase()}"]`);
  } else if (type === 'phrase') {
    target = document.querySelector(`.highlight-phrase[data-phrase="${(key || '').toLowerCase()}"]`);
  } else if (type === 'sentence') {
    target = document.querySelector(`.highlight-sentence[data-sentence-idx="${key}"]`);
  }
  if (!target) return;
  target.scrollIntoView({ behavior: 'smooth', block: 'center' });
  target.classList.add('flash');
  setTimeout(() => target.classList.remove('flash'), 1800);
}


// ═══ HIGHLIGHT CLICK → SIDEBAR + TOOLTIP ═══
function bindHighlightClicks() {
  document.querySelectorAll('.highlight-vocab').forEach(el => {
    el.addEventListener('click', (e) => {
      e.stopPropagation();
      const word = el.dataset.word.toLowerCase();
      showTooltipAtElement(el, word, 'vocab');
      scrollToCard(word, 'vocab');
    });
  });
  document.querySelectorAll('.highlight-phrase').forEach(el => {
    el.addEventListener('click', (e) => {
      e.stopPropagation();
      const phrase = el.dataset.phrase.toLowerCase();
      showTooltipAtElement(el, phrase, 'phrase');
      scrollToCard(phrase, 'phrases');
    });
  });

  // Sentence click → jump to sentence breakdown in sidebar
  document.querySelectorAll('.highlight-sentence').forEach(el => {
    el.addEventListener('click', (e) => {
      e.stopPropagation();
      hideTooltip();
      const sIdx = el.dataset.sentenceIdx;
      switchTab('patterns');
      setTimeout(() => {
        const card = document.getElementById('sentence-card-' + sIdx);
        if (card) {
          card.classList.add('focused');
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
          setTimeout(() => card.classList.remove('focused'), 3000);
        }
      }, 100);
    });
  });
}

function scrollToCard(key, tabName) {
  switchTab(tabName);
  const normalizedKey = key.toLowerCase();
  setTimeout(() => {
    const sidebar = document.getElementById('reader-analysis');
    const cards = sidebar.querySelectorAll(tabName === 'vocab' ? '.vocab-card' : '.phrase-card');
    let targetCard = null;
    cards.forEach(card => {
      card.classList.remove('focused');
      if ((card.dataset.key || '').toLowerCase() === normalizedKey) targetCard = card;
    });
    if (targetCard) {
      targetCard.classList.add('focused');
      targetCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
      setTimeout(() => targetCard.classList.remove('focused'), 3000);
    }
  }, 100);
}

// ═══ TOOLTIP ═══
function showTooltipAtElement(el, key, type) {
  const tooltip = document.getElementById('word-tooltip');
  let info = null;
  if (type === 'vocab' && currentAnalysis) {
    info = currentAnalysis.vocabulary.find(v => (v.form_found || v.word).toLowerCase() === key || v.word.toLowerCase() === key);
    if (info) {
      document.getElementById('tooltip-word').textContent = info.word;
      document.getElementById('tooltip-phonetic').textContent = info.phonetic || '';
      document.getElementById('tooltip-chinese').textContent = info.chinese;
      document.getElementById('tooltip-def').textContent = info.definition;
      tooltipWord = info.word;
    }
  } else if (type === 'phrase' && currentAnalysis) {
    info = currentAnalysis.phrases.find(p => p.phrase.toLowerCase() === key);
    if (info) {
      document.getElementById('tooltip-word').textContent = info.phrase;
      document.getElementById('tooltip-phonetic').textContent = '';
      document.getElementById('tooltip-chinese').textContent = info.chinese;
      document.getElementById('tooltip-def').textContent = info.definition;
      tooltipWord = info.phrase;
    }
  }
  if (!info) return;
  document.querySelectorAll('.highlight-vocab.active, .highlight-phrase.active').forEach(e => e.classList.remove('active'));
  el.classList.add('active');
  const rect = el.getBoundingClientRect();
  tooltip.style.display = 'block';
  let top = rect.bottom + 8;
  let left = rect.left;
  const tw = tooltip.offsetWidth, th = tooltip.offsetHeight;
  if (left + tw > window.innerWidth - 16) left = window.innerWidth - tw - 16;
  if (left < 16) left = 16;
  if (top + th > window.innerHeight - 16) top = rect.top - th - 8;
  tooltip.style.top = top + 'px';
  tooltip.style.left = left + 'px';
}

function hideTooltip() {
  document.getElementById('word-tooltip').style.display = 'none';
  document.querySelectorAll('.highlight-vocab.active, .highlight-phrase.active').forEach(e => e.classList.remove('active'));
}

function handleGlobalClick(e) {
  const tooltip = document.getElementById('word-tooltip');
  if (!tooltip.contains(e.target) && !e.target.closest('.highlight-vocab, .highlight-phrase')) hideTooltip();
}

// ═══ READING PROGRESS ═══
function updateReadingProgress() {
  if (currentView !== 'reader') return;
  const body = document.getElementById('reader-body');
  if (!body) return;
  const rect = body.getBoundingClientRect();
  const total = body.scrollHeight;
  const scrolled = Math.max(0, -rect.top);
  const visible = window.innerHeight;
  const progress = Math.min(100, Math.round((scrolled / Math.max(total - visible + 100, 1)) * 100));
  const el = document.getElementById('reading-progress-text');
  if (el) el.textContent = Math.max(0, progress) + '%';
}

// ═══ RENDER TABS ═══
function renderVocabTab(vocab) {
  const container = document.getElementById('tab-vocab');
  if (vocab.length === 0) { container.innerHTML = '<div class="analysis-empty">未发现已收录的高级词汇</div>'; return; }
  container.innerHTML = vocab.map((v, i) => `
    <div class="vocab-card" id="vocab-card-${i}" data-key="${(v.form_found || v.word).toLowerCase()}">
      <div class="vocab-card-header">
        <span class="vocab-word">${v.word}</span>
        <button class="btn-tts-inline" title="英式朗读" onclick="event.stopPropagation(); speak('${escapeAttr(v.word)}', {rate: 0.85})">🔊</button>
        <span class="vocab-pos">${v.pos}</span>
        <span class="vocab-phonetic">${v.phonetic || ''}</span>
        <span class="vocab-level">${v.level}</span>
      </div>
      <div class="vocab-chinese">${v.chinese}</div>
      <div class="vocab-def">${v.definition}</div>
      ${v.linguistics ? `<div class="pattern-desc" style="margin:var(--space-sm) 0;line-height:1.7;font-size:0.82rem"><strong style="color:var(--ink)">语言学解析：</strong>${escapeHtml(v.linguistics)}</div>` : ''}
      ${v.usage ? `<div class="pattern-tip" style="margin:var(--space-sm) 0"><strong>用法与替换：</strong>${escapeHtml(v.usage)}</div>` : ''}
      <div class="vocab-examples">
        <div class="vocab-examples-title">例句</div>
        ${v.examples.map(ex => {
          const text = typeof ex === 'string' ? ex : ex.text;
          const source = typeof ex === 'string' ? '' : (ex.source || '');
          return `<div class="vocab-example"><button class="btn-tts-inline btn-tts-example" title="英式朗读" onclick="event.stopPropagation(); speak('${escapeAttr(text)}')">🔊</button>${escapeHtml(text)}${source ? `<span class="vocab-example-source">— ${source}</span>` : ''}</div>`;
        }).join('')}
      </div>
      ${v.collocations && v.collocations.length > 0 ? `<div class="vocab-collocations">${v.collocations.map(c => `<span class="collocation-tag">${c}</span>`).join('')}</div>` : ''}
      <div class="vocab-actions">
        <button class="btn-save" onclick="saveWord('${escapeAttr(v.word)}', '${escapeAttr(v.chinese + ' — ' + v.definition)}', '${escapeAttr(typeof v.examples[0] === 'string' ? v.examples[0] : v.examples[0]?.text || '')}', this)">收藏</button>
      </div>
    </div>
  `).join('');
}

function renderPhrasesTab(phrases) {
  const container = document.getElementById('tab-phrases');
  if (phrases.length === 0) { container.innerHTML = '<div class="analysis-empty">未发现已收录的高级词组</div>'; return; }
  container.innerHTML = phrases.map((p, i) => `
    <div class="phrase-card" data-key="${p.phrase.toLowerCase()}">
      <div class="vocab-card-header">
        <span class="phrase-text">${p.phrase}</span>
        <button class="btn-tts-inline" title="英式朗读" onclick="event.stopPropagation(); speak('${escapeAttr(p.phrase)}', {rate: 0.85})">🔊</button>
        <span class="vocab-level">${p.level}</span>
      </div>
      <div class="vocab-chinese">${p.chinese}</div>
      <div class="vocab-def">${p.definition}</div>
      ${p.linguistics ? `<div class="pattern-desc" style="margin:var(--space-sm) 0;line-height:1.7;font-size:0.82rem"><strong style="color:var(--ink)">语言学解析：</strong>${escapeHtml(p.linguistics)}</div>` : ''}
      ${p.usage ? `<div class="pattern-tip" style="margin:var(--space-sm) 0"><strong>用法与替换：</strong>${escapeHtml(p.usage)}</div>` : ''}
      <div class="vocab-examples">
        <div class="vocab-examples-title">例句</div>
        ${p.examples.map(ex => {
          const text = typeof ex === 'string' ? ex : ex.text;
          const source = typeof ex === 'string' ? '' : (ex.source || '');
          return `<div class="vocab-example">${escapeHtml(text)}${source ? `<span class="vocab-example-source">— ${source}</span>` : ''}</div>`;
        }).join('')}
      </div>
      <div class="vocab-actions">
        <button class="btn-save" onclick="saveWord('${escapeAttr(p.phrase)}', '${escapeAttr(p.chinese + ' — ' + p.definition)}', '${escapeAttr(typeof p.examples[0] === 'string' ? p.examples[0] : p.examples[0]?.text || '')}', this)">收藏</button>
      </div>
    </div>
  `).join('');
}

function renderSentencesTab(sentences) {
  const container = document.getElementById('tab-patterns');
  if (!sentences || sentences.length === 0) { container.innerHTML = '<div class="analysis-empty">暂无长难句解读</div>'; return; }

  // Support both old format (sentence_patterns) and new format (complex_sentences)
  container.innerHTML = sentences.map((s, i) => {
    // New deep-reading format
    if (s.sentence) {
      return `
        <div class="pattern-card" id="sentence-card-${i}" style="margin-bottom:1.2rem">
          <div class="pattern-found" style="border-left-color:var(--accent);font-style:normal;font-size:0.92rem;color:var(--ink);line-height:1.8;margin:0 0 var(--space-sm) 0">
            <span class="pattern-found-label" style="color:var(--accent)">长难句 #${i + 1}</span>
            <button class="btn-tts-inline" title="英式朗读" onclick="event.stopPropagation(); speak('${escapeAttr(s.sentence)}')">🔊</button>
            ${escapeHtml(s.sentence)}
          </div>
          <div class="vocab-chinese" style="margin:var(--space-sm) 0;font-size:0.88rem">翻译：${escapeHtml(s.translation)}</div>
          <div class="pattern-desc" style="line-height:1.7">
            <strong style="color:var(--ink)">句子拆解：</strong>${escapeHtml(s.breakdown)}
          </div>
          ${s.grammar_points && s.grammar_points.length > 0 ? `
            <div style="margin-top:var(--space-sm)">
              <div class="vocab-examples-title">语法要点</div>
              ${s.grammar_points.map(gp => `<div class="vocab-example">${escapeHtml(gp)}</div>`).join('')}
            </div>
          ` : ''}
          ${s.writing_tip ? `<div class="pattern-tip" style="margin-top:var(--space-sm);line-height:1.7"><strong>写作借鉴：</strong>${escapeHtml(s.writing_tip)}</div>` : ''}
        </div>
      `;
    }
    // Old format fallback
    return `
      <div class="pattern-card">
        <div class="pattern-name">${s.pattern || ''}</div>
        <div class="pattern-chinese">${s.chinese || ''}</div>
        <div class="pattern-desc">${s.description || ''}</div>
        ${s.found_sentence ? `<div class="pattern-found"><span class="pattern-found-label">文中实例</span>${escapeHtml(s.found_sentence)}</div>` : ''}
        ${s.model_example ? `<div class="pattern-model"><span class="pattern-model-label">范例</span>${escapeHtml(s.model_example)}</div>` : ''}
        ${s.usage_tip ? `<div class="pattern-tip">${s.usage_tip}</div>` : ''}
      </div>
    `;
  }).join('');
}

// ═══ PASTE & ANALYZE ═══
async function analyzeText() {
  const titleEl = document.getElementById('paste-title');
  const textEl = document.getElementById('paste-text');
  const btn = document.querySelector('.btn-analyze');
  const title = titleEl.value.trim(), text = textEl.value.trim();
  if (!text) { notify('请先粘贴文章内容', 'error'); return; }
  if (text.length < 100) { notify('文章内容太短，请粘贴完整的文章', 'error'); return; }

  btn.disabled = true;
  btn.querySelector('.btn-text').style.display = 'none';
  btn.querySelector('.btn-loading').style.display = 'inline';
  try {
    const res = await fetch('/api/analyze', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text, title }) });
    const data = await res.json();
    if (data.success) {
      currentAnalysis = data.analysis;
      currentArticleText = text;
      showView('reader');
      document.getElementById('reader-source').textContent = '用户粘贴';
      document.getElementById('reader-title').textContent = title || '粘贴文章';
      renderReader({ title: title || '粘贴文章', source: '用户粘贴', full_text: text }, data.analysis);
    } else { notify(data.error || '分析失败', 'error'); }
  } catch (err) { notify('分析失败，请检查网络', 'error'); }
  finally { btn.disabled = false; btn.querySelector('.btn-text').style.display = 'inline'; btn.querySelector('.btn-loading').style.display = 'none'; }
}

// ═══ TABS ═══
function switchTab(tabName) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.toggle('active', btn.dataset.tab === tabName));
  document.querySelectorAll('.tab-content').forEach(c => c.classList.toggle('active', c.id === 'tab-' + tabName));
}

// ═══ VOCABULARY CRUD ═══
async function saveWord(word, definition, example, btnEl) {
  try {
    const res = await fetch('/api/vocabulary', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ word, definition, example, source: currentAnalysis?.title || '未知来源' }) });
    const data = await res.json();
    if (data.success) { btnEl.classList.add('saved'); btnEl.textContent = '已收藏'; btnEl.onclick = null; notify(`「${word}」已加入生词本`, 'success'); }
  } catch (err) { notify('收藏失败', 'error'); }
}

async function loadVocabulary() {
  const container = document.getElementById('vocab-list');
  try {
    const res = await fetch('/api/vocabulary');
    const data = await res.json();
    if (data.success && data.vocabulary.length > 0) { renderVocabularyList(data.vocabulary); }
    else { container.innerHTML = '<div class="empty-state"><p class="empty-icon">&#9733;</p><p>还没有收藏的词汇</p><p class="empty-hint">在精读文章时，点击词汇卡片上的「收藏」按钮即可添加</p></div>'; }
  } catch (err) { container.innerHTML = '<div class="empty-state"><p>加载失败</p></div>'; }
}

function renderVocabularyList(vocab) {
  const container = document.getElementById('vocab-list');
  container.innerHTML = vocab.map((v, i) => `
    <div class="vocab-saved-card" id="saved-vocab-${i}">
      <div class="vocab-saved-info">
        <div class="vocab-saved-word">${escapeHtml(v.word)}</div>
        <div class="vocab-saved-def">${escapeHtml(v.definition)}</div>
        ${v.example ? `<div class="vocab-saved-def" style="font-style:italic;margin-top:4px;">"${escapeHtml(v.example)}"</div>` : ''}
        <div class="vocab-saved-source">来源: ${escapeHtml(v.source || '未知')} · 已复习 ${v.review_count || 0} 次</div>
      </div>
      <div class="vocab-saved-actions">
        <button class="btn-review" onclick="reviewWord(${i})">复习</button>
        <button class="btn-delete" onclick="deleteWord(${i})">删除</button>
      </div>
    </div>
  `).join('');
}

async function reviewWord(index) {
  try { const res = await fetch(`/api/vocabulary/${index}/review`, { method: 'POST' }); const d = await res.json(); if (d.success) { notify('已标记复习', 'success'); loadVocabulary(); } } catch (e) { notify('操作失败', 'error'); }
}
async function deleteWord(index) {
  try { const res = await fetch(`/api/vocabulary/${index}`, { method: 'DELETE' }); const d = await res.json(); if (d.success) { notify(`已删除「${d.removed.word}」`, 'success'); loadVocabulary(); } } catch (e) { notify('删除失败', 'error'); }
}

// ═══ NOTIFICATIONS ═══
function notify(message, type = 'info') {
  const existing = document.querySelector('.notification');
  if (existing) existing.remove();
  const el = document.createElement('div');
  el.className = `notification ${type}`;
  el.textContent = message;
  document.body.appendChild(el);
  requestAnimationFrame(() => el.classList.add('show'));
  setTimeout(() => { el.classList.remove('show'); setTimeout(() => el.remove(), 400); }, 3500);
}

// ═══ UTILITIES ═══
function escapeHtml(str) { if (!str) return ''; const d = document.createElement('div'); d.textContent = str; return d.innerHTML; }
function escapeAttr(str) { if (!str) return ''; return str.replace(/'/g, "\\'").replace(/"/g, '\\"').replace(/\n/g, ' '); }
function escapeRegExp(str) { return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

/**
 * Safely highlight a word/phrase in HTML text — only matches text OUTSIDE of HTML tags.
 * Splits the string by tags, applies the regex only to text segments.
 */
function highlightInTextNodes(html, target, wrapFn, wordBoundary) {
  // Split into [text, tag, text, tag, ...] — odd indices are text, even are tags (or vice versa)
  const parts = html.split(/(<[^>]+>)/);
  const pattern = wordBoundary
    ? new RegExp('(?<![\\w])(' + escapeRegExp(target) + ')(?![\\w])', 'gi')
    : new RegExp('(' + escapeRegExp(target) + ')', 'gi');
  for (let i = 0; i < parts.length; i++) {
    // Skip HTML tags (those starting with <)
    if (parts[i].startsWith('<')) continue;
    parts[i] = parts[i].replace(pattern, (_, m) => wrapFn(m));
  }
  return parts.join('');
}

// ═══ DOUBLE-CLICK WORD LOOKUP ═══
const COMMON_CHINESE = {
  'the': '定冠词', 'a': '不定冠词', 'an': '不定冠词',
  'abandon': '放弃', 'ability': '能力', 'able': '能够的', 'about': '关于',
  'above': '在...上方', 'abroad': '在国外', 'absence': '缺席', 'absolute': '绝对的',
  'absorb': '吸收', 'abstract': '抽象的', 'abuse': '滥用', 'academic': '学术的',
  'accept': '接受', 'access': '进入；通道', 'accident': '事故', 'accomplish': '完成',
  'account': '账户；解释', 'accurate': '准确的', 'accuse': '指控', 'achieve': '实现',
  'acknowledge': '承认', 'acquire': '获得', 'adapt': '适应', 'add': '添加',
  'address': '地址；处理', 'adequate': '充足的', 'adjust': '调整', 'administration': '管理',
  'admire': '钦佩', 'admit': '承认', 'adopt': '采纳；收养', 'adult': '成年人',
  'advance': '前进；进步', 'advantage': '优势', 'adventure': '冒险', 'advice': '建议',
  'advocate': '倡导者；提倡', 'affect': '影响', 'afford': '负担得起', 'afraid': '害怕的',
  'agenda': '议程', 'agent': '代理人', 'aggressive': '侵略性的', 'agree': '同意',
  'agriculture': '农业', 'aid': '援助', 'aim': '目标；瞄准', 'air': '空气',
  'algorithm': '算法', 'alien': '外星人；外来的', 'align': '对齐', 'allow': '允许',
  'ally': '盟友', 'almost': '几乎', 'alone': '独自的', 'already': '已经',
  'alternative': '替代方案', 'although': '虽然', 'altogether': '完全地', 'always': '总是',
  'ambition': '抱负', 'amend': '修改', 'among': '在...之中', 'amount': '数量',
  'analysis': '分析', 'analyze': '分析', 'ancient': '古代的', 'anger': '愤怒',
  'angle': '角度', 'announce': '宣布', 'annual': '年度的', 'anxiety': '焦虑',
  'apart': '分开', 'apparent': '明显的', 'appeal': '呼吁；吸引力', 'appear': '出现',
  'apply': '申请；应用', 'appoint': '任命', 'approach': '接近；方法', 'appropriate': '适当的',
  'approve': '批准', 'argue': '争论', 'arise': '出现；产生', 'army': '军队',
  'arrange': '安排', 'arrest': '逮捕', 'arrive': '到达', 'article': '文章',
  'artificial': '人工的', 'aspect': '方面', 'assert': '断言', 'assess': '评估',
  'asset': '资产', 'assign': '分配', 'assist': '协助', 'associate': '联系；伙伴',
  'assume': '假设', 'atmosphere': '气氛；大气', 'attach': '附上', 'attack': '攻击',
  'attempt': '尝试', 'attend': '参加', 'attention': '注意力', 'attitude': '态度',
  'attract': '吸引', 'audience': '观众', 'authority': '权威', 'available': '可用的',
  'average': '平均的', 'avoid': '避免', 'aware': '意识到的', 'awful': '糟糕的',
  'balance': '平衡', 'ban': '禁止', 'barrier': '障碍', 'base': '基础',
  'basic': '基本的', 'battle': '战斗', 'bear': '承受；熊', 'beat': '打败',
  'beautiful': '美丽的', 'because': '因为', 'become': '成为', 'before': '在...之前',
  'begin': '开始', 'behavior': '行为', 'behind': '在...后面', 'believe': '相信',
  'belong': '属于', 'below': '在...下面', 'benefit': '好处；受益', 'besides': '此外',
  'better': '更好的', 'between': '在...之间', 'beyond': '超越', 'billion': '十亿',
  'bind': '绑定', 'blame': '责备', 'block': '阻塞；街区', 'blow': '吹',
  'board': '董事会；板', 'bond': '债券；纽带', 'border': '边界', 'born': '出生',
  'bother': '打扰', 'bottom': '底部', 'bound': '必然的', 'brain': '大脑',
  'branch': '分支', 'brand': '品牌', 'brave': '勇敢的', 'breach': '违反',
  'break': '打破', 'brief': '简短的', 'broad': '广泛的', 'budget': '预算',
  'build': '建造', 'burden': '负担', 'burn': '燃烧', 'burst': '爆发',
  'bury': '埋葬', 'campaign': '运动', 'capable': '有能力的', 'capacity': '能力；容量',
  'capital': '首都；资本', 'capture': '捕获', 'carbon': '碳', 'career': '职业',
  'careful': '仔细的', 'carry': '携带', 'case': '案例', 'cast': '投射',
  'catch': '抓住', 'category': '类别', 'cause': '原因；导致', 'celebrate': '庆祝',
  'center': '中心', 'central': '中央的', 'century': '世纪', 'certain': '确定的',
  'chain': '链条', 'chair': '椅子；主席', 'challenge': '挑战', 'champion': '冠军',
  'chance': '机会', 'change': '改变', 'channel': '渠道', 'chapter': '章节',
  'character': '角色；性格', 'charge': '收费；指控', 'charity': '慈善', 'chart': '图表',
  'chase': '追逐', 'cheap': '便宜的', 'check': '检查', 'chief': '首席的',
  'choice': '选择', 'choose': '选择', 'citizen': '公民', 'civil': '民事的',
  'claim': '声称', 'class': '班级；阶级', 'classic': '经典的', 'clean': '干净的',
  'clear': '清楚的', 'climate': '气候', 'close': '关闭；接近的', 'cloud': '云',
  'coalition': '联盟', 'code': '代码', 'cognitive': '认知的', 'collapse': '崩溃',
  'colleague': '同事', 'collect': '收集', 'column': '列；专栏', 'combine': '结合',
  'comfort': '舒适', 'command': '命令', 'comment': '评论', 'commit': '承诺；犯',
  'common': '共同的', 'communicate': '沟通', 'community': '社区', 'company': '公司',
  'compare': '比较', 'compete': '竞争', 'complex': '复杂的', 'component': '组成部分',
  'compose': '组成', 'comprehensive': '全面的', 'compromise': '妥协', 'concept': '概念',
  'concern': '关注；担忧', 'conclude': '总结', 'condition': '条件', 'conduct': '进行；行为',
  'conference': '会议', 'confidence': '信心', 'confirm': '确认', 'conflict': '冲突',
  'confront': '面对', 'congress': '国会', 'connect': '连接', 'conscience': '良心',
  'conscious': '有意识的', 'consensus': '共识', 'consequence': '后果', 'conservative': '保守的',
  'consider': '考虑', 'consist': '组成', 'constant': '不断的', 'constitute': '构成',
  'construct': '建造', 'consume': '消费', 'contact': '联系', 'contain': '包含',
  'contemporary': '当代的', 'content': '内容；满意的', 'context': '上下文', 'continue': '继续',
  'contract': '合同', 'contrast': '对比', 'contribute': '贡献', 'control': '控制',
  'controversy': '争议', 'convention': '惯例；大会', 'conversation': '对话', 'convert': '转换',
  'convince': '说服', 'cooperate': '合作', 'cope': '应对', 'core': '核心',
  'corporate': '企业的', 'correct': '正确的', 'correspond': '对应', 'cost': '花费',
  'council': '理事会', 'count': '计数', 'counter': '柜台；反驳', 'country': '国家',
  'couple': '一对', 'courage': '勇气', 'course': '课程；过程', 'court': '法院',
  'cover': '覆盖', 'crack': '裂缝', 'craft': '手艺', 'crash': '碰撞',
  'create': '创造', 'credit': '信用', 'crew': '船员', 'crime': '犯罪',
  'criminal': '犯罪的', 'crisis': '危机', 'criteria': '标准', 'critical': '关键的；批评的',
  'criticism': '批评', 'crop': '庄稼', 'cross': '穿越', 'crowd': '人群',
  'crucial': '至关重要的', 'cultural': '文化的', 'culture': '文化', 'current': '当前的；水流',
  'curve': '曲线', 'custom': '习惯', 'customer': '客户', 'cycle': '循环',
  'damage': '损害', 'danger': '危险', 'dare': '敢', 'data': '数据',
  'debate': '辩论', 'debt': '债务', 'decade': '十年', 'decent': '体面的',
  'decide': '决定', 'decision': '决定', 'declare': '宣布', 'decline': '下降',
  'deep': '深的', 'defeat': '击败', 'defend': '防御', 'define': '定义',
  'degree': '程度；学位', 'delay': '延迟', 'deliver': '交付', 'demand': '需求；要求',
  'democracy': '民主', 'demonstrate': '展示', 'deny': '否认', 'department': '部门',
  'depend': '依靠', 'deploy': '部署', 'depression': '萧条；抑郁', 'derive': '源于',
  'describe': '描述', 'desert': '沙漠', 'deserve': '值得', 'design': '设计',
  'desire': '渴望', 'despite': '尽管', 'destroy': '摧毁', 'detail': '细节',
  'detect': '检测', 'determine': '决定', 'develop': '发展', 'device': '设备',
  'devote': '奉献', 'dialogue': '对话', 'differ': '不同', 'digital': '数字的',
  'dimension': '维度', 'direct': '直接的', 'direction': '方向', 'disappear': '消失',
  'discipline': '纪律', 'discover': '发现', 'discrimination': '歧视', 'discuss': '讨论',
  'disease': '疾病', 'dismiss': '解雇', 'disorder': '混乱', 'display': '展示',
  'dispute': '争端', 'distance': '距离', 'distinct': '不同的', 'distinguish': '区分',
  'distribute': '分配', 'district': '地区', 'disturb': '打扰', 'diverse': '多样的',
  'divide': '分割', 'document': '文件', 'domain': '领域', 'domestic': '国内的',
  'dominate': '主导', 'doubt': '怀疑', 'draft': '草案', 'drag': '拖',
  'drain': '排水', 'drama': '戏剧', 'dramatic': '戏剧性的', 'draw': '画；吸引',
  'dream': '梦想', 'drive': '驱动', 'drop': '下降', 'drug': '药物；毒品',
  'due': '由于', 'dump': '倾倒', 'duration': '持续时间', 'during': '在...期间',
  'duty': '职责', 'dynamic': '动态的', 'eager': '渴望的', 'earn': '赚取',
  'ease': '缓解', 'economic': '经济的', 'economy': '经济', 'edge': '边缘',
  'edition': '版本', 'editor': '编辑', 'educate': '教育', 'effect': '效果',
  'effective': '有效的', 'efficient': '高效的', 'effort': '努力', 'elaborate': '详尽的',
  'elect': '选举', 'element': '元素', 'eliminate': '消除', 'elite': '精英',
  'else': '其他的', 'embrace': '拥抱；接受', 'emerge': '出现', 'emergency': '紧急情况',
  'emission': '排放', 'emotion': '情感', 'emphasis': '强调', 'empire': '帝国',
  'employ': '雇用', 'enable': '使能够', 'encounter': '遭遇', 'encourage': '鼓励',
  'end': '结束', 'enemy': '敌人', 'energy': '能量', 'enforce': '执行',
  'engage': '参与', 'engine': '引擎', 'engineer': '工程师', 'enhance': '增强',
  'enjoy': '享受', 'enormous': '巨大的', 'enough': '足够的', 'ensure': '确保',
  'enterprise': '企业', 'entire': '整个的', 'entity': '实体', 'environment': '环境',
  'episode': '插曲', 'equal': '平等的', 'equip': '装备', 'era': '时代',
  'error': '错误', 'escape': '逃脱', 'especially': '特别', 'essay': '论文',
  'essential': '必要的', 'establish': '建立', 'estate': '房产', 'estimate': '估计',
  'evaluate': '评估', 'even': '甚至', 'event': '事件', 'eventually': '最终',
  'every': '每个', 'evidence': '证据', 'evil': '邪恶的', 'evolution': '进化',
  'evolve': '进化', 'exact': '精确的', 'examine': '检查', 'example': '例子',
  'exceed': '超过', 'excellent': '优秀的', 'except': '除了', 'exception': '例外',
  'exchange': '交换', 'excitement': '兴奋', 'exclude': '排除', 'execute': '执行',
  'exercise': '练习', 'exhibit': '展览', 'exist': '存在', 'expand': '扩展',
  'expect': '期望', 'expenditure': '支出', 'expense': '费用', 'experience': '经验',
  'experiment': '实验', 'expert': '专家', 'explain': '解释', 'explicit': '明确的',
  'exploit': '利用', 'explore': '探索', 'export': '出口', 'expose': '暴露',
  'express': '表达', 'extend': '延伸', 'extensive': '广泛的', 'extent': '程度',
  'external': '外部的', 'extra': '额外的', 'extraordinary': '非凡的', 'extreme': '极端的',
  'face': '面对；脸', 'facility': '设施', 'fact': '事实', 'factor': '因素',
  'faculty': '院系', 'fail': '失败', 'fair': '公平的', 'faith': '信仰',
  'fall': '下降；秋天', 'false': '错误的', 'familiar': '熟悉的', 'family': '家庭',
  'famous': '著名的', 'far': '远的', 'fashion': '时尚', 'fate': '命运',
  'favor': '偏爱', 'fear': '恐惧', 'feature': '特征', 'federal': '联邦的',
  'feed': '喂养', 'feel': '感觉', 'fellow': '同伴', 'female': '女性的',
  'fence': '围栏', 'fiction': '小说', 'field': '领域；田地', 'fierce': '激烈的',
  'fight': '战斗', 'figure': '数字；人物', 'file': '文件', 'fill': '填充',
  'final': '最终的', 'finance': '金融', 'find': '发现', 'fine': '好的；罚款',
  'finger': '手指', 'finish': '完成', 'firm': '公司；坚定的', 'fit': '适合',
  'fix': '修理', 'flag': '旗帜', 'flame': '火焰', 'flash': '闪光',
  'flat': '平坦的', 'flee': '逃跑', 'flesh': '肉体', 'flexible': '灵活的',
  'flight': '航班', 'float': '漂浮', 'flood': '洪水', 'floor': '地板',
  'flow': '流动', 'focus': '集中', 'fold': '折叠', 'folk': '民间的',
  'follow': '跟随', 'food': '食物', 'fool': '愚蠢的人', 'foot': '脚',
  'force': '力量；强迫', 'foreign': '外国的', 'forest': '森林', 'forever': '永远',
  'forget': '忘记', 'form': '形式', 'formal': '正式的', 'former': '以前的',
  'formula': '公式', 'forth': '向前', 'fortune': '财富', 'forward': '向前',
  'fossil': '化石', 'found': '创立', 'foundation': '基金会', 'frame': '框架',
  'framework': '框架', 'free': '自由的', 'freedom': '自由', 'frequent': '频繁的',
  'fresh': '新鲜的', 'friend': '朋友', 'front': '前面', 'fruit': '水果',
  'fuel': '燃料', 'fulfill': '完成', 'full': '满的', 'function': '功能',
  'fund': '基金', 'fundamental': '基本的', 'furniture': '家具', 'furthermore': '此外',
  'future': '未来', 'gain': '获得', 'gap': '差距', 'gate': '门',
  'gather': '聚集', 'gaze': '凝视', 'gender': '性别', 'gene': '基因',
  'general': '一般的', 'generate': '产生', 'generation': '一代人', 'generous': '慷慨的',
  'genius': '天才', 'gentle': '温和的', 'genuine': '真正的', 'gesture': '姿态',
  'giant': '巨大的', 'gift': '礼物', 'given': '鉴于', 'glad': '高兴的',
  'global': '全球的', 'glory': '荣耀', 'goal': '目标', 'golden': '金色的',
  'good': '好的', 'govern': '治理', 'government': '政府', 'governor': '州长',
  'grab': '抓住', 'grace': '优雅', 'grade': '等级', 'gradually': '逐渐地',
  'grain': '谷物', 'grand': '宏大的', 'grant': '授予', 'grasp': '抓住；理解',
  'grave': '坟墓；严重的', 'great': '伟大的', 'green': '绿色的', 'grip': '握紧',
  'gross': '总的', 'ground': '地面', 'group': '组', 'grow': '增长',
  'growth': '增长', 'guarantee': '保证', 'guard': '守卫', 'guess': '猜测',
  'guide': '引导', 'guilty': '有罪的', 'gun': '枪',
  'habit': '习惯', 'half': '一半', 'halt': '停止', 'hand': '手',
  'handle': '处理', 'happen': '发生', 'happy': '快乐的', 'harbor': '港口',
  'hard': '困难的', 'hardly': '几乎不', 'harm': '伤害', 'harsh': '严厉的',
  'hate': '恨', 'head': '头；领导', 'health': '健康', 'hear': '听到',
  'heart': '心脏', 'heat': '热量', 'heavy': '重的', 'height': '高度',
  'help': '帮助', 'hence': '因此', 'heritage': '遗产', 'hero': '英雄',
  'hide': '隐藏', 'high': '高的', 'highlight': '强调', 'highly': '高度地',
  'hire': '雇用', 'historian': '历史学家', 'history': '历史', 'hit': '打击',
  'hold': '持有', 'hole': '洞', 'holy': '神圣的', 'home': '家',
  'honest': '诚实的', 'honor': '荣誉', 'hope': '希望', 'horizon': '地平线',
  'horror': '恐怖', 'host': '主人', 'hostile': '敌对的', 'household': '家庭',
  'housing': '住房', 'huge': '巨大的', 'human': '人类的', 'humor': '幽默',
  'hunt': '打猎', 'hypothesis': '假说',
  'idea': '想法', 'ideal': '理想的', 'identify': '识别', 'identity': '身份',
  'ignore': '忽视', 'illegal': '非法的', 'illustrate': '说明', 'image': '形象',
  'imagine': '想象', 'immediate': '立即的', 'immigrant': '移民', 'immune': '免疫的',
  'impact': '影响', 'implement': '实施', 'implication': '含义', 'imply': '暗示',
  'import': '进口', 'impose': '施加', 'impossible': '不可能的', 'impress': '给人印象',
  'impression': '印象', 'improve': '改善', 'incident': '事件', 'include': '包括',
  'income': '收入', 'increase': '增加', 'indeed': '确实', 'independent': '独立的',
  'index': '指数', 'indicate': '表明', 'individual': '个人的', 'industrial': '工业的',
  'industry': '行业', 'inevitable': '不可避免的', 'infant': '婴儿', 'inflation': '通货膨胀',
  'influence': '影响', 'inform': '通知', 'initial': '最初的', 'initiative': '倡议',
  'injury': '受伤', 'inner': '内部的', 'innocent': '无辜的', 'innovation': '创新',
  'input': '投入', 'inquiry': '调查', 'insert': '插入', 'inside': '在...里面',
  'insight': '洞察力', 'insist': '坚持', 'inspire': '启发', 'install': '安装',
  'instance': '例子', 'instead': '代替', 'institute': '研究所', 'institution': '机构',
  'instrument': '工具', 'insurance': '保险', 'integrate': '整合', 'intellectual': '知识分子',
  'intelligence': '智力', 'intend': '打算', 'intense': '紧张的', 'intention': '意图',
  'interact': '互动', 'interest': '兴趣', 'internal': '内部的', 'international': '国际的',
  'interpret': '解释', 'intervention': '干预', 'interview': '面试', 'introduce': '介绍',
  'invade': '入侵', 'invest': '投资', 'investigate': '调查', 'investment': '投资',
  'investor': '投资者', 'invisible': '看不见的', 'invite': '邀请', 'involve': '涉及',
  'iron': '铁', 'isolate': '隔离', 'issue': '问题；发行',
  'joint': '联合的', 'journal': '期刊', 'journey': '旅程', 'judge': '法官；判断',
  'judgment': '判断', 'junior': '初级的', 'jury': '陪审团', 'justice': '公正',
  'justify': '证明...正当', 'keen': '敏锐的', 'keep': '保持', 'key': '关键的',
  'kick': '踢', 'kill': '杀死', 'kind': '种类；善良的', 'king': '国王',
  'knee': '膝盖', 'knock': '敲', 'know': '知道', 'knowledge': '知识',
  'label': '标签', 'labor': '劳动', 'lack': '缺乏', 'land': '土地',
  'landscape': '景观', 'language': '语言', 'large': '大的', 'largely': '在很大程度上',
  'last': '最后的', 'late': '迟的', 'launch': '发射', 'law': '法律',
  'layer': '层', 'lead': '领导', 'leader': '领导者', 'leadership': '领导力',
  'lean': '倾斜', 'learn': '学习', 'least': '最少的', 'leave': '离开',
  'legacy': '遗产', 'legal': '合法的', 'legend': '传说', 'legislation': '立法',
  'legitimate': '合法的', 'lend': '借出', 'lesson': '课程', 'level': '水平',
  'liberal': '自由的', 'liberty': '自由', 'library': '图书馆', 'license': '执照',
  'life': '生活', 'lift': '举起', 'light': '光', 'like': '喜欢；像',
  'likely': '可能的', 'limit': '限制', 'line': '线', 'link': '链接',
  'list': '列表', 'listen': '听', 'literary': '文学的', 'literature': '文学',
  'little': '少的', 'live': '生活', 'load': '负荷', 'loan': '贷款',
  'local': '当地的', 'locate': '位于', 'lock': '锁', 'long': '长的',
  'look': '看', 'loose': '松散的', 'lord': '领主', 'lose': '失去',
  'loss': '损失', 'lot': '许多', 'love': '爱', 'low': '低的',
  'lucky': '幸运的', 'lunch': '午餐',
  'machine': '机器', 'magazine': '杂志', 'magic': '魔法', 'main': '主要的',
  'maintain': '维护', 'major': '主要的', 'majority': '多数', 'male': '男性的',
  'manage': '管理', 'manner': '方式', 'manufacture': '制造', 'many': '许多',
  'map': '地图', 'march': '游行', 'margin': '边距', 'mark': '标记',
  'market': '市场', 'marriage': '婚姻', 'marry': '结婚', 'mask': '面具',
  'mass': '大量', 'massive': '大量的', 'master': '掌握', 'match': '匹配',
  'material': '材料', 'matter': '事情', 'mature': '成熟的', 'maximum': '最大的',
  'may': '可能', 'mean': '意味着', 'meaning': '意义', 'measure': '测量',
  'mechanism': '机制', 'media': '媒体', 'medical': '医疗的', 'medicine': '医学',
  'medium': '中等的', 'meet': '遇见', 'member': '成员', 'membership': '会员资格',
  'memory': '记忆', 'mental': '精神的', 'mention': '提到', 'merchant': '商人',
  'mere': '仅仅的', 'merge': '合并', 'merit': '优点', 'message': '消息',
  'method': '方法', 'middle': '中间的', 'might': '可能', 'military': '军事的',
  'mind': '头脑', 'mine': '我的；矿', 'minimum': '最小的', 'minister': '部长',
  'minor': '次要的', 'minority': '少数', 'minute': '分钟', 'miracle': '奇迹',
  'mirror': '镜子', 'miss': '错过', 'mission': '使命', 'mistake': '错误',
  'mix': '混合', 'model': '模型', 'moderate': '温和的', 'modern': '现代的',
  'modest': '谦虚的', 'modify': '修改', 'moment': '时刻', 'monitor': '监控',
  'mood': '心情', 'moral': '道德的', 'moreover': '此外', 'mostly': '大多数',
  'motion': '运动', 'motivate': '激励', 'mount': '增加', 'mountain': '山',
  'move': '移动', 'movement': '运动', 'multiple': '多个的', 'murder': '谋杀',
  'muscle': '肌肉', 'mutual': '相互的', 'mystery': '神秘', 'myth': '神话',
  'naked': '裸体的', 'name': '名字', 'narrative': '叙事', 'narrow': '狭窄的',
  'nation': '国家', 'national': '国家的', 'native': '本地的', 'natural': '自然的',
  'nature': '自然', 'near': '近的', 'nearly': '几乎', 'neat': '整洁的',
  'necessary': '必要的', 'need': '需要', 'negative': '消极的', 'negotiate': '谈判',
  'neighbor': '邻居', 'neither': '两者都不', 'nerve': '神经', 'network': '网络',
  'neutral': '中立的', 'never': '从不', 'nevertheless': '然而', 'next': '下一个',
  'nice': '好的', 'night': '夜晚', 'nobody': '没有人', 'nod': '点头',
  'noise': '噪音', 'none': '没有', 'nonetheless': '尽管如此', 'nor': '也不',
  'normal': '正常的', 'north': '北方', 'notable': '值得注意的', 'note': '注意',
  'nothing': '什么都没有', 'notice': '注意', 'notion': '概念', 'novel': '新颖的；小说',
  'nuclear': '核的', 'number': '数字', 'numerous': '众多的', 'nurse': '护士',
  'object': '物体；反对', 'objective': '目标', 'obligation': '义务', 'observe': '观察',
  'obstacle': '障碍', 'obtain': '获得', 'obvious': '明显的', 'occasion': '场合',
  'occupy': '占据', 'occur': '发生', 'odd': '奇怪的', 'offend': '冒犯',
  'offer': '提供', 'office': '办公室', 'officer': '官员', 'official': '官方的',
  'often': '经常', 'ongoing': '持续的', 'online': '在线的', 'only': '仅仅',
  'open': '打开', 'operate': '操作', 'operation': '运作', 'opinion': '意见',
  'opponent': '对手', 'opportunity': '机会', 'oppose': '反对', 'opposite': '相反的',
  'option': '选择', 'order': '命令；秩序', 'ordinary': '普通的', 'organ': '器官',
  'organize': '组织', 'origin': '起源', 'original': '原始的', 'other': '其他的',
  'otherwise': '否则', 'ought': '应该', 'outcome': '结果', 'output': '产量',
  'outside': '在外面', 'outstanding': '杰出的', 'overcome': '克服', 'overlook': '忽略',
  'owe': '欠', 'own': '拥有',
  'pace': '步伐', 'pack': '打包', 'package': '包裹', 'page': '页面',
  'pain': '疼痛', 'paint': '画', 'pair': '一对', 'palace': '宫殿',
  'pale': '苍白的', 'panel': '面板', 'panic': '恐慌', 'paper': '纸',
  'parallel': '平行的', 'parent': '父母', 'part': '部分', 'partial': '部分的',
  'participate': '参加', 'particular': '特定的', 'partly': '部分地', 'partner': '伙伴',
  'party': '政党；聚会', 'pass': '通过', 'passage': '通道', 'passion': '热情',
  'past': '过去的', 'path': '路径', 'patience': '耐心', 'patient': '病人；耐心的',
  'pattern': '模式', 'pause': '暂停', 'pay': '支付', 'peace': '和平',
  'peak': '顶峰', 'peer': '同龄人', 'penalty': '惩罚', 'pension': '养老金',
  'people': '人们', 'perceive': '感知', 'percent': '百分比', 'perfect': '完美的',
  'perform': '执行', 'performance': '表现', 'perhaps': '也许', 'period': '时期',
  'permanent': '永久的', 'permit': '允许', 'persist': '坚持', 'person': '人',
  'personal': '个人的', 'perspective': '视角', 'persuade': '说服', 'phase': '阶段',
  'phenomenon': '现象', 'philosophy': '哲学', 'phrase': '短语', 'physical': '身体的',
  'pick': '挑选', 'picture': '图片', 'piece': '片', 'pilot': '飞行员',
  'pioneer': '先驱', 'pitch': '投', 'place': '地方', 'plain': '朴素的',
  'plan': '计划', 'planet': '行星', 'plant': '植物', 'plate': '盘子',
  'platform': '平台', 'play': '玩', 'player': '玩家', 'plead': '恳求',
  'pleasant': '愉快的', 'please': '请', 'pleasure': '快乐', 'plenty': '大量',
  'plot': '情节', 'plus': '加', 'pocket': '口袋', 'poem': '诗',
  'poet': '诗人', 'poetry': '诗歌', 'point': '要点', 'poison': '毒药',
  'policy': '政策', 'political': '政治的', 'politics': '政治', 'poll': '民调',
  'pollution': '污染', 'pool': '池塘', 'poor': '贫穷的', 'popular': '受欢迎的',
  'population': '人口', 'port': '港口', 'portion': '部分', 'portrait': '肖像',
  'pose': '摆姿势', 'position': '位置', 'positive': '积极的', 'possess': '拥有',
  'possibility': '可能性', 'possible': '可能的', 'post': '发布', 'potential': '潜力',
  'poverty': '贫困', 'power': '权力', 'powerful': '强大的', 'practical': '实际的',
  'practice': '练习', 'praise': '赞美', 'pray': '祈祷', 'precious': '珍贵的',
  'precise': '精确的', 'predict': '预测', 'prefer': '更喜欢', 'pregnant': '怀孕的',
  'premise': '前提', 'premium': '保费', 'prepare': '准备', 'presence': '存在',
  'present': '当前的；礼物', 'preserve': '保存', 'president': '总统', 'press': '按；媒体',
  'pressure': '压力', 'presume': '假定', 'pretend': '假装', 'pretty': '漂亮的',
  'prevent': '防止', 'previous': '以前的', 'price': '价格', 'pride': '骄傲',
  'primary': '主要的', 'prime': '主要的', 'prince': '王子', 'principle': '原则',
  'print': '打印', 'prior': '先前的', 'priority': '优先', 'prison': '监狱',
  'privacy': '隐私', 'private': '私人的', 'prize': '奖品', 'probable': '很可能的',
  'probably': '可能', 'probe': '调查', 'problem': '问题', 'procedure': '程序',
  'proceed': '继续', 'process': '过程', 'produce': '生产', 'product': '产品',
  'production': '生产', 'profession': '职业', 'professional': '专业的', 'professor': '教授',
  'profile': '简介', 'profit': '利润', 'program': '项目', 'progress': '进步',
  'project': '项目', 'prominent': '突出的', 'promise': '承诺', 'promote': '促进',
  'prompt': '促使', 'proof': '证据', 'proper': '适当的', 'property': '财产',
  'proportion': '比例', 'proposal': '提议', 'propose': '提议', 'prospect': '前景',
  'prosperity': '繁荣', 'protect': '保护', 'protest': '抗议', 'prove': '证明',
  'provide': '提供', 'province': '省份', 'provision': '规定', 'provoke': '激怒',
  'psychological': '心理的', 'psychology': '心理学', 'public': '公众的', 'publish': '发表',
  'pull': '拉', 'punish': '惩罚', 'purchase': '购买', 'pure': '纯的',
  'purpose': '目的', 'pursue': '追求', 'push': '推', 'put': '放',
  'qualify': '使合格', 'quality': '质量', 'quarter': '四分之一', 'question': '问题',
  'quick': '快的', 'quiet': '安静的', 'quit': '退出', 'quite': '相当',
  'quote': '引用',
  'race': '种族；比赛', 'racial': '种族的', 'radical': '激进的', 'rage': '愤怒',
  'raise': '提高', 'range': '范围', 'rank': '排名', 'rapid': '迅速的',
  'rare': '稀有的', 'rate': '比率', 'rather': '相当', 'raw': '原始的',
  'reach': '到达', 'react': '反应', 'read': '读', 'ready': '准备好的',
  'real': '真实的', 'realistic': '现实的', 'reality': '现实', 'realize': '意识到',
  'really': '真的', 'reason': '原因', 'reasonable': '合理的', 'recall': '回忆',
  'receive': '收到', 'recent': '最近的', 'recognize': '认出', 'recommend': '推荐',
  'record': '记录', 'recover': '恢复', 'recruit': '招募', 'reduce': '减少',
  'refer': '参考', 'reference': '参考', 'reflect': '反映', 'reform': '改革',
  'refuse': '拒绝', 'regard': '关于', 'regime': '政权', 'region': '地区',
  'register': '注册', 'regret': '后悔', 'regular': '定期的', 'regulate': '调节',
  'regulation': '法规', 'reinforce': '加强', 'reject': '拒绝', 'relate': '联系',
  'relation': '关系', 'relationship': '关系', 'relative': '相对的', 'relax': '放松',
  'release': '释放', 'relevant': '相关的', 'relief': '救济', 'religion': '宗教',
  'reluctant': '不情愿的', 'rely': '依赖', 'remain': '保持', 'remark': '评论',
  'remarkable': '显著的', 'remedy': '补救', 'remember': '记住', 'remind': '提醒',
  'remote': '远程的', 'remove': '移除', 'render': '使成为', 'renew': '更新',
  'repeat': '重复', 'replace': '替换', 'report': '报告', 'represent': '代表',
  'reputation': '声誉', 'request': '请求', 'require': '要求', 'research': '研究',
  'reserve': '储备', 'resident': '居民', 'resign': '辞职', 'resist': '抵抗',
  'resolution': '决议', 'resolve': '解决', 'resort': '度假村', 'resource': '资源',
  'respond': '回应', 'response': '反应', 'responsibility': '责任', 'responsible': '负责的',
  'rest': '休息', 'restore': '恢复', 'restrict': '限制', 'result': '结果',
  'retain': '保留', 'retire': '退休', 'retreat': '撤退', 'retrieve': '检索',
  'reveal': '揭示', 'revenue': '收入', 'reverse': '反转', 'review': '评论',
  'revolution': '革命', 'reward': '奖励', 'rhetoric': '修辞', 'rhythm': '节奏',
  'rich': '富有的', 'ride': '骑', 'right': '正确的；权利', 'rigid': '僵硬的',
  'ring': '戒指', 'rise': '上升', 'risk': '风险', 'rival': '竞争对手',
  'river': '河', 'road': '道路', 'robust': '强壮的', 'role': '角色',
  'roll': '滚动', 'romantic': '浪漫的', 'roof': '屋顶', 'room': '房间',
  'root': '根', 'rough': '粗糙的', 'round': '圆的', 'route': '路线',
  'routine': '日常的', 'row': '行', 'royal': '皇家的', 'ruin': '毁灭',
  'rule': '规则', 'run': '跑', 'rural': '农村的', 'rush': '冲',
  'sacred': '神圣的', 'sacrifice': '牺牲', 'safe': '安全的', 'sake': '缘故',
  'salary': '工资', 'sale': '销售', 'sample': '样本', 'sanction': '制裁',
  'sand': '沙子', 'satellite': '卫星', 'satisfy': '满足', 'save': '节省',
  'scale': '规模', 'scandal': '丑闻', 'scene': '场景', 'schedule': '时间表',
  'scheme': '方案', 'scholar': '学者', 'school': '学校', 'science': '科学',
  'scientific': '科学的', 'scope': '范围', 'score': '分数', 'screen': '屏幕',
  'script': '剧本', 'search': '搜索', 'season': '季节', 'seat': '座位',
  'second': '第二', 'secret': '秘密', 'secretary': '秘书', 'section': '部分',
  'sector': '部门', 'secure': '安全的', 'security': '安全', 'seed': '种子',
  'seek': '寻求', 'seem': '似乎', 'segment': '部分', 'seize': '抓住',
  'select': '选择', 'self': '自我', 'sell': '卖', 'senate': '参议院',
  'senior': '高级的', 'sense': '感觉', 'sensitive': '敏感的', 'sentence': '句子',
  'separate': '分开', 'sequence': '序列', 'series': '系列', 'serious': '严重的',
  'serve': '服务', 'service': '服务', 'session': '会议', 'set': '设置',
  'settle': '解决', 'settlement': '定居点', 'severe': '严重的', 'shade': '阴影',
  'shadow': '影子', 'shake': '摇', 'shall': '将', 'shame': '耻辱',
  'shape': '形状', 'share': '分享', 'sharp': '锐利的', 'shed': '流出',
  'sheer': '纯粹的', 'shelter': '避难所', 'shift': '转变', 'shine': '发光',
  'ship': '船', 'shock': '震惊', 'shoot': '射击', 'shop': '商店',
  'shore': '海岸', 'short': '短的', 'shot': '射击', 'shoulder': '肩膀',
  'shout': '喊', 'show': '展示', 'shut': '关闭', 'sick': '生病的',
  'side': '方面', 'sight': '视力', 'sign': '标志', 'signal': '信号',
  'significant': '重要的', 'silence': '沉默', 'silly': '愚蠢的', 'similar': '类似的',
  'simple': '简单的', 'since': '自从', 'single': '单一的', 'sir': '先生',
  'sister': '姐妹', 'sit': '坐', 'site': '地点', 'situation': '情况',
  'size': '大小', 'skill': '技能', 'skin': '皮肤', 'slave': '奴隶',
  'sleep': '睡觉', 'slide': '滑动', 'slight': '轻微的', 'slip': '滑倒',
  'slow': '慢的', 'small': '小的', 'smart': '聪明的', 'smell': '闻',
  'smile': '微笑', 'smoke': '烟', 'smooth': '光滑的', 'snap': '折断',
  'snow': '雪', 'so': '所以', 'social': '社会的', 'society': '社会',
  'soft': '柔软的', 'software': '软件', 'soil': '土壤', 'solar': '太阳的',
  'soldier': '士兵', 'solid': '固体的', 'solution': '解决方案', 'solve': '解决',
  'somebody': '某人', 'somehow': '不知怎地', 'someone': '某人', 'something': '某事',
  'sometimes': '有时', 'somewhat': '稍微', 'somewhere': '某处', 'son': '儿子',
  'soon': '很快', 'sophisticated': '复杂精密的', 'sorry': '抱歉的', 'sort': '种类',
  'soul': '灵魂', 'sound': '声音', 'source': '来源', 'south': '南方',
  'southern': '南方的', 'sovereign': '主权的', 'space': '空间', 'span': '跨度',
  'speak': '说', 'special': '特殊的', 'species': '物种', 'specific': '具体的',
  'spectrum': '光谱', 'speech': '演讲', 'speed': '速度', 'spend': '花费',
  'sphere': '范围', 'spirit': '精神', 'split': '分裂', 'spokesman': '发言人',
  'sponsor': '赞助商', 'spot': '地点', 'spread': '传播', 'spring': '春天',
  'square': '广场', 'squeeze': '挤压', 'stability': '稳定性', 'stable': '稳定的',
  'staff': '员工', 'stage': '阶段', 'stake': '股份', 'stand': '站立',
  'standard': '标准', 'star': '星星', 'start': '开始', 'state': '状态；国家',
  'statement': '声明', 'station': '车站', 'status': '地位', 'statute': '法规',
  'stay': '停留', 'steady': '稳定的', 'steal': '偷', 'steel': '钢铁',
  'stem': '源于', 'step': '步骤', 'stick': '粘', 'stiff': '僵硬的',
  'still': '仍然', 'stimulate': '刺激', 'stock': '股票', 'stomach': '胃',
  'stone': '石头', 'stop': '停止', 'store': '商店', 'storm': '暴风雨',
  'story': '故事', 'straight': '直的', 'strange': '奇怪的', 'stranger': '陌生人',
  'strategic': '战略的', 'strategy': '策略', 'stream': '溪流', 'street': '街道',
  'strength': '力量', 'stress': '压力', 'stretch': '伸展', 'strict': '严格的',
  'strike': '罢工', 'string': '绳子', 'strip': '剥夺', 'stroke': '中风',
  'strong': '强的', 'structure': '结构', 'struggle': '斗争', 'student': '学生',
  'study': '学习', 'stuff': '东西', 'stupid': '愚蠢的', 'style': '风格',
  'subject': '主题', 'submit': '提交', 'subsequent': '随后的', 'substance': '物质',
  'substantial': '大量的', 'subtle': '微妙的', 'succeed': '成功', 'success': '成功',
  'such': '这样的', 'sudden': '突然的', 'suffer': '遭受', 'sufficient': '充足的',
  'suggest': '建议', 'suit': '适合；西装', 'suitable': '合适的', 'sum': '总和',
  'summary': '摘要', 'summer': '夏天', 'summit': '峰会', 'super': '超级的',
  'supply': '供应', 'support': '支持', 'suppose': '假设', 'supreme': '最高的',
  'sure': '确定的', 'surface': '表面', 'surgery': '手术', 'surplus': '盈余',
  'surprise': '惊喜', 'surround': '包围', 'survey': '调查', 'survival': '生存',
  'survive': '幸存', 'suspect': '怀疑', 'suspend': '暂停', 'sustain': '维持',
  'sustainable': '可持续的', 'swallow': '吞', 'swear': '发誓', 'sweep': '扫',
  'sweet': '甜的', 'swim': '游泳', 'swing': '摇摆', 'switch': '切换',
  'symbol': '象征', 'sympathy': '同情', 'symptom': '症状', 'syndrome': '综合症',
  'system': '系统',
  'table': '桌子', 'tackle': '处理', 'tactic': '策略', 'tail': '尾巴',
  'take': '拿', 'tale': '故事', 'talent': '人才', 'talk': '说话',
  'tank': '坦克', 'tap': '轻敲', 'tape': '磁带', 'target': '目标',
  'task': '任务', 'taste': '品味', 'tax': '税', 'teach': '教',
  'team': '团队', 'tear': '眼泪；撕', 'technology': '技术', 'telephone': '电话',
  'television': '电视', 'tell': '告诉', 'temperature': '温度', 'temporary': '暂时的',
  'tend': '倾向', 'tendency': '倾向', 'tension': '紧张', 'term': '学期；条款',
  'terrible': '可怕的', 'territory': '领土', 'terror': '恐怖', 'terrorism': '恐怖主义',
  'test': '测试', 'testimony': '证词', 'text': '文本', 'thank': '谢谢',
  'theme': '主题', 'then': '然后', 'theory': '理论', 'therapy': '治疗',
  'thereby': '因此', 'thick': '厚的', 'thin': '薄的', 'thing': '事物',
  'think': '思考', 'thorough': '彻底的', 'though': '虽然', 'thought': '想法',
  'threat': '威胁', 'threaten': '威胁', 'threshold': '阈值', 'thrive': '茁壮成长',
  'throughout': '自始至终', 'throw': '扔', 'thus': '因此', 'ticket': '票',
  'tide': '潮汐', 'tie': '领带；联系', 'tight': '紧的', 'timber': '木材',
  'time': '时间', 'tiny': '微小的', 'tip': '提示', 'title': '标题',
  'today': '今天', 'together': '一起', 'tolerate': '容忍', 'tomorrow': '明天',
  'tone': '语气', 'tongue': '舌头', 'tonight': '今晚', 'tool': '工具',
  'top': '顶部', 'topic': '话题', 'torture': '酷刑', 'total': '总计',
  'touch': '触摸', 'tough': '困难的', 'tour': '旅行', 'tourist': '游客',
  'toward': '朝向', 'tower': '塔', 'town': '城镇', 'trace': '追踪',
  'track': '轨道', 'trade': '贸易', 'tradition': '传统', 'traditional': '传统的',
  'traffic': '交通', 'tragedy': '悲剧', 'trail': '小径', 'train': '训练',
  'trait': '特征', 'transfer': '转移', 'transform': '转变', 'transition': '过渡',
  'translate': '翻译', 'transmission': '传输', 'transport': '运输', 'trap': '陷阱',
  'travel': '旅行', 'treasure': '宝藏', 'treat': '对待', 'treatment': '治疗',
  'treaty': '条约', 'tree': '树', 'tremendous': '巨大的', 'trend': '趋势',
  'trial': '审判', 'tribe': '部落', 'trick': '技巧', 'trigger': '触发',
  'trip': '旅行', 'triumph': '胜利', 'troop': '部队', 'trouble': '麻烦',
  'truck': '卡车', 'true': '真的', 'truly': '真正地', 'trust': '信任',
  'truth': '真相', 'try': '尝试', 'tube': '管子', 'turn': '转动',
  'twice': '两次', 'type': '类型', 'typical': '典型的',
  'ugly': '丑陋的', 'ultimate': '最终的', 'unable': '无法', 'uncertain': '不确定的',
  'uncle': '叔叔', 'undergo': '经历', 'undermine': '破坏', 'understand': '理解',
  'undertake': '承担', 'unemployment': '失业', 'unfair': '不公平的', 'unfortunately': '不幸地',
  'uniform': '统一的', 'union': '联盟', 'unique': '独特的', 'unit': '单位',
  'unite': '团结', 'universal': '普遍的', 'universe': '宇宙', 'university': '大学',
  'unknown': '未知的', 'unless': '除非', 'unlike': '不像', 'unlikely': '不太可能的',
  'until': '直到', 'unusual': '不寻常的', 'update': '更新', 'upon': '在...上',
  'upper': '上面的', 'upset': '沮丧的', 'urban': '城市的', 'urge': '敦促',
  'urgent': '紧急的', 'usage': '用法', 'use': '使用', 'useful': '有用的',
  'user': '用户', 'usual': '通常的', 'utility': '实用性',
  'vacation': '假期', 'vague': '模糊的', 'valid': '有效的', 'valley': '山谷',
  'valuable': '有价值的', 'value': '价值', 'variable': '变量', 'variation': '变化',
  'variety': '种类', 'various': '各种各样的', 'vast': '广阔的', 'vehicle': '车辆',
  'venture': '冒险', 'version': '版本', 'versus': '与...相比', 'very': '非常',
  'veteran': '老兵', 'via': '通过', 'victim': '受害者', 'victory': '胜利',
  'video': '视频', 'view': '观点', 'violate': '违反', 'violence': '暴力',
  'virtual': '虚拟的', 'virtue': '美德', 'visible': '可见的', 'vision': '视野',
  'visit': '访问', 'visual': '视觉的', 'vital': '至关重要的', 'vocabulary': '词汇',
  'voice': '声音', 'volume': '体积', 'voluntary': '自愿的', 'volunteer': '志愿者',
  'vote': '投票', 'vulnerable': '脆弱的',
  'wage': '工资', 'wait': '等待', 'wake': '唤醒', 'walk': '走',
  'wall': '墙', 'wander': '漫游', 'want': '想要', 'war': '战争',
  'warn': '警告', 'wash': '洗', 'waste': '浪费', 'watch': '观看',
  'water': '水', 'wave': '波浪', 'way': '方式', 'weak': '弱的',
  'wealth': '财富', 'weapon': '武器', 'wear': '穿', 'weather': '天气',
  'web': '网', 'website': '网站', 'wedding': '婚礼', 'week': '周',
  'weigh': '称重', 'weight': '重量', 'welcome': '欢迎', 'welfare': '福利',
  'well': '好', 'west': '西方', 'western': '西方的', 'wet': '湿的',
  'whatever': '无论什么', 'wheel': '轮子', 'whenever': '每当', 'whereas': '然而',
  'whether': '是否', 'while': '而', 'whisper': '耳语', 'white': '白色的',
  'whole': '整个的', 'whom': '谁', 'whose': '谁的', 'wide': '宽的',
  'widely': '广泛地', 'wild': '野生的', 'will': '将', 'willing': '愿意的',
  'win': '赢', 'wind': '风', 'window': '窗户', 'wine': '葡萄酒',
  'wing': '翅膀', 'winter': '冬天', 'wire': '电线', 'wisdom': '智慧',
  'wise': '明智的', 'wish': '希望', 'withdraw': '撤回', 'witness': '证人',
  'woman': '女人', 'wonder': '想知道', 'wonderful': '精彩的', 'wood': '木头',
  'word': '单词', 'work': '工作', 'worker': '工人', 'world': '世界',
  'worry': '担心', 'worse': '更坏的', 'worst': '最坏的', 'worth': '值得',
  'would': '将会', 'wound': '伤口', 'wrap': '包裹', 'write': '写',
  'writer': '作家', 'wrong': '错误的',
  'yard': '院子', 'year': '年', 'yellow': '黄色的', 'yesterday': '昨天',
  'yet': '然而', 'yield': '产量；屈服', 'young': '年轻的', 'youth': '青年',
  'zone': '区域',
  // Common academic / journalistic vocabulary
  'albeit': '尽管', 'amid': '在...之中', 'amidst': '在...之中', 'akin': '类似的',
  'albeit': '虽然', 'alleviate': '减轻', 'ambiguous': '模棱两可的', 'ameliorate': '改善',
  'anomaly': '异常', 'antagonism': '对抗', 'antithesis': '对立面', 'apparatus': '装置',
  'apprehension': '忧虑', 'arbitrary': '任意的', 'archaic': '古老的', 'arduous': '艰巨的',
  'articulate': '清晰表达', 'ascertain': '确定', 'aspiration': '渴望', 'assimilate': '同化',
  'atrocity': '暴行', 'augment': '增加', 'auspicious': '吉利的', 'austerity': '紧缩',
  'autonomous': '自治的', 'aversion': '厌恶',
  'benevolent': '仁慈的', 'bestow': '授予', 'bias': '偏见', 'blatant': '公然的',
  'bolster': '支持', 'bureaucracy': '官僚主义', 'burgeon': '迅速发展',
  'candid': '坦率的', 'catalyst': '催化剂', 'cede': '割让', 'chronic': '慢性的',
  'circumscribe': '限制', 'coerce': '强迫', 'coherent': '连贯的', 'commensurate': '相称的',
  'compel': '强迫', 'complacent': '自满的', 'compliant': '服从的', 'concede': '承认',
  'conceive': '构想', 'conducive': '有助于的', 'confluence': '汇合', 'conjecture': '推测',
  'connotation': '含义', 'conscientious': '认真的', 'conspicuous': '显著的', 'constrain': '约束',
  'contemplate': '沉思', 'contentious': '有争议的', 'contingent': '取决于的', 'conundrum': '难题',
  'converge': '汇聚', 'convey': '传达', 'corroborate': '证实', 'culminate': '达到顶点',
  'curtail': '缩减',
  'daunting': '令人畏惧的', 'debacle': '崩溃', 'decimate': '大量毁灭', 'deference': '尊重',
  'deficiency': '缺陷', 'deliberate': '故意的', 'delicate': '精致的', 'delineate': '描述',
  'delusion': '幻想', 'demise': '消亡', 'denounce': '谴责', 'depict': '描绘',
  'deplete': '耗尽', 'deploy': '部署', 'desolate': '荒凉的', 'deteriorate': '恶化',
  'detrimental': '有害的', 'deviate': '偏离', 'dichotomy': '二分法', 'diffuse': '扩散',
  'dilemma': '困境', 'diminish': '减少', 'dire': '可怕的', 'disclose': '披露',
  'discrepancy': '差异', 'discrete': '离散的', 'disdain': '蔑视', 'dismal': '阴沉的',
  'dismantle': '拆除', 'disparity': '差距', 'dispel': '消除', 'disposition': '倾向',
  'disproportionate': '不成比例的', 'disrupt': '破坏', 'disseminate': '传播', 'dissent': '异议',
  'dissolution': '解散', 'diverge': '分歧', 'doctrine': '教义', 'dogma': '教条',
  'dormant': '休眠的', 'dubious': '可疑的', 'dwarf': '使相形见绌', 'dwindle': '减少',
  'eclipse': '掩盖', 'efficacy': '功效', 'elicit': '引出', 'eloquent': '雄辩的',
  'elusive': '难以捉摸的', 'emanate': '散发', 'embark': '开始', 'embody': '体现',
  'empirical': '实证的', 'emulate': '效仿', 'endemic': '地方性的', 'endorse': '支持',
  'endure': '忍受', 'enigma': '谜', 'entail': '涉及', 'entrepreneur': '企业家',
  'enumerate': '列举', 'envision': '设想', 'ephemeral': '短暂的', 'epitome': '典型',
  'equitable': '公平的', 'eradicate': '根除', 'erode': '侵蚀', 'erratic': '不规则的',
  'espouse': '拥护', 'ethereal': '缥缈的', 'exacerbate': '加剧', 'exalt': '赞扬',
  'excerpt': '摘录', 'exemplify': '举例说明', 'exert': '施加', 'exhaust': '耗尽',
  'exile': '流放', 'exorbitant': '过高的', 'expedite': '加快', 'explicit': '明确的',
  'expound': '阐述', 'exquisite': '精致的', 'extravagant': '奢侈的',
  'fabricate': '捏造', 'facet': '方面', 'facilitate': '促进', 'fallacy': '谬论',
  'famine': '饥荒', 'feasible': '可行的', 'fervent': '热情的', 'fiscal': '财政的',
  'flaw': '缺陷', 'fledgling': '初出茅庐的', 'flourish': '繁荣', 'fluctuate': '波动',
  'foment': '煽动', 'forbid': '禁止', 'formidable': '强大的', 'fortify': '加强',
  'foster': '培养', 'fragile': '脆弱的', 'friction': '摩擦', 'frugal': '节俭的',
  'futile': '无用的',
  'galvanize': '激励', 'garner': '获取', 'gauge': '衡量', 'genesis': '起源',
  'genocide': '种族灭绝', 'gist': '要点', 'glaring': '明显的', 'grapple': '努力解决',
  'gratitude': '感激', 'gravity': '严重性', 'gregarious': '合群的', 'grievance': '不满',
  'grim': '严酷的', 'gross': '总的',
  'hamper': '阻碍', 'harassment': '骚扰', 'haven': '避风港', 'hazard': '危害',
  'hegemony': '霸权', 'hinder': '阻碍', 'holistic': '整体的', 'homogeneous': '同质的',
  'humanitarian': '人道主义的',
  'ideology': '意识形态', 'idiosyncratic': '特殊的', 'illicit': '非法的', 'imminent': '即将发生的',
  'imperative': '必要的', 'impetus': '推动力', 'implicit': '隐含的', 'impose': '强加',
  'impoverish': '使贫困', 'inadvertent': '无意的', 'inaugurate': '开创', 'incentive': '激励',
  'incite': '煽动', 'inclusive': '包容的', 'incumbent': '在职的', 'indigenous': '土著的',
  'indispensable': '不可或缺的', 'induce': '引起', 'inertia': '惰性', 'infamous': '臭名昭著的',
  'infer': '推断', 'influx': '涌入', 'inherent': '固有的', 'inhibit': '抑制',
  'innate': '先天的', 'innocuous': '无害的', 'instigate': '煽动', 'integral': '不可分割的',
  'integrity': '正直', 'intermittent': '间歇的', 'intricate': '复杂的', 'intrinsic': '内在的',
  'inundate': '淹没', 'invoke': '援引', 'irrational': '不理性的',
  'jeopardize': '危害', 'jurisdiction': '管辖权', 'juxtapose': '并列',
  'kinship': '亲属关系',
  'lag': '落后', 'landmark': '里程碑', 'latent': '潜在的', 'latitude': '纬度',
  'latter': '后者', 'lax': '松懈的', 'legitimate': '合法的', 'lethal': '致命的',
  'leverage': '利用', 'liable': '有责任的', 'liberate': '解放', 'linger': '逗留',
  'literacy': '读写能力', 'lobby': '游说', 'loom': '逼近', 'lucrative': '有利可图的',
  'manifest': '显示', 'manipulate': '操纵', 'marital': '婚姻的', 'maritime': '海事的',
  'meager': '微薄的', 'mediate': '调解', 'menace': '威胁', 'metaphor': '隐喻',
  'meticulous': '一丝不苟的', 'migrate': '迁移', 'militia': '民兵', 'mitigate': '缓解',
  'momentum': '势头', 'monopoly': '垄断', 'moratorium': '暂停', 'mundane': '平凡的',
  'nascent': '新兴的', 'negligible': '微不足道的', 'nexus': '联系', 'niche': '利基',
  'nominate': '提名', 'norm': '规范', 'nostalgia': '怀旧', 'notorious': '臭名昭著的',
  'nuance': '细微差别',
  'obnoxious': '令人讨厌的', 'obscure': '模糊的', 'obsolete': '过时的', 'ominous': '不祥的',
  'opaque': '不透明的', 'optimal': '最佳的', 'orthodox': '正统的', 'oscillate': '摇摆',
  'ostensible': '表面上的', 'oust': '驱逐', 'outweigh': '超过',
  'paradigm': '范式', 'paradox': '悖论', 'paramount': '最重要的', 'partisan': '党派的',
  'pedagogy': '教育学', 'penal': '刑事的', 'penetrate': '穿透', 'perennial': '持久的',
  'perilous': '危险的', 'permeate': '渗透', 'perpetuate': '使永久化', 'pervasive': '普遍的',
  'petition': '请愿', 'pivotal': '关键的', 'plausible': '似是而非的', 'plight': '困境',
  'plunge': '暴跌', 'plurality': '多元', 'polarize': '两极化', 'polemical': '有争议的',
  'pragmatic': '务实的', 'precarious': '不稳定的', 'precede': '先于', 'precedent': '先例',
  'precipitate': '促成', 'preclude': '排除', 'predator': '捕食者', 'predecessor': '前任',
  'predicament': '困境', 'predominantly': '主要地', 'preemptive': '先发制人的', 'prejudice': '偏见',
  'preliminary': '初步的', 'prelude': '前奏', 'prevalent': '流行的', 'pristine': '原始的',
  'probe': '调查', 'proclaim': '宣布', 'prodigy': '天才', 'profound': '深刻的',
  'prohibit': '禁止', 'proliferate': '增殖', 'prolific': '多产的', 'pronounced': '显著的',
  'propaganda': '宣传', 'propel': '推动', 'proponent': '支持者', 'prosecute': '起诉',
  'protagonist': '主角', 'provenance': '起源', 'proxy': '代理', 'prudent': '谨慎的',
  'purport': '声称',
  'quandary': '困境', 'quarantine': '隔离', 'quasi': '准',
  'ramification': '影响', 'rampant': '猖獗的', 'ratify': '批准', 'rationale': '理由',
  'realm': '领域', 'rebuke': '指责', 'reckon': '认为', 'reconcile': '调和',
  'redundant': '多余的', 'referendum': '公投', 'refine': '精炼', 'refute': '反驳',
  'reiterate': '重申', 'relentless': '不懈的', 'relinquish': '放弃', 'reminiscent': '令人想起的',
  'remnant': '残余', 'renounce': '放弃', 'repeal': '废除', 'repercussion': '影响',
  'replenish': '补充', 'repression': '镇压', 'reproach': '责备', 'repudiate': '否认',
  'requisite': '必需的', 'resemble': '类似', 'resentment': '怨恨', 'residual': '剩余的',
  'resilience': '韧性', 'resilient': '有韧性的', 'resonance': '共鸣', 'resonate': '引起共鸣',
  'restrain': '克制', 'retaliate': '报复', 'retention': '保留', 'retrospect': '回顾',
  'revamp': '改造', 'rhetoric': '修辞', 'rigorous': '严格的', 'robust': '健壮的',
  'rudimentary': '基本的',
  'sabotage': '破坏', 'safeguard': '保障', 'salient': '显著的', 'sanction': '制裁',
  'saturate': '使饱和', 'savvy': '精明的', 'scapegoat': '替罪羊', 'scarcity': '稀缺',
  'scenario': '情景', 'schism': '分裂', 'scrutiny': '审查', 'secular': '世俗的',
  'sediment': '沉淀物', 'segregate': '隔离', 'semblance': '外表', 'sentiment': '情绪',
  'severity': '严重性', 'skeptical': '怀疑的', 'solidarity': '团结', 'solitude': '孤独',
  'sovereign': '主权的', 'spawn': '产生', 'speculate': '推测', 'sporadic': '零星的',
  'squander': '浪费', 'stagnant': '停滞的', 'staunch': '坚定的', 'stereotype': '刻板印象',
  'stigma': '耻辱', 'stipulate': '规定', 'strife': '冲突', 'stringent': '严格的',
  'strive': '努力', 'subjective': '主观的', 'subordinate': '下属的', 'subside': '平息',
  'subsidiary': '子公司', 'subsidy': '补贴', 'substantiate': '证实', 'subvert': '颠覆',
  'succumb': '屈服', 'superficial': '肤浅的', 'superfluous': '多余的', 'supplant': '取代',
  'supplement': '补充', 'suppress': '压制', 'surge': '激增', 'surmount': '克服',
  'surpass': '超过', 'surveillance': '监视', 'susceptible': '易受影响的', 'sway': '影响',
  'synopsis': '概要', 'synthesis': '综合',
  'taboo': '禁忌', 'tangible': '有形的', 'tariff': '关税', 'tenacious': '坚韧的',
  'tentative': '暂定的', 'tenure': '任期', 'terminate': '终止', 'testament': '证明',
  'testimony': '证词', 'tilt': '倾斜', 'token': '象征性的', 'trajectory': '轨迹',
  'transcend': '超越', 'transgression': '违反', 'transient': '短暂的', 'transparency': '透明度',
  'trauma': '创伤', 'traverse': '穿越', 'treaty': '条约', 'tribunal': '法庭',
  'trivial': '琐碎的', 'tumultuous': '动荡的', 'tyranny': '暴政',
  'ubiquitous': '无处不在的', 'ulterior': '隐秘的', 'unanimous': '一致的', 'uncover': '揭露',
  'underestimate': '低估', 'underpin': '支撑', 'underscore': '强调', 'underprivileged': '弱势的',
  'unilateral': '单方面的', 'unprecedented': '史无前例的', 'unrest': '动荡', 'unveil': '揭开',
  'uphold': '维护', 'upheaval': '剧变', 'utmost': '最大的',
  'validate': '验证', 'vanish': '消失', 'vehement': '激烈的', 'vendetta': '世仇',
  'verge': '边缘', 'verify': '核实', 'versatile': '多才多艺的', 'viable': '可行的',
  'vigilant': '警惕的', 'vigor': '活力', 'vindicate': '证明...正确', 'virulent': '恶性的',
  'vivid': '生动的', 'volatile': '不稳定的', 'voluminous': '大量的',
  'warrant': '保证', 'wary': '警惕的', 'wield': '行使', 'withstand': '承受',
  'wreak': '造成',
  'xenophobia': '仇外心理',
  'yearn': '渴望',
  'zealous': '热心的', 'zenith': '顶点'
};

function initDblclickLookup() {
  const readerBody = document.getElementById('reader-body');
  if (!readerBody) return;

  readerBody.addEventListener('dblclick', handleDblclickLookup);

  // Click-outside dismissal for the dblclick tooltip
  document.addEventListener('click', (e) => {
    const dblTooltip = document.getElementById('dblclick-tooltip');
    if (dblTooltip.style.display !== 'none' && !dblTooltip.contains(e.target)) {
      dblTooltip.style.display = 'none';
    }
  });
}

function handleDblclickLookup(e) {
  // Don't interfere with existing highlight clicks
  if (e.target.closest('.highlight-vocab, .highlight-phrase, .highlight-sentence')) return;

  const selection = window.getSelection();
  const word = (selection.toString() || '').trim();

  // Validate: 2-30 chars, only letters
  if (!word || word.length < 2 || word.length > 30 || !/^[a-zA-Z]+$/.test(word)) return;

  const lowerWord = word.toLowerCase();

  // Position the tooltip near the selection
  const range = selection.getRangeAt(0);
  const rect = range.getBoundingClientRect();
  showDblclickTooltip(rect, lowerWord);
}

function showDblclickTooltip(rect, word) {
  const tooltip = document.getElementById('dblclick-tooltip');
  const wordEl = document.getElementById('dblclick-word');
  const phoneticEl = document.getElementById('dblclick-phonetic');
  const defEl = document.getElementById('dblclick-def');
  const chineseEl = document.getElementById('dblclick-chinese');

  // Check if word exists in current analysis vocabulary
  let analysisMatch = null;
  if (currentAnalysis) {
    analysisMatch = currentAnalysis.vocabulary.find(v =>
      (v.form_found || v.word).toLowerCase() === word || v.word.toLowerCase() === word
    );
    if (!analysisMatch) {
      analysisMatch = currentAnalysis.phrases.find(p => p.phrase.toLowerCase() === word);
    }
  }

  if (analysisMatch) {
    // Use analysis data directly
    wordEl.textContent = analysisMatch.word || analysisMatch.phrase || word;
    phoneticEl.textContent = analysisMatch.phonetic || '';
    defEl.textContent = analysisMatch.definition || '';
    chineseEl.textContent = analysisMatch.chinese || COMMON_CHINESE[word] || '暂无中文释义';
    tooltip.style.display = 'block';
    positionDblclickTooltip(tooltip, rect);
    return;
  }

  // Show loading state
  wordEl.textContent = word;
  phoneticEl.textContent = '';
  defEl.innerHTML = '<span class="dblclick-tooltip-loading">查询中...</span>';
  chineseEl.textContent = '';
  tooltip.style.display = 'block';
  positionDblclickTooltip(tooltip, rect);

  // Fetch from free dictionary API
  fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${encodeURIComponent(word)}`)
    .then(res => {
      if (!res.ok) throw new Error('Not found');
      return res.json();
    })
    .then(data => {
      const entry = data[0];
      const phonetic = entry.phonetic
        || (entry.phonetics && entry.phonetics.find(p => p.text)?.text)
        || '';
      // Get the first available definition
      let definition = '未找到释义';
      if (entry.meanings && entry.meanings.length > 0) {
        const meanings = entry.meanings.slice(0, 2);
        definition = meanings.map(m => {
          const pos = m.partOfSpeech || '';
          const def = m.definitions[0]?.definition || '';
          return pos ? `(${pos}) ${def}` : def;
        }).join(' | ');
      }

      wordEl.textContent = entry.word || word;
      phoneticEl.textContent = phonetic;
      defEl.textContent = definition;
      chineseEl.textContent = COMMON_CHINESE[word] || '暂无中文释义';

      // Reposition after content update
      positionDblclickTooltip(tooltip, rect);
    })
    .catch(() => {
      wordEl.textContent = word;
      phoneticEl.textContent = '';
      defEl.textContent = '未找到释义';
      chineseEl.textContent = COMMON_CHINESE[word] || '暂无中文释义';
      positionDblclickTooltip(tooltip, rect);
    });
}

function positionDblclickTooltip(tooltip, rect) {
  let top = rect.bottom + 8;
  let left = rect.left;
  const tw = tooltip.offsetWidth;
  const th = tooltip.offsetHeight;
  if (left + tw > window.innerWidth - 16) left = window.innerWidth - tw - 16;
  if (left < 16) left = 16;
  if (top + th > window.innerHeight - 16) top = rect.top - th - 8;
  tooltip.style.top = top + 'px';
  tooltip.style.left = left + 'px';
}

// Pre-load voices
if ('speechSynthesis' in window) { window.speechSynthesis.cancel(); }

// ═════════════════════════════════════════════════════════════
// 朗读模块 (Web Speech API, 英式发音, 零成本)
// ═════════════════════════════════════════════════════════════
let _ttsState = { speaking: false, voice: null, queue: [], qIdx: 0 };

function _getBritishVoice() {
  if (_ttsState.voice) return _ttsState.voice;
  const voices = window.speechSynthesis ? speechSynthesis.getVoices() : [];
  if (!voices.length) return null;
  // 优先级:macOS 高质量英音 > Google/Microsoft 英音 > 任意 en-GB > 任意英语
  const preferred = ['Daniel', 'Kate', 'Serena', 'Stephanie', 'Oliver', 'Arthur',
                     'Google UK English Female', 'Google UK English Male',
                     'Microsoft Hazel', 'Microsoft George', 'Microsoft Susan'];
  for (const name of preferred) {
    const v = voices.find(x => x.name.includes(name));
    if (v) { _ttsState.voice = v; return v; }
  }
  const enGB = voices.find(v => v.lang === 'en-GB' || v.lang === 'en_GB');
  if (enGB) { _ttsState.voice = enGB; return enGB; }
  const anyEn = voices.find(v => v.lang.startsWith('en'));
  if (anyEn) { _ttsState.voice = anyEn; return anyEn; }
  return null;
}

function speak(text, opts) {
  opts = opts || {};
  if (!('speechSynthesis' in window)) { notify('当前浏览器不支持语音功能', 'error'); return; }
  if (!text) return;
  speechSynthesis.cancel();
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = 'en-GB';
  utter.rate = opts.rate || 0.95;
  utter.pitch = 1.0;
  utter.volume = 1.0;
  const voice = _getBritishVoice();
  if (voice) utter.voice = voice;
  utter.onstart = () => { _ttsState.speaking = true; updateTtsBtn(); };
  utter.onend = () => { _ttsState.speaking = false; updateTtsBtn(); _maybeNextInQueue(); };
  utter.onerror = () => { _ttsState.speaking = false; updateTtsBtn(); };
  speechSynthesis.speak(utter);
}

function _maybeNextInQueue() {
  if (_ttsState.qIdx < _ttsState.queue.length) {
    const next = _ttsState.queue[_ttsState.qIdx++];
    const u = new SpeechSynthesisUtterance(next);
    u.lang = 'en-GB';
    u.rate = 0.9;
    const voice = _getBritishVoice();
    if (voice) u.voice = voice;
    u.onstart = () => { _ttsState.speaking = true; updateTtsBtn(); };
    u.onend = () => { _ttsState.speaking = false; updateTtsBtn(); _maybeNextInQueue(); };
    u.onerror = () => { _ttsState.speaking = false; updateTtsBtn(); };
    speechSynthesis.speak(u);
  } else {
    _ttsState.queue = [];
    _ttsState.qIdx = 0;
  }
}

function stopSpeak() {
  speechSynthesis.cancel();
  _ttsState.speaking = false;
  _ttsState.queue = [];
  _ttsState.qIdx = 0;
  updateTtsBtn();
}

function toggleArticleSpeak() {
  if (_ttsState.speaking || _ttsState.queue.length > _ttsState.qIdx) {
    stopSpeak();
    return;
  }
  if (!currentArticleText) { notify('暂无可朗读内容', 'error'); return; }
  // 按段落切分,逐段排队,避免超长 utterance 在某些浏览器卡顿
  const paragraphs = currentArticleText.split(/\n{2,}/).map(p => p.trim()).filter(Boolean);
  if (!paragraphs.length) return;
  _ttsState.queue = paragraphs;
  _ttsState.qIdx = 1;
  speak(paragraphs[0], { rate: 0.9 });
}

function updateTtsBtn() {
  const b = document.getElementById('btn-tts-article');
  if (!b) return;
  const playing = _ttsState.speaking || _ttsState.qIdx < _ttsState.queue.length;
  b.textContent = playing ? '⏸ 停止朗读' : '🔊 朗读全文';
  b.classList.toggle('tts-playing', playing);
}

// 部分浏览器(Chrome)需要监听 voiceschanged 事件
if ('speechSynthesis' in window) {
  speechSynthesis.onvoiceschanged = () => { _ttsState.voice = null; _getBritishVoice(); };
  // 首次访问页面时主动触发一次
  setTimeout(() => _getBritishVoice(), 200);
}

// 切换页面时自动停止朗读
window.addEventListener('beforeunload', stopSpeak);
