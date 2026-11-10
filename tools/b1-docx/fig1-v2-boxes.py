"""Generate Figure 1 of B1: islands within the Web, each raising the Web's contract.

  python3 fig1.py out.svg
The outer box is the Web with its own NFP selection (the contract between all
clients and servers). Each island inherits that contract and adds NFPs for its
members; Island F trades one Web NFP (evolvability) for static binding.
Render a PNG fallback with: inkscape out.svg --export-type=png --export-dpi=300
"""
import sys
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
INK, SEL, WEB, WEBCHIP, SAND, SHORE, MUTE = '#2B2B2B', '#1F5F7A', '#EEF4F9', '#5B7F99', '#F4ECDC', '#9C8556', '#8A8A8A'
W, X0, Y0 = 1130, 10, 10
IW, GAP = 202, 18
ix0 = (W - (5 * IW + 4 * GAP)) / 2
TOP = 108                     # top of islands
ROWS = max(len(a) + len(t) for _, _, a, t in ISLANDS)
IH = 96 + 26 * ROWS + 8
H = TOP + IH + 58

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">',
     f'<rect x="{X0}" y="{Y0}" width="{W - 2 * X0}" height="{H - 2 * Y0}" rx="14" fill="{WEB}" stroke="{WEBCHIP}" stroke-width="2"/>',
     f'<text x="{X0 + 18}" y="{Y0 + 30}" font-size="18" fill="{INK}"><tspan font-weight="bold">The Web</tspan>'
     ' · the contract between all clients and servers</text>']
# Web NFP chips
cx = X0 + 18
for n in WEB_NFPS:
    w = 14 + 8.2 * len(n)
    o.append(f'<rect x="{cx}" y="{Y0 + 44}" width="{w}" height="24" rx="12" fill="{WEBCHIP}"/>')
    o.append(f'<text x="{cx + w / 2}" y="{Y0 + 61}" text-anchor="middle" font-size="14" fill="white">{escape(n)}</text>')
    cx += w + 8
o.append(f'<text x="{cx + 6}" y="{Y0 + 61}" font-size="14" font-style="italic" fill="{INK}">+ classic Web links, no further guarantees</text>')
for k, (name, sub, added, traded) in enumerate(ISLANDS):
    x = ix0 + k * (IW + GAP)
    o.append(f'<rect x="{x}" y="{TOP}" width="{IW}" height="{IH}" rx="20" fill="{SAND}" stroke="{SHORE}" stroke-width="2"/>')
    o.append(f'<text x="{x + IW / 2}" y="{TOP + 26}" text-anchor="middle" font-size="18" font-weight="bold" fill="{INK}">{escape(name)}</text>')
    for li, line in enumerate(sub):
        o.append(f'<text x="{x + IW / 2}" y="{TOP + 45 + 16 * li}" text-anchor="middle" font-size="14" font-style="italic" fill="{INK}">{escape(line)}</text>')
    # inherited Web contract
    o.append(f'<rect x="{x + 10}" y="{TOP + 72}" width="{IW - 20}" height="22" rx="4" fill="{WEB}" stroke="{WEBCHIP}" stroke-width="1" stroke-dasharray="3 2"/>')
    o.append(f'<text x="{x + IW / 2}" y="{TOP + 88}" text-anchor="middle" font-size="13" fill="{WEBCHIP}">Web contract, raised by:</text>')
    y = TOP + 102
    for n in added:
        o.append(f'<rect x="{x + 12}" y="{y}" width="{IW - 24}" height="21" rx="10.5" fill="{SEL}"/>')
        o.append(f'<text x="{x + IW / 2}" y="{y + 15}" text-anchor="middle" font-size="14" fill="white">+ {escape(n)}</text>')
        y += 26
    for n in traded:
        o.append(f'<rect x="{x + 12}" y="{y}" width="{IW - 24}" height="21" rx="10.5" fill="white" stroke="#B5533C" stroke-width="1.2" stroke-dasharray="4 2"/>')
        o.append(f'<text x="{x + IW / 2}" y="{y + 15}" text-anchor="middle" font-size="14" fill="#B5533C">− {escape(n)}</text>')
        y += 26
o.append(f'<text x="{W / 2}" y="{TOP + IH + 32}" text-anchor="middle" font-size="14" fill="{INK}">'
         'Entering an island means accepting its raised contract (admission); references that leave it fall back to the Web contract.</text>')
o.append('</svg>')
open(sys.argv[1], 'w').write('\n'.join(o))
