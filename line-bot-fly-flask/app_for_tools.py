from flask import Flask, request, abort, render_template

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
import my_moduls.my_functions as mf

from config import (
    CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET, LINE_USER_ID
) 

import os

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


# Messages on start and restart
line_bot_api.push_message(
    LINE_USER_ID, 
    TextSendMessage(text='Tools Bot Starting')
    )

@app.route('/')
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
        content = mf.translate_text(event.message.text[3:], "en")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@翻日":
        content = mf.translate_text(event.message.text[3:] , "ja")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@翻中":
        content = mf.translate_text(event.message.text[3:] , "zh-tw")
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@違法":
        content = mf.query_illegal_announcement(event.message.text[3:])
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text[:3] == "@職務":
        content = mf.search_jobbooks(event.message.text[3:])
        message = TextSendMessage(text=content)
        line_bot_api.reply_message(event.reply_token, message)
    else: line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

# if __name__ == "__main__":
#     app.run()