from flask import Flask, url_for, redirect, request
from flask import render_template

import os
from werkzeug.utils import secure_filename
from flask import send_from_directory


import requests
from requests.auth import HTTPBasicAuth

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'csv', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
            return redirect(url_for('index') )

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
	def post_van():
	print("Here we go")
	url = 'https://api.securevan.com/v4/echoes'
	username = 'demo.usersite.api'
	password = 'apikeyhere|1'
	payload = {'message':'Hello, World'}
	headers = {'content-type': 'application/json', 'accepts': 'application/json'}
	r = requests.post(url,
	 auth=HTTPBasicAuth(username, password),
	 json=payload, headers=headers)
	return 'Post to NGP VAN'

#GET route Volunteer Match

@app.route('/getvm')
def get_vm():
    return 'Getting from Volunteer Match'

if __name__ == "__main__":
	app.run()
