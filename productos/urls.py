from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_producto, name = 'productos-admin'),
    path('eliminar/<int:id>', views.eliminar_producto, name = 'eliminar_producto')            
]
