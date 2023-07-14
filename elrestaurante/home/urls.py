from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("contacto", views.contacto, name="contacto"),
    path("sucursales", views.sucursales, name="sucursales"),
    path("carta", views.carta, name="carta"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("blog", views.blog, name="blog"),
    path("buscadorcomidas", views.buscadorcomidas, name="buscadorcomidas"),
]