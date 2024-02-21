from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('listar_item/', views.listar_item, name='listar_item'),
    path('adicionar_produto', views.adicionar_produto, name='adicionar_produto'),
]