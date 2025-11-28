# 🚲 台中 YouBike 即時資訊 API

提供台中市 YouBike 2.0 站點即時資訊查詢的 RESTful API 服務。

## 快速開始

### 安裝依賴

```bash
# 使用 uv（推薦）
uv venv
uv pip install flask pandas requests

# 或使用 pip
pip install flask pandas requests
```

### 更新資料

```bash
python get_taichung_Ubike.py
```

### 啟動服務

```bash
python bike.py
```

服務將在 http://127.0.0.1:5000 啟動

---

## 📡 API 端點

### 基本資訊

| 項目 | 說明 |
|------|------|
| Base URL | `http://127.0.0.1:5000` |
| 回應格式 | JSON |
| 編碼 | UTF-8 |

---

### 1. 首頁

```
GET /
```

顯示 API 說明文件（HTML 頁面）

---

### 2. 取得所有站點

```
GET /api/bikes
```

**回應範例：**

```json
{
    "success": true,
    "count": 1256,
    "data": [
        {
            "scity": "台中市",
            "sna": "YouBike2.0_綠川東中山路口",
            "sarea": "中區",
            "ar": "綠川東街/中山路口(東側)",
            "sno": "500601001",
            "tot": "16",
            "sbi": "7",
            "bemp": "9",
            "lat": "24.13785",
            "lng": "120.68337",
            "act": 1
        }
    ]
}
```

---

### 3. 取得統計資訊

```
GET /api/bikes/stats
```

**回應範例：**

```json
{
    "success": true,
    "stats": {
        "total_stations": 1256,
        "total_capacity": 25890,
        "total_available_bikes": 12543,
        "total_empty_slots": 13245,
        "active_stations": 1250,
        "areas": 29
    }
}
```

---

### 4. 依行政區分組統計

```
GET /api/bikes/area
```

**回應範例：**

```json
{
    "success": true,
    "areas": {
        "中區": {
            "stations": 45,
            "total_capacity": 890,
            "available_bikes": 423,
            "empty_slots": 456
        },
        "西屯區": {
            "stations": 120,
            "total_capacity": 2450,
            "available_bikes": 1234,
            "empty_slots": 1200
        }
    }
}
```

---

### 5. 查詢特定行政區

```
GET /api/bikes/area/<area_name>
```

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| area_name | string | 行政區名稱（如：西屯區、北區） |

**範例：**

```
GET /api/bikes/area/西屯區
```

**回應範例：**

```json
{
    "success": true,
    "area": "西屯區",
    "count": 120,
    "data": [
        {
            "sna": "YouBike2.0_臺中市政府",
            "sarea": "西屯區",
            "ar": "臺灣大道三段99號",
            "sno": "500607001",
            "tot": "60",
            "sbi": "25",
            "bemp": "35"
        }
    ]
}
```

**錯誤回應（404）：**

```json
{
    "success": false,
    "message": "找不到行政區: 不存在區"
}
```

---

### 6. 查詢特定站點

```
GET /api/bikes/station/<station_no>
```

**參數：**

| 參數 | 類型 | 說明 |
|------|------|------|
| station_no | string | 站點編號（如：500601001） |

**範例：**

```
GET /api/bikes/station/500601001
```

**回應範例：**

```json
{
    "success": true,
    "data": {
        "scity": "台中市",
        "sna": "YouBike2.0_綠川東中山路口",
        "sarea": "中區",
        "ar": "綠川東街/中山路口(東側)",
        "sno": "500601001",
        "tot": "16",
        "sbi": "7",
        "bemp": "9",
        "lat": "24.13785",
        "lng": "120.68337",
        "act": 1
    }
}
```

---

### 7. 搜尋站點

```
GET /api/bikes/search?q=<keyword>
```

**查詢參數：**

| 參數 | 類型 | 必填 | 說明 |
|------|------|------|------|
| q | string | ✅ | 搜尋關鍵字 |

**範例：**

```
GET /api/bikes/search?q=火車站
```

**回應範例：**

```json
{
    "success": true,
    "keyword": "火車站",
    "count": 5,
    "data": [
        {
            "sna": "YouBike2.0_臺中火車站(建國路)",
            "sarea": "中區",
            "ar": "建國路/臺灣大道一段口",
            "sbi": "12",
            "bemp": "8"
        }
    ]
}
```

**錯誤回應（400）：**

```json
{
    "success": false,
    "message": "請提供搜尋關鍵字 ?q=關鍵字"
}
```

---

### 8. 可借車輛站點

```
GET /api/bikes/available
```

只回傳有可借車輛（sbi > 0）的站點。

**回應範例：**

```json
{
    "success": true,
    "count": 1100,
    "data": [
        {
            "sna": "YouBike2.0_綠川東中山路口",
            "sbi": "7",
            "bemp": "9"
        }
    ]
}
```

---

### 9. HTML 表格顯示

```
GET /df
```

以 HTML 表格形式顯示所有站點資料，適合瀏覽器直接檢視。

---

## 📊 資料欄位說明

| 欄位 | 說明 | 範例 |
|------|------|------|
| `scity` | 城市 | 台中市 |
| `sna` | 站點名稱 | YouBike2.0_綠川東中山路口 |
| `sarea` | 行政區 | 中區 |
| `ar` | 地址 | 綠川東街/中山路口(東側) |
| `sno` | 站點編號 | 500601001 |
| `tot` | 總車位數 | 16 |
| `sbi` | 可借車輛數 | 7 |
| `bemp` | 可還空位數 | 9 |
| `lat` | 緯度 | 24.13785 |
| `lng` | 經度 | 120.68337 |
| `act` | 站點狀態 | 1（營運中） |
| `mday` | 資料更新時間 | 20251128141402 |
| `sbi_detail` | 車輛細節 | {"yb2": "6", "eyb": "1"} |

### sbi_detail 說明

| 欄位 | 說明 |
|------|------|
| `yb2` | YouBike 2.0 車輛數 |
| `eyb` | YouBike 2.0E（電動）車輛數 |

---

## 🔧 檔案結構

```
flask05-bike/
├── bike.py                    # Flask API 主程式
├── get_taichung_Ubike.py      # 資料下載腳本
├── README.md                  # API 文件（本檔案）
└── static/
    ├── bike_data.json         # YouBike 資料（JSON）
    └── bike_data.csv          # YouBike 資料（CSV）
```

---

## 💡 使用範例

### Python

```python
import requests

# 取得所有站點
response = requests.get('http://127.0.0.1:5000/api/bikes')
data = response.json()
print(f"共有 {data['count']} 個站點")

# 搜尋站點
response = requests.get('http://127.0.0.1:5000/api/bikes/search', params={'q': '火車站'})
results = response.json()
for station in results['data']:
    print(f"{station['sna']}: 可借 {station['sbi']} 輛")
```

### JavaScript (Fetch)

```javascript
// 取得統計資訊
fetch('http://127.0.0.1:5000/api/bikes/stats')
    .then(res => res.json())
    .then(data => {
        console.log(`總站點: ${data.stats.total_stations}`);
        console.log(`可借車輛: ${data.stats.total_available_bikes}`);
    });
```

### cURL

```bash
# 取得所有站點
curl http://127.0.0.1:5000/api/bikes

# 搜尋站點
curl "http://127.0.0.1:5000/api/bikes/search?q=市政府"

# 查詢特定行政區
curl http://127.0.0.1:5000/api/bikes/area/西屯區
```

---

## 📝 注意事項

1. **資料來源**：台中市政府開放資料平台
2. **更新頻率**：建議定期執行 `get_taichung_Ubike.py` 更新資料
3. **本地快取**：API 優先使用本地 `static/bike_data.json`，加快回應速度
4. **CORS**：如需跨域存取，請自行加入 Flask-CORS

---

## 📜 授權

本專案資料來源為台中市政府開放資料，請遵守相關使用規範。
