from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['title', 'price', 'stock']
    
    title = forms.CharField(label='Producto', min_length=1, max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del Producto',
            'class': "form-control",
        })
    )
    price = forms.CharField(label='Precio', min_length=1, max_length=8,
        widget=forms.TextInput(attrs={
            'placeholder': 'Indique un Precio',
            'class': "form-control",
        })
    )
    stock = forms.CharField(label='Stock', min_length=0, max_length=5,
        widget=forms.TextInput(attrs={
            'placeholder': 'Indique la Cantidad',
            'class': "form-control",
        })
    )
