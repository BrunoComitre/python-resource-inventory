import os
from app import create_app
from app import cli


app = create_app(os.getenv('SESC_CONFIG') or 'default')
# cli.reset_db(app)
cli.register(app)
