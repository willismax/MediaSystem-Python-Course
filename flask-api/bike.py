# 更快的顯示df: RESTful API
from flask import Flask
from flask.json import jsonify
import requests
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>台中iBike即時資訊</h1>"

@app.route("/df")
def get_all_bike_df():
    """以DataFrame顯示台中iBike即時資訊"""
    url = "https://datacenter.taichung.gov.tw/swagger/OpenData/34c2aa94-7924-40cc-96aa-b8d090f0ab69"
    res = requests.get(url)
    data = res.json()
    df = pd.DataFrame(data['retVal']).T
    return df.to_html()

@app.route("/df2json")
def get_all_df2json():
    """
    由df.to_json顯示台中iBike info
    Note: 觀察Response Headers
    """
    url = "https://datacenter.taichung.gov.tw/swagger/OpenData/34c2aa94-7924-40cc-96aa-b8d090f0ab69"
    res = requests.get(url)
    data = res.json()
    df = pd.DataFrame(data)
    return df.to_json()


@app.route("/json")
def get_all_json():
    """
    由requests.get.json顯示台中iBike info
    Note: 觀察Response Headers
    """
    url = "https://datacenter.taichung.gov.tw/swagger/OpenData/34c2aa94-7924-40cc-96aa-b8d090f0ab69"
    res = requests.get(url)
    data = res.json()
    return data

@app.route("/jsonify")
def get_all_jsonify():
    """
    由Flask.json.jsonify顯示台中iBike info
    Note: 觀察Response Headers
    """
    url = "https://datacenter.taichung.gov.tw/swagger/OpenData/34c2aa94-7924-40cc-96aa-b8d090f0ab69"
    res = requests.get(url)
    data = res.json()
    return  jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)