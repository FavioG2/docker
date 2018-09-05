from flask import Flask, jsonify, request
app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 }
 ]
 
@app.route("/api", methods=['GET'])
def hello():
    return jsonify({'emps':empDB})

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['producto']
    desc = request.form['descripcion']
    r.set(nombre, desc)
    return 'Ingresó el producto - ' + nombre + ': ' + desc

@app.route('/leer', methods=['POST'])
def leer():
    nombre = request.form['producto']
    return r.get(nombre)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
