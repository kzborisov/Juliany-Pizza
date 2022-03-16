from django.urls import path

from juliany_pizza.authentication.views import UserRegistrationView, UserLogoutView, UserLoginView, \
    UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password_reset/', UserPasswordResetView.as_view(), name="reset password"),
    path('password_reset_sent/', UserPasswordResetDoneView.as_view(), name="password reset done"),
    path('reset_password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', UserPasswordResetCompleteView.as_view(), name="password reset complete"),
)
