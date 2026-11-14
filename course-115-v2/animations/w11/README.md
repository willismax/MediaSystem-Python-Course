# W11 聲音剪輯與訊號處理：教學動畫（HyperFrames）

三支無聲教學動畫，上課時由老師口述搭配，並嵌入 `docs/labs/w11/` 的網頁實驗室。
用 [HyperFrames](https://github.com/heygen-com/hyperframes)（「寫 HTML，渲染成影片」）製作，版本 **0.9.45**。

| 資料夾 | 主題 | 長度 | 成品 |
| --- | --- | --- | --- |
| `w11-1-edit-is-math/` | 剪輯，就是在改樣本（裁切／增益／淡入／混音與削波） | 46 s | `docs/labs/w11/media/w11-1-edit-is-math.mp4` |
| `w11-2-podcast-editor/` | Podcast 自動剪輯器（偵測非靜音段 → 壓停頓 → 音量 → 淡入淡出＋片頭尾 → MP3） | 42 s | `docs/labs/w11/media/w11-2-podcast-editor.mp4` |
| `w11-3-stretch-vs-pitch/` | 變速 vs 變調（改取樣率／time_stretch／pitch_shift／STFT） | 44 s | `docs/labs/w11/media/w11-3-stretch-vs-pitch.mp4` |

規格：1280×720、30 fps、H.264 yuv420p、無音軌、moov 在檔頭（可邊下載邊播）。
第 2 支裡的秒數、dBFS 都是**示範數據**（畫面上有標示）。

## 需求

- Node.js ≥ 22、FFmpeg
- 渲染用的 Chrome：`npx hyperframes browser ensure` 會自動下載；若電腦已經有 Chrome／Chromium，可用環境變數指定，例如
  `export HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`
- 只有「改了畫面上的中文字」才需要：Python 3 + `pip install fonttools brotli`，以及系統字型 Noto Sans CJK（Ubuntu：`sudo apt install fonts-noto-cjk`）

```bash
cd course-115-v2/animations/w11
npm install
npx hyperframes doctor        # 檢查 FFmpeg / Chrome
```

## 預覽

```bash
npm run preview:1             # = npx hyperframes preview w11-1-edit-is-math（瀏覽器開 Studio）
npm run preview:2
npm run preview:3
# 只想看幾張靜態畫面：
npx hyperframes snapshot w11-2-podcast-editor --at 3,10,20,30 -o /tmp/snap
```

## 重新渲染

```bash
npm run lint                  # 三支都要 0 error（「nested_structure / track_too_dense」是結構建議，可忽略）
npm run render                # 三支依序輸出到 docs/labs/w11/media/
# 或單支：
npx hyperframes render w11-1-edit-is-math -o ../../../docs/labs/w11/media/w11-1-edit-is-math.mp4 --fps 30 --crf 20
```

每支約 1 分鐘（軟體繪圖）。渲染是確定性的，同樣的原始碼會產生位元完全相同的 MP4。

海報圖（`<同名>.jpg`）用 ffmpeg 從成品擷取一格：

```bash
M=../../../docs/labs/w11/media
ffmpeg -ss 11.8 -i $M/w11-1-edit-is-math.mp4     -frames:v 1 -q:v 3 -y $M/w11-1-edit-is-math.jpg
ffmpeg -ss 31.5 -i $M/w11-2-podcast-editor.mp4   -frames:v 1 -q:v 3 -y $M/w11-2-podcast-editor.jpg
ffmpeg -ss 10.5 -i $M/w11-3-stretch-vs-pitch.mp4 -frames:v 1 -q:v 3 -y $M/w11-3-stretch-vs-pitch.jpg
```

## 修改內容

- 每支動畫就是該資料夾的 `index.html`：上半是 HTML／CSS（文字都直接寫在裡面），下半的 `<script>` 用一條暫停的 GSAP timeline 排時間（`tl.fromTo(..., 秒數)`）。
- 每個段落是一個 `class="clip"` 的 `div`，`data-start`／`data-duration` 決定它出現的時間；整支長度是 `#root` 的 `data-duration`。
- 不可以用 `Math.random()`、`Date.now()`、計時器：渲染時是一格一格跳著 seek，畫面必須只由時間決定。數字跳動用 `assets/w11-common.js` 的 `numText` 外掛。
- **改了中文字之後要重跑 `npm run fonts`**：`tools/build-fonts.py` 會掃三支的 HTML，把用到的字從 Noto Sans CJK TC 裁成小字型檔（`assets/fonts/NotoSansTC-500/900-subset.woff2`，每支各一份）。沒重跑的話新字會缺字。
- 配色與字型跟課程網頁實驗室一致：底色 `#121212`、卡片 `#1b1b1a`、線 `#33322f`、文字 `#f2f0ea`／`#9c988f`、強調橘 `#ff7a1a`、正確綠 `#5fc48a`、錯誤／削波紅 `#ff6b5e`；Noto Sans TC（標題 900、內文 500）＋ JetBrains Mono。
- GSAP 與字型都放在各專案的 `assets/`，渲染時不需要連外網。
