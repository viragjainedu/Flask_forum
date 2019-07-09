from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def Home():
	return render_template('Home.html')

@app.route('/Login')
def Loginx():
	return render_template('Login.html')

@app.route('/Signup')
def Signup():
	return render_template('Signup.html')

if __name__ == '__main__':
	app.run(debug=True)
