from django.urls import path

from juliany_pizza.cart.views import CartSummaryView, AddToCartView, DeleteCartItemView, UpdateCartView

urlpatterns = (
    path('summary/', CartSummaryView.as_view(), name='cart summary'),
    path('cart-add/', AddToCartView.as_view(), name='cart add'),
    path('cart-update/', UpdateCartView.as_view(), name='cart update'),
    path('cart-delete/', DeleteCartItemView.as_view(), name='cart delete'),
)
