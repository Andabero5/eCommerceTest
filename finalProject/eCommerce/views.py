from django.shortcuts import render
from django.http import HttpResponse
from .models import componente
from django.views.generic import DetailView, CreateView
from .forms import componentForm

# Create your views here.
__listObject = list(componente.objects.all())


def index(request):
    return render(request, "homePage.html", {
        "latestProducts": __listObject[-3:],
        "otherProducts": __listObject[-13:-3]
    })


class productDetail(DetailView):
    model = componente
    template_name = 'productDetail.html'


class addProduct(CreateView):
    model = componente
    form_class = componentForm
    template_name = 'addProduct.html'
