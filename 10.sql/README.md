# 10. SQLite 資料庫

本章節介紹如何使用 Python 操作 SQLite 資料庫，涵蓋資料庫建立、查詢、更新、刪除等基本 CRUD 操作，適合初學者學習資料庫概念與 SQL 語法。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [SQLite資料庫CRUD.ipynb](SQLite資料庫CRUD.ipynb) | SQLite 資料庫 CRUD 完整教學 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/10.sql/SQLite資料庫CRUD.ipynb) |

## 🚀 快速開始

### 在 Google Colab 執行 (推薦)

直接點擊上方的 **Open in Colab** 徽章即可在 Colab 執行，SQLite 為 Python 內建模組，無需額外安裝套件。

### 本機執行

```bash
# SQLite 為 Python 內建，直接啟動 Jupyter 即可
uv run --with jupyter jupyter notebook SQLite資料庫CRUD.ipynb

# 或使用傳統方式
jupyter notebook SQLite資料庫CRUD.ipynb
```

## 📚 學習重點

- SQLite 資料庫建立與連線
- **C**reate：建立資料表與新增資料 (`INSERT`)
- **R**ead：查詢資料 (`SELECT`)
- **U**pdate：更新資料 (`UPDATE`)
- **D**elete：刪除資料 (`DELETE`)
- 使用 Python `sqlite3` 內建模組
- 搭配 Pandas DataFrame 進行資料處理

## 🔗 相關資源

- [Python sqlite3 官方文件](https://docs.python.org/3/library/sqlite3.html)
- [SQLite 官方網站](https://www.sqlite.org/)
- [SQL 語法教學 (W3Schools)](https://www.w3schools.com/sql/)
