from .models import componente, carrito


class Cart:
    def __init__(self, user, product):
        self.cart = carrito()
        self.cart.usuario = user
        self.cart.product = product
        self.cart.cantidad = 1
        self.cart.save()
