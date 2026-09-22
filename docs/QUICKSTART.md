# 快速啟動指南

本文件提供各個專案的快速啟動方式。

## 🚀 使用 uv 快速開始 (推薦)

### 安裝 uv

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Jupyter Notebook 專案 (01-04, 09-11)

```bash
# 執行 Jupyter Notebook
cd 03.Request
uv run --with jupyter jupyter notebook

# 或安裝 JupyterLab
uv run --with jupyterlab jupyter lab
```

### Flask 專案 (05.Flask)

```bash
cd 05.Flask/flask01
uv run app.py

# 或建立虛擬環境
cd 05.Flask
uv venv
uv pip install -r requirements.txt
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
python app.py
```

### FastAPI 專案 (14.FastAPI)

```bash
cd 14.FastAPI
uv venv
uv pip install -r requirements.txt
fastapi dev media_api.py
```

### LINE Bot 專案 (06.Line-bot-fly-flask)

```bash
cd 06.Line-bot-fly-flask
uv venv
uv pip install -r requirements.txt

# 啟動虛擬環境
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 設定 config.py 後執行
python app.py
```

### Pytest 專案 (07.Pytest-DEMO)

```bash
cd 07.Pytest-DEMO
uv venv
uv pip install -r requirements.txt

# 啟動虛擬環境
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 執行測試
pytest

# 執行測試並顯示覆蓋率
pytest --cov=./
```

### OpenCV-Mediapipe 專案 (08.OpenCV-Mediapipe-DEMO)

```bash
cd 08.OpenCV-Mediapipe-DEMO
uv venv --python 3.10
uv pip install opencv-python mediapipe

# 啟動虛擬環境
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

python demo.py
```

## 💡 uv 常用指令

```bash
# 建立虛擬環境
uv venv

# 安裝套件
uv pip install package-name

# 從 requirements.txt 安裝
uv pip install -r requirements.txt

# 直接執行 (自動處理依賴)
uv run script.py

# 臨時安裝套件並執行
uv run --with package-name script.py

# 列出已安裝套件
uv pip list

# 移除套件
uv pip uninstall package-name
```

## 📚 各專案說明

| 專案 | 說明 | 快速啟動 |
|------|------|----------|
| 01.Intro-Python | Python 基礎教學 | `uv run --with jupyter jupyter notebook` |
| 02.Gradio | GUI 介面教學 | `uv run --with gradio --with jupyter jupyter notebook` |
| 03.Request | 網頁擷取與 API | `uv run --with jupyter jupyter notebook` |
| 04.Selenium | 進階爬蟲 | 需下載 WebDriver |
| 04.Playwright | 新一代爬蟲 | `uv pip install playwright && playwright install` |
| 05.Flask | Web 框架 | `uv run app.py` |
| 14.FastAPI | 型別化 Web API | `fastapi dev media_api.py` |
| 06.Line-bot-fly-flask | LINE Bot | 需設定 config.py |
| 07.Pytest-DEMO | 單元測試 | `pytest` |
| 08.OpenCV-Mediapipe-DEMO | 電腦視覺 | 需 Python 3.8+ |
| 09.Apps | 實用工具 | `uv run --with jupyter jupyter notebook` |
| 10.sql | SQLite 教學 | `uv run --with jupyter jupyter notebook` |
| 11.AI | AI 與 LLM | `uv run --with jupyter jupyter notebook` |

## 🔧 傳統方法

如果不使用 uv，可以使用：

1. **venv**: `python -m venv venv && .\venv\Scripts\activate && pip install -r requirements.txt`
2. **pipenv**: `pipenv install && pipenv shell`
3. **conda**: `conda create -n env-name python=3.10 && conda activate env-name`

## ⚠️ 注意事項

- 某些專案需要額外設定（如 LINE Bot 需要 token）
- Selenium 需要下載對應的 WebDriver
- Playwright 需要執行 `playwright install` 安裝瀏覽器
- OpenCV-Mediapipe 建議使用 Python 3.8 以上版本
