from django.db import models

# Create your models here.

class Bordas(models.Model):
    # tabela de bordas
    borda = models.CharField(max_length=200)
    valor_borda = models.DecimalField(max_digits=2, decimal_places=2)

class Sabores(models.Model):
    # tabela com sabores
    sabor = models.CharField(max_length=200)
    valor_sabor = models.DecimalField(max_digits=2, decimal_places=2)