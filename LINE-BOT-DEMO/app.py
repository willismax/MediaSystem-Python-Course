from flask import Flask, request, abort, jsonify, render_template

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from job_functions import (
    translate_text, query_illegal_announcement, search_jobbooks
)

import os


app = Flask(__name__)

# os.environ['放在Github的secrets']  
# CHANNEL_ACCESS_TOKEN = os.environ['CHANNEL_ACCESS_TOKEN']
# CHANNEL_SECRET = os.environ['CHANNEL_SECRET']

# use config.py file (Dev local only)
# from config import *

# Use Heroku Config Vars
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN', 'Optional default value')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET', 'Optional default value')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/callback", methods=['POST'])
def callback():
    """LINE MessageAPI連線"""
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """LINE MessageAPI訊息處理"""
    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
        return 'OK'
    if event.message.text[:3] == "@翻英":
        content = translate_text(event.message.text[3:], "en")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@翻日":
        content = translate_text(event.message.text[3:] , "ja")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@翻中":
        content = translate_text(event.message.text[3:] , "zh-tw")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@違法":
        content = query_illegal_announcement(event.message.text[3:])
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@職務":
        content = search_jobbooks(event.message.text[3:])
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    else: line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()