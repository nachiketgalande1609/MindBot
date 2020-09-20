from chatbot import chatbot
from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    while True:
        userText = request.args.get('msg')
        if userText == "bye":
            return str("Bye. Have a good day!")
            break
        return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run()