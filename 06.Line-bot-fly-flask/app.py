from flask import Flask, request, abort, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage, TextSendMessage, FlexSendMessage
)

# 使用自訂的模組(資料夾-檔案)
import my_moduls.hackmd_bot as hb

# 使用自訂的檔案-變數
from config import (CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET, LINE_USER_ID) 


app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# Messages on start and restart
line_bot_api.push_message(
    LINE_USER_ID, 
    TextSendMessage(text='Bot Starting')
    )

# Listen for all Post Requests from /callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=(TextMessage, ImageMessage))
def handle_message(event):
    """LINE MessageAPI message processing"""
    if event.source.user_id =='Udeadbeefdeadbeefdeadbeefdeadbeef':
        return 'OK'

    # 處裡圖片的方式: 上傳圖床、存HackMD暫存筆記
    if event.message.type=='image':
        image = line_bot_api.get_message_content(event.message.id)
        content = hb.flex_reply_image(image)
        message = FlexSendMessage(
            alt_text = "圖片已上傳至HackMD",
            contents = content
        )
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.type=='text':
        word =  str(event.message.text)

        # 測試API回傳內容
        if word[:5] == "@test":
            message = TextSendMessage(text=str(event))
            line_bot_api.reply_message(event.reply_token, message)
        
        # 無關鍵字則增至HackMD暫存筆記
        else: 
            content = hb.add_temp_note(word)
            message = TextSendMessage(text=content)
            line_bot_api.reply_message(event.reply_token, message)



########### API範例 ##############################



# 建立一個名為 `tasks` 的資料表，用來儲存待辦事項
tasks = [
    {
        'id': 0,
        'title': 'Python程式設計備課',
        'description': '撰寫 API DEMO',
        'done': False

    },
    {
        'id': 1,
        'title': 'Pytest',
        'description': '增加程式單元測試',
        'done': False
    }
]


@app.route('/', methods=['GET'])
def helloworld():
    return "<h1>Hello World</h1>"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [ task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/tasks', methods=['POST'])
def add_task():
    # 取得使用者傳送的待辦事項
    task = request.json
    new_id = max([t['id'] for t in tasks]) + 1 if tasks else 0
    task['id'] = new_id
    tasks.append(task)
    return jsonify({'tasks':tasks}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # 取得使用者傳送的更新資料
    task = request.json

    for index, t in enumerate(tasks):
        if t['id'] == task_id:
            tasks[index].update(task)
            tasks[index]['id'] = task_id
            return jsonify({'message': f'task_id: {task_id} updated'}), 200

    return jsonify({'message': 'task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for index, t in enumerate(tasks):
        if t['id'] == task_id:
            tasks.pop(index)
            return jsonify({'message': 'task deleted'}), 200

    return jsonify({'message': 'task not found'}), 404


#################################################

if __name__ == "__main__":
    app.run(port=5000, debug=True)