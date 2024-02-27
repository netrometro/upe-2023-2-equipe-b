from django.urls import path

from . import views
from .views import apagar_produto

urlpatterns = [
    path("", views.index, name="index"),
    path('listar_produto/', views.listar_produto, name='listar_produto'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('apagar_produto/<int:id>', views.apagar_produto, name='apagar_produto'),
    
]