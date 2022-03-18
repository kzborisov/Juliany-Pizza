from django.contrib import admin

from juliany_pizza.menu.models import Category, Ingredient, Product, Stock


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('id', 'name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description', 'active')
    list_filter = ('category', 'name', 'active')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('size', 'price', 'product')
