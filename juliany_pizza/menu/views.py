from django.views.generic import ListView

from juliany_pizza.menu.models import MenuItem, Category


class MenuView(ListView):
    model = MenuItem
    template_name = 'menu/menu.html'
    context_object_name = 'menu_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related('menuitem_set')
        return context
