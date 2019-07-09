from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField	 , BooleanField
from wtforms.validators import InputRequired , Email, Length

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'virag'

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

class SignUpForm(FlaskForm):
	email    = StringField('email' , validators=[InputRequired() , Length(max=50) , Email(message='Invalid Email') ])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/Home')
def Home():
	return render_template('Home.html')

@app.route('/')
def Login():
	form = LoginForm() 

	return render_template('Login.html' , form=form)

@app.route('/Signup')
def Signup():
	form = SignupForm() 


	return render_template('Signup.html' , form=form)

if __name__ == '__main__':
	app.run(debug=True)
