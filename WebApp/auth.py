from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "You have logged out"

@auth.route('/signup-club', methods=['GET', 'POST'])
def signup_club():
    if request.method == 'POST':
        enid = request.form.get('enid')
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        club_name = request.form.get('club_name')
        area = request.form.get('area')
        city = request.form.get('city')

        if len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(surname) < 2:
            flash('Surname must be greater than 1 character.', category='error')
        elif len(club_name) < 2:
            flash('Club name must be greater than 1 character.', category='error')
        elif len(area) < 2:
            flash('Area must be greater than 1 character.', category='error')
        elif len(city) < 2:
            flash('City must be greater than 1 character.', category='error')
        else:
            flash('Your account has been created successfully!', category='success')

    return render_template("signupclub.html")

@auth.route('/signup-umpire', methods=['GET', 'POST'])
def signup_umpire():
    if request.method == 'POST':
        enid = request.form.get('enid')
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        award = request.form.get('award')
        area = request.form.get('area')
        city = request.form.get('city')
    return render_template("signupumpire.html")