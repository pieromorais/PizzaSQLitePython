from django.db import models

# Create your models here.

class Bordas(models.Model):
    # tabela de bordas
    borda = models.CharField(max_length=200)
    valor_borda = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self) -> str:
        return self.borda


class Sabores(models.Model):
    # tabela com sabores
    sabor = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    valor_sabor = models.DecimalField(max_digits=4, decimal_places=2)
    especial = models.BooleanField(default=0)

    def __str__(self) -> str:
        return self.sabor