from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import logout_user, login_user, current_user, login_required
from werkzeug.security import check_password_hash

from .forms import SignUpForm, LoginForm
from..models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/login', methods=['GET', 'POST'])    
def loginPage():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
        # SELECT * FROM user WHERE username = <username variable>
            if user:
                if check_password_hash(user.password, password):  # <--NEW
                #user.password == password:  --OLD way
                    print('YAY, you\'re logged in!')
                    login_user(user)
                    print(current_user)
                    print(current_user.username)
                    return redirect(url_for('homePage'))
                    
                else:
                    print('WRONG password. . .')
            else:
                print('This isn\'t a user!')
            return redirect(url_for('auth.loginPage'))
    return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def registerPage():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)

            user = User(username, email, password)            
            user.saveUser()
            return redirect(url_for('auth.loginPage'))
        else: 
            render_template('register.html', form=form)
    return render_template('register.html', form=form)

@auth.route('/logout')
def logOut():
    logout_user()
    return redirect(url_for('homePage'))


#Create a Saved trips route once user is logged in 
#this can only be accessed by people that are logged in
#@login.required 
@auth.route('/myTrips')
@login_required
def myTrips():
    trips = current_user.trips.all()
    return render_template('myTrips.html', trips=trips)


#EXTRA
#Add blog route for "Social media" space 
#Users can post about where they've been or where they're going to connect with other solo travelers 
#They can only access if they're signed in
#Need template created for landing page (HTML)