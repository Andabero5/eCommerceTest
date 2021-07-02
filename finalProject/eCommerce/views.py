from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import componente, carrito, productoCarrito
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, View, DeleteView
from .forms import componentForm
from django.urls import reverse_lazy
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


class deleteProduct(DeleteView):
    model = componente
    template_name = 'deleteProduct.html'
    success_url = reverse_lazy('index')


class aboutUs(TemplateView):
    template_name = "aboutUs.html"


class contact(TemplateView):
    template_name = "contact.html"


def searchProducts(request):
    searched = request.POST['searched']
    products = componente.objects.filter(
        nombre__contains=searched) | componente.objects.filter(caracteristica__contains=searched)
    if request.method == 'POST':
        return render(request, "searchProduct.html", {'searched': searched, 'products': products})


def category(request, nombre):
    products = componente.objects.filter(categoria__nombre=nombre)
    return render(request, "searchProduct.html", {'searched': nombre, 'products': products})


class addToCart(TemplateView):
    template_name = "addToCart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productId = self.kwargs['pk']
        productObj = componente.objects.get(id=productId)
        cartId = self.request.session.get("cart_Id", None)
        if cartId:
            cartObj = carrito.objects.get(id=cartId)
            productInCart = cartObj.productocarrito_set.filter(
                producto=productObj)
            if productInCart.exists():
                cartProduct = productInCart.last()
                cartProduct.cantidad += 1
                cartProduct.subtotal += productObj.precio
                cartProduct.save()
                cartObj.total += productObj.precio
                cartObj.save()
            else:
                cartProduct = productoCarrito.objects.create(carrito=cartObj,
                                                             producto=productObj,
                                                             precio=productObj.precio,
                                                             cantidad=1,
                                                             subtotal=productObj.precio)
                cartObj.total += productObj.precio
                cartObj.save()
        else:
            cartObj = carrito.objects.create(total=0)
            self.request.session["cart_Id"] = cartObj.id
            artProduct = productoCarrito.objects.create(carrito=cartObj,
                                                        producto=productObj,
                                                        precio=productObj.precio,
                                                        cantidad=1,
                                                        subtotal=productObj.precio)
            cartObj.total += productObj.precio
            cartObj.save()
        return context


class MyCart(TemplateView):
    template_name = "myCart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cartId = self.request.session.get("cart_Id", None)
        if cartId:
            cart = carrito.objects.get(id=cartId)
        else:
            cart = None
        context['cart'] = cart
        return context


class ManageCart(View):
    def get(self, request, *args, **kwargs):
        cpId = self.kwargs['cpId']
        action = request.GET.get('action')
        cpObj = productoCarrito.objects.get(id=cpId)
        cartObj = cpObj.carrito
        if action == "inc":
            cpObj.cantidad += 1
            cpObj.subtotal += cpObj.precio
            cpObj.save()
            cartObj.total += cpObj.precio
            cartObj.save()
        elif action == "dec":
            cpObj.cantidad -= 1
            cpObj.subtotal -= cpObj.precio
            cpObj.save()
            cartObj.total -= cpObj.precio
            cartObj.save()
            if cpObj.cantidad == 0:
                cpObj.delete()
        elif action == "rmv":
            cartObj.total -= cpObj.subtotal
            cartObj.save()
            cpObj.delete()

        return redirect("cart")


class EmptyCartView(View):
    def get(self, request, *args, **kwargs):
        cartId = self.request.session.get("cart_Id", None)
        if cartId:
            cart = carrito.objects.get(id=cartId)
            cart.productocarrito_set.all().delete()
            cart.total = 0
            cart.save()
        else:
            cart = None
        return redirect("cart")
