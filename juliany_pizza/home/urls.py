from django.urls import path

from juliany_pizza.home.views import IndexView, ProfileView, ContactsView, AboutView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about/', AboutView.as_view(), name='about'),
)
