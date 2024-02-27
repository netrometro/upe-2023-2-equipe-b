from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('listar_produto/', views.listar_produto, name='listar_produto'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
]