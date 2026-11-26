# W13 影片的時間結構、編碼與容器：教學動畫（HyperFrames）

三支無聲教學動畫，上課時由老師口述搭配，並嵌入 `docs/labs/w13/` 的網頁實驗室。
用 [HyperFrames](https://github.com/heygen-com/hyperframes)（「寫 HTML，渲染成影片」）製作，版本 **0.9.45**；做法與 `../w12/` 相同，但這個資料夾自成一套（不引用 w12 的檔案）。

| 資料夾 | 主題 | 長度 | 成品 |
| --- | --- | --- | --- |
| `w13-1-frames-and-bitrate/` | 影片 = 影格 × 時間：影格沿時間軸排開、影格數 ≈ T × f、1080p 未壓縮資料量、和 MP4 比較、Bitrate 是資料預算 | 42 s | `docs/labs/w13/media/w13-1-frames-and-bitrate.mp4` |
| `w13-2-ipb-gop/` | I、P、B 與 GOP：空間／時間冗餘、動態估計（移動向量＋殘差）、三種影格、GOP、跳播要從前一個 I 解起、`-c copy` 只能切在關鍵格 | 45 s | `docs/labs/w13/media/w13-2-ipb-gop.mp4` |
| `w13-3-codec-container/` | Codec、Encoder、Container 是三層：MP4 盒子裡的串流、三層各舉例、Demux → Decode → 播放、兩個常見誤會、ffprobe、相容性安全牌 | 45 s | `docs/labs/w13/media/w13-3-codec-container.mp4` |

規格：1280×720、30 fps、H.264 yuv420p、無音軌、moov 在檔頭（可邊下載邊播）。

### 第 1 支畫面上的數字

| 項目 | 算式 | 結果 |
| --- | --- | --- |
| 影格數 | 60 s × 30 fps | 1,800 格 |
| 每格像素 | 1920 × 1080 | 2,073,600 |
| 每格位元組（RGB8） | 2,073,600 × 3 | 6,220,800 B |
| 每秒位元組 | 6,220,800 × 30 | 186,624,000 B ≈ 186.6 MB/s |
| 每秒位元 | 186,624,000 × 8 | 1,492,992,000 bit/s ≈ 1,493 Mbps |
| 未壓縮一分鐘 | 186,624,000 × 60 | 11,197,440,000 B ≈ 11,197 MB ≈ 11.2 GB |
| MP4 一分鐘 | (8 + 0.128) Mbps × 60 s ÷ 8 | 60.96 MB |
| 倍數 | 11,197.44 ÷ 60.96 | ≈ 183.7 → 畫面寫「約 180 倍」 |

1 MB = 1,000,000 B。條狀圖依實際比例繪製（860 px 對 4.7 px）。第 2 支的 I／P／B 長條高度只是示意，不是實測。

## 需求

- Node.js ≥ 22、FFmpeg
- 渲染用的 Chrome：`npx hyperframes browser ensure` 會自動下載；若電腦已經有 Chrome／Chromium，可用環境變數指定，例如
  `export HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell`
- 只有「改了畫面上的中文字」才需要：Python 3 + `pip install fonttools brotli`，以及系統字型 Noto Sans CJK（Ubuntu：`sudo apt install fonts-noto-cjk`）

```bash
cd course-115-v2/animations/w13
npm install
npx hyperframes doctor        # 檢查 FFmpeg / Chrome
```

## 預覽

```bash
npm run preview:1             # = npx hyperframes preview w13-1-frames-and-bitrate（瀏覽器開 Studio）
npm run preview:2
npm run preview:3
# 只想看幾張靜態畫面：
npx hyperframes snapshot w13-2-ipb-gop --at 10,20,28,42 -o /tmp/snap
```

## 重新渲染

```bash
npm run lint                  # 三支都要 0 error（「nested_structure」是結構建議，可忽略）
npm run render                # 三支依序輸出到 docs/labs/w13/media/
# 或單支：
npx hyperframes render w13-2-ipb-gop -o ../../../docs/labs/w13/media/w13-2-ipb-gop.mp4 --fps 30 --crf 20
```

海報圖（`<同名>.jpg`）用 ffmpeg 從成品擷取一格：

```bash
M=../../../docs/labs/w13/media
ffmpeg -ss 34 -i $M/w13-1-frames-and-bitrate.mp4 -frames:v 1 -q:v 3 -y $M/w13-1-frames-and-bitrate.jpg
ffmpeg -ss 43 -i $M/w13-2-ipb-gop.mp4            -frames:v 1 -q:v 3 -y $M/w13-2-ipb-gop.jpg
ffmpeg -ss 44 -i $M/w13-3-codec-container.mp4    -frames:v 1 -q:v 3 -y $M/w13-3-codec-container.jpg
```

## 修改內容

- 每支動畫就是該資料夾的 `index.html`：上半是 HTML／CSS（文字都直接寫在裡面），下半的 `<script>` 用一條暫停的 GSAP timeline 排時間（`tl.fromTo(..., 秒數)`）。
- 每個段落是一個 `class="clip"` 的 `div`，`data-start`／`data-duration` 決定它出現的時間；整支長度是 `#root` 的 `data-duration`。
- 不可以用 `Math.random()`、`Date.now()`、計時器：渲染時是一格一格跳著 seek，畫面必須只由時間決定。數字跳動用 `assets/w13-common.js` 的 `numText` 外掛（`comma: true` 會加千分位）；需要「看起來隨機」就用 `W13.seeded(種子)`。
- **改了中文字之後要重跑 `npm run fonts`**：`tools/build-fonts.py` 會掃三支的 HTML 與 `assets/*.js`，把用到的字從 Noto Sans CJK TC 裁成小字型檔（`assets/fonts/NotoSansTC-500/900-subset.woff2`，每支各一份）。沒重跑的話新字會缺字。注意 Noto Sans CJK 沒有 `✗` 這個字，畫面上不要用；全形空白（U+3000）也不會被收進字型，請用 CSS 間距。
- 配色與字型跟課程網頁實驗室一致：底色 `#121212`、卡片 `#1b1b1a`、線 `#33322f`、文字 `#f2f0ea`／`#9c988f`、強調橘 `#ff7a1a`、正確綠 `#5fc48a`、錯誤紅 `#ff6b5e`；Noto Sans TC（標題 900、內文 500）＋ JetBrains Mono。
- GSAP 與字型都放在各專案的 `assets/`，渲染時不需要連外網。
