from django.db import models
from django import forms
import datetime

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    # show that user have to put decimals in preco
    preco = models.DecimalField(help_text='Para o preço, não esqueça dos centavos! Exemplo: 10.99',max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    cor = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
        
class Fornecedor(models.Model):
    nome = models.CharField(max_length=75)
    sede_local = models.CharField(max_length=150)
    telefone_contato = models.BigIntegerField()
    entrada_data = models.DateTimeField("Data publicada", blank=True, null=True, default=datetime.date.today)
    def __str__(self):
        return self.nome
        