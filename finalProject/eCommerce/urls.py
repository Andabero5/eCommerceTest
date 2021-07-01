from django.urls import path
from . import views
from .views import productDetail, addProduct
urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:pk>', productDetail.as_view(), name="product-detail"),
    path('addProduct/', addProduct.as_view(), name="add-product"),

]
