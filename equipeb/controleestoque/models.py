from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=75)
    sede_local = models.CharField(max_length=150)
    telefone_contato = models.BigIntegerField()
    entrada_data = models.DateTimeField("Data publicada")

    def __str__(self):
        return self.nome
        