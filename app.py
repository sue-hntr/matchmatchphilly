from flask import Flask, url_for, redirect, request
from flask import render_template

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

#POST route NGP VAN

@app.route('/postvan')
def post_van():
    return render_template('welcome.html')

#GET route Volunteer Match

@app.route('/getvm')
def get_vm():
    return render_template('getvm.html')
