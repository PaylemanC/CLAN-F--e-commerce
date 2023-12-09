from django.urls import path
from . import views

urlpatterns = [
        path('', views.crear_producto, name = 'productos-admin'),
]
