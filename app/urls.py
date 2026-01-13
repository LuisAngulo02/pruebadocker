from django.contrib import admin
from django.urls import path
from .views import productoList, productoCrear, productoup, productodelete
urlpatterns = [
    path("", productoList.as_view(),name="producto_list"),
    path("nuevo", productoCrear.as_view(),name="producto_crear"),
    path("editar/<int:pk>", productoup.as_view(),name="producto_editar"),
    path("borrar/<int:pk>", productodelete.as_view(),name="producto_borrar"),
]