const fs=require('fs');
const d=require('docx');
const {Document,Packer,Paragraph,TextRun,ImageRun,Header,Footer,AlignmentType,TabStopType,PageNumber,LevelFormat,PageBreak,HeadingLevel}=d;
const B=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const FONT=process.argv[4]||'Times New Roman';
const cm=x=>Math.round(x*567);
function runs(text,base={}){
  // inline: ***x***, **x**, *x*, `x`
  const out=[];const re=/(\*\*\*[^*]+\*\*\*|\*\*[^*]+\*\*|\*[^*\s][^*]*\*|`[^`]+`)/g;
  let last=0,m;
  while((m=re.exec(text))){
    if(m.index>last) out.push(new TextRun({text:text.slice(last,m.index),...base}));
    const t=m[0];
    if(t.startsWith('***')) out.push(new TextRun({text:t.slice(3,-3),bold:true,italics:true,...base}));
    else if(t.startsWith('**')) out.push(new TextRun({text:t.slice(2,-2),bold:true,...base}));
    else if(t.startsWith('`')) out.push(new TextRun({text:t.slice(1,-1),font:'Courier New',...base}));
    else out.push(new TextRun({text:t.slice(1,-1),italics:true,...base}));
    last=m.index+t.length;
  }
  if(last<text.length) out.push(new TextRun({text:text.slice(last),...base}));
  return out;
}
let olInstance=0;
function render(blocks,opts={}){
  const ps=[];let prev=null;
  for(const b of blocks){
    if(b.t!=='ol'&&prev==='ol') olInstance++;
    if(b.t==='h'){
      const txt=b.text.replace(/\s*\((~|max)[^)]*\)\s*$/,'').replace(/\s*\(½ page\)/,'');
      ps.push(new Paragraph({heading:b.level<=3?HeadingLevel.HEADING_2:HeadingLevel.HEADING_3,children:runs(txt),keepNext:true}));
    } else if(b.t==='p'){
      const isCaption=/^\*Figure \d/.test(b.text);
      ps.push(new Paragraph({children:runs(b.text),alignment:AlignmentType.JUSTIFIED,style:isCaption?'Caption':undefined}));
    } else if(b.t==='ul'){
      ps.push(new Paragraph({children:runs(b.text),numbering:{reference:'bul',level:0},alignment:AlignmentType.JUSTIFIED}));
    } else if(b.t==='ol'){
      ps.push(new Paragraph({children:runs(b.text),numbering:{reference:'num',level:0,instance:olInstance},alignment:AlignmentType.JUSTIFIED}));
    } else if(b.t==='img'){
      // full text width (17 cm = 643 px at 96 dpi); height from the SVG viewBox
      const svg=fs.readFileSync(b.path);const vb=/viewBox="0 0 ([\d.]+) ([\d.]+)"/.exec(svg.toString());
      const w=643,h=Math.round(w*vb[2]/vb[1]);
      ps.push(new Paragraph({alignment:AlignmentType.CENTER,keepNext:true,spacing:{before:120,after:60},children:[new ImageRun({type:'svg',data:svg,
        transformation:{width:w,height:h},fallback:{type:'png',data:fs.readFileSync(b.path.replace(/\.svg$/,'.png'))},altText:{title:b.alt,description:b.alt,name:b.alt}})]}));
    } else if(b.t==='code'){
      b.lines.forEach((l,i)=>ps.push(new Paragraph({style:'Figure',keepLines:true,keepNext:i<b.lines.length-1,children:[new TextRun({text:l.length?l:' '})]})));
    }
    prev=b.t;
  }
  return ps;
}
function refParas(blocks){
  const txt=blocks.map(b=>b.text).join(' ');
  return txt.split(/\s(?=\[\d+\] )/).map(r=>new Paragraph({style:'Ref',children:runs(r)}));
}
const pb=()=>new Paragraph({children:[new PageBreak()]});
const H=(t,lvl=HeadingLevel.HEADING_1)=>new Paragraph({heading:lvl,children:[new TextRun(t)],keepNext:true});
const kv=(k,v)=>new Paragraph({spacing:{after:40},children:[new TextRun({text:k+': ',bold:true}),...runs(v)]});
const children=[
  new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:120},children:[new TextRun({text:'ERC Consolidator Grant 2027',bold:true,size:28})]}),
  new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:240},children:[new TextRun({text:'Research proposal [Part B1]',bold:true,size:24})]}),
  new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:120},children:[new TextRun({text:'A New Web: Bridging NFPs for Heterogeneous Societal Requirements',bold:true,size:28})]}),
  new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:360},children:[new TextRun({text:'ISLANDS',bold:true,size:28})]}),
  kv('Principal Investigator','Prof. Dr. Simon Mayer'),
  kv('Host institution','University of St. Gallen (USG)'),
  kv('Proposal duration','60 months'),
  H('Abstract',HeadingLevel.HEADING_2),
  ...render(B.abstract),
  H('Cross-panel / interdisciplinary explanation',HeadingLevel.HEADING_2),
  ...render(B.crosspanel),
  pb(),
  H('Section a: Part I of the Scientific Proposal'),
  ...render(B.partI),
  pb(),
  H('References (not counted towards the page limit)',HeadingLevel.HEADING_2),
  ...refParas(B.refs),
  pb(),
  H('Section b: Curriculum Vitae and Track Record'),
  ...render(B.cv),
];
const header=new Header({children:[new Paragraph({style:'Hdr',tabStops:[{type:TabStopType.CENTER,position:cm(8.5)},{type:TabStopType.RIGHT,position:cm(17)}],
  children:[new TextRun('Mayer'),new TextRun('\tPart B1'),new TextRun('\tISLANDS')]})]});
const footer=new Footer({children:[new Paragraph({style:'Hdr',alignment:AlignmentType.CENTER,children:[new TextRun({children:[PageNumber.CURRENT]})]})]});
const doc=new Document({
  styles:{
    default:{document:{run:{font:FONT,size:22},paragraph:{spacing:{line:240,after:80}}}},
    paragraphStyles:[
      {id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:26,bold:true},paragraph:{spacing:{before:120,after:120},outlineLevel:0}},
      {id:'Heading2',name:'Heading 2',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:24,bold:true},paragraph:{spacing:{before:160,after:60},outlineLevel:1}},
      {id:'Heading3',name:'Heading 3',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:22,bold:true},paragraph:{spacing:{before:120,after:40},outlineLevel:2}},
      {id:'Figure',name:'Figure Placeholder',basedOn:'Normal',run:{font:'Courier New',size:18},paragraph:{spacing:{line:240,after:0}}},
      {id:'Caption',name:'Caption',basedOn:'Normal',run:{font:FONT,size:22,italics:false},paragraph:{spacing:{before:80,after:120}}},
      {id:'Ref',name:'Reference',basedOn:'Normal',run:{font:FONT,size:22},paragraph:{spacing:{after:40},indent:{left:cm(0.8),hanging:cm(0.8)}}},
      {id:'Hdr',name:'Header Text',basedOn:'Normal',run:{font:FONT,size:22},paragraph:{spacing:{after:0}}},
    ]},
  numbering:{config:[
    {reference:'bul',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:cm(0.63),hanging:cm(0.4)}}}}]},
    {reference:'num',levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:cm(0.63),hanging:cm(0.5)}}}}]},
  ]},
  sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:cm(1.5),bottom:cm(1.5),left:cm(2),right:cm(2),header:cm(0.6),footer:cm(0.6)}}},
    headers:{default:header},footers:{default:footer},children}]
});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(process.argv[3],b);console.log('wrote',process.argv[3])});
