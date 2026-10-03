// Captures the iPhone 17 screenshots for the "mpi.fund on iPhone" gallery with Playwright's WebKit.
// Setup:  npm i playwright && npx playwright install webkit
// Run:    python3 -m http.server 8791 --bind 127.0.0.1   (from the repo root, in another terminal)
//         node artifacts/iphone-gallery/capture.js artifacts/iphone-gallery/shots
// Full pages are taken with the fixed header hidden; the gallery pins header.jpg on top while scrolling.
const { webkit, devices } = require('playwright');
const OUT = process.argv[2] || 'shots';
const BASE = 'http://127.0.0.1:8791/index.html#';
const PHONE = { ...devices['iPhone 17'], viewport: { width: 402, height: 812 }, deviceScaleFactor: 2 };
const finishAnimations = () => {
  document.querySelectorAll('.reveal,.contact-item').forEach((e) => e.classList.add('visible'));
  document.querySelectorAll('.scroll-reveal-word').forEach((w) => w.classList.add('lit'));
  document.querySelectorAll('.fund-card').forEach((c) => c.classList.add('show'));
};
const FULL = [
  ['home'], ['about'], ['funds', "document.querySelector('.fund-card .fund-head').click()"],
  ['portfolios'], ['services'], ['docs-customer'], ['distribution'], ['contact'],
];
const SCREENS = [
  ['menu', 'home', 'en', 'toggleMenu()'],
  ['meeting', 'services', 'en', "openMeeting('advisory')"],
  ['hu-home', 'home', 'hu', "document.querySelectorAll('#hero-rotate span').forEach((s,i)=>s.classList.toggle('active',i===2))"],
  ['hu-portfolios', 'portfolios', 'hu', "window.scrollTo(0, document.querySelector('.port-tab').getBoundingClientRect().top + scrollY - 110)"],
];
(async () => {
  const b = await webkit.launch();
  const errors = [];
  // Each capture gets a fresh page, so no menu or overlay state carries over between shots.
  const open = async (hash, lang) => {
    const ctx = await b.newContext(PHONE);
    const p = await ctx.newPage();
    p.on('pageerror', (e) => errors.push(String(e)));
    await p.goto(BASE + hash, { waitUntil: 'load' });
    if (lang === 'hu') await p.evaluate(() => setLang('hu'));
    await p.waitForTimeout(2200);
    return { ctx, p };
  };
  for (const [hash, js] of FULL) {
    const { ctx, p } = await open(hash, 'en');
    await p.evaluate(finishAnimations);
    if (js) await p.evaluate(js);
    await p.waitForTimeout(1500);
    if (hash === 'home') await p.locator('header').screenshot({ path: `${OUT}/header.jpg`, type: 'jpeg', quality: 85 });
    await p.evaluate(() => { document.querySelector('header').style.visibility = 'hidden'; window.scrollTo(0, 0); });
    await p.waitForTimeout(400);
    await p.screenshot({ path: `${OUT}/page-${hash}.jpg`, type: 'jpeg', quality: 78, fullPage: true });
    await ctx.close();
  }
  for (const [name, hash, lang, js] of SCREENS) {
    const { ctx, p } = await open(hash, lang);
    await p.evaluate(finishAnimations);
    await p.evaluate(js);
    await p.waitForTimeout(1500);
    await p.screenshot({ path: `${OUT}/moment-${name}.jpg`, type: 'jpeg', quality: 82 });
    await ctx.close();
  }
  await b.close();
  if (errors.length) { console.error('page errors:', errors); process.exit(1); }
  console.log('captured', FULL.length + SCREENS.length + 1, 'images into', OUT);
})();
