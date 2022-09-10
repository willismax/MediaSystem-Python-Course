import datetime
from flask  import Flask, jsonify
import requests
import json
import time



app = Flask(__name__)

def get_cinema_income():
    start_date = (datetime.datetime.now() - datetime.timedelta(80)).strftime("%Y/%m/%d") #前80日
    end_date = datetime.datetime.now().strftime("%Y/%m/%d")
    url = f'https://boxoffice.tfi.org.tw/api/export?start={str(start_date)}&end={str(end_date)}'
    res = requests.get(url)
    # time.sleep(3)
    return res.json()

def save_josn_data():
    data = get_cinema_income()
    with open('./static/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json_data():
    try:
        with open('./static/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except:
        print('load json data error')
    

data = load_json_data()




@app.route('/')
def index():
    save_josn_data()
    return '<h1>電影票房API</h1>'


@app.route('/api/')
def all():
    """取得全部影片"""
    data = load_json_data()
    return jsonify(data)

@app.route('/api/<search_key>')
def search_key(search_key):
    """取得對應資訊
    :parm: str: "美國"、"期末考"
    """
    try:
        data = load_json_data()
        data = [ i for i in data['list'] for k,v in i.items() if v == search_key ]
    except:
        data = {'error':'搜尋條件錯誤'}
    return jsonify(data)

# 第2版API
@app.route('/api/v2/GET/movies/all')
def all_v2():
    """取得全部影片"""
    data = load_json_data()
    return jsonify(data)

@app.route('/api/v2/GET/movies/from_country/<search_key>')
def country(search_key):
    """取得對應國家的票房資訊"""
    data = load_json_data()
    data = [ i for i in data['list'] for k,v in i.items() if v == search_key ]
    return jsonify(data)

@app.route('/api/v2/GET/movies/from_name/<search_key>')
def movie(search_key):
    """取得對應電影名稱的票房資訊"""
    data = load_json_data()
    data = [ i for i in data['list'] for k,v in i.items() if v == search_key ]
    return jsonify(data)
if __name__ == '__main__':
    app.debug = True
    app.run()
    # save_josn_data()
