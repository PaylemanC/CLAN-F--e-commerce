from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['title', 'price', 'stock', 'image']
    
    title = forms.CharField(label='Producto', min_length=1, max_length=125,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del producto',
            'class': "form-control",
        })
    )
    
    price = forms.DecimalField(required=True, label='Precio', max_digits=8, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Indique un precio',
            'class': "form-control",
        })
    )
    
    stock = forms.IntegerField(label='Stock', 
        widget=forms.NumberInput(attrs={
            'placeholder': 'Indique la cantidad',
            'class': "form-control",
        })
    )
    
    image = forms.ImageField(required=True, label='Imagen',
        widget=forms.ClearableFileInput(attrs={ 
            'class': 'form-control',
            'id': 'photo',
            'accept': 'image/*'
        }))