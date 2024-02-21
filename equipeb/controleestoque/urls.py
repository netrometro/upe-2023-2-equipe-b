from django.urls import path

from controleestoque.views import list_supplier, new_supplier

urlpatterns = [
    path("", views.index, name="index"),
    path("supplier/list", list_supplier, name="list_supplier"),
    path("supplier/new", new_supplier, name="new_supplier"),
]