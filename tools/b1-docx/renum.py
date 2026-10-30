"""Renumber B1 citations by first appearance.

Citations in Section b may be numbers ([3, 5]) or keys ([@key]); reference
entries may be "[n] ..." or "[@key] ...". Numbers are first turned into keys
@nN, then everything is renumbered by first appearance outside HTML comments.
"""
import re, sys
p = sys.argv[1]
L = open(p).read().split('\n')
start = next(i for i, l in enumerate(L) if l.startswith('## Section b'))
refs = next(i for i, l in enumerate(L) if l.startswith('### References (not counted'))
end = next(i for i, l in enumerate(L) if l.startswith('## Section c'))
for i in range(start, refs):
    L[i] = re.sub(r'\[(\d+(?:,\s*\d+)*)\]',
                  lambda m: '[' + ', '.join('@n' + n.strip() for n in m.group(1).split(',')) + ']', L[i])
for i in range(refs, end):
    L[i] = re.sub(r'^\[(\d+)\] ', lambda m: '[@n' + m.group(1) + '] ', L[i])
body = '\n'.join(L[start:refs])
order = []
for g in re.findall(r'\[(@[^\]]+)\]', re.sub(r'<!--.*?-->', '', body, flags=re.S)):
    for k in re.split(r',\s*', g):
        if k[1:] not in order:
            order.append(k[1:])
entries = {}
for l in L[refs:end]:
    m = re.match(r'^\[@([^\]]+)\] (.*)$', l)
    if m:
        entries[m.group(1)] = m.group(2)
missing = [k for k in order if k not in entries]
assert not missing, missing
num = {k: i + 1 for i, k in enumerate(order)}
body = re.sub(r'\[(@[^\]]+)\]', lambda m: '[' + ', '.join(
    str(num[k[1:]]) if k[1:] in num else 'removed: ' + k[1:] for k in re.split(r',\s*', m.group(1))) + ']', body)
rest = [l for l in L[refs + 1:end] if l.strip() and not re.match(r'^\[@', l)]
newrefs = [L[refs], ''] + [f'[{num[k]}] {entries[k]}' for k in order] + [''] + (rest + [''] if rest else [])
open(p, 'w').write('\n'.join(L[:start] + body.split('\n') + newrefs + L[end:]))
print('cited', len(order), 'uncited entries dropped:', [k for k in entries if k not in num])
