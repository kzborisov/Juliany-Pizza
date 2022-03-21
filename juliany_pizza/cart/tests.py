from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from juliany_pizza.menu.models import Category, Ingredient, Product, Stock

UserModel = get_user_model()


class TestCartViews(TestCase):
    def setUp(self):
        UserModel.objects.create(username='admin')
        category = Category.objects.create(name='django')
        Ingredient.objects.create(name='test-ingredient')
        product = Product.objects.create(
            name='test-product',
            active=True,
            category=category,
        )
        product_2 = Product.objects.create(
            name='test-product-2',
            active=True,
            category=category,
        )
        Stock.objects.create(
            size='L',
            price=10,
            product=product,
        )
        Stock.objects.create(
            size='Xl',
            price=2,
            product=product_2,
        )

        # Add data to the session
        self.client.post(
            reverse('cart add'),
            {
                'itemId': 1,
                'action': 'post'
            },
            xhr=True,
        )
        self.client.post(
            reverse('cart add'),
            {
                'itemId': 2,
                'action': 'post'
            },
            xhr=True,
        )

    def test_cart_url(self):
        """
        Test cart summary url.
        """
        response = self.client.get(
            reverse('cart summary'),
        )
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """
        Test add to cart.
        """
        response = self.client.post(
            reverse('cart add'),
            {
                'itemId': 1,
                'action': 'post'
            },
            xhr=True,
        )
        self.assertEqual(
            response.json(),
            {
                'qty': 3,
                'subtotal': '22.00',
            }
        )
        response = self.client.post(
            reverse('cart add'),
            {
                'itemId': 2,
                'action': 'post'
            },
            xhr=True,
        )
        self.assertEqual(
            response.json(),
            {
                'qty': 4,
                'subtotal': '24.00',
            }
        )

    def test_cart_delete(self):
        response = self.client.post(
            reverse('cart delete'),
            {
                'itemId': 2,
                'action': 'post'
            },
            xhr=True,
        )
        self.assertEqual(
            response.json(),
            {
                'subtotal': '10.00',
                'qty': 1,
                'final_price': '12.00',
            }
        )

    def test_cart_update(self):
        response = self.client.post(
            reverse('cart update'),
            {
                'itemId': 2,
                'itemQty': 3,
                'action': 'post'
            },
            xhr=True,
        )
        self.assertEqual(
            response.json(),
            {
                'subtotal': '16.00',
                'qty': 4,
                'final_price': '18.00',
                'item_total_price': '6.00',
            }
        )
