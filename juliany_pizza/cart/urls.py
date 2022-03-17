from django.urls import path

from juliany_pizza.cart.views import CartSummaryView, AddToCartView

urlpatterns = (
    path('summary/', CartSummaryView.as_view(), name='cart summary'),
    path('cart-add/', AddToCartView.as_view(), name='cart add'),
)
