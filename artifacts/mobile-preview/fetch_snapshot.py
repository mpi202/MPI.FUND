# Downloads the site's public Firestore collections and writes snapshot.json, which the
# claude.ai preview reads instead of Firebase. Run it before build_preview.py to refresh the data.
import json, os, urllib.request
BASE = 'https://firestore.googleapis.com/v1/projects/mpifund-v2/databases/(default)/documents/'
COLLECTIONS = ['funds', 'documents', 'categories', 'distribution', 'customerInfo', 'siteSettings']

def val(v):
    k, x = next(iter(v.items()))
    if k in ('stringValue', 'booleanValue', 'timestampValue', 'referenceValue'): return x
    if k == 'integerValue': return int(x)
    if k == 'doubleValue': return float(x)
    if k == 'nullValue': return None
    if k == 'mapValue': return {kk: val(vv) for kk, vv in x.get('fields', {}).items()}
    if k == 'arrayValue': return [val(i) for i in x.get('values', [])]
    raise ValueError('unsupported Firestore type ' + k)

out = {}
for c in COLLECTIONS:
    with urllib.request.urlopen(BASE + c + '?pageSize=500') as r:
        d = json.load(r)
    assert 'nextPageToken' not in d, c + ' has more than 500 documents'
    out[c] = [{'id': doc['name'].rsplit('/', 1)[1], 'data': {k: val(v) for k, v in doc.get('fields', {}).items()}}
              for doc in d.get('documents', [])]
    print(c, len(out[c]))
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'snapshot.json')
json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'), sort_keys=True)
