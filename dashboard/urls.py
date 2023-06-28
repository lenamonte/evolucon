from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro', views.cadastro_vendedor, name='cadastro_vendedor'),
    path('clientes', views.clientes_list, name='clientes_list'),
    path('cliente/novo/', views.cliente_novo, name='cliente_novo'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.user_login, name='login'),
]
