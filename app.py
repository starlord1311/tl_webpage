from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
damn

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	rollno = db.Column(db.Integer())
	email = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self, rollno,email, password):
		self.rollno = rollno
		self.email = email
		self.password = password

class Reason1(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roll_no = db.Column(db.Integer())

	def __init__(self,roll_no):
		self.roll_no=roll_no

class Reason2(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roll_no = db.Column(db.Integer())
	
	def __init__(self,roll_no):
		self.roll_no=roll_no

class Reason3(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roll_no = db.Column(db.Integer())
	
	def __init__(self,roll_no):
		self.roll_no=roll_no

class Other(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roll_no = db.Column(db.Integer())
	reason = db.Column(db.String(200))

	def __init__(self,roll_no,reason):
		self.roll_no= roll_no
		self.reason= reason
		

class register:

	def __init__(self):
		self.a=None
		self.b=None

one= register()

@app.route('/', methods=['GET', 'POST'])
def home():
	""" Session control"""
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		#if request.method == 'POST':
		#	username = getname(request.form['username'])
		#	return render_template('index.html', data=getfollowedby(username))
		return render_template('options.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	"""Login Form"""
	if request.method == 'GET':
		return render_template('login.html')
	else:
		one.a = request.form['rollno']
		one.b = request.form['password']
		try:
			data = User.query.filter_by(rollno=one.a, password=one.b).first()
			if data is not None:
				session['logged_in'] = True
				return redirect(url_for('home'))
			else:
				return 'Dont Login'
		except:
			return "Dont Login"

# class register:

# 	def __init__(self):
# 		self.a=None
# 		self.b=None



@app.route('/register/', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		a= request.form['rollno']
		b=request.form['email']
		c= User.query.filter_by(rollno=a, email = b).first()
		if c is not None:
			return 'Dont try'
		else:
			new_user = User(rollno=request.form['rollno'],email=request.form['email'], password=request.form['password'])
			db.session.add(new_user)
			db.session.commit()
			return render_template('login.html')
	return render_template('register.html')

@app.route('/reason/',methods=['GET','POST'])
def reason():
	if request.method=='POST':
		if request.form['submit'] == 'Option1':
			# d=User.query.filter_by(rollno=one.a).first()
			# e= d.id
			e=(one.a)
			new_user = Reason1(roll_no=e)
			db.session.add(new_user)
			db.session.commit()
			return 'thanks for using this' 

		if request.form['submit'] == 'Option2':
			# d=User.query.filter_by(rollno=one.a).first()
			# e= d.id
			e=(one.a)
			new_user = Reason2(roll_no=e)
			db.session.add(new_user)
			db.session.commit()
			return 'thanks for using this' 

		if request.form['submit'] == 'Option3':
			# d=User.query.filter_by(rollno=one.a).first()
			# e= d.id
			e=(one.a)
			new_user = Reason3(roll_no=e)
			db.session.add(new_user)
			db.session.commit()
			return 'thanks for using this' 

		if request.form['submit']=='other':
			return render_template('other.html')

@app.route('/other/',methods=['GET','POST'])
def other():
	if request.method=='POST':
		a = request.form['text']
		e=one.a
		new_user = Other(roll_no = e,reason=a)
		db.session.add(new_user)
		db.session.commit()
		return 'thanks for using this'


@app.route("/logout")
def logout():
	"""Logout Form"""
	session['logged_in'] = False
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.debug = True
	db.create_all()
	app.secret_key = "123"
	app.run(host='0.0.0.0')
