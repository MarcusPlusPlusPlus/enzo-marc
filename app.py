from flask import request, render_template, redirect, url_for
import config.server as SERVER


app = SERVER.app

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
