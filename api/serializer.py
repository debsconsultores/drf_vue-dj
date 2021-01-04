from rest_framework import serializers

from .models import Documento, Categoria, \
    SubCategoria, Producto, Proveedor, \
    ComprasDet, ComprasEnc, \
    Cliente, FacturaDet, FacturaEnc


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


class ProductoSerializer(serializers.ModelSerializer):
    scat_descripcion = serializers.ReadOnlyField(source='subcategoria.descripcion')
    class Meta:
        model=Producto
        # fields='__all__'
        fields = ("id","codigo","descripcion","existencia", \
            "precio","subcategoria","scat_descripcion")


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proveedor
        fields='__all__'



class ComprasDetSerializer(serializers.ModelSerializer):
    producto_descripcion = serializers.ReadOnlyField(source='producto.descripcion')
    class Meta:
        model=ComprasDet
        fields=['cabecera','id','producto','cantidad','precio','subtotal','descuento', 
        'total',"producto_descripcion"]


class ComprasSerializer(serializers.ModelSerializer):
    detalle= ComprasDetSerializer(many=True, read_only=True)

    class Meta:
        model = ComprasEnc
        fields = ['id','proveedor','fecha', 'detalle']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'



class FacturasDetSerializer(serializers.ModelSerializer):
    producto_descripcion = serializers.ReadOnlyField(source='producto.descripcion')
    class Meta:
        model=FacturaDet
        fields=['cabecera','id','producto','cantidad','precio','subtotal','descuento','total',"producto_descripcion"]


class FacturasSerializer(serializers.ModelSerializer):
    detalle = FacturasDetSerializer(many=True, read_only=True)
    class Meta:
        model = FacturaEnc
        fields = ['id','cliente','fecha', 'detalle']

