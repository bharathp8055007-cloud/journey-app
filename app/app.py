import os
from flask import Flask

app = Flask(__name__)
GREETING = os.environ.get("GREETING", "HELLO")

@app.route("/")
def home():
    return f"{GREETING} from Journey app, version 3"

app.run(host="0.0.0.0", port=5000)

