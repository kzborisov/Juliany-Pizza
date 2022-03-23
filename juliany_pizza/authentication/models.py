from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, RegexValidator, validate_email
from django.db import models
from django.db.models import OneToOneField


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    email = models.EmailField(
        'email address',
        unique=True,
        validators=[validate_email],
        error_messages={
            'unique': "An account with that email already exists.",
        },
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
    )
    is_active = models.BooleanField(
        'active',
        default=True,
    )
    date_joined = models.DateTimeField(
        'date joined',
        auto_now_add=True,
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    PHONE_NUMBER_MAX_LENGTH = 10

    ADDRESS_MAX_LENGTH = 1024

    phone_message = 'Phone number must be entered in the format: 0899999999'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH)
        ],
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH)
        ],
        null=True,
        blank=True,
    )
    phone = models.CharField(
        validators=[
            RegexValidator(
                regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
                message=phone_message,
            )
        ],
        max_length=PHONE_NUMBER_MAX_LENGTH,
        null=True,
        blank=True,
    )
    address = models.CharField(
        "Address",
        max_length=ADDRESS_MAX_LENGTH,
    )

    user = OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        editable=False,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else ""

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
