from django import forms

from juliany_pizza.orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'address', 'phone',)
