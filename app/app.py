from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
	#return "hola mundo"
	data={'titulo':'Pagina Principal',
		   'encabezado':'Pagina de Prueba y practica en flask'}
	return render_template("index.html",datos=data)
def hola_mundo():
	return "saludo al mundo"


if __name__=="__main__":
	app.add_url_rule("/saludo/",view_func=hola_mundo)
	app.run(debug=True)