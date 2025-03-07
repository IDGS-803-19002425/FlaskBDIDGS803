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

app.errorhandler(404)(404)
def page_not_found(e):
	return render_template('404.html'), 404





@app.route("/")
@app.route("/index")
def index():
	create_form=Forms.UserForm2(request.form)
	alumno = Alumnos.query.all() #Select * from alumnos
	return render_template("index.html",create_form=create_form,alumno=alumno)

@app.route("/detalles",methods=["GET","POST"])
def detalles():
	create_form=Forms.UserForm2(request.form)
	if request.method=="GET":
		id=request.args.get("id") #Select * from alumnos where id=id
		alumn1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
		id= request.args.get("id")
		nombre=alumn1.nombre
		apaterno = alumn1.apaterno
		email = alumn1.email
		return render_template("detalles.html",nombre=nombre,apaterno=apaterno,email=email)
	
@app.route("/Alumnos1",methods=["GET","POST"])
def Alumnos1():
	create_form=Forms.UserForm(request.form)
	if request.method == "POST":
		alum=Alumnos(nombre=create_form.nombre.data),
		apaterno=create_form.apaterno.data,
		email=create_form.email.data #insert alumnos() values()
		db.session.add(alum)	
		db.session.commit()
		return redirect(url_for("index"))
	return render_template('Alumnos1.html',form=create_form)




if __name__ == '__main__':
	csfr.init_app(app)
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
	
