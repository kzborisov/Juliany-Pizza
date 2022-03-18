from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from juliany_pizza.cart.cart import Cart
from juliany_pizza.menu.models import Stock


class CartSummaryView(TemplateView):
    template_name = 'cart/summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context


class AddToCartView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            item_id = int(request.POST.get('itemId'))
            item = get_object_or_404(Stock, id=item_id)
            cart.add(item=item)
            response = JsonResponse(
                {
                    'data': cart.cart,
                    'qty': len(cart),
                }
            )
            return response
