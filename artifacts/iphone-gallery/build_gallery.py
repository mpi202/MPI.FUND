# Writes the "mpi.fund on iPhone" gallery page from the captured screenshots.
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
PREVIEW = 'https://claude.ai/artifact/WpTGFXGCMf24mQwQgCbaZS'
full = [
  ('home', 'Home', 'The rotating headline wraps onto two lines instead of running off the screen.'),
  ('about', 'About', 'The leadership cards stack in a single column.'),
  ('funds', 'Investment Funds', 'Fund names wrap to two lines, and the chart buttons are easier to tap. The first fund is opened.'),
  ('portfolios', 'Portfolios', 'The three risk levels stack instead of pushing the page sideways.'),
  ('services', 'Services', 'The service cards stack into one column.'),
  ('docs-customer', 'Customer Information', 'The boxes fit narrow screens, and the phone number is a tap-to-call link.'),
  ('distribution', 'Distribution', 'The PDF labels are visible without a mouse hover.'),
  ('contact', 'Contact', 'Contact details, map and transfer data run in one column.'),
]
moments = [
  ('menu', 'Menu', 'Each menu item is a full-width row that is easy to tap.', False),
  ('meeting', 'Meeting form', 'Name and email stack, and the form scrolls on short screens.', True),
  ('hu-home', 'Home in Hungarian', 'The long Hungarian headline wraps cleanly.', False),
  ('hu-portfolios', 'Portfolios in Hungarian', 'Long Hungarian risk labels fit their rows.', False),
]
status_icons = ('<svg viewBox="0 0 78 14" aria-hidden="true"><g fill="currentColor">'
  '<rect x="0" y="9" width="3.2" height="4.5" rx="1"/><rect x="5" y="6.5" width="3.2" height="7" rx="1"/>'
  '<rect x="10" y="4" width="3.2" height="9.5" rx="1"/><rect x="15" y="1.5" width="3.2" height="12" rx="1"/>'
  '<path d="M33 3.2c2.6 0 5 1 6.8 2.7l1.3-1.3A11.4 11.4 0 0 0 33 1.3 11.4 11.4 0 0 0 24.9 4.6l1.3 1.3A9.6 9.6 0 0 1 33 3.2Zm0 3.6c1.6 0 3.1.6 4.2 1.7l1.3-1.3A7.6 7.6 0 0 0 33 4.9a7.6 7.6 0 0 0-5.5 2.3l1.3 1.3A5.9 5.9 0 0 1 33 6.8Zm0 3.5c.7 0 1.3.3 1.7.7L33 12.7 31.3 11c.4-.4 1-.7 1.7-.7Z"/>'
  '<rect x="48.5" y="1.5" width="24" height="11.5" rx="3.4" fill="none" stroke="currentColor" stroke-opacity=".4"/>'
  '<rect x="50.5" y="3.5" width="18" height="7.5" rx="2"/><path d="M74.2 5.5v3.5c.8-.3 1.3-1 1.3-1.75S75 5.8 74.2 5.5Z" opacity=".45"/></g></svg>')

def phone(img_html, label, dark_top=False, scroll=True):
    cls = 'phone' + (' dark-top' if dark_top else '')
    vp = (f'<div class="viewport" tabindex="0" role="region" aria-label="{html.escape(label)}, scroll to move through the page">{img_html}</div>'
          if scroll else f'<div class="viewport still">{img_html}</div>')
    return (f'<div class="frame"><div class="{cls}"><div class="screen">'
            f'<div class="statusbar"><span class="time">9:41</span><span class="island"></span><span class="sys">{status_icons}</span></div>'
            f'{vp}<div class="urlbar"><svg viewBox="0 0 10 13" aria-hidden="true"><path d="M2 5.5V4a3 3 0 0 1 6 0v1.5h.5A1.5 1.5 0 0 1 10 7v4.5A1.5 1.5 0 0 1 8.5 13h-7A1.5 1.5 0 0 1 0 11.5V7a1.5 1.5 0 0 1 1.5-1.5H2Zm1.5 0h3V4a1.5 1.5 0 0 0-3 0v1.5Z" fill="currentColor"/></svg>mpi.fund</div>'
            f'<span class="homebar"></span></div></div></div>')

def figure(phone_html, title, note):
    return f'<figure class="device">{phone_html}<figcaption><strong>{html.escape(title)}</strong><span>{html.escape(note)}</span></figcaption></figure>'

full_html = '\n'.join(figure(phone(
    f'<img class="hdr" src="shots/header.jpg" alt="" width="804" height="146">'
    f'<img class="pg" src="shots/page-{key}.jpg" alt="{html.escape(title)} page as it renders on an iPhone 17" loading="{"eager" if i < 4 else "lazy"}" decoding="async">',
    title), title, note) for i, (key, title, note) in enumerate(full))
moment_html = '\n'.join(figure(phone(
    f'<img class="pg" src="shots/moment-{key}.jpg" alt="{html.escape(title)} on an iPhone 17" loading="lazy" decoding="async">',
    title, dark_top=dark, scroll=False), title, note) for key, title, note, dark in moments)

page = '''<title>mpi.fund on iPhone</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>
  /* Layout: a quiet, slightly green-tinted ground with iPhone frames in a wrapping grid; each screen scrolls like the real device */
  :root{
    --bg:#f2f5f2; --fg:#0f1411; --muted:#5b665f; --line:#dbe3dd; --accent:#15803d; --chip:#e3ece5;
    --bezel:#121413; --bezel-edge:#2b2f2c; --screen:#ffffff; --screen-ink:#0a0a0a; --overlay-top:#1e222d; --overlay-ink:#ffffff;
    --font-display:'Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
    --font-body:'Inter',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
    --font-utility:ui-monospace,'SF Mono',Menlo,Consolas,monospace;
  }
  @media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0c100e;--fg:#e7ece8;--muted:#98a39c;--line:#232a26;--accent:#4ade80;--chip:#18201b;--bezel-edge:#3a403c;color-scheme:dark}}
  :root[data-theme="dark"]{--bg:#0c100e;--fg:#e7ece8;--muted:#98a39c;--line:#232a26;--accent:#4ade80;--chip:#18201b;--bezel-edge:#3a403c;color-scheme:dark}
  *,*::before,*::after{box-sizing:border-box}
  html body{background:var(--bg);color:var(--fg);font:400 16px/1.55 var(--font-body);-webkit-font-smoothing:antialiased}
  .wrap{max-width:1240px;margin:0 auto;padding-inline:clamp(16px,4vw,40px);padding-block:clamp(32px,6vw,64px) 56px}
  header.intro{display:grid;gap:14px;max-width:62ch;margin-bottom:clamp(36px,6vw,64px)}
  .eyebrow{font:500 12px/1.2 var(--font-utility);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
  h1{font:700 clamp(30px,5vw,44px)/1.08 var(--font-display);letter-spacing:-.025em;margin:0;text-wrap:balance}
  h1 span{color:var(--accent)}
  .lead{margin:0;color:var(--muted);font-size:17px}
  .actions{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin-top:6px}
  .btn{display:inline-flex;align-items:center;gap:8px;padding:11px 18px;border-radius:10px;background:var(--fg);color:var(--bg);font-weight:600;font-size:15px;text-decoration:none}
  .btn:focus-visible,.viewport:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
  .hint{font-size:14px;color:var(--muted)}
  section{display:grid;gap:22px;margin-bottom:clamp(48px,7vw,80px)}
  h2{font:600 13px/1.2 var(--font-utility);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0;padding-bottom:12px;border-bottom:1px solid var(--line)}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,250px),1fr));gap:48px 28px}
  .device{margin:0;display:grid;gap:16px;align-content:start;min-width:0}
  figcaption{display:grid;gap:4px;max-width:330px;margin-inline:auto;width:100%;font-size:14px;color:var(--muted)}
  figcaption strong{color:var(--fg);font-size:15px;font-weight:600}

  /* iPhone 17: 402 x 874 pt screen. .frame is the size container: 1pt = 94/402 cqw of its width (the bezel takes 3cqw a side). */
  .frame{container-type:inline-size;width:100%;max-width:330px;margin-inline:auto}
  .phone{width:100%;padding:3cqw;background:var(--bezel);border-radius:16cqw;box-shadow:0 0 0 1px var(--bezel-edge),0 18px 40px -18px rgba(0,0,0,.45)}
  .screen{position:relative;width:94cqw;height:204.4cqw;border-radius:13cqw;overflow:hidden;background:var(--screen);color:var(--screen-ink);isolation:isolate}
  .statusbar{position:relative;z-index:3;height:14.5cqw;display:flex;align-items:center;justify-content:space-between;padding:1.6cqw 6.5cqw 0 9.5cqw;background:var(--screen);font:600 4cqw/1 var(--font-body);letter-spacing:-.01em}
  .statusbar .island{position:absolute;left:50%;top:2.6cqw;width:29cqw;height:8.4cqw;transform:translateX(-50%);border-radius:5cqw;background:#000}
  .statusbar .sys svg{display:block;width:18cqw;height:auto}
  .dark-top .statusbar{background:var(--overlay-top);color:var(--overlay-ink)}
  .viewport{position:relative;height:189.9cqw;overflow-y:auto;overscroll-behavior:contain;scrollbar-width:none;background:var(--screen)}
  .viewport::-webkit-scrollbar{display:none}
  .viewport.still{overflow:hidden}
  .viewport img{display:block;width:100%;height:auto;max-width:100%}
  .viewport .hdr{position:sticky;top:0;z-index:2;margin-bottom:-17.07cqw}
  .urlbar{position:absolute;z-index:3;left:50%;bottom:6.5cqw;transform:translateX(-50%);display:flex;align-items:center;justify-content:center;gap:1.6cqw;width:62cqw;height:10.5cqw;border-radius:6cqw;background:rgba(250,250,250,.86);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);box-shadow:0 1px 6px rgba(0,0,0,.18);color:#111;font:500 3.6cqw/1 var(--font-body);pointer-events:none}
  .urlbar svg{width:2.4cqw;height:auto;opacity:.7}
  .homebar{position:absolute;z-index:3;left:50%;bottom:1.9cqw;width:31cqw;height:1.2cqw;transform:translateX(-50%);border-radius:1cqw;background:rgba(0,0,0,.82);pointer-events:none}
  footer.notes{border-top:1px solid var(--line);padding-top:20px;color:var(--muted);font-size:14px;max-width:70ch;display:grid;gap:8px}
  footer.notes p{margin:0}
  @media (prefers-reduced-motion: reduce){*{scroll-behavior:auto}}
</style>
<div class="wrap">
  <header class="intro">
    <span class="eyebrow">iPhone 17 &middot; 402 &times; 874 pt &middot; Safari</span>
    <h1>mpi.fund on <span>iPhone</span></h1>
    <p class="lead">Every page of the redesigned site as it renders on an iPhone 17 in portrait. Scroll inside a phone to move through that page. The site header stays pinned at the top, as it does on the device.</p>
    <div class="actions">
      <a class="btn" href="''' + PREVIEW + '''" target="_blank" rel="noopener">Open the live preview <span aria-hidden="true">&#8599;</span></a>
      <span class="hint">Captured 3 October 2026 in English, with live fund data.</span>
    </div>
  </header>
  <section aria-labelledby="full-pages">
    <h2 id="full-pages">Full pages</h2>
    <div class="grid">
''' + full_html + '''
    </div>
  </section>
  <section aria-labelledby="screens">
    <h2 id="screens">Single screens</h2>
    <div class="grid">
''' + moment_html + '''
    </div>
  </section>
  <footer class="notes">
    <p>Captured with WebKit, the engine inside Safari, emulating an iPhone 17. The status bar and Safari address bar are drawn in for context.</p>
    <p>The hero videos show their still frame, and the fund chart and reveal animations are shown in their finished state.</p>
  </footer>
</div>
'''
open(os.path.join(HERE, 'mpi-fund-on-iphone.html'), 'w', encoding='utf-8').write(page)
print('written', len(page))
