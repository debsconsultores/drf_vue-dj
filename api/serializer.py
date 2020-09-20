from rest_framework import serializers

from .models import Documento, Categoria, \
    SubCategoria


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documento
        fields='__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'


class SubCategoriaSerializer(serializers.ModelSerializer):
    cat_descripcion = serializers.ReadOnlyField(source='categoria.descripcion')
    class Meta:
        model=SubCategoria
        # fields='__all__'
        fields = ("id","categoria","descripcion","cat_descripcion")