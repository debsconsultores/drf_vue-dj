from rest_framework import serializers

from .models import Documento, Categoria


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documento
        fields='__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'