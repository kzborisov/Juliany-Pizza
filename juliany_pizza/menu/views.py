from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class MenuView(LoginRequiredMixin, ListView):
    pass
