from django import forms
from .models import FornecedorModel

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = FornecedorModel
        fields = [
            "nome",
            "sede_local",
            "telefone_contato",
            "entrada_data",
        ]
        # or fields = "__all__"