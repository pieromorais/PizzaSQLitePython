from django.db import models

# Create your models here.

class Bordas(models.Model):
    # tabela de bordas
    borda = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
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

class Pizza(models.Model):
    # Cria a pizza - e ajuda para organizar e conseguir combinar sabores
    pizza = models.CharField(max_length=1000)
    tamanho = models.IntegerField()
    def __str__(self) -> str:
        return self.pizza

class PedidoPizza(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class PedidoPizzaFinal(models.Model):
    order = models.ForeignKey(PedidoPizza, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Sabores, on_delete=models.CASCADE)
    borda = models.ForeignKey(Bordas, on_delete=models.CASCADE)

    
