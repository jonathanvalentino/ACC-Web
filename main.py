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
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)