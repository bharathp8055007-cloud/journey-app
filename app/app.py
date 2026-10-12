from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Journey app, version 1"

app.run(host="0.0.0.0", port=5000)

