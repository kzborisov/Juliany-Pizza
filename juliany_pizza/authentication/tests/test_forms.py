from unittest import mock

from django.contrib.auth import get_user_model
from django.test import TestCase

from juliany_pizza.authentication.forms import UserRegistrationForm, UserPasswordResetForm, UserSetPasswordForm, \
    UserPasswordChangeForm
from juliany_pizza.authentication.models import Profile

UserModel = get_user_model()


class TestUserRegistrationForm(TestCase):
    def test_user_registration_save_user_and_profile(self):
        data = {
            'username': 'test_username',
            'email': 'test@test.com',
            'password1': 'test_pass',
            'password2': 'test_pass'
        }
        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        profile = Profile(user=user)
        self.assertIsNotNone(profile.user.pk)


class TestUserPasswordResetForm(TestCase):
    def test_clean_email__when_email_is_valid__expected_success(self):
        UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
        )
        data = {
            'email': 'test@test.com',
        }
        form = UserPasswordResetForm(data)

        self.assertTrue(form.is_valid())
        email = form.clean_email()
        self.assertEqual('test@test.com', email)

    def test_clean_email__when_email_is_invalid__expected_validation_error(self):
        UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
        )
        data = {
            'email': 'invalid_email@test.com',
        }
        form = UserPasswordResetForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form["email"].errors,
            [UserPasswordResetForm.EMAIL_ERROR_MESSAGE])


class TestUserSetPasswordForm(TestCase):
    @mock.patch('django.contrib.auth.password_validation.password_changed')
    def test_password_set_success(self, password_changed):
        user = UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
            password='TestPassword123@',
        )
        data = {
            'new_password1': 'TestPassword123',
            'new_password2': 'TestPassword123',
        }
        form = UserSetPasswordForm(user, data)
        self.assertTrue(form.is_valid())
        form.save(commit=False)
        self.assertEqual(password_changed.call_count, 0)
        form.save()
        self.assertEqual(password_changed.call_count, 1)


class TestUserPasswordChangeForm(TestCase):
    @mock.patch('django.contrib.auth.password_validation.password_changed')
    def test_password_change_success(self, password_changed):
        user = UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
            password='TestPassword123@',
        )
        data = {
            'old_password': 'TestPassword123@',
            'new_password1': 'NewTestPassword1',
            'new_password2': 'NewTestPassword1'
        }
        form = UserPasswordChangeForm(user, data)
        form.is_valid()
        self.assertTrue(form.is_valid())
        form.save(commit=False)
        self.assertEqual(password_changed.call_count, 0)
        form.save()
        self.assertEqual(password_changed.call_count, 1)
