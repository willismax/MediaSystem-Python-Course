import datetime
from flask import Flask, jsonify
import requests
import json
import time

app = Flask(__name__)

def get_cinema_income():
    start_date = (datetime.datetime.now() - datetime.timedelta(80)).strftime("%Y/%m/%d") # 前80日
    end_date = datetime.datetime.now().strftime("%Y/%m/%d")
    url = f'https://boxoffice.tfi.org.tw/api/export?start={start_date}&end={end_date}'
    res = requests.get(url)
    time.sleep(3)
    return res.json()

def save_json_data(): 
    data = get_cinema_income()
    with open('./static/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json_data():
    try:
        with open('./static/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except Exception as e:  
        print('load json data error:', e)
        return None

def filter_data(data, key, value):  
    if not data:
        return None
    return [i for i in data.get('list', []) if i.get(key) == value]

@app.route('/')
def index():
    return '<h1>電影票房API</h1>'

@app.route('/api/movies') 
def all_movies():
    data = load_json_data()
    return jsonify(data)

@app.route('/api/movies/<search_key>')
def search_key(search_key):
    data = load_json_data()
    filtered_data = filter_data(data, 'search_key', search_key)  # 使用獨立函式過濾資料
    return jsonify(filtered_data if filtered_data is not None else {'error':'搜尋條件錯誤'})

# 第2版API
@app.route('/api/v2/movies')
def all_v2():
    data = load_json_data()
    return jsonify(data)

@app.route('/api/v2/movies/country/<country_name>')
def country(country_name):
    data = load_json_data()
    filtered_data = filter_data(data, 'country', country_name)
    return jsonify(filtered_data if filtered_data is not None else {'error':'搜尋條件錯誤'})

@app.route('/api/v2/movies/name/<movie_name>')
def movie(movie_name):
    data = load_json_data()
    filtered_data = filter_data(data, 'name', movie_name)
    return jsonify(filtered_data if filtered_data is not None else {'error':'搜尋條件錯誤'})

if __name__ == '__main__':
    app.run(debug=True)
