"""Italicize key terms: first use per section (### heading) in the body.

  python3 italicize.py file.md START_MARKER END_MARKER [--dry]
Bold key terms in running prose become italic; run-in headings stay bold.
"""
import re, sys
path, start, end = sys.argv[1:4]; dry = '--dry' in sys.argv
LINK = r'(?:Classic Jumplinks?|Archived Links?|Trusted Links?|Verified Links?|Cryptographic Links?|Endorsed Links?|Credentialed Links?|Purpose-Bound Links?|Capability Links?|Static Links?|Attributed|Anonymous/Pseudonymous Links)'
TERMS = [
    r'non-functional\s+propert(?:y|ies)', r'(?<![A-Z] )\b[iI]slands?\b(?!\s+[LSM]\b)(?!-)', r'theory\s+of\s+chosen\s+guarantees',
    r'link\s+class(?:es)?(?!\s+of)', r'guarantee\s+calculus', r'admission\s+protocol', r'border\s+crossing',
    r'confidentiality-preserving\s+references?', r'purpose\s+binding', r'capability\s+discovery',
    r'verifiable\s+credentials?', r'credible\s+commitment', r'[Rr]ealizability', r'[Nn]ecessity',
    r'link\s+time', r'transclusion', r'secure\s+multi-party\s+computation', r'affordances?', r'signifiers?',
    r'data\s+sovereignty', r'portability', r'mutable\s+architecture', r'tussle',
] + [c + r'(?:s|\b)' for c in (r'Classic\s+Jumplink', r'Archived\s+Link', r'Trusted\s+Link', r'Verified\s+Link',
     r'Cryptographic\s+Link', r'Endorsed\s+Link', r'Credentialed\s+Link', r'Purpose-Bound\s+Link', r'Capability\s+Link',
     r'Static\s+Link', r'Attributed', r'Anonymous/Pseudonymous\s+Link')]
BOLD_TO_ITALIC = re.compile(r'\*\*(' + LINK + r'|theory\s+of\s+chosen\s+guarantees|link\s+classes)\*\*')
s = open(path).read()
a = s.index(start); b = s.index(end, a)
body = s[a:b]
# protect comments, code blocks, headings, images, table rows of headers
prot = []
def keep(m):
    prot.append(m.group(0)); return f'\x00{len(prot) - 1}\x00'
body = BOLD_TO_ITALIC.sub(r'*\1*', body)
body = re.sub(r'<!--.*?-->|```.*?```|^#{1,6} [^\n]*$|^!\[[^\n]*$|`[^`\n]+`|^\*Figure \d.*?\*(?=\s*(?:<!--|\n\n|$))|^\|(?![^|\n]*(?:Link|Jumplink|Attributed)[^|\n]*\|)[^\n]*$',
              keep, body, flags=re.S | re.M)
def spans(text):
    """character ranges inside *...* or **...** emphasis"""
    out = []
    for m in re.finditer(r'\*\*[^*]+?\*\*|(?<!\*)\*(?![\s*])[^*\n]*(?:\n(?!\n)[^*\n]*)*?(?<![\s*])\*(?!\*)', text):
        out.append((m.start(), m.end()))
    return out
changes = []
parts = re.split(r'(\x00\d+\x00)', body)
# sections: split on protected headings
sect_text = ''.join(parts)
sections = re.split(r'(\x00\d+\x00)', sect_text)
newbody, seen = [], set()
for seg in sections:
    if re.fullmatch(r'\x00\d+\x00', seg):
        if prot[int(seg[1:-1])].startswith('#'): seen = set()
        newbody.append(seg); continue
    for k, t in enumerate(TERMS):
        if k in seen: continue
        for m in re.finditer(t, seg):
            sp = spans(seg)
            if any(x <= m.start() < y for x, y in sp): seen.add(k); break
            # skip inside bold run-in lead (line starting with **...)
            seg = seg[:m.start()] + '*' + m.group(0) + '*' + seg[m.end():]
            changes.append(m.group(0).replace('\n', ' ')); seen.add(k); break
    newbody.append(seg)
body = ''.join(newbody)
body = re.sub(r'\x00(\d+)\x00', lambda m: prot[int(m.group(1))], body)
print(len(changes), 'terms italicized:', '; '.join(changes))
if not dry: open(path, 'w').write(s[:a] + body + s[b:])
