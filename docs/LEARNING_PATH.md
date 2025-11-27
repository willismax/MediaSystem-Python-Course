# 專案概覽與學習路徑

本文件提供完整的課程結構與建議的學習路徑。

## 📚 課程架構

### 第一階段：Python 基礎 (Week 1-2)
**目標：掌握 Python 基本語法與環境設定**

1. **01.Intro-Python** - Python 基礎
   - 變數與資料型態
   - 流程控制（if/for/while）
   - 函數定義與使用
   - 常用內建模組
   
2. **02.Gradio** - 快速建立 GUI
   - 理解使用者介面的重要性
   - 學習如何包裝程式為可用工具
   - 在 Colab 上建立互動式應用

**實作項目**：建立一個簡單的計算器 GUI

---

### 第二階段：網路爬蟲 (Week 3-4)
**目標：學習資料擷取與 API 使用**

3. **03.Request** - 基礎網頁擷取
   - HTTP 請求基礎
   - 使用 Requests 庫
   - 存取 Open Data API
   - JSON 資料處理
   
   **啟動方式**：
   ```bash
   cd 03.Request
   uv run --with jupyter jupyter notebook
   ```

4. **04.Selenium** - 動態網頁爬蟲
   - 處理需要 JavaScript 的網頁
   - 自動化瀏覽器操作
   - 表單填寫與提交
   
   **注意**：需自行下載 WebDriver

5. **04.Playwright** - 新一代爬蟲工具
   - 錄製腳本功能
   - 多瀏覽器支援
   - 更穩定的自動化
   
   **安裝**：
   ```bash
   uv pip install playwright
   playwright install
   ```

**實作項目**：爬取政府開放資料並製作分析報告

---

### 第三階段：Web 開發 (Week 5-6)
**目標：建立自己的 Web 服務與 API**

6. **05.Flask** - Web 框架基礎
   - 路由與請求處理
   - 模板渲染
   - RESTful API 設計
   - 資料庫整合
   
   **快速啟動**：
   ```bash
   # 使用腳本
   .\scripts\run-flask.ps1  # Windows
   ./scripts/run-flask.sh   # Linux/macOS
   
   # 或直接使用 uv
   cd 05.Flask/flask01
   uv run app.py
   ```
   
   **學習成果**：
   - 建立個人網站
   - 設計 RESTful API
   - 整合前端與後端

7. **06.Line-bot-fly-flask** - LINE Bot 開發
   - LINE Messaging API
   - Webhook 處理
   - 第三方 API 整合
   - 部署到雲端 (Fly.io)
   
   **配置需求**：
   - LINE Channel Access Token
   - LINE Channel Secret
   - 其他 API Keys（HackMD, Imgur, OpenAI）
   
   **功能特色**：
   - 訊息自動回覆
   - 整合 OpenAI GPT
   - 圖片上傳至 Imgur
   - 記錄至 HackMD

**實作項目**：建立一個具有 AI 對話功能的 LINE Bot

---

### 第四階段：軟體測試 (Week 7)
**目標：撰寫可靠的程式碼**

8. **07.Pytest-DEMO** - 單元測試
   - pytest 基礎
   - 測試案例撰寫
   - 測試覆蓋率分析
   - TDD 開發流程
   
   **執行測試**：
   ```bash
   cd 07.Pytest-DEMO
   uv venv
   uv pip install -r requirements.txt
   
   # 執行測試
   pytest
   
   # 查看覆蓋率
   pytest --cov=./
   pytest --cov-report=html
   ```

**實作項目**：為之前的專案加入單元測試

---

### 第五階段：電腦視覺 (Week 8-9)
**目標：處理圖像與視訊資料**

9. **08.OpenCV-Mediapipe-DEMO** - 電腦視覺
   - OpenCV 影像處理
   - Mediapipe 機器學習
   - 臉部辨識
   - 手勢追蹤
   - 姿態估計
   
   **系統需求**：
   - Python 3.8+
   - 網路攝影機
   
   **快速啟動**：
   ```bash
   cd 08.OpenCV-Mediapipe-DEMO
   uv venv --python 3.10
   uv pip install opencv-python mediapipe
   
   # 啟動虛擬環境
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/macOS
   
   python demo.py
   ```

**實作項目**：開發手勢控制應用程式

---

### 第六階段：實用工具開發 (Week 10)
**目標：製作日常實用工具**

10. **09.Apps** - 應用程式範例
    - QR Code 產生器
    - 圖片處理工具
    - 資料轉換工具
    
    **特色功能**：
    - 純黑白 QR Code
    - 彩色背景 QR Code
    - GIF 動態 QR Code
    
    **啟動**：
    ```bash
    cd 09.Apps
    uv run --with jupyter jupyter notebook QRCode.ipynb
    ```

**實作項目**：製作個人化 QR Code 名片

---

### 第七階段：資料庫操作 (Week 11)
**目標：資料持久化與管理**

11. **10.sql** - SQLite 資料庫
    - SQL 基礎語法
    - CRUD 操作
    - 資料庫設計
    - Python 資料庫整合
    
    **學習內容**：
    ```bash
    cd 10.sql
    uv run --with jupyter jupyter notebook SQLite資料庫CRUD.ipynb
    ```

**實作項目**：設計並實作個人記帳系統

---

### 第八階段：AI 應用開發 (Week 12)
**目標：整合大型語言模型**

12. **11.AI** - AI 與 LLM 應用
    - Gemini API 使用
    - OpenAI API 整合
    - Prompt Engineering
    - AI 應用開發
    
    **範例筆記本**：
    - `動手串接_LLM_API_入門教學(Gemini_).ipynb`
    - `在_Colab_終端機使用_Gemini_CLI.ipynb`
    - `gemini_cli_colab_tutorial.ipynb`
    
    **啟動**：
    ```bash
    cd 11.AI
    uv run --with jupyter jupyter notebook
    ```

**實作項目**：建立 AI 聊天機器人或內容生成工具

---

## 🎯 建議學習路徑

### 初學者路徑（12 週完整課程）
```
Week 1-2:  Python 基礎 + Gradio GUI
Week 3-4:  網頁爬蟲（Requests → Selenium → Playwright）
Week 5-6:  Web 開發（Flask → LINE Bot）
Week 7:    軟體測試（Pytest）
Week 8-9:  電腦視覺（OpenCV + Mediapipe）
Week 10:   實用工具開發
Week 11:   資料庫操作
Week 12:   AI 應用開發
```

### 快速上手路徑（6 週速成）
```
Week 1:  01+02 (Python 基礎)
Week 2:  03 (網頁擷取與 API)
Week 3:  05 (Flask Web 開發)
Week 4:  06 (LINE Bot 開發)
Week 5:  10 (資料庫) + 09 (實用工具)
Week 6:  11 (AI 應用)
```

### 專題導向路徑（依興趣選擇）
- **Web 開發專題**：01 → 05 → 06 → 10 → 11
- **資料科學專題**：01 → 03 → 10 → 11
- **電腦視覺專題**：01 → 08 → 11
- **自動化專題**：01 → 03 → 04.Selenium → 04.Playwright → 09

---

## 💡 學習建議

### 1. 環境設定
- **強烈推薦使用 uv**：速度快、簡單易用
- 使用提供的啟動腳本快速開始
- 遇到問題先查看各專案的 README.md

### 2. 實作為主
- 每個章節都要動手實作
- 修改範例程式碼，加入自己的想法
- 建立個人專案組合

### 3. 循序漸進
- 不要跳過基礎章節
- 確實理解每個概念後再進入下一章
- 遇到困難時回頭複習

### 4. 善用資源
- 參考官方文檔
- 加入開發者社群
- 查看 GitHub Issues 和 Discussions

### 5. 專案導向學習
- 設定一個最終目標專案
- 將學到的技能逐步應用到專案中
- 完成後發布到 GitHub

---

## 🔗 相關資源

### 官方文檔
- [Python 官方教學](https://docs.python.org/zh-tw/3/)
- [Flask 文檔](https://flask.palletsprojects.com/)
- [LINE Messaging API](https://developers.line.biz/en/docs/messaging-api/)
- [OpenCV 文檔](https://docs.opencv.org/)
- [Mediapipe 文檔](https://google.github.io/mediapipe/)

### 工具文檔
- [uv 官方文檔](https://docs.astral.sh/uv/)
- [Jupyter Notebook](https://jupyter.org/documentation)
- [Pytest 文檔](https://docs.pytest.org/)

### 學習平台
- [Colab](https://colab.research.google.com/) - 免費的 Jupyter 環境
- [GitHub](https://github.com/) - 版本控制與專案託管
- [Stack Overflow](https://stackoverflow.com/) - 問題求助

---

## 📝 評量與認證

完成課程後，建議：

1. **建立專案組合**
   - 在 GitHub 上建立個人專案
   - 撰寫完整的 README
   - 加入測試與文檔

2. **參與開源專案**
   - 為本專案發 PR
   - 參與其他開源專案
   - 累積實戰經驗

3. **持續學習**
   - 關注新技術趨勢
   - 深入學習感興趣的領域
   - 參加技術社群活動

---

## 🤝 貢獻與回饋

歡迎：
- 回報問題 (Issues)
- 改進文檔 (Pull Requests)
- 分享學習心得
- 提供新的範例專案

讓我們一起讓這個課程變得更好！🚀
