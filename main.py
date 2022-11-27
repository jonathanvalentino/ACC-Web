from flask import Flask, render_template, redirect, flash, session, request
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET','POST'])
def index():
    if not session.get("name"):
        return redirect("/login")
    name = session["name"]
    return render_template('home.html', username = name)

@app.route('/login', methods=['GET','POST'])
def login():
    if session.get("name"):
        return redirect("/")
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template('login.html')

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route('/cPassword', methods=['GET','POST'])
def cPassword():
    name = session["name"]
    return render_template('lupa-password.html', username = name)

@app.route('/company', methods=['GET','POST'])
def help():
    name = session["name"]
    return render_template('company.html', username = name)

@app.route('/setting', methods=['GET','POST'])
def setting():
    name = session["name"]
    return render_template('setting.html', username = name)

@app.route('/transaction', methods=['GET','POST'])
def transaction():
    name = session["name"]
    return render_template('transaction.html', username = name)

@app.route('/help', methods=['GET','POST'])
def bantuan():
    name = session["name"]
    return render_template('help.html', username = name)

@app.route('/report', methods=['GET','POST'])
def report():
    name = session["name"]
    return render_template('report.html', username = name)

if __name__ == '__main__':
    app.run(debug=True)