from flask import Blueprint
from app.controller.controller import app

api = Blueprint('api', __name__)

api.register_blueprint(app, url_prefix="/app")