# Publisher：每隔幾秒發布一筆模擬的溫度資料
#
# 執行：python mqtt_pub.py
# 停止：Ctrl+C（Colab 請按儲存格左側的停止鍵）

import datetime
import json
import time
from random import randint

import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"  # 也可改成 "broker.hivemq.com"
PORT = 1883
TOPIC = "nutc/csie/2701/sensor01"
QOS = 0  # 0：最多一次；1：至少一次；2：剛好一次
INTERVAL = 5  # 每次發布間隔幾秒
COUNT = 0  # 要發布幾筆；0 表示一直發布到手動停止


def make_message(temperature, now=None):
    """把溫度與時間包成一個 dict，之後再轉成 JSON 字串送出。"""
    now = now or datetime.datetime.now()
    return {"Temperature": temperature, "Time": now.strftime("%m/%d %H:%M:%S")}


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()  # 在背景處理網路收發

    sent = 0
    try:
        while COUNT == 0 or sent < COUNT:
            message = make_message(randint(18, 32))
            info = client.publish(TOPIC, json.dumps(message), qos=QOS)
            info.wait_for_publish()
            sent += 1
            print(f"topic: {TOPIC}, message: {message}")
            if COUNT == 0 or sent < COUNT:
                time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("已停止發布")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
