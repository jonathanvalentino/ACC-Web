from flask import Flask, render_template, redirect, flash, session, request
from flask_session import Session
from datetime import datetime, date

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
    if session.get("name"):
        return redirect("/")
    if request.method == "POST":
        if(request.form.get("name") == ''):
            flash('Please insert correct username!','warning')
            return redirect(request.url)
        elif(request.form.get("password") == ''):
            flash('Please insert your password!','warning')
            return redirect(request.url)
        session["name"] = request.form.get("name")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        session["datetime"] = dt_string
        session["date"] = date.today().strftime("%d %B, %Y")
        return redirect("/")
    return render_template('login.html')

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route('/cPassword', methods=['GET','POST'])
def cPassword():
    type = request.args.get("type")
    if(type == 'ubahsandi'):
        return render_template('lupa-password.html', type = 'Change Password')
    else:
        return render_template('lupa-password.html', type = 'Forget Password')
    

@app.route('/company', methods=['GET','POST'])
def help():
    return render_template('company.html')

@app.route('/setting', methods=['GET','POST'])
def setting():
    return render_template('setting.html')

@app.route('/transaction', methods=['GET','POST'])
def transaction():
    return render_template('transaction.html')

@app.route('/help', methods=['GET','POST'])
def bantuan():
    return render_template('help.html')

@app.route('/report', methods=['GET','POST'])
def report():
    return render_template('report.html')

@app.route('/summary', methods=['GET','POST'])
def summary():
    return render_template('summary.html')

@app.route('/pph', methods=['GET','POST'])
def pph():
    return render_template('pendapatanpenjualanharian.html')
@app.route('/undercon', methods=['GET','POST'])
def undercon():
    return render_template('undercon.html')

if __name__ == '__main__':
    app.run(debug=False)
