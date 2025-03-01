from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
app.config['SQLACLCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
