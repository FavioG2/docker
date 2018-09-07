from flask import Flask, jsonify, request
import redis
from flask_cors import CORS
app = Flask(__name__)
r = redis.StrictRedis(host= 'redis', port=6379, db=0)
cors = CORS(app, resorces={r'/*': {"origins": '*'}})

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
    content = request.json
    nombre = content['nombre']
    desc = content['desc']
    print(nombre)
    r.set(nombre, desc)
    return 'Usuario: ' + nombre + ", comentario: " + desc

@app.route('/leer', methods=['POST'])
def leer():
    content = request.json
    nombre = content['nombre']
    return r.get(nombre)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
