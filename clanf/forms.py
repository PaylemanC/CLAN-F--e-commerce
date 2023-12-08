# forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True,
                               widget=forms.TextInput(attrs={ 
                                   'id': 'username',
                                   'placeholder': 'Ingresa tu usuario'
                                }))
    password = forms.CharField(label='Contraseña', required=True, 
                               widget=forms.PasswordInput(attrs={ 
                                'id': 'password',
                                'placeholder': 'Ingresa tu contraseña'
                            }))
