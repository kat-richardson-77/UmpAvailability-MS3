from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>Login Page</h1><p>This is the login page.</p>"

@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1><p>This is the logout page.</p>"

@auth.route('/sign-up')
def sign_up():
    return "<h1>Sign Up Page</h1><p>This is the sign up page.</p>"