from juliany_pizza.menu.models import Product, Stock


class Cart:
    SESSION_KEY = 'session-key'

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)
        if self.SESSION_KEY not in request.session:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add(self, item: Stock):
        """
        Add items to the cart.
        :param item: Stock object
        """
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'id': item_id,
                'price': float(item.price),
                'size': item.size if not item.size == '---' else None,
                'qty': 1,
            }
        else:
            self.cart[item_id]['qty'] += 1

        self.__save()

    def delete(self, item_id: str):
        """
        Remove item from the cart.
        :param item_id: Used as key in the cart
        """
        if item_id in self.cart:
            del self.cart[item_id]
        self.__save()

    def update(self, item_id, item_qty: int):
        """
        Update items in the cart.
        :param item_id: Used as key in the cart.
        :param item_qty: The new quantity of the item in the cart.
        """
        if item_id in self.cart:
            self.cart[item_id]['qty'] = item_qty

        self.__save()

    @property
    def subtotal_price(self):
        """
        Calculate the sum of all products in the cart.
        :return: The total sum of all products
        """
        return sum(self.item_total_price(item) for item in self.cart.values())

    @property
    def total_price(self):
        """
        If the order is less than 10lv, the delivery fee is added to the sum of all products.
        :return: The total sum of all products plus the delivery fee.
        """
        # TODO: # 2 is the delivery fee => In the restaurant app - Restaurant.DELIVERY_FEE
        return self.subtotal_price + 2

    @staticmethod
    def item_total_price(item):
        """
        Calculates the total price of an item in the cart.
        :param item: An item from the cart.
        :return: the sum of the item price multiplied by the item quantity.
        """
        return item['price'] * item['qty']

    def __save(self):
        self.session.modified = True

    def __iter__(self):
        """
        Collect the cart keys to query the database and return products
        :return:
        """
        cart = self.cart.copy()

        for item_id in cart:
            product = Product.objects.get(stock__id=item_id)
            cart[item_id]['product'] = product

        for item in cart.values():
            item['total_price'] = self.item_total_price(item)
            yield item

    def __len__(self):
        """
        Calculates the items quantity.
        :return: The quantity of all items in the basket.
        """
        return sum(item['qty'] for item in self.cart.values())
