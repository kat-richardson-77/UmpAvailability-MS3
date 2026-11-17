from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Welcome to the Umpire Availability App</h1><p>This is the home page.</h1>"
    