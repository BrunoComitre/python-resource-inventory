from flask import Flask, Blueprint
# from config import client


# database = client
# collection = database.notes.notes


developers = Blueprint('notes', __name__)

app = Flask(__name__)
app.register_blueprint(developers)


from app import routes, models
