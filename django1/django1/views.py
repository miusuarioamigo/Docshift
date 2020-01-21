from django.http import HttpResponse
import datetime

def saludo(request):

    return HttpResponse("<html><body><h1>Boats and hoes</h1></body></html>")

def despedida(request):
    
    return HttpResponse("I know what you did last summer!")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    f = "<html><body><h1>Fecha y hora actuales %s</h1></body></html>"% fecha_actual
    return HttpResponse(f)

def calcedad(request,edad, anno):
    # edadActual = 23
    periodo = anno - 2020
    edadFutura = edad + periodo
    doc = "<html><body><h1>Tienes %s annos, en el anno %s tendrás %s annos</h1></body></html>"%(edad,anno,edadFutura)

    return HttpResponse(doc)