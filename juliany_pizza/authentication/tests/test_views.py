from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestUserRegistrationView(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.user = UserModel(
            username='test_username',
            email='test@test.com',
            password='TestPassword',
        )

    def test_page_viewed_correct(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_user_can_register(self):
        data = {
            'username': 'test_username',
            'email': 'test@test.com',
            'password': 'TestPassword',
        }
        response = self.client.post(
            self.register_url,
            data,
            format='text/html',
        )
        self.assertEqual(response.status_code, 200)
