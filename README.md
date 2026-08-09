# MediaSystem-Python-Course

這是「多媒體系統」課程本身的共用教材庫。同一組可重用的實作素材，依學生背景組成兩條不同的教學路線：日間部從影像、音訊、視訊與互動媒體概念出發；進修部則從 Python 銜接到網路、API 與雲端應用。既有章節路徑會保留，避免舊講義與 Colab 連結失效。

> 課程名稱相同，不代表必須共用同一份週次表。請先從下方選擇班別，再依課程地圖進入教材；章節編號是「素材編號」，不是兩班共同進度。

## 🧭 選擇你的課程

| 教學路線 | 核心問題 | 起點 | 課程地圖 |
|---|---|---|---|
| 日間部四技一年級：媒體素養與實作 | 數位影像、音訊、視訊如何表示、處理並成為互動作品？ | 媒體基本概念 | [日間部課程地圖](courses/day/README.md) |
| 進修部一年級：Python、API 與雲端應用 | 程式如何透過網路取得資料、串接服務並部署專題？ | Python 程度診斷與銜接 | [進修部課程地圖](courses/evening/README.md) |

兩班共用的模組、先備能力與分流方式，請見[雙軌課程架構](courses/README.md)。教師可在 HackMD 維護每週公告，本 repository 則作為可執行程式、作業模板與穩定課程地圖的單一來源。

## 📖 目錄

- [📚 文檔中心](docs/) ⭐ **完整學習資源**
- [🧭 雙軌課程架構](courses/) - 日間部／進修部入口與共用原則
- [🚀 快速啟動指南](docs/QUICKSTART.md) - 各專案快速啟動
- [📖 學習路徑規劃](docs/LEARNING_PATH.md) - 課程學習建議
- [🗓️ HackMD 每週教學講義](docs/HACKMD_WEEKLY_GUIDE.md) - 18 週完整教案與 GitHub 教材連結
- [📝 更新日誌](docs/CHANGELOG.md) - 專案更新記錄
- [範例程式碼下載](#範例程式碼下載)
- [環境設定](#-快速開始-推薦使用-uv)
- [專案說明](#相關專案摘要說明)

## 📂 章節導覽

| 章節 | 主題 | 說明 |
|------|------|------|
| [01.Intro-Python](01.Intro-Python/README.md) | Python 入門與資料分析 | Python 基礎語法、NumPy、Pandas、資料視覺化 |
| [02.Gradio](02.Gradio/README.md) | 互動式 AI 介面 | 使用 Gradio 快速建立 AI 示範介面 |
| [03.Request](03.Request/README.md) | 網頁擷取與 API 存取 | Requests、BeautifulSoup、開放資料 API |
| [04.Playwright](04.Playwright/README.md) | 瀏覽器自動化爬蟲 | Playwright 動態網頁爬蟲、腳本錄製 |
| [04.Selenium](04.Selenium/README.md) | 動態網頁爬蟲 | Selenium WebDriver 進階爬蟲 |
| [05.Flask](05.Flask/README.md) | Flask 網站開發 | 從基本網站到 RESTful API |
| [06.Line-bot-fly-flask](06.Line-bot-fly-flask/README.md) | LINE Bot 部署 | 在 Fly.io 部署 LINE Bot |
| [07.Pytest-DEMO](07.Pytest-DEMO/README.md) | 自動化測試 | pytest 單元測試與覆蓋率報告 |
| [08.OpenCV-Mediapipe-DEMO](08.OpenCV-Mediapipe-DEMO/readme.md) | 電腦視覺 | OpenCV + MediaPipe 肢體辨識 |
| [09.Apps](09.Apps/README.md) | 實用應用程式 | QR Code 產生器、OpenAI 應用 |
| [10.sql](10.sql/README.md) | SQLite 資料庫 | Python 資料庫 CRUD 操作 |
| [11.AI](11.AI/README.md) | AI 與大型語言模型 | Gemini API 串接與 LLM 應用 |

## 範例程式碼下載
- 安裝[Git Cli](https://git-scm.com/)
- 在終端機`git clone`專案  
  ```bash
  git clone https://github.com/willismax/MediaSystem-Python-Course.git
  cd MediaSystem-Python-Course
  ```

## 🚀 快速開始 (推薦使用 uv)

### 使用 uv (推薦⭐)
[uv](https://docs.astral.sh/uv/) 是新一代的 Python 套件管理工具，速度極快且使用簡單！

#### 安裝 uv
```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用安裝腳本 (Windows)
.\scripts\setup-uv.ps1
```

#### 🎯 一鍵啟動腳本

本專案提供了方便的啟動腳本，讓您可以快速開始學習：

**Windows (PowerShell)**
```powershell
# 啟動 Flask 應用
.\scripts\run-flask.ps1

# 啟動 Jupyter Notebook
.\scripts\run-jupyter.ps1

# 在特定目錄啟動 Jupyter
.\scripts\run-jupyter.ps1 -Path "11.AI"
```

**Linux/macOS**
```bash
# 給予執行權限（首次使用）
chmod +x scripts/*.sh

# 啟動 Flask 應用
./scripts/run-flask.sh

# 啟動 Jupyter Notebook
./scripts/run-jupyter.sh

# 在特定目錄啟動 Jupyter
./scripts/run-jupyter.sh "11.AI"
```

詳細的腳本使用說明請參考 [scripts/README.md](scripts/README.md)

#### 使用 uv 執行專案
```bash
# 方法 1: 使用 uv run 直接執行 (自動管理環境)
cd 05.Flask/flask01
uv run app.py

# 方法 2: 執行 Jupyter Notebook
cd 03.Request
uv run --with jupyter jupyter notebook 網頁擷取_Request.ipynb

# 方法 3: 安裝特定套件後執行
uv run --with flask --with requests python app.py
```

#### 為子專案建立虛擬環境 (可選)
```bash
# 進入特定專案目錄
cd 05.Flask

# 使用 uv 建立虛擬環境並安裝套件
uv venv
uv pip install -r requirements.txt

# 啟動虛擬環境
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# 執行應用
python app.py
```

#### uv 常用指令
```bash
# 安裝套件
uv pip install flask pandas requests

# 從 requirements.txt 安裝
uv pip install -r requirements.txt

# 列出已安裝套件
uv pip list

# 執行 Python 腳本 (自動處理依賴)
uv run script.py

# 執行 Python 互動式介面
uv run python
```

---

## 傳統方法 (3 選 1)

### 方法 1: 使用 Python 內建的虛擬機 `venv`
- [官方說明](https://docs.python.org/zh-tw/3.10/tutorial/venv.html)
- 建虛擬機 venv
  ```bash
  python -m venv venv
  ```
- 啟動 VM
  ```bash
  # Windows
  .\venv\Scripts\activate
  
  # macOS/Linux
  source venv/bin/activate
  ```
- 安裝相關套件
  ```bash
  pip install -r requirements.txt
  ```
- 離開 VM
  ```bash
  deactivate
  ```

### 方法 2: 使用 pipenv 虛擬環境+套件管理
- pipenv (需先 `pip install pipenv`，並在本機安裝對應的 Python 版本)
  ```bash
  pipenv --python 3.10
  ```
- 建立好資料夾要 CD 切換路徑
  ```bash
  cd MediaSystem-Python-Course
  ```
- 在 pipenv 安裝相依套件
  
  以 requirements.txt 裝:
  ```bash
  pipenv install -r requirements.txt
  ```
  以 Pipfile 裝:
  ```bash
  pipenv sync
  ```
- 進入環境執行服務
  ```bash
  pipenv shell
  python app.py
  
  # 或未進入虛擬環境由本機執行
  pipenv run python app.py
  ```
- 移除虛擬環境
  ```bash
  pipenv --rm
  ```

### 方法 3: 直接使用系統 Python (不推薦)
```bash
pip install -r requirements.txt
python app.py
```

#
## 相關專案摘要說明

### 01.Intro-Python
- 課程使用到的ipynb檔，在Colab執行

### 02.Gradio
- 可在Colab建立GUI，輔助課程使用

### 03.Request
- 網頁擷取與 API 資料存取教學
- 包含使用 Requests 函式庫進行網頁擷取
- 介紹如何存取開放資料 (Open Data) API
- 範例檔案包括:
  - `網頁擷取_Request.ipynb`: 基礎網頁擷取
  - `擷取API資料.ipynb`: API 資料存取
  - `RequestsOpenData_HW.ipynb`: 開放資料實作練習

### 04.Selenium
- 需自行下載 webkit 等 Driver 測試，為進階爬蟲教學
- 適用於需要執行 JavaScript 的動態網頁爬蟲

### 04.Playwright
- 可錄製腳本抓 HTML，再自己客製化
- 新一代的網頁自動化工具，支援多種瀏覽器

### 05.Flask
- 從基本網站服務到建立基本API

### 06.LINE-Bot-on-Fly
- 在 Fly.io 建立 LINE Bot ，服務以 Flask 框架實現，並包含 API 測試
- 在`config.py`填入相關tocken
- 服務包含:
  - LINE 訊息傳送 (需LINE Channel acess token、Channel secret、LINE user id)
  - LINE 文字與圖片訊息增加至 HackMD (需HackMD API、Imgure API)
  - LINE 文字訊息翻譯
  - LINE 文字訊息由 OpenAI 回應，並且記錄於 HhackMD (需OpenAI API) 

- 建立 Tasks API 測試:
  - [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/1745585-89afac06-ad51-4fc8-83c0-c26ccf8db7b9?action=collection%2Ffork&collection-url=entityId%3D1745585-89afac06-ad51-4fc8-83c0-c26ccf8db7b9%26entityType%3Dcollection%26workspaceId%3D9132735b-dff0-46b8-8852-839d022a2ac3)
  - Get, Post, Put, Delete測試

### 07.Pytest-DEMO
- 簡易的 pytest demo，寫好在終端機下`pytest`指令測試
- 另外也裝`pytest-cov`套件的話，`pytest --cov=./`可以測試覆蓋率Coverage
  ```
  pytest --cov=./ 
  或
  pytest --cov-report=html
  ```
### 08.OpenCV-Mediapipe-DEMO
- Mediapipe 簡易操作
- 電腦視覺應用示範
- 建議使用 pipenv 虛擬環境，Python 3.8 以上版本

### 09.Apps
- 實用應用程式範例
- 包含 QRCode 產生器等工具
- `QRCode.ipynb`: 在 Colab 上製作 QR Code
  - 可製作純黑白 QR Code
  - 可加入背景圖片製作彩色或黑白 QR Code
  - 支援 GIF 動態背景

### 10.sql
- SQLite 資料庫基礎教學
- `SQLite資料庫CRUD.ipynb`: 涵蓋資料庫的建立、查詢、更新、刪除等基本操作
- 適合初學者學習資料庫概念與 SQL 語法

### 11.AI
- AI 與大型語言模型 (LLM) 相關教學
- Gemini API 串接實作
- 範例檔案:
  - `動手串接_LLM_API_入門教學(Gemini_).ipynb`: Gemini API 入門教學
  - `在_Colab_終端機使用_Gemini_CLI.ipynb`: 在 Colab 環境使用 Gemini CLI
  - `gemini_cli_colab_tutorial.ipynb`: Gemini CLI 完整教學
- OpenAI API 應用範例

## 注意事項
- 請配合課程使用，歡迎 issue 討論或發 PR (Pull Request)
- [如何發PR | W3HexSchool](https://w3c.hexschool.com/git/cc7d70b7)

## 🌟 為什麼推薦使用 uv？

1. **極快的速度**: 比 pip 快 10-100 倍
2. **簡單易用**: 單一指令即可安裝和執行
3. **智能依賴管理**: 自動解析和安裝依賴
4. **跨平台一致性**: Windows、macOS、Linux 使用體驗一致
5. **無需預先安裝 Python**: uv 可以自動下載所需的 Python 版本
6. **零配置**: 不需要額外的配置文件即可開始使用

### 速度對比範例

```bash
# 傳統方式 (約 30-60 秒)
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# uv 方式 (約 3-5 秒) ⚡
uv venv
uv pip install -r requirements.txt
```

## 📚 更多資源

- [uv 官方文檔](https://docs.astral.sh/uv/)
- [Python 官方教學](https://docs.python.org/zh-tw/3/)
- [Flask 官方文檔](https://flask.palletsprojects.com/)
- [LINE Messaging API 文檔](https://developers.line.biz/en/docs/messaging-api/)

## 💬 問題反饋

如有任何問題或建議，歡迎：
- 開啟 [Issue](https://github.com/willismax/MediaSystem-Python-Course/issues)
- 提交 [Pull Request](https://github.com/willismax/MediaSystem-Python-Course/pulls)
- 參考 [如何發 PR 教學](https://w3c.hexschool.com/git/cc7d70b7)
