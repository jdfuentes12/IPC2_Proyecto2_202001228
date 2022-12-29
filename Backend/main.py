from flask import Flask,request
from flask.json import jsonify
from flask_cors import CORS
import json
from NodoUsuario import ListaUsuario
from NodoCancion import ListaCanciones

ListadoUsuarios = ListaUsuario()
ListadoCanciones = ListaCanciones()


app = Flask(__name__)
app.config['DEBUG'] = True

CORS(app)


@app.route('/')
def home():
    return 'Hello World'

@app.route('/login')
def login():
    json = request.get_json()
    user = json['user']
    password = json['password']
    usuraio = ListadoUsuarios.buscarUsuario(user,password)
    if usuraio == None:
        return jsonify({'status': 'error', 'message': 'Usuario no encontrado'})

@app.route('/consulta')
def consulta():
    pass

@app.route('/carga')
def carga():
    pass

if __name__ == '__main__':
    app.run(debug=True)