from django.urls import path
from . import views
from .views import productDetail, addProduct, index, updateProduct, addToCart, MyCart, ManageCart, EmptyCartView, deleteProduct, aboutUs, contact
urlpatterns = [
    path('', index.as_view(), name="index"),
    path('product/<int:pk>', productDetail.as_view(), name="product-detail"),
    path('aboutUs/', aboutUs.as_view(), name="about-us"),
    path('contact/', contact.as_view(), name="contact"),
    path('addProduct/', addProduct.as_view(), name="add-product"),
    path('product/edit/<int:pk>', updateProduct.as_view(), name="update-product"),
    path('product/<int:pk>/remove', deleteProduct.as_view(), name="delete-product"),
    path('searchProduct', views.searchProducts, name="search-product"),
    path('category/<str:nombre>', views.category, name="category"),
    path('addToCart/<int:pk>', addToCart.as_view(), name="add-to-cart"),
    path('cart/', MyCart.as_view(), name="cart"),
    path('manageCart/<int:cpId>', ManageCart.as_view(), name="manage-cart"),
    path('emptyCart/', EmptyCartView.as_view(), name="empty-cart"),


]
