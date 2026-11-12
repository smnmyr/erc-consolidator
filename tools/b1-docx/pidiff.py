"""Word-level diff of paragraph text between two docx files: python3 pidiff.py a.docx b.docx"""
import zipfile,re,html,sys,difflib
def paras(f):
    x=zipfile.ZipFile(f).read('word/document.xml').decode()
    return [re.sub(r'\s+',' ',html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>',p)))).strip() for p in re.findall(r'<w:p[ >].*?</w:p>',x,flags=re.S)]
a=[p for p in paras(sys.argv[1]) if p]; b=[p for p in paras(sys.argv[2]) if p]
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op=='equal': continue
    for x,y in zip(a[i1:i2]+['']*10,b[j1:j2]+['']*10):
        if not x and not y: break
        wa=x.split(); wb=y.split(); out=[]
        for o,k1,k2,l1,l2 in difflib.SequenceMatcher(None,wa,wb,autojunk=False).get_opcodes():
            if o=='equal': out.append(' '.join(wa[k1:k2]) if k2-k1<8 else ' '.join(wa[k1:k1+3])+' … '+' '.join(wa[k2-3:k2]))
            else: out.append('[-'+' '.join(wa[k1:k2])+'-]{+'+' '.join(wb[l1:l2])+'+}')
        print(op,'::',' '.join(out)); print()
