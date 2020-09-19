import click
from sqlalchemy_utils import create_database, database_exists, drop_database


def register(app):
    @app.cli.group()
    def manage_db():
        '''Commands that manage the databases'''
    
    @manage_db.command()
    @click.argument('reset-db')
    def reset_db():
        '''This command will delete and create database and tables'''
        db_url = app.config['SQLALCHEMY_DATABASE_URI']
        if database_exists(db_url):
            print('Deleting database')
            drop_database(db_url)
        else:
            print('Creating database')
            create_database(db_url)
        
        db = app.extensions.get('sqlalchemy').db
        db.create_all()

    @manage_db.command()
    @click.argument('create-admin')
    def create_admin():
        '''This command will create a super user'''
        #TODO: criar lógica para adicionar um usuário admin na aplicação
    



