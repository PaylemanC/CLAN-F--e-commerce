# forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', required=True, min_length=4, max_length=24,
                               widget=forms.TextInput(attrs={ 
                                   'class': '',
                                   'id': 'username',
                                   'placeholder': 'Nombre de Usuario'
                                }))
    password = forms.CharField(label='Contraseña', required=True, min_length=4, max_length=16,
                               widget=forms.PasswordInput(attrs={ 
                                'class': '',
                                'id': 'password',
                                'placeholder': '*******'
                            }))
