from flask import Flask, render_template, request
import torch
from emotion_model import EmotionDetector

app = Flask(__name__)

model = EmotionDetector()
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/process_speech", methods = [POST])
def process_speech():
    user_speech = request.form["speech"]
    emotion = model.predict_emotion(user_speech)
    return f="The detected emotion is:{emotion}"



if __name__ == "__main__":
    app.run(debug = True)

