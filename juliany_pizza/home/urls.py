from django.urls import path

from juliany_pizza.home.views import IndexView, ProfileView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
)
