const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');
const html2pptx = require('C:/Users/Willis/.agents/skills/pptx/scripts/html2pptx.js');

const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'slides');
const HTML = path.join(OUT, '_html');
const TMP = path.join(OUT, '_tmp');

const weeks = [
  {w:'W01',t:'先拆解，再創作',q:'什麼才算一個多媒體系統？',m:'系統與紀錄',c:'#24d7ff',img:'course-map.png',
   goals:['分辨多媒體檔案與多媒體系統','用輸入—處理—輸出—驗證拆解短片','用 Markdown 建立可追溯筆記'],
   principles:['媒體管線不是工具清單，而是資料如何流動','輸出要能播放，也要能說明來源與限制','AI 可以協作，但提示、採用與驗證都要留下'],
   terms:['input','process','output','validation'],lab:['選一支 15–30 秒短片','記錄圖片、聲音、字幕與時間','畫出最小系統圖','完成 HackMD 個人筆記'],
   day:'固定六格觀察表；指出一個可見效果與一個隱藏設定。',night:'拆解工作或生活流程；增加效能限制與權利風險。',
   deliver:['HackMD 筆記','媒體拆解表','100–150 字反思'],exit:['檔案與系統差在哪裡？','哪一步最可能出錯？','期末希望觀眾理解什麼？']},
  {w:'W02',t:'數位影像與像素',q:'一張圖片在電腦裡是什麼？',m:'影像模組',c:'#24d7ff',img:'pixel-rgb.png',
   goals:['讀取尺寸、模式、格式與像素','解釋 RGB／RGBA 與色彩深度','比較 PNG 與多組 JPEG 品質'],
   principles:['解析度是像素數，不等於整體畫質','未壓縮量＝寬×高×通道×位元÷8','格式選擇要同時看用途、品質、大小與相容性'],
   terms:['pixel','RGB／RGBA','bit depth','lossy／lossless'],lab:['用 Pillow 讀取 input.jpg','輸出 PNG 與 JPEG 95／70／40','記錄檔案大小與可見瑕疵','每次只改一個變因'],
   day:'固定輸入與觀察表，回答「最小是否最適合」。',night:'比較照片與文字截圖，分析內容複雜度。',deliver:['程式與四張輸出','格式比較表','150 字結論'],exit:['寬高減半剩多少像素？','透明圖為何不選 JPEG？','格式名稱能保證品質嗎？']},
  {w:'W03',t:'卷積與影像處理',q:'濾鏡為什麼能找出邊緣？',m:'影像模組',c:'#24d7ff',img:'convolution.png',
   goals:['手算一個 3×3 卷積','辨認模糊、銳化與邊緣核','解釋 padding 與資料型別'],
   principles:['卷積是鄰域加權和，不是魔法按鈕','邊界策略會改變輸出邊緣','負值與大於 255 的結果需要正確處理'],
   terms:['kernel','padding','clipping','gradient'],lab:['紙上算 3×3 灰階區塊','用 NumPy 實作卷積','與 OpenCV／Pillow 對照','製作柔和、銳利與線稿三版'],
   day:'固定 kernel，只改一個權重或門檻。',night:'建立資料夾批次處理與命名規則。',deliver:['三種濾鏡輸出','參數與時間紀錄','失敗案例'],exit:['平均核為何除以總和？','邊緣等於物體辨識嗎？','整張發黑先查什麼？']},
  {w:'W04',t:'擴散模型原理',q:'AI 如何從雜訊生成圖片？',m:'生成影像',c:'#ef4ed8',img:'diffusion-process.png',
   goals:['區分前向加噪與反向生成','解釋時間步條件與雜訊預測','用 CPU 驗證訊號／雜訊比例'],
   principles:['前向過程可直接依排程加高斯雜訊','模型常學習 εθ(xₜ,t) 的雜訊估計','生成從隨機雜訊開始，逐步取得較乾淨樣本'],
   terms:['DDPM','noise schedule','U-Net','timestep'],lab:['固定 seed＝42','比較 ᾱ＝.95／.70／.30／.05','輸出連續加噪圖','畫四格技術概念卡'],
   day:'固定圖片、seed，只改 ᾱ。',night:'比較線性／餘弦概念排程的加噪速度。',deliver:['CPU 加噪圖','四格概念卡','參數觀察'],exit:['前向加噪需要神經網路嗎？','模型每步預測什麼？','同提示為何有不同結果？']},
  {w:'W05',t:'潛在擴散與提示控制',q:'文字如何控制生成影像？',m:'生成影像',c:'#ef4ed8',img:'latent-diffusion.png',
   goals:['說明 VAE 壓縮與解碼','理解文字編碼與交叉注意力','公平比較 prompt、seed、steps、CFG'],
   principles:['在 latent 空間去噪可降低空間計算量','交叉注意力把文字條件帶入影像特徵','CFG 過高可能造成失真，steps 也非越多越好'],
   terms:['VAE','latent','cross-attention','CFG／seed'],lab:['選中性且可公開的主題','固定比例與可見參數','A／B／C 每次只加一層規格','記錄改善與新失敗'],
   day:'固定三段式提示模板，只調整一個段落。',night:'建立三張圖共用的角色與風格規格。',deliver:['三版生成結果','控制變因表','提示與採用紀錄'],exit:['VAE 為何省計算？','seed 不能保證什麼？','CFG 越高一定越好嗎？']},
  {w:'W06',t:'LoRA 與影像微調',q:'影像微調到底改了什麼？',m:'生成影像',c:'#ef4ed8',img:'lora.png',
   goals:['區分提示控制與參數更新','用 W′＝W＋BA 解釋低秩更新','設計合法、可測試的小型資料集'],
   principles:['LoRA 凍結原權重，學習小型低秩更新','資料角度、背景與標註決定模型學到什麼','訓練損失下降不等於未見情境表現變好'],
   terms:['fine-tuning','rank r','overfitting','hold-out test'],lab:['規劃 12–20 張候選圖','填寫來源、同意與標註資料卡','區分訓練候選與測試提示','判斷欠擬合／適當／過擬合'],
   day:'用固定虛構角色找出四類資料問題。',night:'自訂非人物概念，提出測試矩陣與停止條件。',deliver:['LoRA 微調企畫','資料卡','測試與停止條件'],exit:['為何稱為低秩？','小檔案等於低風險嗎？','如何判斷泛化？']},
  {w:'W07',t:'生成影像工作室',q:'如何做出一致而可信的影像系列？',m:'影像作品',c:'#ef4ed8',img:'image-story-workflow.png',
   goals:['先建立視覺規格再生成','用版本比較改善一致性','完成尺寸、色調與安全區後製'],
   principles:['單張好看不等於能形成影片','固定角色、色盤、構圖語言與字幕空間','AI 輸出是素材；瑕疵與來源仍需人工檢查'],
   terms:['visual bible','consistency','safe area','versioning'],lab:['寫故事句與四格分鏡','建立角色／色盤／構圖規格','生成、拒絕、修正並記錄','輸出 3–6 張統一比例圖片'],
   day:'固定「狀態—問題—處理—結果」四格。',night:'自訂敘事並建立可重用提示元件。',deliver:['3–6 張影像','視覺規格與分鏡','來源、提示與瑕疵表'],exit:['固定了哪些變因？','哪種一致性最難？','哪張圖最可能造成誤解？']},
  {w:'W08',t:'期中影像展與技術答辯',q:'我能不能解釋作品背後的技術？',m:'期中評量',c:'#ff6b5e',img:'image-showcase.png',
   goals:['用三分鐘說明影像作品','以控制實驗支持改善判斷','個別回答影像與生成原理'],
   principles:['評量可重現性，不只看華麗程度','展示失敗版比只秀成品更能說明決策','不確定時先區分觀察、推論與待查證'],
   terms:['evidence','baseline','failure case','oral defense'],lab:['30 秒問題','60 秒流程','45 秒核心技術','30 秒比較＋15 秒限制'],
   day:'依固定檢核表說明參數、輸出與錯誤。',night:'補充設計取捨與專題延伸路徑。',deliver:['影像故事組','3–5 頁展示','個人反思'],exit:['哪個證據支持你的選擇？','哪項限制仍存在？','哪些素材進入期末？']},
  {w:'W09',t:'期中考週',q:'本週不授新課',m:'校務週',c:'#7c8799',img:'course-map.png',
   goals:['確認班級首頁公告','檢查 W01–W08 檔案可開啟','保留時間準備其他科目'],principles:['不新增技術內容','不新增實作進度','可選整理不列新作業'],terms:['no new lesson'],lab:['確認期中評量安排','整理回饋：保留／修改／待查證','準備下週耳機','不需提前製作後半作品'],day:'依班級公告處理。',night:'依班級公告處理。',deliver:['無新作業'],exit:['下週：數位聲音與頻譜']},
  {w:'W10',t:'數位聲音與頻譜',q:'聲音如何變成可以運算的數字？',m:'聲音模組',c:'#9b6cff',img:'audio-sampling-stft.png',
   goals:['解釋取樣率、位元深度與 Nyquist','區分波形、FFT 與 STFT','比較窗長與 hop length'],
   principles:['取樣率要高於最高頻率兩倍只是理想基礎','FFT 看整段頻率，STFT 保留局部時間','窗長增加通常改善頻率解析、犧牲時間解析'],
   terms:['sample rate','Nyquist','FFT','STFT'],lab:['載入 3–5 秒 WAV','畫波形與 STFT dB 圖','只改 n_fft 或 hop length','比較拍手、母音、環境聲'],
   day:'用固定三段音檔辨認時間與頻率特徵。',night:'提出一個必須用 STFT 才容易回答的問題。',deliver:['波形與時頻圖','參數比較','觀察說明'],exit:['44.1 kHz 是可聽上限嗎？','為何要分窗？','窗長如何取捨？']},
  {w:'W11',t:'聲音剪輯與訊號處理',q:'剪輯聲音時，實際改變了什麼？',m:'聲音模組',c:'#9b6cff',img:'audio-editing.png',
   goals:['區分裁切、淡化、正規化與壓縮','解釋變速與變調不是同一件事','完成可用於短片的 20–30 秒旁白'],
   principles:['淡入淡出是隨時間變化的增益','峰值正規化不等於動態壓縮','極端降噪、time stretch 與 pitch shift 都會產生瑕疵'],
   terms:['gain envelope','normalization','compressor','phase vocoder'],lab:['備份原音再裁切','套用淡入淡出與峰值檢查','做一次變速或變調 A／B','以耳機與喇叭複查'],
   day:'固定旁白完成三項基本處理。',night:'建立批次腳本與參數停止條件。',deliver:['原音／成品對照','參數與瑕疵紀錄','旁白檔'],exit:['正規化與壓縮差在哪裡？','加快為何會升音？','哪些問題應重錄？']},
  {w:'W12',t:'語音合成與深偽辨識',q:'聲音深偽如何生成，又如何辨識風險？',m:'聲音模組',c:'#9b6cff',img:'voice-synthesis-safety.png',
   goals:['區分 TTS、voice cloning、voice conversion','說明 mel、vocoder、speaker embedding','建立多證據查證流程'],
   principles:['文字／音素→聲學模型→mel→vocoder→波形','speaker embedding 是說話者特徵表示','偵測器分數只能當線索，不能單獨定論'],
   terms:['TTS','mel spectrogram','vocoder','speaker embedding'],lab:['盲聽授權真實／合成音檔','寫判斷、信心與可觀察線索','查看波形與頻譜後修正','提出仍需的外部證據'],
   day:'固定音檔比較，排序 TTS 管線。',night:'設計收到可疑語音時的技術＋情境查證流程。',deliver:['盲聽紀錄','揭露卡','安全查證流程'],exit:['embedding 是聲音檔嗎？','vocoder 輸入輸出為何？','為何不可單靠偵測分數？']},
  {w:'W13',t:'短影音腳本與數位影片',q:'短影音不是把素材排在一起而已嗎？',m:'影片模組',c:'#ff9f43',img:'short-video-storyboard.png',
   goals:['以時間預算寫 15–30 秒腳本','理解 FPS、解析度、timebase 與同步','完成 4–6 格分鏡'],
   principles:['FPS 是時間取樣密度，不等於敘事內容量','旁白、字幕與畫面要共享同一時間設計','直式畫面需保留字幕與平台介面安全區'],
   terms:['FPS','timebase','9:16','storyboard'],lab:['寫一句核心訊息','朗讀旁白並實際計時','分配 Hook／Context／Process／Result','填入素材、字幕與聲音'],
   day:'固定五段時間模板與四格分鏡。',night:'自訂節奏，但需低算力備援與素材風險。',deliver:['15–30 秒旁白','4–6 格分鏡','時間與素材清單'],exit:['影格增加等於內容增加嗎？','字幕安全區在哪裡？','素材不足時先縮小什麼？']},
  {w:'W14',t:'生成內容與素材溯源',q:'如何建立可追溯的多媒體素材庫？',m:'影片模組',c:'#ff9f43',img:'media-provenance.png',
   goals:['建立 source／image／audio／subtitle 結構','填寫素材來源、授權、同意與 AI 紀錄','讓素材包可由他人快速接手'],
   principles:['素材包是剪輯流程的輸入契約','內嵌 metadata 可能在轉檔或上傳時消失','provenance 應記錄來源、處理與用途鏈'],
   terms:['metadata','provenance','asset ID','consent scope'],lab:['整理 8–12 個素材','填 ASSET_LOG.csv','交換素材包做五分鐘驗收','替缺檔或失權素材準備備援'],
   day:'使用固定資料夾與表格欄位。',night:'增加版本規則與缺檔自動檢查。',deliver:['完整素材包','ASSET_LOG.csv','AI_USAGE.md'],exit:['metadata 與 provenance 差在哪？','為何不覆寫原始檔？','哪個素材失權就要換？']},
  {w:'W15',t:'FFmpeg 與短影音合成',q:'影片如何被合成與壓縮？',m:'影片模組',c:'#ff9f43',img:'video-codec-gop.png',
   goals:['分辨 container 與 codec','理解 I／P／B frame、GOP 與 bitrate','輸出 720×1280 MP4 粗剪版'],
   principles:['MP4 是容器，H.264 是視訊編碼方式','編碼利用影格內與影格間冗餘','關鍵影格密度、bitrate、內容動態與品質互相牽動'],
   terms:['container','codec','keyframe／GOP','CRF／bitrate'],lab:['用 ffprobe 讀取 streams','維持比例縮放並補邊','合成圖片、旁白與字幕','換兩個 CRF 比較大小與瑕疵'],
   day:'固定四張圖與旁白完成組裝。',night:'依自選分鏡建立可重跑腳本與 CPU 降級路徑。',deliver:['720×1280 rough cut','ffprobe 紀錄','兩組壓縮比較'],exit:['MP4 與 H.264 能互換嗎？','關鍵影格越多越好嗎？','為何不可直接拉伸？']},
  {w:'W16',t:'進度小報告與系統測試',q:'作品是否已經成為一個系統？',m:'專題整合',c:'#ff6b5e',img:'final-project-pipeline.png',
   goals:['播放從頭到尾可運作的 rough cut','用架構圖說明資料流','完成正常、邊界與錯誤測試'],
   principles:['先修不能播放、看不懂、聽不清楚','再修來源、同意、揭露與可重現性','最後才增加轉場、動畫與裝飾'],
   terms:['rough cut','architecture','edge case','fallback'],lab:['30 秒問題＋60 秒播放','60 秒架構＋60 秒技術比較','45 秒權利與 AI 揭露','45 秒風險與期限'],
   day:'固定表逐組檢查播放、聲畫、字幕與來源。',night:'說明刪除或延後一項功能如何降低風險。',deliver:['Rough cut','一頁架構圖','三類測試與任務表'],exit:['哪個錯誤最先修？','雲端失效時怎麼辦？','期末前只保留哪三件事？']},
  {w:'W17',t:'期末成果發表 A',q:'如何讓觀眾相信我的技術說明？',m:'期末發表',c:'#ff6b5e',img:'final-project-pipeline.png',
   goals:['完整播放與個別答辯','連結作品流程與技術原理','給出可操作的同儕回饋'],principles:['不以特效數與生成量評分','每項主張要有作品或紀錄支持','個人仍需說明自己的決策、失敗與限制'],terms:['demo','evidence','oral defense','peer review'],lab:['播放作品','說明問題與管線','展示技術比較與失敗','回答個別原理問題'],day:'依固定答辯範圍準備。',night:'補充整合取捨與實務限制。',deliver:['完整作品','答辯','兩組同儕回饋'],exit:['哪個證據最有說服力？','哪個問題仍待改善？']},
  {w:'W18',t:'成果發表 B 與封存',q:'如何從成果回推可改進的系統？',m:'期末發表',c:'#ff6b5e',img:'final-project-pipeline.png',
   goals:['完成第二梯次發表','封存素材、程式與紀錄','用具體案例完成個人反思'],principles:['雲端網址與免費額度可能失效','應保留原始素材、開放紀錄與可重現步驟','反思要區分觀察、判斷、限制與下一步'],terms:['archive','README','AI_USAGE','reflection'],lab:['完整播放與答辯','確認 final.mp4','檢查 README／ASSET_LOG／AI_USAGE','完成五題個人反思'],day:'依封存清單逐項驗收。',night:'補充未來部署或再利用條件。',deliver:['完整專題資料夾','個人反思','可開啟的最終連結'],exit:['哪個概念改變了決策？','哪次 AI 建議被拒絕？','公開前還要查什麼？']},
];

function esc(s){return String(s).replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));}
function dataUri(file){const p=path.join(ROOT,'assets','diagrams',file);return `data:image/png;base64,${fs.readFileSync(p).toString('base64')}`;}
function baseCss(color){return `
*{box-sizing:border-box} html,body{margin:0;width:720pt;height:405pt;overflow:hidden;background:#11151d;color:#f5f7fb;font-family:Arial,sans-serif}
body{position:relative} .slide{width:720pt;height:405pt;padding:30pt 34pt;position:relative;overflow:hidden}
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:18pt}.week{font:700 12pt 'Courier New',monospace;color:${color};letter-spacing:1.2pt}.module{font-size:10pt;color:#aab3c3}
h1{font-size:30pt;line-height:1.08;margin:0 0 10pt 0;letter-spacing:-.5pt} h2{font-size:21pt;line-height:1.12;margin:0 0 14pt 0} h3{font-size:13pt;margin:0 0 8pt 0;color:${color}}
p{font-size:13pt;line-height:1.35;margin:0}.muted{color:#aab3c3}.accent{color:${color}} .small{font-size:9.5pt;line-height:1.3}
.rule{height:3pt;width:70pt;background:${color};margin:13pt 0}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18pt}.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:12pt}
.card{background:#1a202b;border:1pt solid #313a49;border-radius:10pt;padding:14pt}.card.ac{border-color:${color}} .num{width:28pt;height:28pt;border-radius:50%;background:${color};color:#10141c;display:flex;align-items:center;justify-content:center;margin-bottom:8pt}.num p{font-weight:800;font-size:13pt}
ul{margin:4pt 0 0 17pt;padding:0}li{font-size:12pt;line-height:1.32;margin-bottom:6pt}.chips{display:flex;gap:7pt;flex-wrap:wrap}.chip{border:1pt solid ${color};border-radius:20pt;padding:5pt 9pt;background:#151b24}.chip p{font:700 9pt 'Courier New',monospace;color:${color}}
.hero{display:grid;grid-template-columns:42% 58%;gap:25pt;align-items:center;height:320pt}.heroImg{width:100%;height:285pt;object-fit:cover;border-radius:13pt;border:1pt solid #30394a}
.wideImg{width:100%;height:185pt;object-fit:cover;border-radius:12pt;border:1pt solid #30394a}.footer{position:absolute;bottom:16pt;left:34pt;right:34pt;display:flex;justify-content:space-between}.footer p{font:8pt 'Courier New',monospace;color:#697386}
.split{display:grid;grid-template-columns:1fr 1fr;gap:16pt;margin-top:18pt}.split .card{min-height:130pt}.tag{font:700 10pt 'Courier New',monospace;color:${color};margin-bottom:7pt}.question{font-size:19pt;line-height:1.22;color:#dfe5ef}
`}
function page(w,body){return `<!doctype html><html><head><meta charset="utf-8"><style>${baseCss(w.c)}</style></head><body><div class="slide">${body}<div class="footer"><p>多媒體系統 115</p><p>${esc(w.w)} · ${esc(w.m)}</p></div></div></body></html>`;}
function top(w){return `<div class="top"><p class="week">${esc(w.w)}</p><p class="module">${esc(w.m)}</p></div>`;}
function bullets(items){return `<ul>${items.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`;}

function slidesFor(w){
  const img=dataUri(w.img); const slides=[];
  slides.push(page(w,`<div class="hero"><div>${top(w)}<h1>${esc(w.t)}</h1><div class="rule"></div><p class="question">${esc(w.q)}</p><p class="muted" style="margin-top:16pt">從原理、實驗到可說明的作品</p></div><img class="heroImg" src="${img}"></div>`));
  slides.push(page(w,`${top(w)}<h2>本週學習地圖</h2><div class="grid3">${w.goals.map((x,i)=>`<div class="card ac"><div class="num"><p>${i+1}</p></div><p>${esc(x)}</p></div>`).join('')}</div><div style="margin-top:18pt"><img class="wideImg" src="${img}"></div>`));
  slides.push(page(w,`${top(w)}<h2>核心原理</h2><div class="grid2"><div>${w.principles.map((x,i)=>`<div class="card" style="margin-bottom:10pt"><h3>0${i+1}</h3><p>${esc(x)}</p></div>`).join('')}</div><div><h3>關鍵詞</h3><div class="chips">${w.terms.map(x=>`<div class="chip"><p>${esc(x)}</p></div>`).join('')}</div><div class="card ac" style="margin-top:18pt"><p class="muted">說明規則</p><p style="margin-top:8pt">指出輸入、改變的參數、觀察到的輸出，以及仍不能確定的部分。</p></div></div></div>`));
  slides.push(page(w,`${top(w)}<h2>課堂實驗／任務</h2><div class="grid2">${w.lab.map((x,i)=>`<div class="card"><div class="num"><p>${i+1}</p></div><p>${esc(x)}</p></div>`).join('')}</div>`));
  if(w.w!=='W09') slides.push(page(w,`${top(w)}<h2>同一核心，兩種支架</h2><div class="split"><div class="card ac"><p class="tag">日間引導</p><p>${esc(w.day)}</p></div><div class="card"><p class="tag">進修挑戰</p><p>${esc(w.night)}</p></div></div><div class="card" style="margin-top:18pt"><p class="muted">共同底線</p><p style="margin-top:7pt">CPU 路徑可完成；AI 生成需記錄；素材需有來源與同意；每位學生都能說明關鍵原理。</p></div>`));
  slides.push(page(w,`${top(w)}<h2>本週完成條件</h2><div class="grid2"><div class="card ac"><h3>繳交</h3>${bullets(w.deliver)}</div><div class="card"><h3>Exit Ticket</h3>${bullets(w.exit)}</div></div><div class="rule"></div><p class="muted">不要只交成品：留下變因、觀察、判斷與限制，才能把作品變成可學習的系統。</p>`));
  return slides;
}

async function buildDeck(w){
  const deckDir=path.join(HTML,w.w); fs.mkdirSync(deckDir,{recursive:true});
  const htmlSlides=slidesFor(w); const files=[];
  htmlSlides.forEach((html,i)=>{const f=path.join(deckDir,`slide-${String(i+1).padStart(2,'0')}.html`);fs.writeFileSync(f,html);files.push(f)});
  const pptx=new pptxgen(); pptx.layout='LAYOUT_16X9'; pptx.author='Willis Max'; pptx.subject='多媒體系統 115'; pptx.title=`${w.w}｜${w.t}`; pptx.company='課程教材'; pptx.lang='zh-TW';
  pptx.defineSlideMaster({title:'BASE',background:{color:'11151D'},objects:[],slideNumber:{x:12.45,y:7.1,w:.35,h:.18,color:'697386',fontFace:'Arial',fontSize:7}});
  for(const file of files){await html2pptx(file,pptx,{tmpDir:TMP});}
  const out=path.join(OUT,`${w.w}_${w.t.replace(/[\\/:*?"<>|]/g,'_')}.pptx`); await pptx.writeFile({fileName:out}); console.log(out);
}

(async()=>{fs.mkdirSync(OUT,{recursive:true});fs.mkdirSync(TMP,{recursive:true});for(const w of weeks)await buildDeck(w);})().catch(e=>{console.error(e);process.exit(1)});

