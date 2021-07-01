from django.shortcuts import render
from django.http import HttpResponse
from .models import componente
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import componentForm
from django.db.models import Q
# Create your views here.
__listObject = list(componente.objects.all())


class index(ListView):
    model = componente
    template_name = 'homePage.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(index, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


class productDetail(DetailView):
    model = componente
    template_name = 'productDetail.html'


class addProduct(CreateView):
    model = componente
    form_class = componentForm
    template_name = 'addProduct.html'


class updateProduct(UpdateView):
    model = componente
    form_class = componentForm
    template_name = 'updateProduct.html'


def searchProducts(request):
    searched = request.POST['searched']
    products = componente.objects.filter(
        nombre__contains=searched) | componente.objects.filter(caracteristica__contains=searched)
    if request.method == 'POST':
        return render(request, "searchProduct.html", {'searched': searched, 'products': products})


def category(request, nombre):
    products = componente.objects.filter(categoria__nombre=nombre)
    return render(request, "searchProduct.html", {'searched': nombre, 'products': products})
