from django.db import models
from django.urls import reverse
# Create your models here.


class categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class componente(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="images/")
    caracteristica = models.TextField()
    precio = models.CharField(max_length=7)
    categoria = models.ForeignKey(
        categoria, on_delete=models.CASCADE, related_name="tipo")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('index')
