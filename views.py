from flask import Blueprint, redirect, render_template, request, session, Flask
from auth import firebaseConfig
import pyrebase

app = Flask(__name__)

views = Blueprint(__name__, "views")
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app.secret_key = 'secret'

@views.route("/", methods={'GET','POST'})
def login():
    if('user' in session):
        return redirect("/home")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return redirect("/home")
        except:
            return 'Login failed'
    return render_template("index.html")

@views.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


@views.route("/register", methods={'GET','POST'})
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        auth.create_user_with_email_and_password(email, password)
        return redirect("/")
    return render_template("register.html")


@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/scheduler")
def scheduler():
    if request.method == 'POST':
        date = request.form.get('date')
        startTime = request.form.get('startTime')
        endTime = request.form.get('endTime')
    return render_template("scheduler.html")