import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = os.environ.get("DB_USER") or 'pmozzCzgfXevRyGSfgRqCSgstYLdoagx'
    DB_PASSWORD = os.environ.get("DB_PASSWORD") or '6wI1yVQlSC1n97ZapCSLeCXO1GlaWcRYTdoIPYhtgx8ctGkuvNKD435volffJtOg'
    DB_NAME = os.environ.get('DB_NAME') or 'sesc'
    DB_PORT = os.environ.get('DB_PORT') or 5432

class LocalDevelopment(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] or 'postgresql:///wordcount_dev'
    DB_HOST = os.environ.get("DB_HOST") or 'localhost'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}'

class RemoteDevelopment(Config):
    DB_HOST = os.environ.get("DB_HOST") or '10.0.200.127'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}'

class ProductionDevelopment(Config):
    if os.getenv('SECRET_KEY') == 'hard to guess':
        raise EnvironmentError('need real secret key')


config = {
    'local': LocalDevelopment,
    'remote': RemoteDevelopment,
    'production': ProductionDevelopment,
    'default': LocalDevelopment,
}
