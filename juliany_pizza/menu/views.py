from django.views.generic import ListView

from juliany_pizza.menu.models import Category, Stock


class MenuView(ListView):
    model = Stock
    template_name = 'menu/menu.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('product_set')
        return context
