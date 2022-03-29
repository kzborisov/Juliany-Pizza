from django.contrib.auth import get_user_model
from django.db import models

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
    items = models.JSONField()
    finished = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.created)
