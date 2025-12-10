from flask import Flask
from datetime import datetime

app = Flask(__name__)

app_start_time = datetime.utcnow()


@app.route("/")
def index():
    return f"Welcome to My App {app_start_time}"


if __name__ == "__main__":
    app.run(debug=True)
