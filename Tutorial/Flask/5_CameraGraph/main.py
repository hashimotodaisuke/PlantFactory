import os
import json
import datetime
import random
import time
import base64
from camera import VideoCamera
from gevent import pywsgi
# WSGI（ウィズキー）はwebサーバーとpythonアプリを接続するためのインターフェース
from geventwebsocket.handler import WebSocketHandler
from flask import Flask 
from flask import request
from flask import render_template
from flask import Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publish')
def publish():
    # request.environはWSGIに従ったリクエスト情報。以下のようなデータを含む
    # 'wsgi.url_scheme': 'http',
    # 'SERVER_NAME': 'localhost',
    # 'PATH_INFO': '/',
    # 'SERVER_PORT': '5000',
    # 'REQUEST_METHOD': 'GET' 
    if request.environ.get('wsgi.websocket'):        
        # environ['wsgi.websocket'] から WebSocket オブジェクトが得られる（セッションが取れる）
        ws = request.environ['wsgi.websocket']
        videocamera = VideoCamera()
        old_jpeg = 0
        while True:
            # 画像取得
            jpeg = videocamera.get_frame()
            if jpeg is None:
                jpeg = old_jpeg
                print("video read error")
            else:
                old_jpeg = jpeg
            # 温湿度取得
            tempature = random.random() * 100
            humidity = random.random() * 100               

            # 画像を送信可能な形式に変換してJSONに格納
            image_data = "data:image/jpeg;base64,"+base64.b64encode(jpeg).decode('utf-8')
                                
            # 時間取得
            t = int(time.mktime(datetime.datetime.now().timetuple()))
            
            # websocketにはsend、recieveがある。html側で送信していないのでrecive処理はしない
            # message = ws.receive()
            # print(message)
            # json.dumpsでデータをJSON形式にエンコードしてsendで送信。
            ws.send(json.dumps([{"time": t, "y": tempature},
                                {"time": t, "y": humidity},
                                {'image': image_data}]))                                
            # time.sleep(1)
    return

if __name__ == '__main__':
    app.debug = True
    app.thread = True
    # WebSocketHandler が environ['wsgi.websocket'] をセットする
    server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
