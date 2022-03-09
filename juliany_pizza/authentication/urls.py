from django.urls import path

from juliany_pizza.authentication.views import UserRegistrationView, UserLogoutView, UserLoginView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
)
