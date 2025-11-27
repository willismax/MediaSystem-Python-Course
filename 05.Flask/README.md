# Flask 基礎教學

從基本網站服務到建立基本 API。

## 🚀 快速開始

### 使用 uv (推薦)

```bash
# 方法 1: 直接執行 (最簡單)
cd flask01
uv run app.py

# 方法 2: 建立虛擬環境
uv venv
uv pip install -r requirements.txt

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

python app.py
```

### 使用傳統 pip

```bash
# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 安裝套件
pip install -r requirements.txt

# 執行應用
python app.py
```

## 套件說明

- **Flask**: Web 框架
- **pandas**: 資料處理
- **requests**: HTTP 請求
- **Flask-RESTful**: RESTful API 擴充
- **ngrok**: 建立外網通道（用於測試）

## 學習內容

1. Flask 基礎路由
2. 模板渲染
3. RESTful API 設計
4. 資料處理與整合
