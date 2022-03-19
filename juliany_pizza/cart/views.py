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
            subtotal_price = f'{cart.subtotal_price:.2f}'
            response = JsonResponse(
                {
                    'subtotal': subtotal_price,
                    'qty': len(cart),
                }
            )
            return response


class UpdateCartView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            item_id = request.POST.get('itemId')
            item_qty = int(request.POST.get('itemQty'))
            cart.update(item_id=item_id, item_qty=item_qty)
            item = cart.cart[item_id]
            subtotal_price = f'{cart.subtotal_price:.2f}'
            item_total_price = f'{cart.item_total_price(item):.2f}'
            final_price = f'{cart.total_price:.2f}'
            response = JsonResponse(
                {
                    'qty': len(cart),
                    'item_total_price': item_total_price,
                    'subtotal': subtotal_price,
                    'final_price': final_price,
                }
            )
            return response


class DeleteCartItemView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            item_id = request.POST.get('itemId')
            cart.delete(item_id=item_id)
            subtotal_price = f'{cart.subtotal_price:.2f}'
            final_price = f'{cart.total_price:.2f}'
            response = JsonResponse(
                {
                    'subtotal': subtotal_price,
                    'qty': len(cart),
                    'final_price': final_price,
                }
            )
            return response
