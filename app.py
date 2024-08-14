from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"

@app.route('/contacto')
def contacto():
    return "<h3>Intruciendo HTML desde el serverr</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNamemascota')
    razaMascota = request.form.get('txtRaza')
    return f"Ya llego tu mascota {nombreMascota}, la raza es {razaMascota} al server"

# se pregunta por el proceso principalla
if __name__=='__main__':
    app.run(debug=True)