"""Generate Figure 1 of B1: connected islands, each with its own NFP selection.

  python3 fig1.py out.svg
Edit ISLANDS below to change selections; render a PNG fallback with
  inkscape out.svg --export-type=png --export-dpi=300
"""
import sys
from xml.sax.saxutils import escape

NFPS = ['persistence', 'span addressing', 'backlinks', 'attribution', 'credentials',
        'confidential refs', 'purpose binding', 'capability discovery', 'static binding']
ISLANDS = [
    ('Island L', 'legal citation', {'persistence', 'span addressing', 'backlinks', 'attribution', 'credentials'}),
    ('Island S', 'supply chain', {'persistence', 'attribution', 'credentials', 'confidential refs',
                                  'purpose binding', 'capability discovery'}),
    ('Island M', 'social media', {'persistence', 'attribution', 'credentials', 'confidential refs'}),
    ('Fixed installation', 'e.g., building automation', {'static binding'}),
]
W, H = 900, 400
IW, GAP, X0, Y0, IH = 190, 40, 10, 8, 302
FONT = 'Arial, Arimo, Helvetica, sans-serif'
SAND, SHORE, INK, SEL, OFF, SEA, BAND = '#F4ECDC', '#9C8556', '#2B2B2B', '#1F5F7A', '#BDBDBD', '#EEF4F9', '#D5E5F1'

o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">',
     '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto-start-reverse">'
     f'<path d="M0,0 L10,5 L0,10 z" fill="#4A6B82"/></marker></defs>',
     f'<rect width="{W}" height="{H}" fill="{SEA}"/>']
for k, (name, sub, sel) in enumerate(ISLANDS):
    x = X0 + k * (IW + GAP)
    o.append(f'<rect x="{x}" y="{Y0}" width="{IW}" height="{IH}" rx="26" fill="{SAND}" stroke="{SHORE}" stroke-width="2"/>')
    o.append(f'<text x="{x + IW / 2}" y="{Y0 + 27}" text-anchor="middle" font-size="18" font-weight="bold" fill="{INK}">{escape(name)}</text>')
    o.append(f'<text x="{x + IW / 2}" y="{Y0 + 47}" text-anchor="middle" font-size="14" font-style="italic" fill="{INK}">{escape(sub)}</text>')
    for j, n in enumerate(NFPS):
        y = Y0 + 60 + j * 26
        on = n in sel
        o.append(f'<rect x="{x + 12}" y="{y}" width="{IW - 24}" height="21" rx="10.5" '
                 + (f'fill="{SEL}"/>' if on else f'fill="white" stroke="{OFF}" stroke-width="1"/>'))
        o.append(f'<text x="{x + IW / 2}" y="{y + 15}" text-anchor="middle" font-size="14" '
                 f'fill="{"white" if on else "#9E9E9E"}">{escape(n)}</text>')
    # border crossing to the open Web
    cx = x + IW / 2
    o.append(f'<line x1="{cx}" y1="{Y0 + IH + 4}" x2="{cx}" y2="{352}" stroke="#4A6B82" stroke-width="2" '
             'marker-start="url(#a)" marker-end="url(#a)"/>')
    if k < len(ISLANDS) - 1:  # inter-island references
        gx = x + IW
        for yy in (Y0 + IH / 2,):
            o.append(f'<line x1="{gx + 3}" y1="{yy}" x2="{gx + GAP - 3}" y2="{yy}" stroke="#4A6B82" '
                     'stroke-width="2" stroke-dasharray="3 3" marker-start="url(#a)" marker-end="url(#a)"/>')
o.append(f'<text x="{X0 + IW / 2 + 8}" y="{Y0 + IH + 28}" font-size="12" fill="#4A6B82">admission / degradation</text>')
o.append(f'<rect x="{X0}" y="356" width="{W - 2 * X0}" height="36" rx="8" fill="{BAND}" stroke="#4A6B82" stroke-width="1"/>')
o.append(f'<text x="{W / 2}" y="379" text-anchor="middle" font-size="15" fill="{INK}"><tspan font-weight="bold">Open Web:</tspan>'
         ' Classic Jumplinks, no guarantees, low coordination, planetary scale</text>')
o.append('</svg>')
open(sys.argv[1], 'w').write('\n'.join(o))
