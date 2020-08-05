from django.shortcuts import render
from django.http import HttpResponse


def prueba(request):
    return HttpResponse("Primera Vista del Curso")

