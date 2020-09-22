from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Documento, Categoria, SubCategoria, Producto

from .serializer import DocumentoSerializer, CategoriaSerializer, \
    SubCategoriaSerializer, ProductoSerializer



def prueba(request):
    return HttpResponse("Primera Vista del Curso")



class DocumentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Documento.objects.all().order_by('id')
    serializer_class = DocumentoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Categoria.objects.all().order_by('descripcion')
    serializer_class = CategoriaSerializer


class SubCategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubCategoria.objects.all().order_by('descripcion')
    serializer_class = SubCategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Producto.objects.all().order_by('descripcion')
    serializer_class = ProductoSerializer