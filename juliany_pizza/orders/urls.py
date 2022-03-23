from django.urls import path

from juliany_pizza.orders.views import PlaceOrder, SuccessfulOrder

urlpatterns = (
    path('', PlaceOrder.as_view(), name='place order'),
    path('order-placed/', SuccessfulOrder.as_view(), name='successful order'),
)
