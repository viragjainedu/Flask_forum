from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField	 , BooleanField
from wtforms.validators import InputRequired , Email, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'virag'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/DELL/Desktop/Flask_forum/database.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(15), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

class SignUpForm(FlaskForm):
	email    = StringField('email' , validators=[InputRequired() , Email(message='Invalid Email'), Length(max=50) ])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def Home():
	form = SignUpForm()
	return render_template('Signup.html' , form=form)


@app.route('/Login'  , methods=['GET' , 'POST'])
def Login():
	form = LoginForm() 
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
			  	return redirect(url_for('Home'))
		return '<h1>Invalid username or password</h1>'
        
		#return '<h1>' + "USERNAME" + form.username.data + ' ' + " PASSWORD "+form.password.data + '</h1>'

	return render_template('Login.html' , form=form)

@app.route('/Signup'  , methods=['GET' , 'POST'])
def Signup():
	form = SignUpForm() 
	if form.validate_on_submit():
		new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
		db.session.add(new_user)
		db.session.commit()
		return '<h1> New user is created</h1>'
		#return '<h1>' + "USERNAME" + form.username.data + ' ' + " PASSWORD "+form.password.data + " Email "+form.email.data + '</h1>'

	return render_template('Signup.html' , form=form)

if __name__ == '__main__':
	app.run(debug=True)
