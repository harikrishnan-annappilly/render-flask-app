from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

now = datetime.now().astimezone().replace(microsecond=0)


@app.route("/")
def index():
    return render_template("index.html", app_start_time=now.strftime("%Y-%m-%d %H:%M:%S %Z %z"))


if __name__ == "__main__":
    app.run(debug=True)
