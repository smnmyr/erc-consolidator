"""Mark Claude's edits in a built B1.docx with a yellow highlight (no tracked changes).

  python3 mark.py in.docx out.docx --abstract OLD_P1 OLD_P2 NEW_P1 NEW_P2
      Replace the two abstract paragraphs (found by the opening words of the
      old text) with the new text; inserted words are highlighted.
  python3 mark.py in.docx out.docx --from "Opening words of new text" [...]
      Highlight from each given phrase to the end of its paragraph.
  python3 mark.py in.docx out.docx --diff reference.docx
      Highlight every word of in.docx that is new relative to reference.docx
      (e.g., the PI's last saved version). Citation renumbering is ignored.
      Yellow highlights still present in reference.docx carry over.
Text files use *...* for italics.
"""
import zipfile, re, sys, html, difflib

AFTER_HL = ('<w:u ', '<w:u/', '<w:effect', '<w:bdr', '<w:shd', '<w:fitText', '<w:vertAlign',
            '<w:rtl', '<w:cs', '<w:em', '<w:lang', '<w:eastAsianLayout', '<w:specVanish', '<w:oMath')

def hl_rpr(r):
    if '<w:highlight' in r: return r
    m = re.search(r'<w:rPr>(.*?)</w:rPr>', r, flags=re.S)
    if not m:
        return r.replace('>', '><w:rPr><w:highlight w:val="yellow"/></w:rPr>', 1)
    inner = m.group(1)
    pos = min([inner.find(t) for t in AFTER_HL if t in inner] or [len(inner)])
    inner = inner[:pos] + '<w:highlight w:val="yellow"/>' + inner[pos:]
    return r[:m.start(1)] + inner + r[m.end(1):]

def ptext(p): return html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, flags=re.S)))
def paras(x): return re.findall(r'<w:p[ >].*?</w:p>', x, flags=re.S)
def toks(s): return re.findall(r'\s+|[^\s]+', s)

def tokens_from_text(s):
    res, it = [], False
    for part in re.split(r'(\*)', s):
        if part == '*': it = not it; continue
        res += [(t, it) for t in toks(part)]
    return res

def run(t, it, hl):
    rpr = '<w:rPr>' + ('<w:i/><w:iCs/>' if it else '') + ('<w:highlight w:val="yellow"/>' if hl else '') + '<w:lang w:val="en-US"/></w:rPr>'
    return f'<w:r>{rpr}<w:t xml:space="preserve">{html.escape(t, quote=False)}</w:t></w:r>'

def replace_marked(p, old, new):
    a, b = tokens_from_text(old), tokens_from_text(new)
    head = re.match(r'<w:p(?: [^>]*)?>', p).group(0)
    m = re.search(r'<w:pPr>.*?</w:pPr>', p, flags=re.S)
    seq = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op in ('equal', 'replace', 'insert'):
            seq += [[t, i, op != 'equal'] for t, i in b[j1:j2]]
    for k in range(1, len(seq) - 1):  # close gaps between highlighted words
        if seq[k][0].isspace() and seq[k - 1][2] and seq[k + 1][2]: seq[k][2] = True
    merged = []
    for t, i, h in seq:
        if merged and merged[-1][1:] == [i, h]: merged[-1][0] += t
        else: merged.append([t, i, h])
    body = ''.join(run(t, i, h) for t, i, h in merged)
    return head + (m.group(0) if m else '') + body + '</w:p>'

def highlight_from(p, phrase):
    runs = list(re.finditer(r'<w:r[ >].*?</w:r>', p, flags=re.S))
    full, spans = '', []
    for r in runs:
        t = ptext(r.group(0)); spans.append((len(full), len(full) + len(t))); full += t
    k = full.find(phrase)
    if k < 0: return None
    out, last = '', 0
    for r, (s, e) in zip(runs, spans):
        out += p[last:r.start()]; last = r.end(); rx = r.group(0)
        if e <= k: out += rx
        elif s >= k: out += hl_rpr(rx)
        else:  # split run at k
            t = ptext(rx); cut = k - s
            pre = re.sub(r'<w:t[^>]*>.*?</w:t>', lambda _: f'<w:t xml:space="preserve">{html.escape(t[:cut], quote=False)}</w:t>', rx, count=1, flags=re.S)
            post = re.sub(r'<w:t[^>]*>.*?</w:t>', lambda _: f'<w:t xml:space="preserve">{html.escape(t[cut:], quote=False)}</w:t>', rx, count=1, flags=re.S)
            out += pre + hl_rpr(post)
    return out + p[last:]

def cite_key(t):
    return re.sub(r'\d+', '#', t) if ('[' in t or ']' in t or re.fullmatch(r'\d+[,\]][.,;:)]*', t)) else t

def word_mask(old, new, old_mask=None):
    """Per-character highlight mask for new, from a word diff against old.
    old_mask (per character of old) carries existing highlights over."""
    a, b = toks(old), toks(new)
    apos = [0]
    for t in a: apos.append(apos[-1] + len(t))
    mask = [False] * len(new); pos = [0]
    for t in b: pos.append(pos[-1] + len(t))
    flags = [False] * len(b)
    sm = difflib.SequenceMatcher(None, [cite_key(t) for t in a], [cite_key(t) for t in b], autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            for j in range(j1, j2): flags[j] = not b[j].isspace()
        elif old_mask:
            for i, j in zip(range(i1, i2), range(j1, j2)):
                flags[j] = any(old_mask[apos[i]:apos[i + 1]]) and not b[j].isspace()
    for j in range(1, len(b) - 1):
        if b[j].isspace() and flags[j - 1] and flags[j + 1]: flags[j] = True
    for j, f in enumerate(flags):
        if f:
            for c in range(pos[j], pos[j + 1]): mask[c] = True
    return mask

def apply_mask(p, mask):
    out, last, off = '', 0, 0
    for r in re.finditer(r'<w:r[ >].*?</w:r>', p, flags=re.S):
        rx = r.group(0); out += p[last:r.start()]; last = r.end()
        ts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', rx, flags=re.S)
        if len(ts) != 1:
            off += len(ptext(rx)); out += rx; continue
        t = html.unescape(ts[0]); m = mask[off:off + len(t)]; off += len(t)
        segs, k = [], 0
        while k < len(t):
            e = k
            while e < len(t) and m[e] == m[k]: e += 1
            segs.append((t[k:e], m[k])); k = e
        for seg, h in segs:
            piece = re.sub(r'<w:t[^>]*>.*?</w:t>', lambda _: f'<w:t xml:space="preserve">{html.escape(seg, quote=False)}</w:t>', rx, count=1, flags=re.S)
            out += hl_rpr(piece) if h else piece
    return out + p[last:]

def norm(t): return re.sub(r'\s+', ' ', t).strip()

def ref_mask(p):
    m = []
    for r in re.findall(r'<w:r[ >].*?</w:r>', p, flags=re.S):
        m += ['w:val="yellow"' in r] * len(ptext(r))
    return m

def diff_mark(x, ref):
    oldraw = {}
    for p in paras(ref):
        t = ptext(p)
        if norm(t): oldraw.setdefault(norm(t), (t, ref_mask(p)))
    olds = list(oldraw)
    new_ps = [p for p in paras(x)]
    news = [norm(ptext(p)) for p in new_ps]
    idx = [i for i, t in enumerate(news) if t]
    key = lambda t: ' '.join(cite_key(w) for w in t.split(' '))
    sm = difflib.SequenceMatcher(None, [key(t) for t in olds], [key(news[i]) for i in idx], autojunk=False)
    repl = {}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            for i, j in zip(range(i1, i2), range(j1, j2)):
                o = oldraw[olds[i]]
                if any(o[1]):
                    repl[idx[j]] = apply_mask(new_ps[idx[j]], word_mask(o[0], ptext(new_ps[idx[j]]), o[1]))
            continue
        for j in range(j1, j2):
            t = news[idx[j]]
            # word-level similarity; reference entries must match closely, prose may have changed more
            ratio = lambda o: difflib.SequenceMatcher(None, key(o).split(' '), key(t).split(' '), autojunk=False).ratio()
            thr = 0.8 if re.match(r'^\[\d+\] ', t) else 0.4
            best = max(olds[i1:i2], key=ratio, default=None)
            if best is None or ratio(best) <= thr:  # block misaligned: search all
                cands = [o for o in olds if difflib.SequenceMatcher(None, key(o), key(t)).quick_ratio() > thr]
                best = max(cands, key=ratio, default=None)
            if best is not None and ratio(best) > thr:
                mask = word_mask(oldraw[best][0], ptext(new_ps[idx[j]]), oldraw[best][1])
            else:
                mask = [not c.isspace() or 0 < k < len(t) - 1 for k, c in enumerate(ptext(new_ps[idx[j]]))]
            repl[idx[j]] = apply_mask(new_ps[idx[j]], mask)
    out, last = '', 0
    for i, m in enumerate(re.finditer(r'<w:p[ >].*?</w:p>', x, flags=re.S)):
        out += x[last:m.start()] + repl.get(i, m.group(0)); last = m.end()
    return out + x[last:]

src, dst, mode, *args = sys.argv[1:]
z = zipfile.ZipFile(src); x = z.read('word/document.xml').decode()
if mode == '--abstract':
    olds = [open(f).read().strip() for f in args[:2]]; news = [open(f).read().strip() for f in args[2:4]]
    for old, new in zip(olds, news):
        start = old.replace('*', '')[:30]
        p = next((p for p in paras(x) if ptext(p).startswith(start)), None)
        if p is None: sys.exit('not found: ' + start)
        x = x.replace(p, replace_marked(p, old, new), 1)
elif mode == '--diff':
    x = diff_mark(x, zipfile.ZipFile(args[0]).read('word/document.xml').decode())
elif mode == '--from':
    for phrase in args:
        for p in paras(x):
            q = highlight_from(p, phrase)
            if q is not None: x = x.replace(p, q, 1); break
        else: sys.exit('not found: ' + phrase)
zo = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
for it in z.infolist():
    zo.writestr(it, x.encode() if it.filename == 'word/document.xml' else z.read(it.filename))
zo.close()
