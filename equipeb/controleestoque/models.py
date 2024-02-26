from django.db import models
from django import forms

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