import pandas as pd
import requests
from io import BytesIO
import urllib3
import os
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 確保 static 資料夾存在
os.makedirs('./static', exist_ok=True)

url = "https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download"
params = {
    "rid": "cab8f056-93e3-4aec-8909-1ba45d2b5d0d",
    "limit": 1000,
}

res = requests.get(url, params=params, verify=False)
content_type = res.headers.get("Content-Type", "")
print("Content-Type:", content_type)

if "text/csv" in content_type:
    df = pd.read_csv(BytesIO(res.content), encoding="utf-8")
    print(df.head())
    # 儲存為 CSV
    df.to_csv('./static/bike_data.csv', index=False, encoding='utf-8')
    # 也儲存為 JSON
    df.to_json('./static/bike_data.json', orient='records', force_ascii=False, indent=4)
    print('資料已儲存至 ./static/bike_data.csv 和 ./static/bike_data.json')
elif "application/json" in content_type:
    data = res.json()
    print(str(data)[:500])
    # 儲存 JSON 資料
    with open('./static/bike_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('資料已儲存至 ./static/bike_data.json')
else:
    print(res.text[:500])
