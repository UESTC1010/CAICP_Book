/* Analytics loads only after the reader opts in. */
(() => {
  'use strict';
  const id = document.currentScript?.dataset.measurementId;
  if (!/^G-[A-Z0-9]+$/.test(id || '')) return;
  const legacySite = location.hostname === 'uestc1010.github.io' && location.pathname.startsWith('/CAICP_Book/');
  const production = ['caicpbook.cn', 'www.caicpbook.cn'].includes(location.hostname) || legacySite;
  const cookiePath = legacySite ? '/CAICP_Book/' : '/';
  const key = 'caicp-analytics-consent-v1';
  const lifetime = 180 * 24 * 60 * 60 * 1000;
  let started = false;
  const panel = document.getElementById('analytics-choice');
  const status = document.getElementById('analytics-status');
  function preference() {
    try {
      const saved = JSON.parse(localStorage.getItem(key));
      return saved && saved.expires > Date.now() && ['allow', 'deny'].includes(saved.value) ? saved.value : null;
    } catch (_) { return null; }
  }
  function start() {
    if (started || !production) return;
    started = true;
    window['ga-disable-' + id] = false;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      analytics_storage: 'granted', ad_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied'
    });
    window.gtag('js', new Date());
    let referrer = '';
    try { const url = new URL(document.referrer); referrer = url.origin + url.pathname; } catch (_) {}
    window.gtag('config', id, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      page_location: location.origin + location.pathname,
      page_referrer: referrer,
      cookie_domain: 'none', cookie_path: cookiePath,
      cookie_prefix: 'caicp', cookie_expires: lifetime / 1000
    });
    const tag = document.createElement('script');
    tag.async = true;
    tag.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
    document.head.appendChild(tag);
  }
  function render(value) {
    if (status) status.textContent = value === 'allow' ? '当前设置：允许访问统计。' : value === 'deny' ? '当前设置：不参与访问统计。' : '当前设置：尚未开启访问统计。';
  }
  function choose(value) {
    try { localStorage.setItem(key, JSON.stringify({value, expires: Date.now() + lifetime})); } catch (_) {}
    if (panel) panel.hidden = true;
    render(value);
    if (value === 'allow') start();
    else {
      window['ga-disable-' + id] = true;
      for (const item of document.cookie.split(';')) {
        const name = item.split('=')[0].trim();
        if (name.startsWith('caicp_ga')) document.cookie = name + '=; Max-Age=0; Path=' + cookiePath + '; SameSite=Lax';
      }
      // Unload the tag after withdrawal, including its automatic event handlers.
      if (started) location.reload();
    }
  }
  document.querySelectorAll('[data-analytics-choice]').forEach(button => {
    button.addEventListener('click', () => choose(button.dataset.analyticsChoice));
  });
  document.querySelectorAll('[data-analytics-settings]').forEach(button => {
    button.hidden = false;
    button.addEventListener('click', () => {
      if (panel) { panel.hidden = false; panel.querySelector('button')?.focus(); }
    });
  });
  window.addEventListener('storage', event => { if (event.key === key) location.reload(); });
  const value = preference();
  render(value);
  if (value === 'allow') start();
  else if (value !== 'deny' && panel) panel.hidden = false;
})();
