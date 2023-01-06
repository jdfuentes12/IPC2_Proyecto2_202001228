from flask import Flask,request
from flask.json import jsonify
from flask_cors import CORS
import json
import xml
import webbrowser as wb
from xml.etree import ElementTree as ET

'''
    CORRER EL SERVIDOR FRONTEND:
    py manage.py runserver
'''

app = Flask(__name__)
app.config['DEBUG'] = True

CORS(app)
#-------------------------------------GET'S-------------------------------------#
@app.route('/login',methods=['GET'])
def login():
    datos = request.get_json()
    with open('BaseDeDatos.json') as json_file:
        data = json.load(json_file)
        for usuario in data['listaClientes']:
            if usuario['usuario'] == datos['usuario'] and usuario['clave'] == datos['clave']:
                return jsonify({'status': 'ok', 'message': 'Usuario encontrado'})
    return jsonify({'status': 'error', 'message': 'Usuario no encontrado'})

#-------------------------------------POST'S-------------------------------------#
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

@app.route('/crearEmpresa', methods=['POST'])
def crearEmpresa():
    try:
        datos = request.get_json()
        with open('BaseDeDatos.json', 'r') as json_file:
            base = json.load(json_file)
        for empresas in base["listaEmpresas"]:
            if datos["id"] == empresas["id"]:
                return jsonify({'message': 'error', 'message': 'Empresa ya existe'})
        base["listaEmpresas"].append(datos)
        with open('BaseDeDatos.json', 'w') as json_file:
            json.dump(base, json_file, indent=4)
        return jsonify({'status': 'ok', 'message': 'Empresa creada'})
    except:
        return jsonify({'status': 'error', 'message': 'Error al crear empresa'})

@app.route('/crearPlaylist', methods=['POST'])
def crearPlaylist():
    try:
        datos = request.get_json()
        with open('BaseDeDatos.json', 'r') as json_file:
            base = json.load(json_file)
        for playlist in base["listaPlaylist"]:
            if datos["id"] == playlist["id"]:
                return jsonify({'message': 'error', 'message': 'Playlist ya existe'})
        base["listaPlaylist"].append(datos)
        with open('BaseDeDatos.json', 'w') as json_file:
            json.dump(base, json_file, indent=4)
        return jsonify({'status': 'ok', 'message': 'Playlist creada'})
    except:
        return jsonify({'status': 'error', 'message': 'Error al crear playlist'})

@app.route('/crearCliente', methods=['POST'])
def crearCliente():
    try:
        datos = request.get_json()
        with open('BaseDeDatos.json', 'r') as json_file:
            base = json.load(json_file)
        for cliente in base["listaClientes"]:
            if datos["nit"] == cliente["nit"]:
                return jsonify({'message': 'error', 'message': 'Cliente ya existe'})
        base["listaClientes"].append(datos)
        with open('BaseDeDatos.json', 'w') as json_file:
            json.dump(base, json_file, indent=4)
        return jsonify({'status': 'ok', 'message': 'Cliente creado'})
    except:
        return jsonify({'status': 'error', 'message': 'Error al crear cliente'})

#-------------------------------------DELETE'S-------------------------------------#
@app.route('/eliminarEmpresa', methods=['DELETE'])
def elimnarEmpresa():
    try:
        datos = request.get_json()
        with open('BaseDeDatos.json', 'r') as json_file:
            base = json.load(json_file)
        for empresa in base["listaEmpresas"]:
            if datos["id"] == empresa["id"]:
                base["listaEmpresas"].remove(empresa)
                with open('BaseDeDatos.json', 'w') as json_file:
                    json.dump(base, json_file, indent=4)
                return jsonify({'status': 'ok', 'message': 'Empresa eliminada'})
        return jsonify({'status': 'error', 'message': 'Empresa no existe'})
    except:
        return jsonify({'status': 'error', 'message': 'Error al eliminar empresa'})

@app.route('/eliminarPlaylist', methods=['DELETE'])
def eliminarPlaylist():
    try:
        datos = request.get_json()
        with open('BaseDeDatos.json', 'r') as json_file:
            base = json.load(json_file)
        for playlist in base["listaPlaylist"]:
            if datos["id"] == playlist["id"]:
                base["listaPlaylist"].remove(playlist)
                with open('BaseDeDatos.json', 'w') as json_file:
                    json.dump(base, json_file, indent=4)
                return jsonify({'status': 'ok', 'message': 'Playlist eliminada'})
        return jsonify({'status': 'error', 'message': 'Playlist no existe'})
    except:
        return jsonify({'status': 'error', 'message': 'Error al eliminar playlist'})

@app.route('/eliminarCliente', methods=['DELETE'])
def eliminarCliente():
    try:
        datos = request.get_json()
        with open('BaseDeDatos.json', 'r') as json_file:
            base = json.load(json_file)
        for cliente in base["listaClientes"]:
            if datos["nit"] == cliente["nit"]:
                base["listaClientes"].remove(cliente)
                with open('BaseDeDatos.json', 'w') as json_file:
                    json.dump(base, json_file, indent=4)
                return jsonify({'status': 'ok', 'message': 'Cliente eliminado'})
        return jsonify({'status': 'error', 'message': 'Cliente no existe'})
    except:
        return jsonify({'status': 'error', 'message': 'Error al eliminar cliente'})

@app.route('/eliminarCancion', methods=['DELETE'])
def eliminarCancion():
    datos = request.get_json()
    with open('BaseDeDatos.json', 'r') as json_file:
        base = json.load(json_file)
    for playlist in base["listaPlaylist"]:
        if datos["idPlaylist"] == playlist["id"]:
            for cancion in playlist["canciones"]:
                if datos["idCancion"] == cancion["id"]:
                    playlist["canciones"].remove(cancion)
                    with open('BaseDeDatos.json', 'w') as json_file:
                        json.dump(base, json_file, indent=4)
                    return jsonify({'status': 'ok', 'message': 'Cancion eliminada'})
            return jsonify({'status': 'error', 'message': 'Cancion no existe'})

if __name__ == '__main__':
    app.run(debug=True)