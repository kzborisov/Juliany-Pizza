from django.contrib import admin

from juliany_pizza.menu.models import Category, Ingredient, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('id', 'name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('id', 'name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'description', 'active')
    list_filter = ('category', 'name', 'price', 'active')
