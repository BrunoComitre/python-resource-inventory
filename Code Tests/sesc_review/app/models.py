from . import database
from datetime import datetime


class Evaluator(db.Model):
    """Model for Evaluator."""
    __tablename__ = 'login'
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    evaluation = database.relationship('Lunch', backref='evaluator', lazy=True)
    users = database.relationship('User', backref='evaluator', lazy='dynamic')

    def __repr__(self):
        return '<Evaluator %r>' % self.username

class User(db.Model):
    """Model for User Relationship."""
    __tablename__ = 'user'
    id = database.Column(database.Integer, primary_key=True)
    user = database.Column(database.String(64), unique=True, index=True)
    last_review = database.Column(database.DateTime(), default=datetime.utcnow)
    created = database.Column(database.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user


class Lunch(db.Model):
    """Model for Luch Time."""
    id = database.Column(database.Integer, primary_key=True)
    food_description = database.Column(database.Text(200), database.ForeignKey('spent.id'))
    quality_food = database.Column(database.Integer)
    date = database.Column(database.Datetime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Lunch %r>' % self.food_description


class Spent(db.Model):
    """Model for Money Cost."""
    id = database.Column(database.Integer, primary_key=True)
    total_spent_during_lunch = database.Column(database.Float)
    addresses = database.relationship('Lunch', backref='food_description', lazy=True)

    def __repr__(self):
        return '<Spent %r>' % self.total_spent_during_lunch


class Service(db.Model):
    """Model for Service Avaiable."""
    id = database.Column(database.Integer, primary_key=True)
    service = database.Column(database.Integer)
    waiting_time = database.Column(database.Float)
    queue_time = database.Column(database.Integer)
    cashier_queue_size = database.Column(database.Integer)
    queue_time_and_payment_service = database.Column(database.Integer)

    def __repr__(self):
        return '<Service %r>' % self.service
