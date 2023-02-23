from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('montar', views.montar_pizza, name='montar'),
    path('checar', views.conferir_pedido, name='conferir')
]
