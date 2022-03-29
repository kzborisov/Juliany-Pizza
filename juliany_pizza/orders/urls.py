from django.urls import path

from juliany_pizza.orders.views import PlaceOrder, SuccessfulOrder, OrdersView, OrderDetailsView

urlpatterns = (
    path('', PlaceOrder.as_view(), name='place order'),
    path('view-orders', OrdersView.as_view(), name='orders'),
    path('details/<int:pk>/', OrderDetailsView.as_view(), name='order'),
    path('order-placed/', SuccessfulOrder.as_view(), name='successful order'),
)
