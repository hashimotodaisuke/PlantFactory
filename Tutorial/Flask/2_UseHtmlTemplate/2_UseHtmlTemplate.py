from flask import Flask,render_template

#Flaskオブジェクトの生成
app = Flask(__name__)

#「/」へアクセスがあった場合に、"Go to /index"の文字列を返す
@app.route("/")
def hello():
    return "Go to /index"

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("index.html")

#おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

# 0.0.0.0はすべてのアクセスを受け付ける    
# サーバー自身のwebブラウザーには、「http://127.0.0.1:5000/」または「http://localhost:5000/」と入力
# 他pcのwebブラウザーには、「http://【サーバーのIPアドレス】:5000/」と入力
