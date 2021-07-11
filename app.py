import os
from flask import Flask, request, flash, redirect, url_for
from flask.templating import render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return "In development"

@app.route("/prueba")
def prueba():
    return render_template('base.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    file = request.files.get('file')
    if file.filename == '':
        return 'Error not file', 400
    if file and allowed_file(file.filename):
        secfilename = secure_filename(file.filename)
        filename = secfilename.rsplit('.')[0]
        file.save(secfilename)
        os.system('java -Xmx512m -jar OSM2World/OSM2World.jar -i {} -o {}'.format(secfilename, filename + '.obj'))
        return 'OK', 200
    return 'Format not valid', 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() == 'osm'
