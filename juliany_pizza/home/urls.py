from django.urls import path

from juliany_pizza.home.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
