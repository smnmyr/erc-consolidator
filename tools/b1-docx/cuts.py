"""Shade suggested cuts in a built B1.docx in light blue (no deletion).

  python3 cuts.py in.docx out.docx cuts.json
Each entry: "start" text, and "end" (span runs to the end of the sentence
containing it) or "end_exact" (span ends right after this text); optional
"para" text to choose among paragraphs that contain "start". Yellow
highlighting inside a shaded span is removed so that the blue shows.
"""
import json, re, sys, zipfile, html
src, dst, spec = sys.argv[1:4]
src_mark = open(__file__.replace('cuts.py', 'mark.py')).read()
ns = {}; exec(src_mark[:src_mark.index('src, dst, mode, *args = sys.argv[1:]')], ns)
paras, ptext = ns['paras'], ns['ptext']
SHD = '<w:shd w:val="clear" w:color="auto" w:fill="BDD7EE"/>'
def shade_run(r):
    r = r.replace('<w:highlight w:val="yellow"/>', '')
    m = re.search(r'<w:rPr>(.*?)</w:rPr>', r, flags=re.S)
    if not m: return r.replace('>', '><w:rPr>' + SHD + '</w:rPr>', 1)
    inner = re.sub(r'<w:shd [^>]*/>', '', m.group(1))
    pos = min([inner.find(t) for t in ('<w:fitText', '<w:vertAlign', '<w:rtl', '<w:cs', '<w:em', '<w:lang', '<w:eastAsianLayout') if t in inner] or [len(inner)])
    return r[:m.start(1)] + inner[:pos] + SHD + inner[pos:] + r[m.end(1):]
def apply(p, mask):
    out, last, off = '', 0, 0
    for r in re.finditer(r'<w:r[ >].*?</w:r>', p, flags=re.S):
        rx = r.group(0); out += p[last:r.start()]; last = r.end()
        ts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', rx, flags=re.S)
        if len(ts) != 1: off += len(ptext(rx)); out += rx; continue
        t = html.unescape(ts[0]); m = mask[off:off + len(t)]; off += len(t); k = 0
        while k < len(t):
            e = k
            while e < len(t) and m[e] == m[k]: e += 1
            piece = re.sub(r'<w:t[^>]*>.*?</w:t>', lambda _: f'<w:t xml:space="preserve">{html.escape(t[k:e], quote=False)}</w:t>', rx, count=1, flags=re.S)
            out += shade_run(piece) if m[k] else piece; k = e
    return out + p[last:]
z = zipfile.ZipFile(src); x = z.read('word/document.xml').decode()
missing = []
for c in json.load(open(spec)):
    cand = [p for p in paras(x) if c['start'] in ptext(p) and c.get('para', '') in ptext(p)]
    if not cand: missing.append(c['start']); continue
    p = cand[0]; t = ptext(p); a = t.index(c['start'])
    if 'end_exact' in c: b = t.index(c['end_exact'], a) + len(c['end_exact'])
    else:
        e = t.index(c['end'], a) + len(c['end']); b = t.index('.', e) + 1
    x = x.replace(p, apply(p, [a <= i < b for i in range(len(t))]), 1)
zo = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for it in z.infolist(): zo.writestr(it, x.encode() if it.filename == 'word/document.xml' else z.read(it.filename))
zo.close(); print('missing:', missing)
