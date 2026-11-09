// Build Part B2 (Part II of the Scientific Proposal) in ERC 2027 layout.
// node build_b2.js work/b2-blocks.json out.docx
// A4, Times New Roman 11 pt everywhere (tables included), single spacing,
// margins 2 cm left/right and 1.5 cm top/bottom; references and annex start on new pages.
const fs=require('fs');
const d=require('docx');
const {Document,Packer,Paragraph,TextRun,Header,Footer,AlignmentType,TabStopType,PageNumber,LevelFormat,PageBreak,HeadingLevel,
       Table,TableRow,TableCell,WidthType,BorderStyle,ShadingType}=d;
const B=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const FONT='Times New Roman';
const cm=x=>Math.round(x*567);
function runs(text,base={}){
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
const W=cm(17);  // text width
const border={style:BorderStyle.SINGLE,size:4,color:'999999'};
const borders={top:border,bottom:border,left:border,right:border};
function widthsFor(rows){
  // column widths proportional to sqrt of the longest cell text, with a minimum
  const n=rows[0].length, len=Array(n).fill(1);
  rows.forEach(r=>r.forEach((c,i)=>{len[i]=Math.max(len[i],Math.sqrt(c.replace(/[*`]/g,'').length+4))}));
  const tot=len.reduce((a,b)=>a+b,0);
  const maxlen=Array(n).fill(0); rows.forEach(r=>r.forEach((c,i)=>{maxlen[i]=Math.max(maxlen[i],c.replace(/[*`]/g,'').length)}));
  const narrow=maxlen.map(m=>m<=4);  // e.g., #, L, I columns
  const rest=W-narrow.filter(x=>x).length*cm(0.75), tot2=len.reduce((a,b,i)=>a+(narrow[i]?0:b),0);
  let w=len.map((l,i)=>narrow[i]?cm(0.75):Math.max(cm(1.0),Math.round(rest*l/tot2)));
  const s=w.reduce((a,b)=>a+b,0); w[w.indexOf(Math.max(...w))]+=W-s;
  return w;
}
function table(rows){
  const w=widthsFor(rows);
  return new Table({width:{size:W,type:WidthType.DXA},columnWidths:w,rows:rows.map((r,ri)=>new TableRow({tableHeader:ri===0,cantSplit:true,
    children:r.map((c,ci)=>new TableCell({borders,width:{size:w[ci],type:WidthType.DXA},margins:{top:30,bottom:30,left:70,right:70},
      shading:ri===0?{fill:'E7E6E6',type:ShadingType.CLEAR,color:'auto'}:undefined,
      children:[new Paragraph({spacing:{after:0},children:runs(c,ri===0?{bold:true}:{})})]}))}))});
}
let olInstance=0;
function render(blocks){
  const ps=[];let prev=null;
  for(const b of blocks){
    if(b.t!=='ol'&&prev==='ol') olInstance++;
    if(b.t==='h'){
      let txt=b.text.replace(/\s*\((~|max)[^)]*\)\s*$/,'').replace(/\s*\(outside the page limit\)/,'');
      txt=txt.replace(/^Section (\d) — /,'$1. ');
      ps.push(new Paragraph({heading:b.level<=2?HeadingLevel.HEADING_2:HeadingLevel.HEADING_3,children:runs(txt),keepNext:true}));
    } else if(b.t==='p'){
      const isCaption=/^\*Table \d/.test(b.text);
      ps.push(new Paragraph({children:runs(b.text),alignment:AlignmentType.JUSTIFIED,style:isCaption?'Caption':undefined}));
    } else if(b.t==='ul'){
      ps.push(new Paragraph({children:runs(b.text),numbering:{reference:'bul',level:0},alignment:AlignmentType.JUSTIFIED}));
    } else if(b.t==='ol'){
      ps.push(new Paragraph({children:runs(b.text),numbering:{reference:'num',level:0,instance:olInstance},alignment:AlignmentType.JUSTIFIED}));
    } else if(b.t==='table'){
      ps.push(table(b.rows)); ps.push(new Paragraph({spacing:{after:0},children:[]}));
    }
    prev=b.t;
  }
  return ps;
}
const refParas=blocks=>blocks.map(b=>new Paragraph({style:'Ref',children:runs(b.text)}));
const pb=()=>new Paragraph({children:[new PageBreak()]});
const H=(t,lvl=HeadingLevel.HEADING_1)=>new Paragraph({heading:lvl,children:[new TextRun(t)],keepNext:true});
const children=[
  H('Part II of the Scientific Proposal'),
  ...render(B.partII),
  pb(),
  H('References (not counted towards the page limit)',HeadingLevel.HEADING_2),
  ...refParas(B.refs),
  pb(),
  ...render(B.annex),
];
const header=new Header({children:[new Paragraph({style:'Hdr',tabStops:[{type:TabStopType.CENTER,position:cm(8.5)},{type:TabStopType.RIGHT,position:cm(17)}],
  children:[new TextRun('Mayer'),new TextRun('\tPart B2'),new TextRun('\tISLANDS')]})]});
const footer=new Footer({children:[new Paragraph({style:'Hdr',alignment:AlignmentType.CENTER,children:[new TextRun({children:[PageNumber.CURRENT]})]})]});
const doc=new Document({
  styles:{
    default:{document:{run:{font:FONT,size:22},paragraph:{spacing:{line:240,after:80}}}},
    paragraphStyles:[
      {id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:26,bold:true},paragraph:{spacing:{before:0,after:120},outlineLevel:0}},
      {id:'Heading2',name:'Heading 2',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:24,bold:true},paragraph:{spacing:{before:160,after:60},outlineLevel:1}},
      {id:'Heading3',name:'Heading 3',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:FONT,size:22,bold:true},paragraph:{spacing:{before:120,after:40},outlineLevel:2}},
      {id:'Caption',name:'Caption',basedOn:'Normal',run:{font:FONT,size:22},paragraph:{spacing:{before:40,after:120}}},
      {id:'Ref',name:'Reference',basedOn:'Normal',run:{font:FONT,size:22},paragraph:{spacing:{after:40},indent:{left:cm(0.5),hanging:cm(0.5)}}},
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
