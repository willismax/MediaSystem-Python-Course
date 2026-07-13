# 04. Playwright — 瀏覽器自動化爬蟲

本章節介紹如何使用 [Playwright](https://playwright.dev/python/) 進行瀏覽器自動化操作，適合處理需要執行 JavaScript 的動態網頁。Playwright 支援錄製腳本功能，可大幅降低撰寫爬蟲的門檻。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [damun.ipynb](damun.ipynb) | Playwright 實作示範 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/04.Playwright/damun.ipynb) |

## 📁 檔案說明

| 檔案 | 說明 |
|------|------|
| `damun.ipynb` | Playwright 互動式教學筆記本 |
| `damun.py` | Playwright 爬蟲腳本 |
| `damun_33846.json` | 擷取資料範例 |
| `page.json` | 頁面結構範例 |
| `Playwright_proj/` | Playwright 專案範例 |

## 🚀 快速開始

### 安裝 Playwright

```bash
# 使用 uv (推薦)
uv run --with playwright python -m playwright install chromium

# 或使用傳統方式
pip install playwright
playwright install chromium
```

### 執行腳本

```bash
# 使用 uv 執行
uv run --with playwright damun.py

# 或直接執行
python damun.py
```

### 錄製腳本 (Codegen)

```bash
# 啟動錄製模式，操作瀏覽器後自動產生程式碼
playwright codegen https://example.com
```

## 📚 學習重點

- Playwright 安裝與基本設定
- 啟動瀏覽器並導航至網頁
- 定位元素與擷取資料
- 使用 Codegen 錄製操作腳本
- 處理動態載入內容

## 🔗 相關資源

- [Playwright Python 官方文件](https://playwright.dev/python/)
- [Playwright GitHub](https://github.com/microsoft/playwright-python)
