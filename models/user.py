import config.database as DB

class User(DB.db.Models):
    id = DB.db.Column(DB.db.Integer, primary_key=True)
    username = DB.db.Column(DB.db.String(80), unique=True, nullable=False)
    email = DB.db.Column(DB.db.String(120), unique=True, nullable=False)