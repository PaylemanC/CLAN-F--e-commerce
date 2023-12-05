#URL.py donde se va a renderizar.

"""
URL configuration for clanf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('quienes-somos', views.quienes_somos, name = 'quienes_somos'), #La URL, la función definida en view = de view traeme ESO, el nombre de la página es opcional.
    path('contacto', views.contacto, name = 'contacto'),
    path('productos', views.lista_productos, name = 'lista_productos'),
    path('login', views.login_view, name = 'login'),
    # Se incluyen todas las URLs de la app productos mediante el prefijo administrador/
    path('administrador/', include('productos.urls')),
    path('admin/', admin.site.urls),
]
