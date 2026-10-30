Builds `draft/B1.docx` in the ERC 2027 Part B1 layout (A4, Times New
Roman 11 pt, single spacing, 2 cm side and 1.5 cm top/bottom margins,
header "Mayer | Part B1 | ISLANDS"; Information for Applicants
StG/CoG 2027, v11.0, §2.3).

    cd tools/b1-docx && npm install docx
    python3 md2blocks.py ../../draft/B1.md blocks.json
    node build.js blocks.json ../../draft/B1.docx

`renum.py ../../draft/B1.md` renumbers Section b citations by first
appearance; new references can be cited as `[@key]` with a matching
`[@key] ...` entry in the reference list.

Layout: cover page (title, PI, host, duration, abstract, cross-panel
note), then Part I from a new page, references from a new page, and
the CV from a new page, so each part's page count can be read
directly. Figure 1 is set as its ASCII spec in Courier New 9 pt as a
stand-in for the vector figure.

## Figures and highlighting

- `fig1.py out.svg` draws Figure 1 (connected islands with NFP selections);
  render the PNG fallback with `inkscape out.svg --export-type=png --export-dpi=300`.
  `md2blocks.py` turns `![alt](figures/x.svg)` into an SVG image with `x.png` as fallback.
- `mark.py built.docx out.docx --diff pi-version.docx` highlights in yellow every
  word that is new relative to the PI's last saved docx; yellow still present in
  the PI's version carries over. Never use tracked changes.
