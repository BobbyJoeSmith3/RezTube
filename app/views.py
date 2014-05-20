#=====================================
#views.py 
#=====================================

# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('3Divs2.html')

@app.route('/account')
@app.route('/account_page')
def account():
	return render_template('3Divs2Account.html')

@app.route('/profile')
@app.route('/profile_page')
def profile():
	return render_template('3Divs2Profile.html')