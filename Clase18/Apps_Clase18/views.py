from django.shortcuts import render
from .models import IngresarFamiliar
from django.http import HttpResponse
from random import *
from datetime import date,datetime

def crearRandom(request):
    nombres=["Hugo "," Martín "," Lucas "," Mateo "," Leo "," Daniel "," Alejandro "," Pablo "," Manuel"," Álvaro "," Adrián "," David "," Mario "," Enzo "," Diego "," Marcos "," Izan"," Javier "," Marco "," Álex "," Bruno "," Oliver "," Miguel "," Thiago "," Antonio "," Marc "," Carlos "," Ángel "," Juan "," Gonzalo "," Gael "," Sergio "," Nicolás "," Dylan "," Gabriel "," Jorge "," José "," Adam "," Liam "," Eric "," Samuel "," Darío "," Héctor "," Luca "," Iker "," Amir "," Rodrigo "," Saúl "," Víctor "," Francisco "," Iván "," Jesús "," Jaime "," Aarón "," Rubén "," Ian "," Guillermo "," Erik "," Mohamed "," Julen "," Luis "," Pau "," Unai "," Rafael "," Joel "," Alberto "," Pedro "," Raúl "," Aitor "," Santiago "," Rayan "," Pol "," Nil "," Noah "," Jan "," Asier "," Fernando "," Alonso "," Matías "," Biel "," Andrés "," Axel "," Ismael "," Martí "," Arnau "," Imran "," Luka "," Ignacio "," Aleix "," Alan "," Elías "," Omar "," Isaac "," Youssef "," Jon "," Teo "," Mauro "," Óscar "," Cristian "," Leonardo"]
    nombre=choice(nombres) #ELIJO UN NUMERO DE LA LISTA
    
    #GENERO UNA FECHA DE NACIMIENTO ALEATOREA
    anio=str(choice(range(1960,2002)))
    mes=str(choice(range(1,12)))
    if int(mes) < 10:
        mes = "0"+mes
    dia=str(choice(range(1,28)))
    if int(dia) < 10:
        dia = "0"+dia

    nacimiento=str(anio+"-"+mes+"-"+dia)
    
    #CALCULO LA EDAD A PARTIR DE LA FECHA DE HOY MENOS LA ALEATOREA
    edad=date.today().year - datetime.strptime(nacimiento, '%Y-%m-%d').date().year

    familiar1=IngresarFamiliar(nombre=nombre,cumple=nacimiento,edad=edad)
    familiar1.save()
    texto=f"Familiar creado correctamente> {familiar1.nombre} de {familiar1.edad} años de edad. <br> <input type='button' value='Volver' onclick='window.location.href=`/inicio`' >"
    return HttpResponse(texto)

