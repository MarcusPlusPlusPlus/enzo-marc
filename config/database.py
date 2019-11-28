from server import app
from flask_alchemy import SQLAlchemy

db = SQLAlchemy(app)