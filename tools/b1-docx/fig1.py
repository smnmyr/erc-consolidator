"""Generate Figure 1 of B1: the Web as a network of clients and servers, with
islands as regions of that network that raise the Web's contract.

  python3 fig1.py out.svg
Thin grey links carry the Web contract; thick links inside an island carry the
island's raised contract; dashed links cross an island border (admission
inbound, fallback to the Web contract outbound).
Render a PNG fallback with: inkscape out.svg --export-type=png --export-dpi=300
"""
import sys, math
from xml.sax.saxutils import escape

WEB_NFPS = ['scalability', 'simplicity', 'extensibility', 'evolvability', 'visibility', 'low coordination']
ISLANDS = [  # (name, two-line description, added NFPs, traded Web NFPs)
    ('Island L', ('legal citation', 'and copyright'), ['persistence', 'span addressing', 'backlinks', 'attribution', 'credentials'], []),
    ('Island S', ('supply-chain', 'carbon accounting'), ['persistence', 'attribution', 'credentials', 'confidential refs',
                                                        'purpose binding', 'capability discovery'], []),
    ('Island M', ('public-interest', 'social media'), ['persistence', 'attribution', 'credentials', 'confidential refs'], []),
    ('Island N', ('signed research claims', '(nanopublications)'), ['persistence', 'span addressing', 'attribution'], []),
    ('Island F', ('fixed industrial', 'installations'), ['static binding'], ['evolvability']),
]
FONT = 'Arial, Arimo, Helvetica, sans-serif'
INK, SEL, WEB, WEBCHIP, SAND, SHORE = '#2B2B2B', '#1F5F7A', '#EEF4F9', '#5B7F99', '#F4ECDC', '#9C8556'
NODE_OUT, NODE_IN, LINK_OUT, RED = '#9AA9B5', '#1F5F7A', '#AEB9C2', '#B5533C'
W = 1130
IW, GAP = 186, 34
ix0 = (W - (5 * IW + 4 * GAP)) / 2
TOP, IH = 112, 300
H = TOP + IH + 150

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">',
     f'<rect x="10" y="10" width="{W - 20}" height="{H - 20}" rx="14" fill="{WEB}" stroke="{WEBCHIP}" stroke-width="2"/>',
     f'<text x="28" y="40" font-size="18" fill="{INK}"><tspan font-weight="bold">The Web</tspan>'
     ' · a network of clients and servers that share one contract</text>']
cx = 28
for n in WEB_NFPS:
    w = 14 + 8.2 * len(n)
    o.append(f'<rect x="{cx}" y="54" width="{w}" height="24" rx="12" fill="{WEBCHIP}"/>')
    o.append(f'<text x="{cx + w / 2}" y="71" text-anchor="middle" font-size="14" fill="white">{escape(n)}</text>')
    cx += w + 8
o.append(f'<text x="{cx + 6}" y="71" font-size="14" font-style="italic" fill="{INK}">+ classic Web links, no further guarantees</text>')

links, nodes = [], []      # links drawn first, nodes on top
island_nodes = []
for k, (name, sub, added, traded) in enumerate(ISLANDS):
    x = ix0 + k * (IW + GAP)
    ny = TOP + IH - 46
    pts = [(x + 40, ny + 14), (x + IW / 2, ny - 22), (x + IW - 40, ny + 14)]
    island_nodes.append(pts)
# outside nodes: between islands, above the row, and below it
out_mid = [(ix0 + k * (IW + GAP) + IW + GAP / 2, TOP + IH - 120 + (25 if k % 2 else -15)) for k in range(4)]
out_low = [(ix0 + 40 + j * ((5 * IW + 4 * GAP - 80) / 8), TOP + IH + 62 + (14 if j % 2 else 0)) for j in range(9)]
# Web links among outside nodes
for a, b in zip(out_low, out_low[1:]): links.append(('out', a, b))
for k, m in enumerate(out_mid):  # link each gap node to the bottom node nearest below it
    nb = min(out_low, key=lambda q: abs(q[0] - m[0]))
    links.append(('out', m, nb))
# border-crossing links from island nodes to outside nodes
for k, pts in enumerate(island_nodes):
    links.append(('cross', pts[0], min(out_low, key=lambda q: abs(q[0] - pts[0][0]))))
    links.append(('cross', pts[2], min(out_low, key=lambda q: abs(q[0] - pts[2][0]))))
    if k < 4: links.append(('cross', pts[2], out_mid[k]))
    if k > 0: links.append(('cross', pts[0], out_mid[k - 1]))
style = {'out': f'stroke="{LINK_OUT}" stroke-width="1.6"',
         'cross': f'stroke="{LINK_OUT}" stroke-width="1.6" stroke-dasharray="5 4"'}
for kind, a, b in links:
    if kind == 'out':
        o.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" {style[kind]}/>')
# islands on top of the outside links, then their inner links and nodes
for k, (name, sub, added, traded) in enumerate(ISLANDS):
    x = ix0 + k * (IW + GAP)
    o.append(f'<rect x="{x}" y="{TOP}" width="{IW}" height="{IH}" rx="22" fill="{SAND}" stroke="{SHORE}" stroke-width="2"/>')
    o.append(f'<text x="{x + IW / 2}" y="{TOP + 25}" text-anchor="middle" font-size="18" font-weight="bold" fill="{INK}">{escape(name)}</text>')
    for li, line in enumerate(sub):
        o.append(f'<text x="{x + IW / 2}" y="{TOP + 44 + 16 * li}" text-anchor="middle" font-size="14" font-style="italic" fill="{INK}">{escape(line)}</text>')
    y = TOP + 72
    for n in added:
        o.append(f'<rect x="{x + 12}" y="{y}" width="{IW - 24}" height="20" rx="10" fill="{SEL}"/>')
        o.append(f'<text x="{x + IW / 2}" y="{y + 14.5}" text-anchor="middle" font-size="13.5" fill="white">+ {escape(n)}</text>')
        y += 24
    for n in traded:
        o.append(f'<rect x="{x + 12}" y="{y}" width="{IW - 24}" height="20" rx="10" fill="white" stroke="{RED}" stroke-width="1.2" stroke-dasharray="4 2"/>')
        o.append(f'<text x="{x + IW / 2}" y="{y + 14.5}" text-anchor="middle" font-size="13.5" fill="{RED}">− {escape(n)}</text>')
        y += 24
    pts = island_nodes[k]
    for kind, a, b in links:  # border crossings drawn on top of the island
        if kind == 'cross' and a in pts:
            o.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{WEBCHIP}" stroke-width="1.8" stroke-dasharray="5 4"/>')
    for a, b in [(0, 1), (1, 2), (0, 2)]:
        o.append(f'<line x1="{pts[a][0]:.1f}" y1="{pts[a][1]:.1f}" x2="{pts[b][0]:.1f}" y2="{pts[b][1]:.1f}" stroke="{SEL}" stroke-width="4"/>')
    for (px, py) in pts:
        o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="8" fill="{NODE_IN}" stroke="white" stroke-width="2"/>')
for (px, py) in out_mid + out_low:
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="{NODE_OUT}" stroke="white" stroke-width="2"/>')
# legend
ly = H - 34
o.append(f'<line x1="40" y1="{ly}" x2="80" y2="{ly}" stroke="{LINK_OUT}" stroke-width="1.6"/>')
o.append(f'<text x="88" y="{ly + 5}" font-size="14" fill="{INK}">Web contract</text>')
o.append(f'<line x1="210" y1="{ly}" x2="250" y2="{ly}" stroke="{SEL}" stroke-width="4"/>')
o.append(f'<text x="258" y="{ly + 5}" font-size="14" fill="{INK}">raised contract inside an island</text>')
o.append(f'<line x1="490" y1="{ly}" x2="530" y2="{ly}" stroke="{WEBCHIP}" stroke-width="1.8" stroke-dasharray="5 4"/>')
o.append(f'<text x="538" y="{ly + 5}" font-size="14" fill="{INK}">border crossing: admission inbound, fallback to the Web contract outbound</text>')
o.append('</svg>')
open(sys.argv[1], 'w').write('\n'.join(o))
