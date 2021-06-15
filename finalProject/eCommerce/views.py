from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

latestProducts = ["carro", "Moto", "Camion"]
otherProducts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def index(request):
    return render(request, "a.html", {
        "latestProducts": latestProducts,
        "otherProducts": otherProducts
    })
