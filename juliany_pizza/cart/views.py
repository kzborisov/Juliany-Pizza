from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from juliany_pizza.cart.cart import Cart
from juliany_pizza.menu.models import Size, MenuItem


class CartSummaryView(TemplateView):
    template_name = 'cart/summary.html'


#
# def add_to_cart(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         item_id = int(request.POST.get('itemId'))
#         item_size = request.POST.get('itemSize')
#         item = get_object_or_404(MenuItem, id=item_id)
#         size = get_object_or_404(Size, size=item_size, menuitem__id=item_id)
#         cart.add(item=item, size=size)
#         response = JsonResponse(
#             {
#                 # TODO: Replace with actual data
#                 'test': 'data',
#             }
#         )
#         return response


class AddToCartView(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
            item_id = int(request.POST.get('itemId'))
            item_size = request.POST.get('itemSize')
            item = get_object_or_404(MenuItem, id=item_id)
            size = get_object_or_404(Size, size=item_size, menuitem__id=item_id)
            cart.add(item=item, size=size)
            response = JsonResponse(
                {
                    'data': cart.cart,
                    'qty': len(cart),
                }
            )
            return response
