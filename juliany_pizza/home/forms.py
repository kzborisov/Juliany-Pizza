from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator

from juliany_pizza import settings
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


class ContactForm(forms.Form):
    NAME_MIN_LENGTH = 2
    NAME_MAX_LENGTH = 30

    SUBJECT_MAX_LENGTH = 30
    SUBJECT_MIN_LENGTH = 2

    MESSAGE_MAX_LENGTH = 2000
    MESSAGE_MIN_LENGTH = 5

    name = forms.CharField(
        max_length=NAME_MAX_LENGTH,
        required=True,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your name'
            },
        ),
    )
    subject = forms.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        required=True,
        validators=(
            MinLengthValidator(SUBJECT_MIN_LENGTH),
        ),
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter query subject'
            },
        )
    )
    message = forms.CharField(
        max_length=MESSAGE_MAX_LENGTH,
        required=True,
        validators=(
            MinLengthValidator(MESSAGE_MIN_LENGTH),
        ),
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter your message'
            },
        ),
    )

    def send_mail(self):
        sender = self.cleaned_data['name']
        message = self.cleaned_data['message']
        subject = self.cleaned_data['subject']
        send_mail(
            f'[Juliany Pizza] FROM:{sender} - {subject}',
            message,
            settings.EMAIL_HOST_USER,
            ['kzborisov94@gmail.com'],
        )
