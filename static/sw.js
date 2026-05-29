/**
 * Foreign Journal Reader — Service Worker
 * 策略:
 *  - 静态资源 (CSS/JS/icons/manifest) → cache-first
 *  - 文章 JSON / API → network-first,失败回退缓存,允许离线读
 *  - HTML 页面 → network-first(总是拿最新),失败回退缓存
 */

const VERSION = 'fr-v6.0';
const STATIC_CACHE = 'fr-static-' + VERSION;
const DYNAMIC_CACHE = 'fr-dyn-' + VERSION;

const STATIC_ASSETS = [
  '/',
  '/static/css/style.css',
  '/static/js/app.js',
  '/static/manifest.json',
  '/static/icons/icon-192.png',
  '/static/icons/icon-512.png',
  '/static/icons/apple-touch-icon.png',
  '/static/icons/favicon-32.png',
  '/static/icons/favicon-16.png',
  'https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,400&family=Noto+Serif+SC:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap'
];

// 安装:预缓存静态资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) => {
      return Promise.allSettled(STATIC_ASSETS.map(url =>
        cache.add(url).catch(e => console.warn('SW cache miss:', url, e))
      ));
    }).then(() => self.skipWaiting())
  );
});

// 激活:清理旧版本缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(
      keys.filter(k => k !== STATIC_CACHE && k !== DYNAMIC_CACHE)
          .map(k => caches.delete(k))
    )).then(() => self.clients.claim())
  );
});

// 网络请求处理
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // 跨域字体走 cache-first
  if (url.hostname.includes('fonts.googleapis.com') || url.hostname.includes('fonts.gstatic.com')) {
    event.respondWith(_cacheFirst(req, DYNAMIC_CACHE));
    return;
  }

  // 同源:
  if (url.origin !== self.location.origin) return;

  // 静态资源(/static/)走 cache-first
  if (url.pathname.startsWith('/static/')) {
    event.respondWith(_cacheFirst(req, STATIC_CACHE));
    return;
  }

  // API 走 network-first(确保数据最新,离线回退缓存)
  if (url.pathname.startsWith('/api/')) {
    event.respondWith(_networkFirst(req, DYNAMIC_CACHE));
    return;
  }

  // HTML 页面 network-first
  if (req.mode === 'navigate' || req.headers.get('accept')?.includes('text/html')) {
    event.respondWith(_networkFirst(req, DYNAMIC_CACHE));
    return;
  }

  // 默认 network-first
  event.respondWith(_networkFirst(req, DYNAMIC_CACHE));
});

async function _cacheFirst(req, cacheName) {
  const cached = await caches.match(req);
  if (cached) return cached;
  try {
    const res = await fetch(req);
    if (res.ok) {
      const cache = await caches.open(cacheName);
      cache.put(req, res.clone());
    }
    return res;
  } catch (e) {
    return new Response('Offline', { status: 503, statusText: 'Offline' });
  }
}

async function _networkFirst(req, cacheName) {
  try {
    const res = await fetch(req);
    if (res.ok) {
      const cache = await caches.open(cacheName);
      cache.put(req, res.clone());
    }
    return res;
  } catch (e) {
    const cached = await caches.match(req);
    if (cached) return cached;
    // 离线兜底:对 HTML 返回主页缓存
    if (req.mode === 'navigate') {
      const home = await caches.match('/');
      if (home) return home;
    }
    return new Response(JSON.stringify({ success: false, error: '离线状态,缓存中无此数据' }),
      { status: 503, headers: { 'Content-Type': 'application/json' } });
  }
}

// 消息处理(用于跳过 waiting 等)
self.addEventListener('message', (event) => {
  if (event.data === 'skipWaiting') self.skipWaiting();
});
