from flask import Flask, request, render_template
import redis
import sys

app = Flask(__name__)
r = redis.StrictRedis(host= 'redis', port=6379, db=0)
app.add_url_rule(app.static_url_path + '/<path:filename>',
                 endpoint='http://reverseproxy:8080',
                 view_func=app.send_static_file,
                 host='http://reverseproxy:8080')
app.url_map.host_matching = True

@app.route('/')
def index():
    ##print(app.static_url_path)
    return render_template('form.html')

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

