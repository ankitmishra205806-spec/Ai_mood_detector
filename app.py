from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from model import predict_mood

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    mood, suggestion = predict_mood(text)
    return jsonify({
        "mood": mood,
        "suggestion": suggestion
    })

if __name__ == "__main__":
    app.run(debug=True)