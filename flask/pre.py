from flask import Flask, render_template, url_for, session, escape, request, redirect, flash


app = Flask(__name__)

app.secret_key = "kjhhhoi]kd"

@app.route('/')
def index():
    login = " <a href='/login'>Log in</a>"
    if 'username' in session:
        logout = " <a href='/logout'>Log out</a>"
        return "You are logged in as %s %s " % (escape(session['username']),  logout)
    return "You are not logged in %s " % login


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    #flash("You are logged out")
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"), 404

if __name__=="__main__":
    app.run()