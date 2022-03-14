from django.core.validators import MinLengthValidator
from django.db import models


class Category(models.Model):
    CATEGORY_NAME_MAX_LENGTH = 255
    CATEGORY_NAME_MIN_LENGTH = 3

    name = models.CharField(
        max_length=CATEGORY_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(CATEGORY_NAME_MIN_LENGTH),
        ],
    )

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    INGREDIENT_NAME_MAX_LENGTH = 255
    INGREDIENT_NAME_MIN_LENGTH = 3

    name = models.CharField(
        max_length=INGREDIENT_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(INGREDIENT_NAME_MIN_LENGTH),
        ],
    )

    class Meta:
        verbose_name_plural = 'Ingredients'
        verbose_name = 'Ingredient'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    NAME_MAX_LENGTH = 255
    NAME_MIN_LENGTH = 3

    PRICE_MAX_DIGITS = 12
    PRICE_DECIMAL_PLACES = 2

    ACTIVE_DEFAULT_VALUE = True

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAME_MIN_LENGTH),
        ],
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
    )
    active = models.BooleanField(
        default=ACTIVE_DEFAULT_VALUE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
    )

    class Meta:
        verbose_name_plural = 'Menu Items'
        verbose_name = 'Menu Items'

    def __str__(self):
        return self.name
