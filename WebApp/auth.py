from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "You have logged out"

@auth.route('/signup-club')
def signup_club():
    return render_template("signupclub.html")

@auth.route('/signup-umpire')
def signup_umpire():
    return render_template("signupumpire.html")