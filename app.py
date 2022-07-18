from flask import Flask, render_template, redirect, url_for
from wtf_formfields import *
from models import *


#configure app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C://Users//admin//PycharmProjects//flaskProject//database.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/' , methods = ['GET' , 'POST'])
def index():
    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        hashed_pswd = pbkdf2_sha512.hash(password)

        user = User(username=username , password=hashed_pswd)
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
