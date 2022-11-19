# Store this code in 'app.py' file

# Store this code in 'app.py' file
'''from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

import mysql.connector
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lokesh@2005",
    database = "userlogin"
)
 


app = Flask(__name__)


app.secret_key = 'london'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lokesh@2005'
app.config['MYSQL_DB'] = 'userlogin'

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		#cursor = mysql.connection.cursor()
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('mainpage.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))#change{}
	#return render_template('login.html', msg = msg)

@app.route('/')
@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		print(username)
		cursor = mysql.connection.cursor()
		#cursor = mydb.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s;', (username, ))
		#cursor.execute('SELECT * FROM accounts')
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s);', (username, password, email, ))
			mysql.connection.commit()
			cursor.close()
			msg = 'You have successfully registered !'
			return render_template('login.html', msg = msg)
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

@app.route('/')
@app.route('/mainpage', methods =['GET', 'POST'])
def mainpage():
	msg=''
	return render_template('mainpage.html', msg = msg)

if __name__ == "__main__":
    app.run(debug = True)'''


#trying after deployment
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

import flask
from flask import request,render_template
from flask_cors import CORS
import numpy as np
import pandas as pd
import requests

import mysql.connector
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Lokesh@2005",
    database = "userlogin"
)
 


app = Flask(__name__)


app.secret_key = 'london'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lokesh@2005'
app.config['MYSQL_DB'] = 'userlogin'

mysql = MySQL(app)
CORS(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		#cursor = mysql.connection.cursor()
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			#session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('mainpage.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))#change{}
	#return render_template('login.html', msg = msg)

@app.route('/')
@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		print(username)
		cursor = mysql.connection.cursor()
		#cursor = mydb.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s;', (username, ))
		#cursor.execute('SELECT * FROM accounts')
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s);', (username, password, email, ))
			mysql.connection.commit()
			cursor.close()
			msg = 'You have successfully registered !'
			return render_template('login.html', msg = msg)
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

@app.route('/')
@app.route('/mainpage', methods =['GET', 'POST'])
def mainpage():
	msg=''
	return render_template('mainpage.html', msg = msg)

API_KEY = "2AjKeBOMtc_4WMPYUQe2GI-opbRdU3E0q7VEZkBiPUkA"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

@app.route('/')
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fname = float (request.form['fname'])
    month = float (request.form['month'])
    daymonth = float (request.form['daymonth'])
    dayweek = float (request.form['dayweek'])
    origin = request.form['origin']
    if origin == "msp":
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if origin == "dtw":
        origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if origin == "jfk":
        origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if origin == "sea":
        origin1,origin2,origin3,origin4,origin5 = 0,1,0,0,0
    if origin == "alt":
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0

    destination = request.form['destination']
    if destination == "msp":
        destination1,destination2,destination3,destination4,destination5 = 0,0,0,0,1
    if destination == "dtw":
        destination1,destination2,destination3,destination4,destination5 = 1,0,0,0,0
    if destination == "jfk":
        destination1,destination2,destination3,destination4,destination5 = 0,0,1,0,0
    if destination == "sea":
        destination1,destination2,destination3,destination4,destination5 = 0,1,0,0,0
    if destination == "alt":
        destination1,destination2,destination3,destination4,destination5 = 0,0,0,1,0

    sarrivaltime = float (request.form['sarrivaltime'])
    sdeparttime = float (request.form['sdeparttime'])
    adeparttime = float (request.form['adeparttime'])
    dept15=int(sdeparttime)-int(adeparttime)

    X = [[fname, month, daymonth, dayweek, sarrivaltime, dept15, origin1, origin2, origin3, origin4, origin5, destination1, destination2, destination3, destination4, destination5]]

    payload_scoring = {"input_data": [{"field": [["FL_NUM", "MONTH", "DAY_OF_MONTH", "DAY_OF_WEEK", "CRS_ARR_TIME", "DEP_DEL15", "ORIGIN_0", "ORIGIN_1", "ORIGIN_2", "ORIGIN_3", "ORIGIN_4", "DEST_0", "DEST_1", "DEST_2", "DEST_3", "DEST_4"]], "values": X}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/70ba7f52-fcd7-4553-bc8b-afbc37d1a0be/predictions?version=2022-11-18', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    predictions = response_scoring.json()

    pred = predictions['predictions'][0]['values'][0][0]

    if pred == 0:
        ans = "The flight will be on time"
    else :
        ans = "The flight will be delayed"

    return render_template("mainpage.html",predict = ans)

if __name__ == '__main__':
    app.debug = True
    app.run()

if __name__ == "__main__":
    app.run(debug = True)