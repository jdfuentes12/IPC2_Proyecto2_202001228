from flask import Flask,request
from flask.json import jsonify
from flask_cors import CORS
import json
import xml
import webbrowser as wb
from xml.etree import ElementTree as ET




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
    
    #f usuraio == None:
    #   return jsonify({'status': 'error', 'message': 'Usuario no encontrado'})
    return jsonify({'status': 'ok', 'message': 'Usuario encontrado'})

@app.route('/consulta')
def consulta():
    pass

@app.route('/carga', methods=['POST'])
def carga():
    
    ruta = request.get_data()
    tree = ET.fromstring(ruta)
    
    listaGeneral = {"listaClientes":None, "listaPlaylist": None, "listaEmpresas": None}
    
    
    listaPlaylist = []
    listaCanciones = []
    validar = False

    listaClientes = []
    listaPlay = []
    
    listaEmpresas = []
    
    for dato in tree:
        if dato.tag == 'playlistClientes':
            for playlist in dato:
                id = playlist.attrib.get('id')
                for datosC in playlist:
                    if datosC.tag == 'nitCliente':
                        nit = datosC.text
                    if datosC.tag == 'vinyl':
                        vinyl = datosC.text
                    if datosC.tag == 'compacto':
                        compacto = datosC.text
                    if datosC.tag == 'categoria':
                        categoria = datosC.text
                        
                    for canciones in datosC:
                        if canciones.tag == 'cancion':
                            idCancion = canciones.attrib.get('id')
                            for cancion in canciones:
                                a = cancion.tag
                                if cancion.tag == 'nombre':
                                    nombreC = cancion.text
                                if cancion.tag == 'anio':
                                    anio = cancion.text
                                if cancion.tag == 'artista':
                                    artista = cancion.text
                                if cancion.tag == 'genero':
                                    genero = cancion.text
                                    cancion = {
                                        "id": idCancion,
                                        "nombre": nombreC,
                                        "anio": anio,
                                        "artista": artista,
                                        "genero": genero
                                    }
                                    listaCanciones.append(cancion)
                                    validar = True
                                    listaGeneral["listaPlaylist"] = listaPlaylist
                    if validar == True:
                        cliente = {
                            "id": id,
                            "nit": nit,
                            "vinyl": vinyl,
                            "compacto": compacto,
                            "categoria": categoria,
                            "canciones": listaCanciones
                        }
                        listaPlaylist.append(cliente)
                        
                        listaCanciones = []
                        validar = False
        
        if dato.tag == 'listaClientes':
            for dato1 in dato:
                nit = dato1.attrib.get('nit')
                for cliente in dato1:
                    if cliente.tag == 'nombre':
                        nombre = cliente.text
                    if cliente.tag == 'usuario':
                        usuario = cliente.text
                    if cliente.tag == 'clave':
                        clave = cliente.text
                    if cliente.tag == 'direccion':
                        direccion = cliente.text
                    if cliente.tag == 'correoElectronico':
                        correo = cliente.text
                    if cliente.tag == 'empresa':
                        empresa = cliente.text
                    if cliente.tag == 'playlistsAsociadas':
                        for playlist in cliente:
                            if playlist.tag == 'playlist':
                                id = playlist.text
                                listaPlay.append(id)
                                validar = True
                    if validar == True:
                        cliente = {
                            "nit": nit,
                            "nombre": nombre,
                            "usuario": usuario,
                            "clave": clave,
                            "direccion": direccion,
                            "correo": correo,
                            "empresa": empresa,
                            "playlists": listaPlay
                        }
                        listaClientes.append(cliente)
                        validar = False
                        listaPlay = []
                        listaGeneral["listaClientes"] = listaClientes
        
        if dato.tag == 'listaEmpresas':
            for empresa in dato:
                id = empresa.attrib.get('id')
                for nombre in empresa:
                    nombre  = nombre.text
                    empresa = {
                        "id": id,
                        "nombre": nombre
                    }
                    listaEmpresas.append(empresa)
                    listaGeneral["listaEmpresas"] = listaEmpresas
    
    with open('BaseDeDatos.json', 'w') as json_file:
        json.dump(listaGeneral, json_file, indent=4)
    
    return jsonify({'status': 'ok', 'clientes': listaClientes, 'playlists': listaPlaylist, 'empresas': listaEmpresas})


if __name__ == '__main__':
    app.run(debug=True)