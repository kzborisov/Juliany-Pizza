from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestMenuView(TestCase):
    def test_context(self):
        response = self.client.get(reverse('menu'))
        self.assertIsNotNone(response.context['categories'])
