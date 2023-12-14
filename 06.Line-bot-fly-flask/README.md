# 使用 GitHub Codespaces 建立 Python LINEBOT 教學

在這個教學中，我們將學習如何使用 Python 建立 LINEBOT。我們將使用 Flask 這個流行的網頁框架來處理 HTTP 請求和回應。

## 前置作業

在開始之前，請確保您擁有以下工具：

- 安裝在您的機器上的 Python
- LINE 開發者帳戶

## 步驟 1：設定專案

1. 在 GitHub 上建立一個新的專案。

2. 在 Codespaces 中打開您的專案。

3. 在 Codespaces 中建立一個名為 `app.py` 的新檔案並在其中撰寫程式碼。

## 步驟 2：設定 LINE Messaging API

1. 前往 [LINE 開發者控制台](https://developers.line.biz/console/)，並為您的機器人建立一個新的頻道。

2. 在頻道設定中，前往「Messaging API」標籤並啟用「使用 Webhooks」選項。

3. 將 Webhook URL 設定為您的 Codespaces HTTPS URL（例如 `https://your-codespaces-url/callback`）。

4. 生成一個頻道存取權杖並複製它。

5. 在您的 `app.py` 檔案中，新增以下程式碼以設定 LINE Messaging API：
   ```python
   from flask import Flask, request, abort
   from linebot import LineBotApi, WebhookHandler
   from linebot.exceptions import InvalidSignatureError
   from linebot.models import MessageEvent, TextMessage, TextSendMessage

   app = Flask(__name__)
   line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
   handler = WebhookHandler('YOUR_CHANNEL_SECRET')

   @app.route("/callback", methods=['POST'])
   def callback():
     signature = request.headers['X-Line-Signature']
     body = request.get_data(as_text=True)
     try:
       handler.handle(body, signature)
     except InvalidSignatureError:
       abort(400)
     return 'OK'

   @handler.add(MessageEvent, message=TextMessage)
   def handle_message(event):
     line_bot_api.reply_message(
       event.reply_token,
       TextSendMessage(text=event.message.text)
     )

   if __name__ == "__main__":
     app.run()
   ```

## 步驟 3：測試機器人

1. 在 Codespaces 中執行您的 `app.py` 檔案。

2. 將您的機器人添加為 LINE 的好友並發送一條訊息。您應該會收到相同的訊息作為回覆。

恭喜！您已成功使用 Python 和 Flask 建立了一個 LINEBOT。您現在可以根據需求自定義機器人的行為並添加更多功能。

祝您編碼愉快！
