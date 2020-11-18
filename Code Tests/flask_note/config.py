import os
from dotenv import load_dotenv
from pymongo import MongoClient


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


client = MongoClient('mongodb://mongodb:27017')
database = client.notes
collection = database['notes']
