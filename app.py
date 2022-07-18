from flask import Flask, render_template, redirect, url_for
from wtf_formfields import *
from models import *

#configure app
app = Flask(__name__)
app.secret_key = 'replace later'
app.config['SQLALCHEMY_DATABASE_URI'] = 'C:///Users//admin//PycharmProjects//flaskProject//database.db'

@app.route('/' , methods = ['GET' , 'POST'])
def index():
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username , password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html" , form = reg_form)

@app.route("/login" , methods = ['GET' , 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return "000"
    return render_template("login.html" , form = login_form)


if __name__ == '__main__':
    app.run(debug=True)
