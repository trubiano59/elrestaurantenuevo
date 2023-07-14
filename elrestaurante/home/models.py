from django.db import models

# Create your models here.
class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    ingredientes= models.CharField(max_length=100)
    precio=models.FloatField()
    INGREDIENTES = [("Pastas", "Pastas"), ("Pizzas", "Pizzas"), ("Hamburguesas", "Hamburguesas"), 
("Ensaladas", "Ensalada"), ("Empanadas", "Empanadas"), ("Panchos", "Panchos"), ("Bifes", "Bifes"), ("Chorizos", "Chorizos"), ("Milanesas", "Milanesas") 
]
    categoria=models.CharField(max_length=100,choices=INGREDIENTES)
    def __str__(self) -> str:
        return self.nombre
    