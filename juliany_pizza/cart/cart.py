class Cart:
    SESSION_KEY = 'session-key'

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(self.SESSION_KEY)
        if self.SESSION_KEY not in request.session:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add(self, item, size):
        size_id = str(size.id)
        if size_id in self.cart:
            self.cart[size_id]['qty'] += 1
        else:
            self.cart[size_id] = {
                'name': item.name,
                'price': float(size.price),
                'size': size.size,
                'qty': 1,
            }

        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
