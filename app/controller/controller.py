from flask import Blueprint

import app.service.service as service

app = Blueprint("app", __name__)

@app.route('/', methods=['GET'])
def landing_page():
    return "should be landing page"

# @app.route('/upload', methods=['POST'])
# def upload_method():
#     return "should be uploading files to service"

@app.route('/predict', methods=['POST'])
def predict_method():
    return "should be predict files in the server"