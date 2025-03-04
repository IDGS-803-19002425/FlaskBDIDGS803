from flask import Flask, render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import Forms 
from models import Alumnos
from models import db

app = Flask(__name__)

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csfr=CSRFProtect()

app.errorhandler(404)(lambda e: render_template('404.html'))
def page_not_found(e):
	return render_template('404.html'), 404



@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	csfr.init_app(app)
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
	
