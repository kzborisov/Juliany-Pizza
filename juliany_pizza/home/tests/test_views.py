from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from juliany_pizza.authentication.models import Profile
from juliany_pizza.home.forms import ProfileDetailsForm, CustomUserDetailsForm

UserModel = get_user_model()


class TestProfileView(TestCase):
    def test_context(self):
        user = UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
            password='TestPassword123'
        )
        profile = Profile.objects.create(
            first_name='Test',
            last_name='Testov',
            phone='0899999999',
            address='Address 1',
            user=user,
        )

        self.assertTrue(self.client.login(username='test_username', password='TestPassword123'))
        response = self.client.get(reverse('profile', args=[profile.pk]))
        self.assertIsInstance(response.context['profile_form'], ProfileDetailsForm)
        self.assertIsInstance(response.context['user_form'], CustomUserDetailsForm)

    def test_post(self):
        user = UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
            password='TestPassword123'
        )
        profile = Profile.objects.create(
            first_name='Test',
            last_name='Testov',
            phone='0899999999',
            address='Address 1',
            user=user,
        )

        self.assertTrue(self.client.login(username='test_username', password='TestPassword123'))
        data = {
            'first_name': 'Test',
            'last_name': 'Testov',
            'phone': '0899999999',
            'address': 'address',
            'username': 'test_username',
            'email': 'test@test.com',
        }
        response = self.client.post(
            reverse('profile', args=[profile.pk]),
            data,
            format='text/html',
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile', args=[profile.pk]), 302)


class TestContactsView(TestCase):
    def test_contacts_view_valid(self):
        data = {
            'name': 'Test',
            'subject': 'Subject here',
            'message': 'Message here',
        }
        response = self.client.post(
            reverse('contacts'),
            data,
            format='text/html',
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'), 302)
