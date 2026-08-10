# HackMD 與 GitHub 教材工作流程

## 決策

目前不導入 HackMD API。

先使用 HackMD 內建的 GitHub Sync，原因如下：

- 只有兩個班級入口與一組共用教材，尚未達到需要批次自動化的規模。
- 教師平常以 HackMD 編寫授課內容，HackMD 應維持正文來源。
- GitHub 主要保存程式、Notebook、素材與 Markdown 版本。
- API 會增加 token 保管、權限、更新衝突與錯誤覆寫風險。

## 單一來源

| 內容 | 主要來源 | 另一端用途 |
|---|---|---|
| 課堂講義與每週筆記 | HackMD | GitHub 保存版本 |
| Python 程式與 Notebook | GitHub | HackMD 放連結與操作說明 |
| 班級公告與期限 | 各班 HackMD 首頁 | 不需同步 |
| 固定圖片與下載檔 | GitHub `assets` | HackMD 引用 |
| 學生課堂筆記 | 學生自己的 HackMD | 只繳連結 |

同一份 Markdown 在一段編輯期間只能有一個主要來源。不要在 HackMD 與 GitHub 同時修改後再互相覆蓋。

## 建議目錄

```text
course-115/
├─ README.md
├─ common-syllabus.md
├─ notes/
│  ├─ week-01-hackmd-markdown.md
│  ├─ week-02-python-ai-workflow.md
│  └─ ...
├─ labs/
│  ├─ common/
│  ├─ day/
│  └─ night/
├─ assets/
└─ templates/
```

目前第一週教材位於 `course-115/week-01-hackmd-markdown.md`。與正式 repo 整合時，可移至 `notes/`，並同步修正連結。

## 初次連結

每份共同教材各自連結一個 GitHub Markdown 檔案：

1. 在 HackMD 開啟共同教材。
2. 開啟「Versions and GitHub Sync」。
3. 安裝並授權 HackMD GitHub App，只開放需要的 repo。
4. 選擇 repo、分支與對應檔案。
5. 確認換行規則。
6. 建立命名版本，例如 `W01 初版`。
7. 將命名版本推送至 GitHub。

建議對應：

```text
HackMD：W01｜HackMD、Markdown 與第一份媒體筆記
GitHub：course-115/notes/week-01-hackmd-markdown.md
```

## 每週發布流程

### 課前

1. 在 HackMD 修改共同教材。
2. 用閱讀模式完整檢查一次。
3. 測試所有連結、圖片、程式碼與分享權限。
4. 儲存命名版本，例如 `W03 上課版`。
5. 從 HackMD 推送到 GitHub。
6. 在日間部與進修部首頁貼上同一份共同教材連結。
7. 各班首頁補上不同的日期、作業與分流活動。

### 課後

1. 修正上課時發現的錯誤。
2. 儲存命名版本，例如 `W03 課後修正版`。
3. 再推送至 GitHub。
4. 程式或 Notebook 若有修正，直接在 GitHub 維護，再更新 HackMD 連結。

## 衝突處理

如果 GitHub 檔案已被修改：

1. 暫停從 HackMD 推送。
2. 先比較 HackMD 與 GitHub 版本。
3. 決定哪一端是這次變更的正本。
4. 將差異合併至正本。
5. 儲存 HackMD 命名版本後再同步。

不要直接選擇整份覆蓋，尤其是學生或協作者已在 GitHub 提交修改時。

## 何時才需要 HackMD API？

符合以下任一情況，再導入 API：

- 要一次建立完整 18 週筆記。
- 要每天或每週自動備份所有課程筆記。
- 要批次更新兩班首頁的週次與連結。
- 要從其他系統自動發布公告或產生筆記。
- 要建立課程儀表板，讀取多份筆記的標題、標籤與更新時間。

不建議用 API 做無人監督的雙向同步。

## 未來導入 API 的最低安全規範

1. Token 只能放在環境變數或祕密管理服務，不得寫入程式、Notebook 或 HackMD。
2. 自動化程式預設只讀；確認備份與差異後才開放更新。
3. 更新前先下載原始內容並保留時間戳記版本。
4. 維護 `noteId` 與 repo 檔案的明確對照表。
5. 每次更新只指定一個方向，不做自動雙向合併。
6. API 回傳失敗時停止，不以空內容覆蓋筆記。
7. 定期撤銷不再使用的 token。

建議的環境變數名稱：

```text
HACKMD_API_TOKEN
```

## 圖片與附件

- 課堂臨時示範可使用 HackMD 上傳。
- 會長期使用的教學圖片放在 GitHub `assets`，並使用清楚檔名。
- 學生上傳圖片前需確認本人有權公開。
- 圖片需撰寫替代文字。
- 不把含個資的原始照片放進公開 repo。
