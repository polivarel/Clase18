from django.http import HttpResponse
from django.template import Template
from django.template import Context, loader

def inicio(request):
    return HttpResponse("Inicio")

def test(request):
    test = loader.get_template('test.html')
    documento = test.render("Pagina de Prueba")
    return HttpResponse(documento)