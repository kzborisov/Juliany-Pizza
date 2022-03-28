from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from juliany_pizza.authentication.models import Profile

UserModel = get_user_model()


class TestProfileModel(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Test',
        'last_name': 'Testov',
        'phone': '0899999999',
        'address': 'test address',
    }

    def test_profile_create__when_valid_phone_format__expected_success(self):
        user = UserModel.objects.create(
            username='test_username',
            email='test@test.com',
        )
        profile = Profile(
            **self.VALID_USER_DATA,
            user=user,
        )

        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_phone__when_phone_has_more_digits__expected_to_fail(self):
        user = UserModel.objects.create(
            username='test_username',
            email='test@test.com',
        )
        phone = '08999999991'
        profile = Profile(
            phone=phone,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_phone__when_phone_has_less_digits__expected_to_fail(self):
        user = UserModel.objects.create(
            username='test_username',
            email='test@test.com',
        )
        phone = '089999999'
        profile = Profile(
            phone=phone,
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expected_correct_ful_name(self):
        profile = Profile(
            **self.VALID_USER_DATA
        )
        full_name = f"{self.VALID_USER_DATA['first_name']} {self.VALID_USER_DATA['last_name']}"
        self.assertEqual(full_name, profile.full_name)

    def test_profile_full_name__when_only_first_name__expected_empty_string(self):
        profile = Profile(
            first_name=self.VALID_USER_DATA['first_name'],
        )
        self.assertEqual('', profile.full_name)

    def test_profile_full_name__when_only_last_name__expected_empty_string(self):
        profile = Profile(
            last_name=self.VALID_USER_DATA['last_name'],
        )
        self.assertEqual('', profile.full_name)

    def test_profile_str__expected_full_name(self):
        profile = Profile(
            **self.VALID_USER_DATA
        )
        full_name = f"{self.VALID_USER_DATA['first_name']} {self.VALID_USER_DATA['last_name']}"
        self.assertEqual(full_name, str(profile))
