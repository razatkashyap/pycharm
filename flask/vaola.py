from flask import Flask, request, render_template

app =Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello</h1>"

@app.route("/ging", methods = ["GET", "POST"])
def ging():
    return "valhalla : %s " % request.method

@app.route("/profile")
def lope():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("new.html", name = name)


if __name__ == "__main__":
    app.run()