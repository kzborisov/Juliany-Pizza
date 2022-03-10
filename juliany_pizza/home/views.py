from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from juliany_pizza.authentication.models import Profile
from juliany_pizza.home.forms import ProfileDetailsForm, CustomUserDetailsForm


class IndexView(TemplateView):
    template_name = 'home/index.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'home/profile.html'
    form_class = ProfileDetailsForm
    second_form_class = CustomUserDetailsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.kwargs['pk'])

        if 'profile_form' not in context:
            context['profile_form'] = self.form_class(instance=profile)

        if 'user_form' not in context:
            context['user_form'] = self.second_form_class(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        profile = Profile.objects.get(pk=self.kwargs['pk'])
        profile_form = self.form_class(request.POST, request.FILES, instance=profile)
        user_form = self.second_form_class(request.POST, instance=self.request.user)

        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(self.request, 'User data successfully saved!')
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(
                self.get_context_data(
                    profile_form=profile_form,
                    user_form=user_form,
                ),
            )

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})
