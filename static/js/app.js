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

// ═══ DAILY ARTICLES (exactly 3, no RSS) ═══
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
  articles.forEach((article, idx) => {
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
    grid.appendChild(card);
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
  if (article.article_index !== null && article.article_index !== undefined) {
    fetch(`/api/article/${article.article_index}`)
      .then(r => r.json())
      .then(data => {
        if (data.success && data.article.full_text) {
          const a = data.article;
          a.source_type = 'classic';
          openArticle(a, article.article_index);
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
      body: JSON.stringify({ text: article.full_text, title: article.title, article_index: article._classic_index })
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
      if (p.includes(escaped.substring(0, 40))) {
        // Find and wrap the sentence
        const sentenceRegex = new RegExp('(' + escapeRegExp(escaped).substring(0, 80) + '[^<]*?' + ')', 'i');
        p = p.replace(sentenceRegex, '<span class="highlight-sentence" data-sentence-idx="' + sIdx + '">$1</span>');
      }
    });

    // 2. Highlight phrases (longest first)
    const sortedPhrases = [...phrases].sort((a, b) => b.length - a.length);
    sortedPhrases.forEach(phrase => {
      const regex = new RegExp('(' + escapeRegExp(phrase) + ')', 'gi');
      p = p.replace(regex, '<span class="highlight-phrase" data-phrase="$1">$1</span>');
    });

    // 3. Highlight vocab words
    vocabWords.forEach(word => {
      const regex = new RegExp('(?<![\\w">])(' + escapeRegExp(word) + ')(?![\\w<])', 'gi');
      p = p.replace(regex, '<span class="highlight-vocab" data-word="' + word.toLowerCase() + '">$1</span>');
    });

    html += `<div class="para-wrapper"><span class="para-number">${idx + 1}</span><p>${p}</p></div>`;
  });
  bodyEl.innerHTML = html;

  renderVocabTab(analysis.vocabulary || []);
  renderPhrasesTab(analysis.phrases || []);
  renderSentencesTab(complexSentences);
  switchTab('vocab');
  bindHighlightClicks();
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
    info = currentAnalysis.vocabulary.find(v => v.form_found.toLowerCase() === key || v.word.toLowerCase() === key);
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
          return `<div class="vocab-example">${escapeHtml(text)}${source ? `<span class="vocab-example-source">— ${source}</span>` : ''}</div>`;
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

// Pre-load voices
if ('speechSynthesis' in window) { window.speechSynthesis.cancel(); }
