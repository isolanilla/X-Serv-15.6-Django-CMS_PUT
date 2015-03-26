from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cms(request, recurso):

    if request.method == "GET":
        try:
            clave = Pages.objects.get(name=recurso)
            return HttpResponse("nombre: " + clave.name + " " + clave.page)

        except Pages.DoesNotExist:
            return HttpResponseNotFound("No encontrado recurso: " + recurso)

    if request.method == "PUT":
        p = Pages(name=recurso, page=request.body)
        p.save()
        return HttpResponse("Pagina guardada: " + request.body)
