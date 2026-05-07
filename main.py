from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI 주식 웹앱 실행중 🚀"

if __name__ == "__main__":
    app.run(debug=True)