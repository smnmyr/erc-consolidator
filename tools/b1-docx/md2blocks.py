import re,json,sys,os
src=open(sys.argv[1]).read()
BASE=os.path.dirname(os.path.abspath(sys.argv[1]))
src=re.sub(r'<!--.*?-->','',src,flags=re.S)
def sect(start,end):
    i=src.index(start); j=src.index(end,i)
    return src[i:j]
def blocks(md):
    out=[]; lines=md.split('\n'); i=0
    para=[]
    def flush():
        nonlocal para
        if para: out.append({'t':'p','text':' '.join(x.strip() for x in para)}); para=[]
    while i<len(lines):
        l=lines[i]
        if l.startswith('```'):
            flush(); i+=1; code=[]
            while not lines[i].startswith('```'): code.append(lines[i].rstrip()); i+=1
            out.append({'t':'code','lines':code}); i+=1; continue
        m=re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$',l)
        if m:  # figure: SVG with a PNG fallback next to it
            flush(); out.append({'t':'img','alt':m.group(1),'path':os.path.join(BASE,m.group(2))}); i+=1; continue
        if l.startswith('>'):  # drafting notes
            flush(); i+=1; continue
        if l.startswith('---'): flush(); i+=1; continue
        m=re.match(r'^(#{2,4}) (.*)',l)
        if m:
            flush(); out.append({'t':'h','level':len(m.group(1)),'text':m.group(2).strip()}); i+=1; continue
        m=re.match(r'^(\s*)(- |\d+\. )(.*)',l)
        if m:
            flush(); kind='ul' if m.group(2)=='- ' else 'ol'
            item=[m.group(3)]; i+=1
            while i<len(lines) and lines[i].strip() and re.match(r'^\s+\S',lines[i]) and not re.match(r'^\s*(- |\d+\. )',lines[i]):
                item.append(lines[i].strip()); i+=1
            out.append({'t':kind,'text':' '.join(item)}); continue
        if not l.strip(): flush(); i+=1; continue
        para.append(l); i+=1
    flush(); return out
doc={}
doc['abstract']=blocks(sect('### Abstract','### Cross-panel'))[1:]
doc['crosspanel']=blocks(sect('### Cross-panel','## Section b'))[1:]
doc['partI']=blocks(sect('### b.1','### References (not counted'))
doc['refs']=blocks(sect('### References (not counted','## Section c'))[1:]
doc['cv']=blocks(sect('## Section c','## Annex'))[1:]
json.dump(doc,open(sys.argv[2],'w'),indent=1,ensure_ascii=False)
for k,v in doc.items(): print(k,len(v),sum(len(b.get('text','').split()) for b in v))
