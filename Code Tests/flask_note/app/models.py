import datetime
from uuid import uuid4

from app import db
from flask_mongoengine.wtf import model_form


class Note(db.Document):
    content = db.StringField(required=True, max_length=140)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

    def __repr__(self):
        return self.content


NoteForm = model_form(Note)
