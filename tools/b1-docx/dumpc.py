"""Dump docx paragraphs with Word comment anchors as ⟦Cn: ... ⟧: python3 dumpc.py x.docx"""
import zipfile,re,html,sys
x=zipfile.ZipFile(sys.argv[1]).read('word/document.xml').decode()
x=re.sub(r'<w:commentRangeStart w:id="(\d+)"/>',r'<w:r><w:t>⟦C\1:</w:t></w:r>',x)
x=re.sub(r'<w:commentRangeEnd w:id="(\d+)"/>',r'<w:r><w:t>⟧</w:t></w:r>',x)
for i,p in enumerate(re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S)):
    out=''.join(html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>',r))) for r in re.findall(r'<w:r[ >].*?</w:r>',p,flags=re.S))
    if out.strip(): print(i,'|',out); print()
