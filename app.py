from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.config.from_object(Config)

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)

import models

with app.app_context():
    db.create_all()