// 最終相容啟動器：HTML 只負責文字與版面，PNG 由 PptxGenJS 直接加入。
const fs = require('fs');
const path = require('path');
let source = fs.readFileSync(path.join(__dirname, 'build_weekly_slides.js'), 'utf8');
source = source.replace("LAYOUT_16X9", "LAYOUT_16x9");
source = source.replace("const HTML = path.join(OUT, '_html');", "const HTML = 'C:/tmp/media-course-slides/html';");
source = source.replace("const TMP = path.join(OUT, '_tmp');", "const TMP = 'C:/tmp/media-course-slides/tmp';");
source = source.replace(/<img class=\\?"heroImg\\?" src=\\?"\$\{img\}\\?">/g, '<div class="heroImg"></div>');
source = source.replace(/<img class=\\?"wideImg\\?" src=\\?"\$\{img\}\\?">/g, '<div class="wideImg"></div>');
source = source.replace(
  "for(const file of files){await html2pptx(file,pptx,{tmpDir:TMP});}",
  "for(let i=0;i<files.length;i++){const {slide}=await html2pptx(files[i],pptx,{tmpDir:TMP});const imagePath=path.join(ROOT,'assets','diagrams',w.img);if(i===0)slide.addImage({path:imagePath,x:7.25,y:2.15,w:5.45,h:3.12});if(i===1)slide.addImage({path:imagePath,x:3.96,y:4.02,w:5.45,h:3.12});}"
);
eval(source);

