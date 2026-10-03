# Git 尋寶隊：部署示範

`docs/git-quest/index.html` 是一個單檔的靜態網頁（HTML、CSS、JavaScript 都在同一個檔案裡），不需要建置，也不需要後端或 API 金鑰。同一個 `docs/` 資料夾部署在兩個平台上，可以拿來對照兩種部署方式。

| 平台 | 網址 | 部署方式 |
|---|---|---|
| GitHub Pages | <https://willismax.github.io/MediaSystem-Python-Course/git-quest/> | 從 `main` 分支的 `/docs` 資料夾發布 |
| Cloudflare Pages | 專案建立後的 `*.pages.dev/git-quest/` | 連動 GitHub repo，輸出資料夾設為 `docs` |

## 資料夾結構

```text
docs/
├── .nojekyll          # 告訴 GitHub Pages 不要用 Jekyll 處理，檔案原樣發布
├── index.html         # 網站首頁（互動教材入口）
└── git-quest/
    ├── index.html     # Git 尋寶隊本體
    └── README.md      # 這份說明
```

## GitHub Pages

1. 到 repo 的 **Settings → Pages**。
2. **Source** 選 **Deploy from a branch**。
3. **Branch** 選 `main`，資料夾選 `/docs`，按 **Save**。
4. 等一兩分鐘，網址是 `https://<帳號>.github.io/<repo 名稱>/`。

之後每次 push 到 `main`，GitHub 會自動重新發布。

## Cloudflare Pages

1. 登入 [Cloudflare dashboard](https://dash.cloudflare.com/)，進入 **Workers & Pages → Create → Pages → Connect to Git**。
2. 授權 GitHub 並選擇這個 repo。
3. 建置設定：

| 設定項目 | 值 |
|---|---|
| Production branch | `main` |
| Framework preset | None |
| Build command | （留空） |
| Build output directory | `docs` |

4. 按 **Save and Deploy**，完成後會得到 `<專案名稱>.pages.dev`。

之後每次 push 到 `main`，Cloudflare 也會自動重新部署。這個網站沒有用到任何金鑰，所以不需要設定環境變數。

## 兩個平台的差別

| | GitHub Pages | Cloudflare Pages |
|---|---|---|
| 設定位置 | repo 的 Settings | Cloudflare dashboard |
| 網址 | `帳號.github.io/repo/` | `專案.pages.dev/` |
| 網站根目錄 | 多一層 repo 名稱 | 直接在網域根目錄 |
| 預覽部署 | 沒有 | 每個分支、每個 PR 都有預覽網址 |
| 需要建置時 | 用 GitHub Actions | 內建 build 指令 |

網站根目錄不同，是靜態網站最常踩到的坑：連結寫成 `/git-quest/`（從網域根目錄算起）在 Cloudflare 可以用，在 GitHub Pages 會壞掉。這個網站的連結都用相對路徑（`git-quest/`），兩邊都能用。

## 更新網站

修改 `docs/` 裡的檔案，commit 後 push 到 `main`（或發 Pull Request 合併），兩個平台都會自動更新。

進度存在瀏覽器的 localStorage，兩個網址各自獨立，換網址或換瀏覽器會從頭開始。
