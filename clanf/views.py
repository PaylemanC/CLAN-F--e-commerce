# views.py ==> Tener todas la funciones o clases para renderizar las vistas de una aplicación, es decir, mostrar los HTML.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
        'title': 'CLAN-F'
    })

def quienes_somos(request):
    return render(request, 'quienes_somos.html', {}) #Recibe tres parámetros: petición de tipo, el archivo a renderizar, y el contexto)

def contacto(request):
    return render(request, 'contacto.html', {})

def lista_productos(request):
    return render(request, 'productos.html', {})

def administrador(request):
    return render(request, 'administrador.html', {})