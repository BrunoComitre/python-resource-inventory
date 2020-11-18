from app import app, routes, models
import os


if __name__ == '__main__':
    os.environ['MONGO_HOST'] = '127.0.0.1'
    app.run(debug=True)
