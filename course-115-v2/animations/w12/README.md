# W12 語音合成與辨識：教學動畫（HyperFrames）

三支無聲教學動畫，上課時由老師口述搭配，並嵌入 `docs/labs/w12/` 的網頁實驗室。
用 [HyperFrames](https://github.com/heygen-com/hyperframes)（「寫 HTML，渲染成影片」）製作，版本 **0.9.45**；做法與 `../w11/` 相同，但這個資料夾自成一套（不引用 w11 的檔案）。

| 資料夾 | 主題 | 長度 | 成品 |
| --- | --- | --- | --- |
| `w12-1-tts-stt-loop/` | 文字 ⇄ 聲音：TTS 流程、STT 流程、TTS → Whisper 來回測試、三個不同的問題 | 42 s | `docs/labs/w12/media/w12-1-tts-stt-loop.mp4` |
| `w12-2-cer/` | CER 怎麼算：逐字對齊、S／D／I、正規化前後、為什麼中文用 CER | 45 s | `docs/labs/w12/media/w12-2-cer.mp4` |
| `w12-3-deepfake-card/` | 聽起來像，不等於是本人：可疑來電 → 回撥確認、深偽證據卡、信心程度 | 45 s | `docs/labs/w12/media/w12-3-deepfake-card.mp4` |

規格：1280×720、30 fps、H.264 yuv420p、無音軌、moov 在檔頭（可邊下載邊播）。

### 第 2 支畫面上的數字（字元層級 Levenshtein 距離）

| 參考 | 辨識 | S | D | I | N | CER |
| --- | --- | --- | --- | --- | --- | --- |
| 今天學習語音 | 今天學習語言 | 1 | 0 | 0 | 6 | 1/6 ≈ 16.7% |
| 學習語音 | 學習語言／學語音／學習的語音 | 各 1 處 | | | 4 | 1/4 = 25% |
| `STFT 的視窗是 2048。`（未正規化） | `stft的視窗是2048` | 4 | 3 | 0 | 15 | 7/15 ≈ 46.7% |
| 正規化後 `stft的視窗是2048` | `stft的視窗是2048` | 0 | 0 | 0 | 12 | 0% |

正規化規則：去空白、去標點、英文轉小寫。WER 例子：斷成「今天／學習／語音」是 1/3 ≈ 33.3%，斷成「今天學習／語音」是 1/2 = 50%。

## 需求

- Node.js ≥ 22、FFmpeg
- 渲染用的 Chrome：`npx hyperframes browser ensure` 會自動下載；若電腦已經有 Chrome／Chromium，可用環境變數指定，例如
  `export HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`
- 只有「改了畫面上的中文字」才需要：Python 3 + `pip install fonttools brotli`，以及系統字型 Noto Sans CJK（Ubuntu：`sudo apt install fonts-noto-cjk`）

```bash
cd course-115-v2/animations/w12
npm install
npx hyperframes doctor        # 檢查 FFmpeg / Chrome
```

## 預覽

```bash
npm run preview:1             # = npx hyperframes preview w12-1-tts-stt-loop（瀏覽器開 Studio）
npm run preview:2
npm run preview:3
# 只想看幾張靜態畫面：
npx hyperframes snapshot w12-2-cer --at 3,10,20,30 -o /tmp/snap
```

## 重新渲染

```bash
npm run lint                  # 三支都要 0 error（「nested_structure」是結構建議，可忽略）
npm run render                # 三支依序輸出到 docs/labs/w12/media/
# 或單支：
npx hyperframes render w12-2-cer -o ../../../docs/labs/w12/media/w12-2-cer.mp4 --fps 30 --crf 20
```

海報圖（`<同名>.jpg`）用 ffmpeg 從成品擷取一格：

```bash
M=../../../docs/labs/w12/media
ffmpeg -ss 33 -i $M/w12-1-tts-stt-loop.mp4  -frames:v 1 -q:v 3 -y $M/w12-1-tts-stt-loop.jpg
ffmpeg -ss 13 -i $M/w12-2-cer.mp4           -frames:v 1 -q:v 3 -y $M/w12-2-cer.jpg
ffmpeg -ss 30 -i $M/w12-3-deepfake-card.mp4 -frames:v 1 -q:v 3 -y $M/w12-3-deepfake-card.jpg
```

## 修改內容

- 每支動畫就是該資料夾的 `index.html`：上半是 HTML／CSS（文字都直接寫在裡面），下半的 `<script>` 用一條暫停的 GSAP timeline 排時間（`tl.fromTo(..., 秒數)`）。
- 每個段落是一個 `class="clip"` 的 `div`，`data-start`／`data-duration` 決定它出現的時間；整支長度是 `#root` 的 `data-duration`。
- 不可以用 `Math.random()`、`Date.now()`、計時器：渲染時是一格一格跳著 seek，畫面必須只由時間決定。數字跳動用 `assets/w12-common.js` 的 `numText` 外掛；需要「看起來隨機」就用 `W12.seeded(種子)`。
- **改了中文字之後要重跑 `npm run fonts`**：`tools/build-fonts.py` 會掃三支的 HTML 與 `assets/*.js`，把用到的字從 Noto Sans CJK TC 裁成小字型檔（`assets/fonts/NotoSansTC-500/900-subset.woff2`，每支各一份）。沒重跑的話新字會缺字。注意 Noto Sans CJK 沒有 `✗` 這個字，畫面上不要用。
- 配色與字型跟課程網頁實驗室一致：底色 `#121212`、卡片 `#1b1b1a`、線 `#33322f`、文字 `#f2f0ea`／`#9c988f`、強調橘 `#ff7a1a`、正確綠 `#5fc48a`、錯誤紅 `#ff6b5e`；Noto Sans TC（標題 900、內文 500）＋ JetBrains Mono。
- GSAP 與字型都放在各專案的 `assets/`，渲染時不需要連外網。
