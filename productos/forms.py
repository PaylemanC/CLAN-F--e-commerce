from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = ['title', 'price', 'stock']
    
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del producto'
        })
    )
