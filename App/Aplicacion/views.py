from django.shortcuts import render, redirect
import requests
from .forms import EntradaForm
from .forms import EntradaFecha


endpoint = 'http://127.0.0.1:5000/'


def inicio(x):
    return render(x, 'index.html')

def consulta_fech(x):
    return render(x, 'consulta_fecha.html')
def peticion_error(x):
    return render(x, 'consulta_error.html')
def ayuda(x):
    return render(x, 'Ayuda.html')
def consulta(x):
    return render(x, 'Consulta_datos.html')

def enviararchivo(request):
    contexto={}
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            archivivo  = request.FILES['file'].read()
            archivivo = archivivo.decode("utf-8")
            file = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/entrada.xml', 'w')
            file.write(archivivo)
            file.close()
            response = requests.post(endpoint + 'enviado', data= archivivo)
            contexto = {
                'organizado': archivivo
            }
    return render(request, 'Inicio.html', contexto)

def salida(request):
    contxt = {}
    if request.method == 'GET':
        estadistica = ""
        entrada = ""
        file = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/estadisticas.xml', 'r')
        cuchao_we = file.read()
        file.close()
        file = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/entrada.xml', 'r')
        con_entrada = file.read()
        file.close()
        contxt = {
            'entradatos': cuchao_we,
            'organizado': con_entrada
        }
    return render(request, 'Inicio.html', contxt)
def salida_entrada(request):
    if request.method == 'GET':
        new = requests.get('http://127.0.0.1:8000/')
        info = {
            'salida_entrada': new.text,
        }
        return render(request, 'Inicio.html',info)

def enviarinfo(request):
    if request.method == 'GET':
        fecha = request.GET['fname']
        fecha = fecha.replace("/", "-")
        resulto = requests.get(endpoint + 'fechas/' + fecha)
        print(fecha)
    return render(request, 'consulta_fecha.html')

def reset(request):
    if request.method == 'POST':
        respuesta = requests.post(endpoint + 'reseteado', data = "")
    return render(request, 'Inicio.html')

def codigo(request):
    if request.method == 'GET':
        codigo = request.GET['fnamee']
        resulto = requests.get(endpoint + 'codigos/' + codigo.strip())
        print(codigo)

    return render(request, 'consulta_error.html')

def datos(request):
    Open_File = open('C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/Backend/estadisticas.xml', "r", encoding="utf-8")
    data3 = Open_File.read()
    Open_File.close()
    return render(request, "Consulta_datos.html", {"consultaR": data3})
