from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
    )
from config import (
    CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET, LINE_USER_ID
    ) 
from my_moduls.openai_bot import OpenAIBot

# import os

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


chatgpt = OpenAIBot()

app = Flask(__name__)

# Messages on start and restart
line_bot_api.push_message(
    LINE_USER_ID, 
    TextSendMessage(text='OpenAI Bot Starting')
    )

@app.route("/")
def hello():
	return "Hello World from Flask in a uWSGI Nginx Docker container with \
	     Python 3.8 (from the example template)"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK' 

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Get user's message
    content = event.message.text
    chatgpt.add_msg(f"HUMAN:{content}?\n")
    reply_msg = chatgpt.get_response()
    message = TextSendMessage(text=reply_msg)
    line_bot_api.reply_message(event.reply_token, message)

# if __name__ == "__main__":
    # Only for debugging while developing
    # app.run(host="0.0.0.0", debug=True, port=80)