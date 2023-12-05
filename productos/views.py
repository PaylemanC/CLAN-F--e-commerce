from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def crear_producto(request):
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
