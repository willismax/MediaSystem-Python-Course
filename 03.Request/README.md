# 03. 網頁擷取與 API 資料存取

本章節介紹如何使用 Python `requests` 函式庫進行網頁內容擷取，以及如何透過 API 存取開放資料，適合初學者學習資料蒐集的基礎技巧。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [網頁擷取_Request.ipynb](網頁擷取_Request.ipynb) | 使用 Requests 進行基礎網頁擷取 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/03.Request/網頁擷取_Request.ipynb) |
| [擷取API資料.ipynb](擷取API資料.ipynb) | API 資料存取與解析 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/03.Request/擷取API資料.ipynb) |
| [RequestsOpenData_HW.ipynb](RequestsOpenData_HW.ipynb) | 開放資料實作練習 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/03.Request/RequestsOpenData_HW.ipynb) |

## 🚀 快速開始

### 在 Google Colab 執行 (推薦)

直接點擊上方的 **Open in Colab** 徽章即可在 Colab 執行，所需套件已預裝於 Colab 環境。

### 本機執行

```bash
# 使用 uv (推薦)
uv run --with requests --with beautifulsoup4 --with jupyter jupyter notebook

# 或使用傳統方式
pip install requests beautifulsoup4
jupyter notebook
```

## 📚 學習重點

- HTTP 請求基礎 (GET / POST)
- 使用 `requests` 抓取網頁 HTML
- 使用 BeautifulSoup 解析 HTML 結構
- 存取 JSON 格式的 REST API
- 解析政府開放資料 (data.gov.tw)

## 🔗 相關資源

- [Requests 官方文件](https://docs.python-requests.org/)
- [BeautifulSoup 文件](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [政府資料開放平臺](https://data.gov.tw/)
