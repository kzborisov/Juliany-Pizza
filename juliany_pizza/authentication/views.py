from django.contrib.auth import login
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from juliany_pizza.authentication.forms import UserRegistrationForm, UserSetPasswordForm, UserPasswordResetForm, \
    UserPasswordChangeForm


class UserRegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(LogoutView):
    pass


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('index')


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = "accounts/password_reset.html"
    success_url = reverse_lazy('password reset done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_sent.html"
    success_url = reverse_lazy('password reset confirm')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserSetPasswordForm
    template_name = "accounts/reset_password_confirm.html"
    success_url = reverse_lazy('password reset complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/reset_password_complete.html"
