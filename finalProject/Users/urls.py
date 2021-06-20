from django.urls import path
from . import views
app_name = 'Users'
urlpatterns = [
    path('', views.registrarse, name="registrarse")

]
