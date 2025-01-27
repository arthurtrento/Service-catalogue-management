from django.urls import path
from . import views

urlpatterns = [
    
    path('ver/', views.ver_catalogo, name="ver_catalogo"),
    path('login/', views.login_catalogo, name="login_catalogo"),
    path('escolher/', views.escolher_catalogo, name="escolher_catalogo"),
    path('inserir/', views.inserir_catalogo, name="inserir_catalogo"),
    path('modificar/', views.modificar_catalogo, name="modificar_catalogo"),
    path('excluir/', views.excluir_catalogo, name="excluir_catalogo"),
    path('pedidos/', views.pedidos_catalogo, name="pedidos_catalogo")
]