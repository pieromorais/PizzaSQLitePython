from django.contrib import admin

from .models import Sabores, Bordas, Pizza, PedidoPizza, PedidoPizzaFinal
# Register your models here.

admin.site.register(Sabores)
admin.site.register(Bordas)
admin.site.register(Pizza)
admin.site.register(PedidoPizza)
admin.site.register(PedidoPizzaFinal)