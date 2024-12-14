from flask import Flask
from router.Task import task
from utils.db import db

app = Flask(__name__)

app.secret_key = "sec_k"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(task)
