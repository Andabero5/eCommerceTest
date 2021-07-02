from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class componente(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="images/")
    caracteristica = models.TextField()
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(
        categoria, on_delete=models.CASCADE, related_name="tipo")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('index')


class carrito(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Carrito: "+str(self.id)


class productoCarrito(models.Model):
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(componente, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return "Carrito: "+str(self.carrito.id) + " Producto: " + str(self.id)
