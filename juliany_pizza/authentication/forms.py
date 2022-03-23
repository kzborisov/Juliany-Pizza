from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm, PasswordChangeForm, \
    AuthenticationForm
from django.core.exceptions import ValidationError

from juliany_pizza.authentication.models import CustomUser, Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'username@example.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(user=user)
        if commit:
            profile.save()

        return user


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'validate',
                'placeholder': 'Email',
            },
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            },
        ),
    )


class UserPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not UserModel.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("Invalid Email! Inactive or Nonexistent User")
        return email


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        self.fields['new_password2'].label = "Confirm New password"
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Enter your new password'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm your new password'})


class UserPasswordChangeForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': 'Invalid password! Please try again.'
    }

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].help_text = None
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        self.fields['new_password2'].label = "Confirm New password"
        self.fields['old_password'].widget.attrs.update({'placeholder': 'Enter your current password'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Enter your new password'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirm your new password'})
