from django.db import models

# Create your models here.

class IngresarFamiliar(models.Model):
    nombre=models.CharField(max_length=50,blank=True,null=True)
    cumple=models.CharField(max_length=10,blank=True,null=True)
    edad  =models.IntegerField(blank=True,null=True)