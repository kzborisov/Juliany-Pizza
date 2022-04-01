from juliany_pizza.orders.models import Order


def orders_count(request):
    return {'orders_count': Order.objects.filter(finished=False).count()}
