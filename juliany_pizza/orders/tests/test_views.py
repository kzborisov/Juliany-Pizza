from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from juliany_pizza.authentication.models import Profile

UserModel = get_user_model()


class TestPlaceOrderView(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='test_username',
            email='test@test.com',
            password='TestPassword123'
        )
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='Testov',
            phone='0899999999',
            address='Address 1',
            user=self.user,
        )

    def test_order_form_initial_data__when_user_is_logged_in(self):
        self.assertTrue(self.client.login(username='test_username', password='TestPassword123'))
        response = self.client.get(reverse('place order'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form']['full_name'].value(), 'Test Testov')

    def test_order_form_initial_data__when_user_is_not_logged_in(self):
        response = self.client.get(reverse('place order'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form']['full_name'].value(), '')
