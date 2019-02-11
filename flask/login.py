from flask import Flask, session, render_template, redirect, request, escape, url_for

app = Flask(__name__)

app.secret_key = "jshdkfkdshfk"

@app.route("/")
def index():
    if 'username' in session:
        return "You are logged in as %s" %escape(session['username'])
    return "You are not logged in"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return '''
    <form method=post>
    <input type=text name=username>
    <input type=submit value=submit>
    </form>
    '''

@app.route("/logout")
def logout():
    session.pop('username' , None)
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run()