from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'marcusplusplus.mysql.pythonanywhere-services.com:3306/marcusplusplus$enzo-marc.db'
#~~#
db = SQLAlchemy(app)
db.create_all()

@app.route('/')
def home():
    return 'Bienvenue !'

# @app.route('/gaz', methods=['GET','POST'])
# def save_gazouille():
# 	if request.method == 'POST':
# 		return redirect(url_for('timeline'))
# 	if request.method == 'GET':
# 		return render_template('formulaire.html')

# @app.route('/timeline', methods=['GET'])
# def timeline():
# 	return render_template("timeline.html")
