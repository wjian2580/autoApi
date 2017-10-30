#!/usr/bin/python
# coding=utf-8
from flask import Flask,request,jsonify,session
app = Flask(__name__)
app.secret_key = 'Passw0rd'

USERNAME = 'admin'
PASSWORD = '123456'

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != USERNAME:
			error = 'invalid username'
		elif request.form['password'] != PASSWORD:
			error = 'invalid password'
		else:
			session['logged_in'] = True
			return jsonify({'code':'200','msg':'success'})
	return jsonify({'code':'401','msg':error})

@app.route('/info',methods=['GET'])
def info():
	if not session['logged_in']:
		return jsonify({'code':'401','msg':'please login!'})
	return jsonify({'code':'200','msg':'success','data':'info'})

if __name__ == '__main__':
	app.run(port=5001,debug=True)
