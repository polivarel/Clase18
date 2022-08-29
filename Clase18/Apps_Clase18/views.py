from django.shortcuts import render
from .models import IngresarFamiliar
from django.http import HttpResponse
from random import *

def crearRandom(request):
    nombres=["Hugo "," Martín "," Lucas "," Mateo "," Leo "," Daniel "," Alejandro "," Pablo "," Manuel"," Álvaro "," Adrián "," David "," Mario "," Enzo "," Diego "," Marcos "," Izan"," Javier "," Marco "," Álex "," Bruno "," Oliver "," Miguel "," Thiago "," Antonio "," Marc "," Carlos "," Ángel "," Juan "," Gonzalo "," Gael "," Sergio "," Nicolás "," Dylan "," Gabriel "," Jorge "," José "," Adam "," Liam "," Eric "," Samuel "," Darío "," Héctor "," Luca "," Iker "," Amir "," Rodrigo "," Saúl "," Víctor "," Francisco "," Iván "," Jesús "," Jaime "," Aarón "," Rubén "," Ian "," Guillermo "," Erik "," Mohamed "," Julen "," Luis "," Pau "," Unai "," Rafael "," Joel "," Alberto "," Pedro "," Raúl "," Aitor "," Santiago "," Rayan "," Pol "," Nil "," Noah "," Jan "," Asier "," Fernando "," Alonso "," Matías "," Biel "," Andrés "," Axel "," Ismael "," Martí "," Arnau "," Imran "," Luka "," Ignacio "," Aleix "," Alan "," Elías "," Omar "," Isaac "," Youssef "," Jon "," Teo "," Mauro "," Óscar "," Cristian "," Leonardo"]
    nombre=choice(nombres)
    edade=choice(range(18,120))

    familiar1=IngresarFamiliar(nombre=nombre,cumple="1984-03-26",edad=edade)
    familiar1.save()
    texto=f"Familiar creado correctamente> {familiar1.nombre} de {familiar1.edad} años de edad. <br> <input type='button' value='Volver' onclick='window.location.href=`/inicio`' >"
    return HttpResponse(texto)

