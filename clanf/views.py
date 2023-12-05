# views.py ==> Tener todas la funciones o clases para renderizar las vistas de una aplicación, es decir, mostrar los HTML.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

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
                print(request, 'Bienvenido {}'.format(user.username.upper()))
                return redirect('productos-admin')
            else:
                print(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()     
        
    return render(request, 'login.html', {
        'form': form
    })  
    
def logout_view(request):
    logout(request)
    print(request, 'Sesión cerrada exitosamente.')
    return redirect('login')