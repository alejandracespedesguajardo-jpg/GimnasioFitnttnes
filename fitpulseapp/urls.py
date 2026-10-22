from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('editar/<str:rut>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<str:rut>/', views.eliminar_cliente, name='eliminar_cliente'),
]