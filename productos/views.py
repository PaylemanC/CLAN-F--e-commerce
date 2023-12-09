from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from productos.models import Product

# Create your views here.
@login_required(login_url='/login')
def crear_producto(request):
    products = Product.objects.all().order_by('-id')    
    form = ProductForm(request.POST or None)
    
    if request.method == 'POST': 
        form = ProductForm(request.POST, request.FILES) #Crea una instancia de productForm
        if form.is_valid():
            form.save()
            return redirect('productos-admin')
    else: #si el metodo es GET genera una instancia y se la pasa al contexto
        form = ProductForm()
    return render(request, 'administrador.html', {
        'form': form,
        'products': products
    })
