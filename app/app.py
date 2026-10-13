import os
from flask import Flask

app = Flask(__name__)
GREETING = os.environ.get("GREETING", "HELLO")
APP_ENV = os.environ.get("APP_ENV", "unkown")

@app.route("/")
def home():
    return f"{GREETING} from Journey app ({APP_env}), version 4"

app.run(host="0.0.0.0", port=5000)

