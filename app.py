from flask import Flask, url_for, redirect, request
from flask import render_template

import requests
from requests.auth import HTTPBasicAuth



app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('welcome'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/results')
def results():
    return render_template('results.html')

#POST route NGP VAN

@app.route('/postvan')
def post_van():
	return 'Post to NGP VAN'

#GET route Volunteer Match

@app.route('/getvm')
def get_vm():
    return 'Getting from Volunteer Match'

if __name__ == "__main__":
	app.run()
