from django.shortcuts import render, redirect
import requests
from .forms import EntradaForm
from .forms import EntradaFecha


endpoint = 'http://127.0.0.1:5000/'


def inicio(x):
    return render(x, 'inicio.html')

def consulta_fech(x):
    return render(x, 'consulta_fecha.html')
def peticion_error(x):
    return render(x, 'consulta_error.html')
def ayuda(x):
    return render(x, 'Ayuda.html')
def consulta(x):
    return render(x, 'Consulta_datos.html')

def enviararchivo(request):
    return render(request, 'Inicio.html')

def salida(request):
    return render(request, 'Inicio.html')

def salida_entrada(request):
    return render(request, 'Inicio.html')

def enviarinfo(request):
    
    return render(request, 'consulta_fecha.html')

def reset(request):
    return render(request, 'Inicio.html')

def codigo(request):
    return render(request, 'consulta_error.html')

def datos(request):
    
    return render(request, "Consulta_datos.html")
