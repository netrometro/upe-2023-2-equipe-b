from django.urls import path

from controleestoque.views import index, listar_produto, adicionar_produto, list_supplier, new_supplier

urlpatterns = [
    path("", index, name="index"),
    path('listar_produto/', listar_produto, name='listar_produto'),
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path("supplier/list", list_supplier, name="list_supplier"),
    path("new_supplier", new_supplier, name="new_supplier"),
]