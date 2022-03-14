from django.urls import path

from juliany_pizza.menu.views import MenuView

urlpatterns = (
    path('', MenuView, name='menu'),
)
