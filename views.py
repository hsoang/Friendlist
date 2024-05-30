from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/login")
def home():
    return render_template("login.html")
 
@views.route("/register")
def profile():
    return render_template("register.html")