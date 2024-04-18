from flask import Blueprint, request, render_template, flash, redirect, url_for
from werkzeug.utils import secure_filename

import app.service.service as service
import os

app = Blueprint("app", __name__)
UPLOAD_FOLDER = './app/files'

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('upload.html')

# @app.route('/upload', methods=['POST'])
# def upload_method():
#     file = request.files['file']
#     # If the user does not select a file, the browser submits an
#     # empty file without a filename.
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(request.url)
#     if file:
#         filename = secure_filename(file.filename)
#         # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         file.save(os.path.join(UPLOAD_FOLDER, filename))
#         # return redirect(url_for('download_file', name=filename))
#         return render_template('upload.html')
#     return "should be uploading files to service"

@app.route('/predict', methods=['POST'])
def predict_method():
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        service.predictYOLO(os.path.join(UPLOAD_FOLDER, filename))
        # return redirect(url_for('download_file', name=filename))
        return render_template('upload.html')
    
    return "should be predict files in the server"