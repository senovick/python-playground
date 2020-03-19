from flask import Flask, render_template, request
from send_email import send_email

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form["email"]
        height = request.form["height"]
        send_email(email, height)
    return render_template("success.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
