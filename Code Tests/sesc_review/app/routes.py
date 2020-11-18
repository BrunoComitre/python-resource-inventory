from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import database, Evaluator, User, Lunch, Spent, Service


@app.rout('/', methods=['GET'])
def create_userr():
    """Create a User."""
    username = request.args.get('user')
    last_review = request.args.get('last_review')
    # created = request.args.get('created')
    if username:
        new_user = User(username=username,
                        last_review=last_review,
                        created=dt.now(),
                        bio = "Thiss is Onlyh for Test",
                        admin = False)

        # Adds new User record to database
        database.session.add(new_user)
        # Commits all change
        database.session.commit()
    
    return make_response(f'[+]  ::{new_user} sucessfully created!')
