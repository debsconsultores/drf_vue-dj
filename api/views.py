from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from .models import Documento, Categoria, SubCategoria, Producto, \
    Proveedor, ComprasEnc, ComprasDet, Cliente

from .serializer import DocumentoSerializer, CategoriaSerializer, \
    SubCategoriaSerializer, ProductoSerializer, \
    ProveedorSerializer, \
    ComprasDetSerializer, ComprasSerializer, \
    ClienteSerializer




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


class ProveedorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer



class ComprasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasEnc.objects.all().order_by('id')
    serializer_class = ComprasSerializer


class ComprasDetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ComprasDet.objects.all().order_by('id')
    serializer_class = ComprasDetSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by('nombre')
    serializer_class = ClienteSerializer