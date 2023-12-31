# views.py ==> Tener todas la funciones o clases para renderizar las vistas de una aplicación, es decir, mostrar los HTML.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from productos.models import Product

def index(request):
    return render(request, 'index.html', {
        'title': 'CLAN-F'
    })

def quienes_somos(request):
    return render(request, 'quienes_somos.html', {}) #Recibe tres parámetros: petición de tipo, el archivo a renderizar, y el contexto)

def contacto(request):
    return render(request, 'contacto.html', {})

def lista_productos(request):
    products = Product.objects.all().order_by('-id')
    print(products)
    return render(request, 'productos.html', {
        'products': products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('productos-admin')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                messages.info(request, 'Bienvenid@ {}'.format(user.username.upper()))
                return redirect('productos-admin')
            else:
                messages.error(request, 'Usuario y/o contraseña incorrectos.')
    else:
        form = LoginForm()     
        
    return render(request, 'login.html', {
        'form': form
    })  
    
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada exitosamente.')    
    return redirect('login')