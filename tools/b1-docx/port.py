"""Port the PI's paragraph edits from a saved B1.docx into B1.md.

  python3 port.py B1.md ref.docx pi.docx
ref.docx is the last version written from B1.md; every paragraph that differs
in pi.docx replaces the matching B1.md block, keeping the old text as a comment.
"""
import zipfile, re, html, sys, difflib, textwrap
md_path, ref_path, pi_path = sys.argv[1:4]
def paras(f):
    x = zipfile.ZipFile(f).read('word/document.xml').decode()
    return re.findall(r'<w:p[ >].*?</w:p>', x, flags=re.S)
def text(p): return re.sub(r'\s+', ' ', html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p)))).strip()
def fmt(p):
    out = ''
    for r in re.findall(r'<w:r[ >].*?</w:r>', p, flags=re.S):
        t = html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', r)))
        if not t: continue
        b = '<w:b/>' in r; it = '<w:i/>' in r
        lead = len(t) - len(t.lstrip()); trail = len(t) - len(t.rstrip()); core = t.strip()
        if core and b: core = f'**{core}**'
        elif core and it: core = f'*{core}*'
        out += t[:lead] + core + (t[len(t) - trail:] if trail else '')
    out = re.sub(r'\*\*(\s*)\*\*', r'\1', out); out = re.sub(r'(?<![*\w])\*(\s+)\*(?![*\w])', r'\1', out)
    return re.sub(r'\s+', ' ', out).strip()
a = [p for p in paras(ref_path) if text(p)]; b = [p for p in paras(pi_path) if text(p)]
md = open(md_path).read()
def norm(s): return re.sub(r'\s+', ' ', re.sub(r'[*`]', '', re.sub(r'<!--.*?-->', '', s, flags=re.S))).strip()
blocks = re.split(r'(\n\n+)', md)
done = 0
sm = difflib.SequenceMatcher(None, [text(p) for p in a], [text(p) for p in b], autojunk=False)
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == 'equal': continue
    if op != 'replace' or (i2 - i1) != (j2 - j1):
        print('SKIP (structural change):', op, [text(p)[:60] for p in a[i1:i2]], [text(p)[:60] for p in b[j1:j2]]); continue
    for pa, pb in zip(a[i1:i2], b[j1:j2]):
        old = text(pa); new = fmt(pb)
        hits = [k for k, blk in enumerate(blocks) if norm(re.sub(r'^- ', '', blk.strip())) == re.sub(r'[*`]', '', old)]
        if len(hits) != 1:
            print('NO UNIQUE MATCH:', old[:80], len(hits)); continue
        k = hits[0]; blk = blocks[k]
        prefix = '- ' if blk.lstrip().startswith('- ') else ''
        body = textwrap.fill(prefix + new, 70, break_on_hyphens=False, subsequent_indent='  ' if prefix else '')
        comment = '<!-- was (before PI edit in B1.docx): ' + norm(blk).replace('--', '- -') + ' -->\n'
        blocks[k] = comment + body; done += 1
open(md_path, 'w').write(''.join(blocks))
print(done, 'paragraphs ported')
