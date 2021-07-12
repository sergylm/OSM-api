import os
from flask import Flask, request, flash, redirect, url_for, Response
from flask.helpers import send_file
from flask.templating import render_template
from werkzeug.utils import secure_filename
import zipfile
import time

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return "In development"

@app.route("/prueba")
def prueba():
    return render_template('base.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    file = request.files.get('file')
    if file.filename == '':
        return 'Error not file', 400
    if file and allowed_file(file.filename):
        secfilename = secure_filename(file.filename)
        filename = secfilename.rsplit('.')[0]
        file.save('uploads/' + secfilename)
        return 'OK', 200
    return 'Format not valid', 400

@app.route('/download', methods=['GET'])
def download():
    return send_file('objects.zip', mimetype='zip', attachment_filename='objects.zip', as_attachment=True)

@app.route('/convert', methods=['POST'])
def osm2obj():
    files = os.listdir('uploads')
    for file in files:
        os.system('java -Xmx512m -jar OSM2World/OSM2World.jar -i {} -o {}'.format('uploads/' + file, 'downloads/' + file.rsplit('.')[0] + '.obj'))
    zip(os.listdir('downloads'))
    return 'Done'

def zip(path):
    with zipfile.ZipFile('objects.zip', 'w' , zipfile.ZIP_DEFLATED) as zf:
        for file in path:
           zf.write('downloads/' +  file, file) 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() == 'osm'
