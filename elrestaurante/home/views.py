from django.shortcuts import render
from .models import Comida
# Create your views here.
def index(request):
    comidas=Comida.objects.all()
    return render(request,"index.html", context={ "comidas": comidas})
def contacto(request):
    comidas=Comida.objects.all()
    return render(request,"contacto.html", context={ "comidas": comidas})
def sucursales(request):
    comidas=Comida.objects.all()
    return render(request,"sucursales.html", context={ "comidas": comidas})
def carta(request):
    comidas=Comida.objects.all()
    return render(request,"carta.html", context={ "comidas": comidas})
def blog(request):
    comidas=Comida.objects.all()
    return render(request,"blog.html", context={ "comidas": comidas})
def nosotros(request):
    comidas=Comida.objects.all()
    return render(request,"nosotros.html", context={ "comidas": comidas})
def buscadorcomidas(request):
    comidas=Comida.objects.all()
    return render(request,"buscadorcomidas.html", context={ "comidas": comidas})