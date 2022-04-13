from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, ListView, DetailView

from juliany_pizza.cart.cart import Cart
from juliany_pizza.menu.models import Stock
from juliany_pizza.orders.forms import OrderForm
from juliany_pizza.orders.models import Order


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
        form.instance.items = cart.cart
        form.save()
        cart.clear()
        return super().form_valid(form)


class SuccessfulOrder(TemplateView):
    template_name = 'orders/successful-order.html'


class OrdersView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/orders.html'


class OrderDetailsView(DetailView):
    model = Order
    template_name = 'orders/order-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = []
        for item, values in context['order'].items.items():
            context['items'].append(
                {Stock.objects.get(id=item): values['qty']}
            )
        return context


class FinishOrder(View):
    def get(self, request, pk):
        product = get_object_or_404(Order, pk=pk)
        product.finished = True
        product.save()
        return redirect('orders')
