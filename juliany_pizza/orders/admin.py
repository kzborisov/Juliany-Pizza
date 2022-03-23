from django.contrib import admin

from juliany_pizza.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     pass
