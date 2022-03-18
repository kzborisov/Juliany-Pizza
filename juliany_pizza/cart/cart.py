from juliany_pizza.menu.models import Product


class Cart:
    SESSION_KEY = 'session-key'

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)
        if self.SESSION_KEY not in request.session:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add(self, item):
        """
        Add items to the cart.
        :param item: Menu Item object
        :param size: Size object
        """
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'productId': item.product.id,
                'price': float(item.price),
                'size': item.size if not item.size == '---' else None,
                'qty': 1,
            }
        else:
            self.cart[item_id]['qty'] += 1

        self.session.modified = True

    def __iter__(self):
        """
        Collect the cart keys to query the database and return products
        :return:
        """
        size_ids = self.cart.keys()
        menu_items = Product.objects.filter(size__id__in=size_ids)
        cart = self.cart.copy()
        yield menu_items

    def __len__(self):
        """
        Calculates the items quantity.
        :return: The quantity of all items in the basket.
        """
        return sum(item['qty'] for item in self.cart.values())
