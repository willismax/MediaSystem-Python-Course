# 07. Pytest — 自動化測試入門

本章節介紹如何使用 [pytest](https://docs.pytest.org/) 為 Python 程式撰寫自動化測試，涵蓋單元測試、API 測試與測試覆蓋率報告。

## 📒 教材清單

| 教材 | 說明 | 開啟方式 |
|------|------|----------|
| [Pytest_Demo.ipynb](Pytest_Demo.ipynb) | pytest 入門示範 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/willismax/MediaSystem-Python-Course/blob/main/07.Pytest-DEMO/Pytest_Demo.ipynb) |

## 📁 檔案說明

| 檔案 | 說明 |
|------|------|
| `Pytest_Demo.ipynb` | pytest 互動式教學筆記本 |
| `my_module.py` | 受測試的模組範例 |
| `test_my_module.py` | 對應的單元測試檔案 |
| `test_tasks_api.py` | Tasks API 測試 |
| `requirements.txt` | 相依套件清單 |

## 🚀 快速開始

### 安裝套件

```bash
# 使用 uv (推薦)
uv pip install -r requirements.txt

# 或使用傳統方式
pip install -r requirements.txt
```

### 執行測試

```bash
# 執行全部測試
pytest

# 執行並顯示詳細資訊
pytest -v

# 執行並產生測試覆蓋率報告
pytest --cov=./

# 產生 HTML 格式的覆蓋率報告
pytest --cov-report=html
```

## 📚 學習重點

- pytest 基本測試寫法
- 測試函式命名慣例 (`test_` 前綴)
- Fixture 的使用
- 參數化測試 (`@pytest.mark.parametrize`)
- API 端點測試
- 測試覆蓋率 (Coverage) 分析

## 🔗 相關資源

- [pytest 官方文件](https://docs.pytest.org/)
- [pytest-cov 插件](https://pytest-cov.readthedocs.io/)
