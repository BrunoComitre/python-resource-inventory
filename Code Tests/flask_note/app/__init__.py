from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config


app = Flask(__name__)
db = MongoEngine()

def create_app():
    app.config.from_object(Config)

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/v1')
    
    db.init_app(app)

    return app


from . import models
