from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<string:name>")
def session(name):
	return  render_template("session.html", name= name)

@app.route("/hello", methods=["POST"])
def login():
	name = request.form.get("nombre")
	lastname = request.form.get("apellido")
	date = request.form.get("fecha")
	email = request.form.get("correo")
	return  render_template("session.html", name = name, lastname = lastname, date = date, email= email )

#@app.route("/data", methods=["POST"])
#def data():
	#email = request.form.get("correo")
	#return render_template("data.html", email= email )

@app.route("/users")
def users():
	#Query a DB for users
	users_list = ["Mayita", "Nataly", "WJ", "Olis"]
	return render_template("list.html", users=users_list)

