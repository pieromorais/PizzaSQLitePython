from django.shortcuts import render, redirect


from .models import Sabores, Pizza, PedidoPizza, PedidoPizzaFinal, Bordas

# Create your views here.
def index(request): 
    return render(request, 'Pizzaria/index.html', {})

def montar_pizza(request):
    if request.method == 'POST':
        tamanho = request.POST.get('tamanho')

        # criação da pizza
        p = Pizza.objects.create(tamanho=tamanho)

        # Criação do pedido da pizza
        pp = PedidoPizza.objects.create(pizza=p)

        context = {
            "tamanho": tamanho,
            "linhas_sabores": Sabores.objects.all(),
            "linhas_bordas": Bordas.objects.all(),
            "pizza_id": p.id,
            "pedido_pizza_id": pp.id
            }
        
        

        return render(request, "Pizzaria/montar.html", context)
    else:
        return render(request, 'Pizzaria/index.html', {})

def conferir_pedido(request):
    if request.method == 'POST':
        tamanho = request.POST.get('tamanho')
        
        sabor1 = request.POST.get('sabor1') or None
        sabor2 = request.POST.get('sabor2') or None
        sabor3 = request.POST.get('sabor3') or None
        borda = request.POST.get('borda')     
        if tamanho == '1':
            # get objects
            sabor_object = Sabores.objects.get(id=sabor1)
            borda_object = Bordas.objects.get(id=borda)
            pedido_pizza_object = PedidoPizza.objects.get(id=request.POST.get('pedido_pizza_id'))

            final1 = PedidoPizzaFinal(order= pedido_pizza_object, flavor = sabor_object, borda = borda_object)
            final1.save()

        elif tamanho == '2':
            # get objects
            sabor_object = Sabores.objects.get(id=sabor1)
            borda_object = Bordas.objects.get(id=borda)
            pedido_pizza_object = PedidoPizza.objects.get(id=request.POST.get('pedido_pizza_id'))

            final1 = PedidoPizzaFinal(order= pedido_pizza_object, flavor = sabor_object, borda = borda_object)
            final1.save()

            sabor_object = Sabores.objects.get(id=sabor2)
            final2 = PedidoPizzaFinal(order= pedido_pizza_object, flavor = sabor_object, borda = borda_object)
            final2.save()
        
        else:
            # get objects
            sabor_object = Sabores.objects.get(id=sabor1)
            borda_object = Bordas.objects.get(id=borda)
            pedido_pizza_object = PedidoPizza.objects.get(id=request.POST.get('pedido_pizza_id'))

            final1 = PedidoPizzaFinal(order= pedido_pizza_object, flavor = sabor_object, borda = borda_object)
            final1.save()

            sabor_object = Sabores.objects.get(id=sabor2)
            final2 = PedidoPizzaFinal(order= pedido_pizza_object, flavor = sabor_object, borda = borda_object)
            final2.save()

            sabor_object = Sabores.objects.get(id=sabor3)
            final3 = PedidoPizzaFinal(order= pedido_pizza_object, flavor = sabor_object, borda = borda_object)
            final3.save()

        # query

        # o meu pedido de pizza é o mesmo para p/ todos
        p1, p2, p3 = PedidoPizzaFinal.objects.get(order_id = request.POST.get('pedido_pizza_id'))
        sabores_final =  p1

        return render(request, 'Pizzaria/finalizar.html', context={"sabor1": sabores_final})
    else:
        return render(request, 'Pizzaria/index.html', {})
