# 04. Selenium — 動態網頁爬蟲

本章節介紹如何使用 [Selenium](https://www.selenium.dev/) 進行動態網頁的自動化操作與資料擷取，適合需要模擬使用者行為（登入、捲動、點擊）的進階爬蟲需求。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [網頁擷取_Selenium.ipynb](網頁擷取_Selenium.ipynb) | Selenium 基礎網頁擷取教學 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/04.Selenium/網頁擷取_Selenium.ipynb) |
| [ptt_selenium.ipynb](ptt_selenium.ipynb) | PTT 看板資料爬蟲 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/04.Selenium/ptt_selenium.ipynb) |
| [yahoo_selenium.ipynb](yahoo_selenium.ipynb) | Yahoo 股市資料爬蟲 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/04.Selenium/yahoo_selenium.ipynb) |

## 📁 檔案說明

| 檔案 | 說明 |
|------|------|
| `網頁擷取_Selenium.ipynb` | Selenium 互動式教學筆記本 |
| `ptt_selenium.py` | PTT 爬蟲 Python 腳本 |
| `yahoo_selenium.py` | Yahoo 股市爬蟲 Python 腳本 |
| `ptt_scraping_dag.py` | PTT 爬蟲 DAG 排程腳本 |

## 🚀 快速開始

### 安裝套件

```bash
# 使用 uv (推薦)
uv run --with selenium --with webdriver-manager python ptt_selenium.py

# 或使用傳統方式
pip install selenium webdriver-manager
```

### 安裝瀏覽器驅動程式

Selenium 需要對應瀏覽器的 WebDriver：

- **Chrome**: [ChromeDriver](https://chromedriver.chromium.org/)
- **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver)

使用 `webdriver-manager` 可自動下載對應版本的驅動程式：

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```

### 執行腳本

```bash
python ptt_selenium.py
python yahoo_selenium.py
```

## 📚 學習重點

- Selenium WebDriver 基本操作
- 定位元素 (CSS Selector、XPath)
- 模擬點擊、輸入、捲動等使用者行為
- 等待頁面載入 (Implicit / Explicit Wait)
- 處理動態 JavaScript 渲染內容

## ⚠️ 注意事項

- 請確認 ChromeDriver 版本與 Chrome 瀏覽器版本相符
- 部分網站對爬蟲有防護機制，請遵守網站使用條款
- 建議加入適當的等待時間，避免請求過於頻繁

## 🔗 相關資源

- [Selenium 官方文件](https://www.selenium.dev/documentation/)
- [webdriver-manager PyPI](https://pypi.org/project/webdriver-manager/)
