from flask import Flask, render_template, redirect, url_for , flash
from wtf_formfields import *
from models import *
from flask_login import LoginManager, login_user,current_user,UserMixin , login_required , logout_user
#configure app



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C://Users//admin//PycharmProjects//flaskProject//database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

login = LoginManager(app)
login.init_app(app)

@login.user_loader()
def load_user(id):

    return User.query.get(int(id))

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
        flash("Registration is successfully", 'success')

        return redirect(url_for('login'))

    return render_template("index.html" , form = reg_form)

@app.route("/login" , methods = ['GET' , 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username = login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))
    return render_template("login.html" , form = login_form)

@app.route("/chat" , methods = ['get' , 'post'])
@login_required
def chat():
    if not current_user.is_authenticated:
        flash("Please login" , 'danger')
        return redirect(url_for('login'))
    return "chat start"

@app.route("/logout" , methods = ['get'])
def logout():
    logout_user()
    flash('You have logged out' , 'success')
    return  redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
