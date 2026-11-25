# Subscriber：訂閱主題，收到溫度資料就判斷要不要開冷氣
#
# 執行：python mqtt_sub.py
# 停止：Ctrl+C（Colab 請按儲存格左側的停止鍵）

import json

import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"  # 要和 Publisher 使用同一個 Broker
PORT = 1883
TOPIC = "nutc/#"  # "#" 會收到 nutc/ 底下所有層級的主題
HOT = 30


def parse_temperature(payload):
    """從收到的 bytes 取出溫度；不是溫度格式就回傳 None。

    公共 Broker 上任何人都能發布訊息，收到的內容不一定是 JSON，
    所以先檢查格式，避免程式因為一筆怪訊息就中斷。
    """
    try:
        data = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None

    # 接受 {"Temperature": 25, ...}，也接受只送一個數字的訊息
    value = data.get("Temperature") if isinstance(data, dict) else data
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value


def advice(temp):
    """依溫度回傳提醒文字；不需要提醒時回傳 None。"""
    if temp >= HOT:
        return f"溫度偵測到 {temp} 度，達到 {HOT} 度，該開冷氣啦！"
    return None


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"connected with result code {reason_code}")
    if reason_code.is_failure:
        return
    # 寫在 on_connect 裡，斷線重連後也會重新訂閱
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode('utf-8', errors='replace')}")
    temp = parse_temperature(msg.payload)
    if temp is None:
        print("  略過：不是溫度格式的訊息")
        return
    text = advice(temp)
    if text:
        print(f"  {text}")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, keepalive=60)
    try:
        client.loop_forever()  # 持續等待訊息
    except KeyboardInterrupt:
        print("已停止訂閱")
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
