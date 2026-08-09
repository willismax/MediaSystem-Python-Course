# 進修部一年級：Python、API 與雲端應用

## 課程定位

承接學生可能具備但程度不一的 Python 經驗，以「程式如何和網路服務合作」為主線，從 HTTP／JSON、開放資料、API 與 Web service，走到可展示的雲端應用及分組專題。

- [前一學年課程主頁（HackMD 書本模式）](https://hackmd.io/@wiimax/Hy4cF6OOgx)
- [HackMD 每週教學講義母稿（18 週完整教案）](../../docs/HACKMD_WEEKLY_GUIDE.md)
- [repository 快速開始](../../docs/QUICKSTART.md)

> 每週的目標、課前任務、150 分鐘課堂流程、分層挑戰、作業與 exit ticket 已整理在教學講義母稿。HackMD 保留公告與課堂互動，程式碼及作業規格以 repository 版本為準。

## 建議單元順序

| 單元 | 核心概念 | Repository 實作 | 檢核成果 |
|---|---|---|---|
| 0. 程度診斷 | 變數、容器、流程、函式、錯誤訊息 | [`01.Intro-Python`](../../01.Intro-Python/README.md) 精選 | 依結果提供補強清單，不讓全班重修 |
| 1. 網路基礎 | client/server、DNS、URL、HTTP method/status/header | [`03.Request`](../../03.Request/README.md) | 能以文字說明一次 request/response |
| 2. API 與資料 | JSON、參數、分頁、錯誤、速率限制、資料授權 | `擷取API資料.ipynb`、`RequestsOpenData_HW.ipynb` | 開放資料擷取與整理 |
| 3. 互動原型 | 輸入驗證、介面、例外情境 | [`02.Gradio`](../../02.Gradio/README.md) | 將資料流程包成可操作 demo |
| 4. Web API | route、REST、CRUD、測試 | [`05.Flask`](../../05.Flask/README.md)、[`07.Pytest-DEMO`](../../07.Pytest-DEMO/README.md) | 小型 API 與自動測試 |
| 5. 資料保存 | schema、SQLite、CRUD | [`10.sql`](../../10.sql/README.md) | 保存與查詢應用資料 |
| 6. 第三方整合 | token、webhook、secret、API 成本與隱私 | [`06.Line-bot-fly-flask`](../../06.Line-bot-fly-flask/README.md)、[`11.AI`](../../11.AI/README.md) | 串接一項外部服務 |
| 7. 雲端初體驗 | environment、log、部署、健康檢查與限制 | Flask／LINE Bot 專案（部署平台依當期選定） | 公開 demo 或可重現部署紀錄 |
| 8. 分組專題 | 題目驗證、版本控制、分工、測試、簡報 | 依題目選用模組 | 程式、README、展示與反思 |

## 核心與選修

- **核心**：Python 診斷、HTTP／JSON、API、互動原型、secret 管理、部署概念及分組專題。
- **選修**：爬蟲、LINE Bot、資料庫、LLM、OpenCV。選修由專題需求驅動，不要求每組使用相同技術。
- **替代方案**：付費 API 或需信用卡的部署平台必須提供免費／本機方案；評分聚焦概念與可重現性，不以付費服務可用性評分。

## 專題關卡

| 關卡 | 應繳內容 |
|---|---|
| 提案 | 使用者、問題、資料／API 候選、風險、最小可行成果 |
| 技術驗證 | 一次成功及一次失敗的 API 呼叫、資料樣本、secret 管理方式 |
| 原型 | 可操作流程、基本錯誤處理、組員貢獻紀錄 |
| 完成版 | 原始碼、安裝與執行文件、測試、授權、展示連結或影片 |
| 發表 | 問題與取捨、現場展示、限制、後續改善，而非只介紹套件 |

## 建議共同評量規準

- 問題與使用者需求：20%
- HTTP／API／雲端概念與技術整合：25%
- 可執行性、例外處理與測試：25%
- 文件、資料來源、授權與安全：15%
- 分工、展示與反思：15%

每學期可調整比例，但應在開題前公布。API key、token 與個資不得出現在 Notebook 輸出、commit 或展示畫面中。
