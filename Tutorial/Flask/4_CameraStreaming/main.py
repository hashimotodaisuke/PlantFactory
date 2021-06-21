# https://qiita.com/Gyutan/items/1f81afacc7cac0b07526
from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    # "/" を呼び出したときには、indexが表示される。

# Generatorとして働くためにgenとの関数名にしている
def gen(camera):
    while True:
        # frameはJPEG形式のバイナリデータ
        frame = camera.get_frame()
        # returnではなくジェネレーターのyieldで逐次出力。        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    # Content-Type（送り返すファイルの種類として）multipart/x-mixed-replace を利用。
    # multipart/x-mixed-replaceはHTTP応答によりサーバーが任意のタイミングで複数の文書を返し、
    # 紙芝居的にレンダリングを切り替えさせるもの。以下参照
    # https://wiki.suikawiki.org/n/multipart%2Fx-mixed-replace
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
