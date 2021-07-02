from django.contrib import admin
from .models import categoria, componente, carrito, productoCarrito

# Register your models here.
admin.site.register(categoria)
admin.site.register(componente)
admin.site.register(carrito)
admin.site.register(productoCarrito)
