"""Print docx paragraphs (by index list) as markdown with bold/italic: python3 fmtdump.py x.docx 3,5,7"""
import zipfile,re,html,sys,os
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'port.py')).read()
exec(src[src.index('def fmt(p):'):src.index('a = [p for p')])
x=zipfile.ZipFile(sys.argv[1]).read('word/document.xml').decode()
ps=re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S)
for i in map(int,sys.argv[2].split(',')):
    print(f'@@{i}'); print(fmt(ps[i])); print()
