# 14. FastAPI — 循序漸進 API 教學

本單元參考 [FastAPI 官方教學](https://fastapi.tiangolo.com/tutorial/)，從回傳第一個 JSON 回應開始，逐步練習路徑與查詢參數、請求資料驗證，以及可測試的 RESTful API。

## FastAPI 能帶來什麼？

- 使用 Python 型別註記描述輸入與輸出，框架會驗證資料並在格式錯誤時回傳清楚的錯誤訊息。
- 自動產生符合 OpenAPI 的互動式文件；啟動後可在 `/docs` 測試 API，也可在 `/redoc` 閱讀文件。
- 可用一般函式或 `async def` 撰寫端點，適合逐步從 Python 程式延伸為 Web API。

## 📒 教材清單

| 檔案 | 學習重點 |
|---|---|
| [`hello.py`](hello.py) | 第一個路由與 JSON 回應 |
| [`parameters.py`](parameters.py) | 型別化的路徑與查詢參數 |
| [`media_api.py`](media_api.py) | Pydantic 模型、驗證、狀態碼與小型多媒體目錄 API |
| [`test_media_api.py`](test_media_api.py) | 以 `TestClient` 測試 API 行為 |

## 🚀 安裝

需要 Python 3.10 以上版本。

### 使用 uv（推薦）

```bash
cd 14.FastAPI
uv venv
uv pip install -r requirements.txt
```

### 使用 pip

```bash
cd 14.FastAPI
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
```

## 1. 建立第一個 API

啟動 `hello.py`：

```bash
fastapi dev hello.py
```

在瀏覽器開啟 <http://127.0.0.1:8000/>，會得到：

```json
{"message":"Hello, FastAPI!"}
```

同時開啟 <http://127.0.0.1:8000/docs>。FastAPI 會依 `@app.get("/")` 與函式的型別註記建立可操作的 API 文件，不必另外手寫 Swagger UI。

## 2. 加入路徑與查詢參數

改為啟動第二個範例：

```bash
fastapi dev parameters.py
```

試著在瀏覽器開啟下列網址：

```text
http://127.0.0.1:8000/media/7
http://127.0.0.1:8000/media/7?media_type=video
```

`media_id: int` 會把路徑參數轉成整數；若輸入不是整數，FastAPI 會回傳 422 驗證錯誤。`media_type` 是可省略的查詢參數，並限制長度最多 20 個字元。

## 3. 驗證請求資料並建立 API

[`media_api.py`](media_api.py) 使用 `MediaCreate` 描述 POST 請求內容，並用 `Literal` 將媒體類型限制為 `image`、`audio` 或 `video`。啟動它：

```bash
fastapi dev media_api.py
```

先讀取範例資料：

```bash
curl http://127.0.0.1:8000/media
```

再新增一筆影片資料：

```bash
curl -X POST http://127.0.0.1:8000/media \
  -H "Content-Type: application/json" \
  -d '{"title":"期末成果影片","media_type":"video"}'
```

成功時會取得 `201 Created` 與自動配發的 `id`。在 `/docs` 的 `POST /media` 區塊也可直接輸入 JSON 測試；嘗試空白標題或不支援的 `media_type`，即可觀察自動產生的 422 驗證結果。

> 範例將資料保存在記憶體中，伺服器重啟後會重設，目的是聚焦於 API 設計與驗證。下一步可將資料儲存邏輯改為 SQLite 或其他資料庫。

## 4. 測試 API

`TestClient` 不需要另開伺服器，即可在 Python 內送出測試請求：

```bash
pytest -q
```

測試涵蓋讀取、篩選、新增、找不到資料時的 404，以及不合法請求資料的 422。

## 下一步

1. 為 `media_api.py` 加入更新與刪除端點。
2. 將記憶體資料替換為 SQLite，並為每個端點增加測試。
3. 閱讀官方的安全性與部署章節，再將服務部署到可控的環境。

## 🔗 官方文件

- [FastAPI Tutorial — First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Testing](https://fastapi.tiangolo.com/tutorial/testing/)
