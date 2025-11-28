import os
import datetime
import requests
import json
import time

def get_cinema_income():
    start_date = (datetime.datetime.now() - datetime.timedelta(80)).strftime("%Y/%m/%d") # 前80日
    end_date = datetime.datetime.now().strftime("%Y/%m/%d")
    url = f'https://boxoffice.tfi.org.tw/api/export?start={start_date}&end={end_date}'
    res = requests.get(url)
    time.sleep(3)
    return res.json()

def save_json_data():
    data = get_cinema_income()
    
    os.makedirs('./static', exist_ok=True)
    
    with open('./static/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print('資料已儲存至 ./static/data.json')

if __name__ == '__main__':
    save_json_data()