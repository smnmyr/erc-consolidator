"""Parse B2.md into JSON blocks for build_b2.js (Part II, references, annex).

  python3 md2blocks_b2.py ../../draft/B2.md work/b2-blocks.json
Supports headings, paragraphs, bullet and numbered lists, and pipe tables.
"""
import re, json, sys
src = open(sys.argv[1]).read()
src = re.sub(r'<!--.*?-->', '', src, flags=re.S)
def sect(start, end):
    i = src.index(start); j = src.index(end, i)
    return src[i:j]
def cells(line): return [c.strip() for c in line.strip().strip('|').split('|')]
def blocks(md):
    out = []; lines = md.split('\n'); i = 0; para = []
    def flush():
        nonlocal para
        if para: out.append({'t': 'p', 'text': ' '.join(x.strip() for x in para)}); para = []
    while i < len(lines):
        l = lines[i]
        if l.startswith('>'): flush(); i += 1; continue
        if l.startswith('---') and not l.startswith('---|'): flush(); i += 1; continue
        if l.lstrip().startswith('|'):
            flush(); rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                if not re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i]): rows.append(cells(lines[i]))
                i += 1
            out.append({'t': 'table', 'rows': rows}); continue
        m = re.match(r'^(#{2,4}) (.*)', l)
        if m: flush(); out.append({'t': 'h', 'level': len(m.group(1)), 'text': m.group(2).strip()}); i += 1; continue
        m = re.match(r'^(\s*)(- |\d+\. )(.*)', l)
        if m:
            flush(); kind = 'ul' if m.group(2) == '- ' else 'ol'; item = [m.group(3)]; i += 1
            while i < len(lines) and lines[i].strip() and re.match(r'^\s+\S', lines[i]) and not re.match(r'^\s*(- |\d+\. )', lines[i]):
                item.append(lines[i].strip()); i += 1
            out.append({'t': kind, 'text': ' '.join(item)}); continue
        if not l.strip(): flush(); i += 1; continue
        para.append(l); i += 1
    flush(); return out
doc = {}
doc['partII'] = blocks(sect('## Section 1', '### References (not counted'))
doc['refs'] = blocks(sect('### References (not counted', '## Annex'))[1:]
doc['annex'] = blocks(sect('## Annex', '## Open TODOs'))
json.dump(doc, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
for k, v in doc.items(): print(k, len(v), sum(len(b.get('text', '').split()) + sum(len(' '.join(r).split()) for r in b.get('rows', [])) for b in v))
