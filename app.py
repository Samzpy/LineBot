from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from crawler import crawler

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('VQ2biZsApj+nlTxtEzBX0uENB8qFs3QmOE9X1h8FvR01Xt/CVKBgzXeh+ZwA4Jb70FCIz9vUBILBidGkbLxLrvBJmF/CKf8dysaDG5xDVziS5Tpit/H9SXizpXG9PXFyT1AZnxdl16bWv+wbqDybvAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('49d6840b0b6bf7b241d4a45afecef791')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    if event.message.text[0] == '0'
        if "資訊" == event.message.text:
            DcardCrawler=crawler()
            result= DcardCrawler.information
        else:
            DcardCrawler=crawler()
            result=DcardCrawler.crawl_specific_forum(event.message.text)
        message = TextSendMessage(text=result)
        line_bot_api.reply_message(event.reply_token, message)
    else:
        

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
