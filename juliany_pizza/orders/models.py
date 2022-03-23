from django.contrib.auth import get_user_model
from django.db import models

from juliany_pizza.menu.models import Stock

UserModel = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='order_user',
        null=True,
        blank=True,
    )
    full_name = models.CharField(
        max_length=50,
    )
    address = models.CharField(
        max_length=250,
    )
    phone = models.CharField(
        max_length=100,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    total_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    finished = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)

#
# class OrderItem(models.Model):
#     order = models.ForeignKey(
#         Order,
#         on_delete=models.CASCADE,
#     )
#     product = models.ForeignKey(
#         Stock,
#         on_delete=models.CASCADE,
#         related_name='order_items',
#     )
#     price = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#     )
#     quantity = models.PositiveIntegerField(
#         default=1,
#     )
#
#     def __str__(self):
#         return str(self.id)
