from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)

URL = "mysql+mysqlconnector://{}:{}@{}/{}".format(*(
    "SQL_USERNAME",
    "SQL_PASSWORD",
    "SQL_HOSTNAME:SQL_PORT",
    "SQL_DATABASE"
))
APP.config['SQLALCHEMY_DATABASE_URI'] = URL
DB = SQLAlchemy(APP)

class Tweet(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(80), unique=False, nullable=False)
    text = DB.Column(DB.String(255), unique=False, nullable=False)
DB.create_all()

@APP.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'max-age=300'
    response.headers['Access-control-Allow-Origin'] = [
        "http://marcusplusplus.pythonanywhere.com/",
        "195.154.176.62"
    ]
    return response
#~ ROUTES ~#

@APP.route('/')
def home():
    return 'Bienvenue !'

@APP.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    if request.method == 'POST':
        data = request.form.to_dict()
        keys = data.keys()
        if "user-name" in keys and "user-text" in keys and len(data["user-text"]) <= 280:
            DB.session.add(Tweet(name=data["user-name"].replace("barre", ""), text=data["user-text"].replace("barre", "")))
            DB.session.commit()
        return redirect(url_for("timeline"))
    if request.method == 'GET':
        return render_template('formulaire.html')


@APP.route('/timeline/')
@APP.route('/timeline/<string:username>')
def timeline(username=None):
    query_tweets = Tweet.query.filter_by(name=username).all() if username else Tweet.query.all()
    list_of_tweets = [{"user": tweet.name, "text": tweet.text} for tweet in query_tweets]
    return render_template("timeline.html", gaz=list_of_tweets)
