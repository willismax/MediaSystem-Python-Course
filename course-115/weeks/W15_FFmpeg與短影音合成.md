# W15｜影片如何被合成與壓縮？

> 本週任務：用 FFmpeg 或 MoviePy 合成 720×1280 的短影音粗剪版，確認聲畫同步與可播放性。

![影格、關鍵影格、GOP、編碼與容器](https://raw.githubusercontent.com/willismax/MediaSystem-Python-Course/course-115-complete-materials/course-115/assets/diagrams/video-codec-gop.png)

## 容器不是編碼器

- **container**：把影像流、聲音流、字幕與 metadata 放在一起，例如 MP4、WebM、MKV。
- **codec**：定義如何編碼／解碼媒體，例如 H.264、H.265、VP9、AV1、AAC。

副檔名 `.mp4` 只告訴你容器，不能保證裡面一定是某個編碼。播放失敗時要查 stream 資訊，而不是只改副檔名。

## 為什麼影片不用每張都存完整圖？

常見視訊編碼會利用：

- **空間冗餘**：同一影格的鄰近區域常相似。
- **時間冗餘**：相鄰影格通常只改變一部分。
- **I-frame／keyframe**：可較獨立解碼的影格。
- **P／B-frame**：參考前後影格描述變化。
- **GOP**：一組影格的結構與關鍵影格間距。

關鍵影格更密集通常有利於尋找與錯誤恢復，但可能增加位元率。實際結果還取決於內容、編碼器與 preset。

## FFmpeg 基本檢查

```bash
ffprobe -hide_banner input.mp4
```

把影片轉為直式 720×1280，維持比例並補邊的概念命令：

```bash
ffmpeg -i input.mp4 -vf "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -c:a aac output.mp4
```

不要把不同比例的畫面直接拉伸到 9:16。`scale` 先維持比例，`pad` 再補足畫布。

## MoviePy 合成路徑

`labs/w15_make_short.py` 會讀取圖片清單、旁白與字幕，建立時間軸。學生需要修改的是素材路徑、每張停留時間與字幕，不必從零背誦整套 API。

完成後用 `ffprobe` 或播放器檢查：

- 720×1280、預期 FPS、H.264／AAC（依課堂環境）。
- 時長 15–30 秒。
- 聲音沒有提早結束或逐漸不同步。
- 字幕沒有超出安全區。
- 檔案在另一台電腦也能播放。

## 位元率與品質

位元率是每秒分配的資料量。相同位元率下，高動態、細節密集的內容通常更難壓縮。CRF 模式傾向以品質目標調整位元率；固定 bitrate 則較容易控制傳輸規模。沒有一個參數能對所有內容最佳。

### 日間引導

使用固定四張圖與一段旁白完成合成，再比較兩個 CRF 設定的大小與瑕疵。

### 進修挑戰

依自選分鏡建立可重跑的組裝腳本，並保留一條 CPU 可完成的降級路徑。

## Exit Ticket

1. MP4 與 H.264 為何不能互換使用？
2. 關鍵影格越多一定越好嗎？
3. 為何不能直接把 4:3 圖片拉伸成 9:16？

## 延伸來源

- [FFmpeg 官方文件](https://ffmpeg.org/documentation.html)


