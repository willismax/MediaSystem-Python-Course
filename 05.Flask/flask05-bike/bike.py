# 台中 YouBike 即時資訊 RESTful API
from flask import Flask, jsonify, render_template_string
import requests
import pandas as pd
import json
import os

app = Flask(__name__)

# 本地 JSON 檔案路徑
BIKE_DATA_PATH = './static/bike_data.json'


def load_local_data():
    """從本地 JSON 檔案載入資料"""
    try:
        with open(BIKE_DATA_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f'載入本地資料失敗: {e}')
        return None


def get_bike_data():
    """取得 YouBike 資料（優先使用本地資料）"""
    # 嘗試從本地載入
    data = load_local_data()
    if data:
        return data.get('retVal', [])
    
    # 本地無資料則從 API 取得
    url = "https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download"
    params = {"rid": "cab8f056-93e3-4aec-8909-1ba45d2b5d0d", "limit": 1000}
    try:
        res = requests.get(url, params=params, verify=False, timeout=10)
        data = res.json()
        return data.get('retVal', [])
    except Exception as e:
        print(f'API 取得資料失敗: {e}')
        return []


@app.route("/")
def index():
    """首頁 - 顯示 API 說明"""
    html = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>台中 YouBike 即時資訊 API</title>
        <style>
            body { font-family: 'Microsoft JhengHei', Arial, sans-serif; max-width: 900px; margin: 50px auto; padding: 20px; background: #f5f5f5; }
            h1 { color: #FF6B00; }
            .endpoint { background: white; padding: 15px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .method { background: #4CAF50; color: white; padding: 3px 8px; border-radius: 4px; font-size: 12px; }
            code { background: #f0f0f0; padding: 2px 6px; border-radius: 4px; }
            a { color: #1976D2; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>🚲 台中 YouBike 即時資訊 API</h1>
        <p>提供台中市 YouBike 2.0 站點即時資訊查詢服務</p>
        
        <h2>📡 API 端點</h2>
        
        <div class="endpoint">
            <span class="method">GET</span> <a href="/api/bikes">/api/bikes</a>
            <p>取得所有站點資訊（JSON 格式）</p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <a href="/api/bikes/stats">/api/bikes/stats</a>
            <p>取得統計資訊（總站點數、總車輛數等）</p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <a href="/api/bikes/area">/api/bikes/area</a>
            <p>依行政區分組統計</p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> /api/bikes/area/<code>&lt;area_name&gt;</code>
            <p>查詢特定行政區的站點，例如：<a href="/api/bikes/area/西屯區">/api/bikes/area/西屯區</a></p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> /api/bikes/station/<code>&lt;station_no&gt;</code>
            <p>查詢特定站點，例如：<a href="/api/bikes/station/500601001">/api/bikes/station/500601001</a></p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> /api/bikes/search?q=<code>&lt;keyword&gt;</code>
            <p>搜尋站點名稱，例如：<a href="/api/bikes/search?q=火車站">/api/bikes/search?q=火車站</a></p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <a href="/api/bikes/available">/api/bikes/available</a>
            <p>只顯示有可借車輛的站點</p>
        </div>
        
        <div class="endpoint">
            <span class="method">GET</span> <a href="/df">/df</a>
            <p>以 HTML 表格顯示所有站點資料</p>
        </div>
        
        <h2>📊 資料欄位說明</h2>
        <ul>
            <li><code>sna</code>: 站點名稱</li>
            <li><code>sarea</code>: 行政區</li>
            <li><code>ar</code>: 地址</li>
            <li><code>sno</code>: 站點編號</li>
            <li><code>tot</code>: 總車位數</li>
            <li><code>sbi</code>: 可借車輛數</li>
            <li><code>bemp</code>: 可還空位數</li>
            <li><code>lat</code>/<code>lng</code>: 經緯度</li>
            <li><code>act</code>: 站點狀態 (1=營運中)</li>
        </ul>
        
        <p style="color: #666; margin-top: 30px;">資料來源：台中市政府開放資料平台</p>
    </body>
    </html>
    """
    return html


@app.route("/api/bikes")
def api_get_all_bikes():
    """取得所有站點資訊"""
    data = get_bike_data()
    return jsonify({
        "success": True,
        "count": len(data),
        "data": data
    })


@app.route("/api/bikes/stats")
def api_get_stats():
    """取得統計資訊"""
    data = get_bike_data()
    df = pd.DataFrame(data)
    
    # 轉換數值欄位
    df['tot'] = pd.to_numeric(df['tot'], errors='coerce').fillna(0).astype(int)
    df['sbi'] = pd.to_numeric(df['sbi'], errors='coerce').fillna(0).astype(int)
    df['bemp'] = pd.to_numeric(df['bemp'], errors='coerce').fillna(0).astype(int)
    
    stats = {
        "total_stations": len(df),
        "total_capacity": int(df['tot'].sum()),
        "total_available_bikes": int(df['sbi'].sum()),
        "total_empty_slots": int(df['bemp'].sum()),
        "active_stations": int(df[df['act'] == 1].shape[0]),
        "areas": df['sarea'].nunique()
    }
    return jsonify({"success": True, "stats": stats})


@app.route("/api/bikes/area")
def api_get_by_area_list():
    """依行政區分組統計"""
    data = get_bike_data()
    df = pd.DataFrame(data)
    
    df['tot'] = pd.to_numeric(df['tot'], errors='coerce').fillna(0).astype(int)
    df['sbi'] = pd.to_numeric(df['sbi'], errors='coerce').fillna(0).astype(int)
    df['bemp'] = pd.to_numeric(df['bemp'], errors='coerce').fillna(0).astype(int)
    
    area_stats = df.groupby('sarea').agg({
        'sno': 'count',
        'tot': 'sum',
        'sbi': 'sum',
        'bemp': 'sum'
    }).rename(columns={
        'sno': 'stations',
        'tot': 'total_capacity',
        'sbi': 'available_bikes',
        'bemp': 'empty_slots'
    }).to_dict('index')
    
    return jsonify({"success": True, "areas": area_stats})


@app.route("/api/bikes/area/<area_name>")
def api_get_by_area(area_name):
    """查詢特定行政區的站點"""
    data = get_bike_data()
    filtered = [station for station in data if station.get('sarea') == area_name]
    
    if not filtered:
        return jsonify({"success": False, "message": f"找不到行政區: {area_name}"}), 404
    
    return jsonify({
        "success": True,
        "area": area_name,
        "count": len(filtered),
        "data": filtered
    })


@app.route("/api/bikes/station/<station_no>")
def api_get_station(station_no):
    """查詢特定站點"""
    data = get_bike_data()
    station = next((s for s in data if s.get('sno') == station_no), None)
    
    if not station:
        return jsonify({"success": False, "message": f"找不到站點: {station_no}"}), 404
    
    return jsonify({"success": True, "data": station})


@app.route("/api/bikes/search")
def api_search():
    """搜尋站點名稱"""
    from flask import request
    keyword = request.args.get('q', '')
    
    if not keyword:
        return jsonify({"success": False, "message": "請提供搜尋關鍵字 ?q=關鍵字"}), 400
    
    data = get_bike_data()
    filtered = [s for s in data if keyword in s.get('sna', '') or keyword in s.get('ar', '')]
    
    return jsonify({
        "success": True,
        "keyword": keyword,
        "count": len(filtered),
        "data": filtered
    })


@app.route("/api/bikes/available")
def api_get_available():
    """只顯示有可借車輛的站點"""
    data = get_bike_data()
    filtered = [s for s in data if int(s.get('sbi', 0)) > 0]
    
    return jsonify({
        "success": True,
        "count": len(filtered),
        "data": filtered
    })


@app.route("/df")
def get_bikes_df():
    """以 HTML 表格顯示台中 YouBike 即時資訊"""
    data = get_bike_data()
    df = pd.DataFrame(data)
    
    # 選取重要欄位
    display_cols = ['sna', 'sarea', 'ar', 'tot', 'sbi', 'bemp', 'act']
    available_cols = [col for col in display_cols if col in df.columns]
    df_display = df[available_cols].copy()
    
    # 重新命名欄位
    df_display.columns = ['站點名稱', '行政區', '地址', '總車位', '可借', '可還', '狀態'][:len(available_cols)]
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>台中 YouBike 站點資訊</title>
        <style>
            body {{ font-family: 'Microsoft JhengHei', Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #FF6B00; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #FF6B00; color: white; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
            tr:hover {{ background-color: #f1f1f1; }}
            .back {{ margin-bottom: 20px; }}
            a {{ color: #1976D2; }}
        </style>
    </head>
    <body>
        <div class="back"><a href="/">← 返回首頁</a></div>
        <h1>🚲 台中 YouBike 站點資訊</h1>
        <p>共 {len(df_display)} 個站點</p>
        {df_display.to_html(index=False, classes='table')}
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(debug=True, port=5000)