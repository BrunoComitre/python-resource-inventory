import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()
app = Flask(__name__)


def create_app(config_name):
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(db, app)

    # Create tables for our models
    db.create_all()

    return app


# @app.route('/')
# def testdb():
#     try:
#         q = db.session.query("1")
#         print(q)
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         print(e)
#         return '<h1>Something is broken.</h1>'

