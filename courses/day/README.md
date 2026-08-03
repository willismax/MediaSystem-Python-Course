# 日間部四技一年級：媒體素養與實作

## 課程定位

從「媒體如何被數位化」開始，依序認識影像、音訊、視訊、壓縮、互動與傳播，再用 Python 小實作驗證概念。程式是觀察與創作媒體的工具，而不是本路徑唯一主題。

- [課程講義草稿（HackMD）](https://hackmd.io/@wiimax/B13kn0DbMe)
- [預計使用的參考書（HyRead）](https://ebook.hyread.com.tw/bookDetail.jsp?id=311734)
- [repository 快速開始](../../docs/QUICKSTART.md)

> 外部講義與書目可能更新；正式開課時請在本頁記錄採用版本、章節及最後檢查日期。書籍內容只列閱讀範圍，不將受著作權保護的內容複製進 repository。

## 建議單元順序

以下是可依學校行事曆伸縮的單元，而非綁死日期的週次表。

| 單元 | 核心概念 | Repository 實作 | 建議產出 |
|---|---|---|---|
| 1. 多媒體系統導論 | 媒體類型、取樣、量化、檔案與串流 | 課程講義＋格式觀察 | 媒體規格比較表 |
| 2. Python 最小銜接 | 變數、容器、函式、Notebook | [`01.Intro-Python`](../../01.Intro-Python/README.md) 精選 | 能讀取並描述一份媒體資料 |
| 3. 數位影像 | 像素、色彩空間、解析度、壓縮與 metadata | [`09.Apps`](../../09.Apps/README.md)、OpenCV 入門 | 影像轉換小作品 |
| 4. 數位音訊 | 波形、取樣率、位元深度、聲道與編碼 | 待補 `media/audio` 共用模組 | 音訊比較與視覺化 |
| 5. 數位視訊 | 畫格、幀率、容器、codec、空間／時間壓縮 | [`08.OpenCV-Mediapipe-DEMO`](../../08.OpenCV-Mediapipe-DEMO/readme.md) | 視訊擷取或處理實驗 |
| 6. 互動媒體 | 輸入、回饋、介面與可用性 | [`02.Gradio`](../../02.Gradio/README.md) | 可操作的媒體 demo |
| 7. 網路與發布 | 容量、頻寬、延遲、媒體傳輸與基本授權 | [`03.Request`](../../03.Request/README.md) 精選 | 取得合法開放素材並標示來源 |
| 8. 整合專題 | 需求、原型、測試、著作權與展示 | 依題目選用共用模組 | 分組作品、README、展示影片 |

## 分流原則

- **核心**：媒體基本概念、影像、音訊、視訊、互動作品及來源／授權。
- **選修**：API、Flask、AI、資料庫；只有專題需要時才帶入，避免課程再次變成 Web/API 課。
- **補強**：沒有 Python 經驗的學生使用 `01.Intro-Python` 精選活動；已有經驗者改做媒體 metadata 挑戰，不需重上全部語法。

## 專題最低規格

1. 至少處理影像、音訊或視訊其中一類，並正確說明兩項媒體參數。
2. 具有可操作的輸入與可觀察的輸出。
3. 專題 README 記錄執行方式、相依套件、素材來源／授權、分工與限制。
4. 展示測試案例，例如不同解析度、格式、裝置或錯誤輸入。
5. 若使用生成式 AI 或第三方 API，揭露工具、資料傳送範圍與人工修改內容。

## 開課前待補教材

以下教材已採用 Colab 友善的 `.ipynb` 格式；每份依序提供目標、環境設定、分格實作、檢查與延伸挑戰。學生先完成基礎必做，再視能力進行標準實作或進階挑戰。

- [`media/image`](../../media/image/README.md)：色彩、解析度、格式、壓縮與 metadata 的小型實驗。
- [`media/audio`](../../media/audio/README.md)：取樣、量化、波形與常見格式比較。
- [`media/video`](../../media/video/README.md)：frame、fps、container／codec 與基本剪輯／轉碼。
- [`media/ethics`](../../media/ethics/README.md)：著作權、Creative Commons、個資、肖像與生成式媒體標示。

日間部主線仍以影像處理與視覺安全為核心：`media/image` 與 `media/ethics` 可直接對應主要週次；音訊與視訊作為導論或專題延伸活動，避免分散核心進度。
