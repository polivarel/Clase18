from django.db import models

# Create your models here.

class IngresarFamiliar(models.Model):
    nombre=models.CharField(max_length=50,blank=True,null=True)
    cumple=models.CharField(max_length=10,blank=True,null=True)
    edad  =models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"\n----------------------------------------------------------\nSe creo correctamente el familiar {self.nombre}. \nEdad: {self.edad} \nCumpleaños:{self.cumple}\n----------------------------------------------------------\n"


familiar1=IngresarFamiliar("Pablo","1984/02/07")        