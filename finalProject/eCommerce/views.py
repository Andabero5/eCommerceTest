from django.shortcuts import render
from django.http import HttpResponse
from .models import componente

# Create your views here.

latestProducts = ["carro", "Moto", "Camion"]
otherProducts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
__listObject = list(componente.objects.all())


def index(request):
    return render(request, "homePage.html", {
        "latestProducts": __listObject[-3:],
        "otherProducts": __listObject[-10:]
    })
