# Builds the claude.ai preview of index.html: same page, but Firestore reads come from an
# embedded snapshot (claude.ai pages can't reach Firebase), the map iframe becomes a link,
# and the 2K hero video (over the 15 MB upload limit) is dropped in favour of the HD one.
# Publish the output with its img/ files (see artifacts/README.md).
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', '..', 'index.html'), encoding='utf-8').read()
snap = open(os.path.join(HERE, 'snapshot.json'), encoding='utf-8').read()

def one(pattern, s, flags=0):
    m = list(re.finditer(pattern, s, flags))
    assert len(m) == 1, (pattern, len(m))
    return m[0]

head = one(r'<head>(.*?)</head>', src, re.S).group(1)
body = one(r'<body class="bg-white text-black antialiased">(.*)</body>', src, re.S).group(1)

# --- head: drop tags the publish skeleton or the claude.ai frame make moot ---
for pat in [r'\s*<meta charset="UTF-8" />', r'\s*<meta name="viewport"[^>]*/>', r'\s*<meta name="theme-color"[^>]*/>',
            r"\s*<!-- iOS: don't turn[^>]*-->", r'\s*<meta name="format-detection"[^>]*/>',
            r'\s*<meta name="apple-mobile-web-app-title"[^>]*/>', r'\s*<link rel="apple-touch-icon"[^>]*/>',
            r'\s*<title>Marketprog Asset Management</title>']:
    head = head.replace(one(pat, head).group(0), '', 1)

# --- Firebase SDK + init -> snapshot-backed stand-in with the same query surface the site uses ---
fb = one(r'<!-- Firebase SDK -->.*?const FS=firebase\.firestore\(\);', head, re.S).group(0)
stub = '''<!-- Preview build: claude.ai pages can't reach Firebase, so the site reads a snapshot of its Firestore data (3 Oct 2026) -->
<script>
const FS_SNAPSHOT=''' + snap + ''';
const FS=(()=>{
  const docSnap=d=>({id:d.id,exists:true,data:()=>JSON.parse(JSON.stringify(d.data))});
  const query=(name,filters,order)=>({
    where(f,op,v){return query(name,filters.concat([[f,v]]),order)},
    orderBy(f){return query(name,filters,f)},
    doc(id){return{get(){const d=(FS_SNAPSHOT[name]||[]).find(x=>x.id===id);return Promise.resolve(d?docSnap(d):{id,exists:false,data:()=>undefined})}}},
    get(){
      let docs=(FS_SNAPSHOT[name]||[]).filter(d=>filters.every(([f,v])=>d.data[f]===v));
      if(order)docs=docs.filter(d=>d.data[order]!==undefined).sort((a,b)=>a.data[order]<b.data[order]?-1:a.data[order]>b.data[order]?1:0);
      docs=docs.map(docSnap);
      return Promise.resolve({empty:!docs.length,size:docs.length,docs,forEach(f){docs.forEach(f)}});
    }
  });
  return{collection:name=>query(name,[],null)};
})();'''
head = head.replace(fb, stub, 1)

# --- body: map iframe -> link out (other sites can't be embedded in an artifact) ---
iframe = one(r'<iframe title="Marketprog office location"[^>]*></iframe>', body).group(0)
maplink = ('<a href="https://www.google.com/maps/search/?api=1&amp;query=Cs%C3%B6rsz%20utca%2045%2C%201124%20Budapest" target="_blank" rel="noopener" '
           'class="flex w-full h-[320px] sm:h-[420px] flex-col items-center justify-center gap-3 bg-neutral-50 text-neutral-500 hover:text-accent-600 transition-colors">'
           '<svg class="w-8 h-8 text-accent-600" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>'
           '<span class="text-sm font-medium text-neutral-800">Csörsz utca 45, 1124 Budapest</span>'
           '<span class="text-sm">Open in Google Maps ↗</span></a>')
body = body.replace(iframe, maplink, 1)
body = body.replace(one(r'\s*<source src="img/nyc-night-2k\.mp4"[^>]*/>', body).group(0), '', 1)

preview_css = '''<style>
  /* Preview frame: the publish skeleton owns the body element, so the site's body classes live here */
  html body{background:#fff;color:#000;font-size:1rem;line-height:inherit;font-family:'Inter',ui-sans-serif,system-ui,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}
  /* The skeleton already pads the page by the safe-area insets, so don't add them twice */
  .site-main{padding-top:var(--hdr)}
  footer{padding-bottom:0}
</style>'''
out = '<title>mpi.fund preview</title>\n' + preview_css + '\n' + head.strip() + '\n' + body.strip() + '\n'
assert 'gstatic.com/firebasejs' not in out and '<iframe' not in out and 'nyc-night-2k' not in out
path = os.path.join(HERE, 'mpi-fund-preview.html')
open(path, 'w', encoding='utf-8').write(out)
print(path, len(out.encode()), 'bytes')
print('img refs:', sorted(set(re.findall(r'img/[A-Za-z0-9_.\-]+', out))))
