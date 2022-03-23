from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from juliany_pizza.cart.cart import Cart
from juliany_pizza.orders.forms import OrderForm


class PlaceOrder(CreateView):
    form_class = OrderForm
    template_name = 'orders/order-form.html'
    success_url = reverse_lazy('successful order')

    def get_initial(self):
        full_name, address1, phone = '', '', ''

        if self.request.user.id:
            full_name = self.request.user.profile.full_name
            address1 = self.request.user.profile.address
            phone = self.request.user.profile.phone

        return {
            'full_name': full_name,
            'address': address1,
            'phone': phone,
        }

    def form_valid(self, form):
        cart = Cart(self.request)
        if self.request.user.id:
            form.instance.user = self.request.user
        form.instance.total_price = cart.total_price
        form.save()
        cart.clear()
        return super().form_valid(form)


class SuccessfulOrder(TemplateView):
    template_name = 'orders/successful-order.html'
