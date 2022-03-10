from django import forms
from django.contrib.auth import get_user_model

from juliany_pizza.authentication.models import Profile

UserModel = get_user_model()


class ProfileDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Your First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Your Last Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Enter your phone (e.g 0899999999)'
        self.fields['address'].widget.attrs['placeholder'] = 'Enter Your Address'

    class Meta:
        model = Profile
        fields = '__all__'


class CustomUserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
