from django.urls import path
from . import views

urlpatterns = [
        path('', views.listar_productos, name = 'productos-admin'),
]
