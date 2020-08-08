from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Documento
from .serializer import DocumentoSerializer



def prueba(request):
    return HttpResponse("Primera Vista del Curso")



class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Documento.objects.all().order_by('id')
    serializer_class = DocumentoSerializer