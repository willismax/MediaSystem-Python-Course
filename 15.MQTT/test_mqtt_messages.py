"""測試訊息的打包與解析，不需要連線到 Broker。"""

import datetime
import json

from mqtt_pub import make_message
from mqtt_sub import advice, parse_temperature


def test_make_message_has_temperature_and_time():
    now = datetime.datetime(2026, 11, 25, 14, 3, 30)
    assert make_message(23, now) == {
        "Temperature": 23,
        "Time": "11/25 14:03:30",
    }


def test_published_payload_can_be_parsed_by_subscriber():
    payload = json.dumps(make_message(31)).encode("utf-8")
    assert parse_temperature(payload) == 31


def test_parse_plain_number_payload():
    assert parse_temperature(b"25") == 25
    assert parse_temperature(b"25.5") == 25.5


def test_parse_ignores_unexpected_payload():
    assert parse_temperature(b"hello") is None
    assert parse_temperature(b'{"Humidity": 60}') is None
    assert parse_temperature(b'{"Temperature": "hot"}') is None
    assert parse_temperature(b"true") is None
    assert parse_temperature(b"\xff\xfe") is None


def test_advice_when_hot():
    assert "開冷氣" in advice(30)
    assert advice(29) is None
