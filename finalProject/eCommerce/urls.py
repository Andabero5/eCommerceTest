from django.urls import path
from . import views
from .views import productDetail, addProduct, index, updateProduct
urlpatterns = [
    path('', index.as_view(), name="index"),
    path('product/<int:pk>', productDetail.as_view(), name="product-detail"),
    path('addProduct/', addProduct.as_view(), name="add-product"),
    path('product/edit/<int:pk>', updateProduct.as_view(), name="update-product"),
    path('searchProduct', views.searchProducts, name="search-product"),
    path('category/<str:nombre>', views.category, name="category")

]
