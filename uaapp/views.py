from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/homepage')
def homepage():
    return render_template("homepage.html")

@views.route('/view-matches')
def viewmatch():
    return render_template("viewmatch.html")