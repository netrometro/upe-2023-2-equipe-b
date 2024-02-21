from django import forms
from .models import Produtos

class ProdutosFormCriar(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'codigo', 'preco', 'quantidade', 'cor', 'tamanho']