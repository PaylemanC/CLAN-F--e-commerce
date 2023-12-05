# views.py ==> Tener todas la funciones o clases para renderizar las vistas de una aplicación, es decir, mostrar los HTML.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from productos.forms import ProductForm

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
    form = ProductForm(request.POST or None)
    if request.method == 'POST': 
        form = ProductForm(request.POST) #para Yeimer, crea una instancia de productForm
        if form.is_valid():
            form.save()
            return redirect('administrador.html')
    else: #si el metodo es GET genera una instancia y se la pasa al contexto
        form = ProductForm()
    return render(request, 'administrador.html', {
        'form': form
    })