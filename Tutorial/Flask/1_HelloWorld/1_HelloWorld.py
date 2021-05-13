from flask import Flask

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/")
def hello():
    return "Hello World"

#おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

# 0.0.0.0はすべてのアクセスを受け付ける    
# サーバー自身のwebブラウザーには、「http://127.0.0.1:5000/」または「http://localhost:5000/」と入力
# 他pcのwebブラウザーには、「http://【サーバーのIPアドレス】:5000/」と入力
