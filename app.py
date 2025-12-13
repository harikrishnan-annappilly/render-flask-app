from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

now = datetime.now().astimezone().replace(microsecond=0)


@app.route("/")
def index():
    return render_template("index.html", app_start_time=now.strftime("%Y-%m-%d %H:%M:%S %Z %z"))


@app.route("/login")
def login():
    return render_template("user/login.html")


@app.route("/register")
def register():
    return render_template("user/register.html")


@app.route("/users")
def users():
    return render_template("user/users.html")


if __name__ == "__main__":
    app.run(debug=True)
