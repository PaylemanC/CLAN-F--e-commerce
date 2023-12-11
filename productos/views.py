from django.shortcuts import render, redirect, get_object_or_404
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
    
@login_required(login_url='/login')
def eliminar_producto(request, id):
    product = get_object_or_404(Product, id = id)
    product.delete()
    return redirect("productos-admin")

@login_required(login_url='/login')
def editar_producto(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productos-admin')

    return render(request, 'editar_producto.html', {
        'form': form,
        'product': product
    })
    
