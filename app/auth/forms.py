from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()
 #Why do I have to add this to every class to not get an error across the pages/ keep the search bar on top across all pages?

 #Is there a way around having to add this to every class?
    cityName = StringField('cityName')

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

    cityName = StringField('cityName')

#Create a search form(destination/city)
#See pokemon search from github to implement 

class SearchCity(FlaskForm):
    cityName = StringField('cityName')
    submit = SubmitField()

    

#EXTRA
#Create a blog post form (see pokemon example)
# Need a username
# Text
# Picture?
# City ? 