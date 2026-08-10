# 多媒體系統 115 學年度課程中心

這個資料夾提供日間部與進修部共用的課程主幹。兩班使用同一套核心教材，再依學生背景調整活動、作業支架與專題自由度。

## 課程入口

- 日間部：[Thu 多媒體系統115（日）資工一](https://hackmd.io/@wiimax/SJemnYy8fg)
- 進修部：[Sat 多媒體系統115（夜）資工一](https://hackmd.io/@wiimax/ryNWHeqSzg)
- 程式與範例：[MediaSystem-Python-Course](https://github.com/willismax/MediaSystem-Python-Course)
- Azure 延伸教材：[azure-multimedia](https://github.com/willismax/books/tree/main/azure-multimedia)

## 課程定位

> 用 AI 協作開發多媒體系統，並能說明媒體資料如何表示、處理、傳輸與驗證。

學生完成課程後，應能：

1. 說明影像、聲音與影片的基本表示方式，以及格式、壓縮與品質之間的關係。
2. 使用 Python 與現成函式庫處理至少兩種媒體資料。
3. 將媒體處理功能包裝成可操作的應用程式。
4. 使用生成式 AI 協助規劃、實作與除錯，並留下驗證過程。
5. 妥善處理 API 金鑰、個人資料、素材授權與 AI 生成內容。
6. 展示作品，說明關鍵技術選擇、限制與改善方向。

## 教材架構

- `common-syllabus.md`：18 週共同課程地圖、日夜間分流與評量方式。
- `week-01-hackmd-markdown.md`：第一週可直接貼入 HackMD 的學生版教材。
- `HACKMD_WORKFLOW.md`：HackMD 與 GitHub 的分工、同步流程及 API 採用條件。
- `templates/weekly-note.md`：後續週次的共同教材模板。
- `templates/ai-usage.md`：學生專題的 AI 使用紀錄模板。

## 日夜間分流原則

共用內容約占 70%，班別調整約占 30%。不是準備兩套投影片，而是在同一份教材中標記三種區塊：

- `共同必學`：兩班都完成。
- `日間引導`：增加概念比較、逐步操作與固定題型。
- `進修挑戰`：增加選題彈性、整合需求與專題工作時間。

日間部不降低專業內容，而是縮小每次實作範圍並增加檢核點。進修部仍需完成共同基礎，但可把更多課堂時間用於自選專題。

## 內容取捨

### 核心內容

- Python／Colab 與 Git 基礎
- Markdown 與 HackMD
- Pillow、NumPy、OpenCV
- 聲音取樣、音訊處理與語音辨識
- 影片影格、容器、編碼、FFmpeg 與攝影機輸入
- MediaPipe 或其他即時多媒體應用
- Gradio／Flask
- 多模態 AI API
- 測試、金鑰管理、著作權、個資與無障礙

### 延伸內容

- Requests 與外部資料 API
- SQLite
- LINE Bot
- pytest 的完整測試流程
- Azure、GCP 或 Zeabur 部署

### 不列入共同主幹

- Selenium
- Playwright
- 大型雲端平台的完整服務導覽

這些內容仍可保留在原 repo，供專題需要時使用，但不占共同課程週次。

## 教材維護原則

1. HackMD 是授課正文與課堂互動入口。
2. GitHub 保存程式、Notebook、固定素材與 Markdown 版本。
3. 每份共用 HackMD 筆記對應 repo 中的一個 Markdown 檔案。
4. 兩班首頁只放班級公告、日期、作業期限與共同教材連結。
5. 不在 HackMD 與 GitHub 同時修改同一份 Markdown；依 `HACKMD_WORKFLOW.md` 操作。
