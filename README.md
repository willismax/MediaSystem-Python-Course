# MediaSystem-Python-Course

這個 repo 收錄多媒體系統 V2 學生教材包與延伸實作。V2 以影像、聲音與短影音為主線，從媒體資料表示、生成式 AI、素材溯源一路進入系統整合與成果驗證。

## 從這裡開始

- [多媒體系統 V2 學生教材包](course-115-v2/README.md)
- [單冊整合教科書](course-115-v2/textbook/MULTIMEDIA_SYSTEMS_V2.md)
- [現行課程主題](course-115-v2/CURRENT_COURSE_TOPICS.md)
- [指定用書與其他教材整合](course-115-v2/TEXTBOOK_INTEGRATION_MAP.md)
- [快速開始](docs/QUICKSTART.md)

## 多媒體系統 V2 教材包

| 類型 | 位置 | 內容 |
|---|---|---|
| 整合教科書 | [多媒體系統 V2](course-115-v2/textbook/MULTIMEDIA_SYSTEMS_V2.md) | 影像、聲音、短影音與系統驗證的單冊教材 |
| 每週講義 | [`course-115-v2/weeks/`](course-115-v2/weeks/) | W01～W18 的概念、實作、作業與檢核題 |
| 程式實驗 | [`course-115-v2/labs/`](course-115-v2/labs/) | 影像、擴散、聲音與短影音處理程式 |
| Colab | [`course-115-v2/colab/`](course-115-v2/colab/) | 可在瀏覽器執行的 Notebook |
| 作業模板 | [`course-115-v2/templates/`](course-115-v2/templates/) | AI 使用、素材來源、同意紀錄與成果規準 |
| 學習指南 | [`course-115-v2/notebooklm/`](course-115-v2/notebooklm/) | 全學期學習指南 |

## 延伸實作

| 主題 | 位置 | 學習內容 |
|---|---|---|
| Python 與資料處理 | [`01.Intro-Python/`](01.Intro-Python/) | Python、NumPy、Pandas 與資料視覺化 |
| Gradio | [`02.Gradio/`](02.Gradio/) | 建立互動式 AI 介面 |
| Requests 與 API | [`03.Request/`](03.Request/) | HTTP、網頁資料與開放資料 API |
| Selenium／Playwright | [`04.Selenium/`](04.Selenium/)、[`04.Playwright/`](04.Playwright/) | 動態網頁與瀏覽器自動化 |
| Flask | [`05.Flask/`](05.Flask/) | Web 應用與 RESTful API |
| LINE Bot | [`06.Line-bot-fly-flask/`](06.Line-bot-fly-flask/) | 訊息服務與雲端部署 |
| pytest | [`07.Pytest-DEMO/`](07.Pytest-DEMO/) | 單元測試與覆蓋率 |
| OpenCV／MediaPipe | [`08.OpenCV-Mediapipe-DEMO/`](08.OpenCV-Mediapipe-DEMO/) | 電腦視覺、手勢與姿態辨識 |
| 實用工具 | [`09.Apps/`](09.Apps/) | QR Code 與其他小型應用 |
| SQLite | [`10.sql/`](10.sql/) | 資料庫 CRUD |
| AI 與 LLM | [`11.AI/`](11.AI/) | Gemini、OpenAI 與 CLI 實作 |

## 快速開始

```bash
git clone https://github.com/willismax/MediaSystem-Python-Course.git
cd MediaSystem-Python-Course
uv venv
uv pip install -r course-115-v2/labs/requirements.txt
```

也可以依各章節的 `README.md` 或 Notebook 安裝需要的套件。不要把 API 金鑰、密碼、Cookie 或個人資料提交到 repo。

## 學習與繳交

1. 先閱讀整合教科書與對應週講義，再執行程式或 Notebook。
2. 修改一個變因，保留輸入、參數、輸出與比較結果。
3. 記錄失敗案例、限制、素材來源與 AI 協作內容。
4. 公開作品前，確認著作權、肖像、聲音、個資與生成內容揭露。
5. 遇到問題時，附上可重現步驟、錯誤訊息與執行環境。

問題或教材修正可透過 [Issue](https://github.com/willismax/MediaSystem-Python-Course/issues) 提出。
