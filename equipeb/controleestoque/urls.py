from django.urls import path

from controleestoque.views import index, listar_produto, adicionar_produto, list_supplier, update_supplier, new_supplier
from . import views
from .views import apagar_produto
from .views import line_chart, line_chart_json

urlpatterns = [
    path("", index, name="index"),
    path('listar_produto/', listar_produto, name='listar_produto'),
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path('editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('apagar_produto/<int:id>', views.apagar_produto, name='apagar_produto'),
    path("list_supplier", list_supplier, name="list_supplier"),
    path("update_supplier/<id>", update_supplier, name="update_supplier"),
    path("new_supplier", new_supplier, name="new_supplier"),
    path('bar_produtos_chart', views.bar_produtos_chart, name='bar_produtos_chart'),
    path('chart', line_chart, name='line_chart'),
    path('chartJSON', line_chart_json, name='line_chart_json'),
]