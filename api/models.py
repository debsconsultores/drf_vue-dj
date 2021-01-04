from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models


class ModeloEdit(models.Model):
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True


class Documento(models.Model):
    nombre = models.CharField(
        max_length = 50,
        null = False,
        blank = False,
        unique = True
    )

    expira = models.DateField()
    alerta1y = models.BooleanField(default=True)
    alerta6m = models.BooleanField(default=True)
    alerta3m = models.BooleanField(default=True)
    alerta1m = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Documento,self).save()
    
    class Meta:
        verbose_name_plural = "Documentos"


class Categoria(models.Model):
    descripcion = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.descripcion
    
    def save(self, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural= "Categorías"


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    def __str__(self):
        return "{}-{}".format(self.categoria,self.descripcion)
    
    def save(self, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub Categorías"
        unique_together=("categoria","descripcion")


class Producto(models.Model):
    codigo = models.CharField(
        max_length=10,null=False,blank=False
    )
    descripcion = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    existencia = models.IntegerField(default=0)
    precio = models.FloatField(default=0)
    subcategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
    
    def save(self, **kwargs):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural= "Productos"


class Proveedor(models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    telefono = models.CharField(max_length=20,null=True,blank=True)
    email = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nombre
    
    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural= "Proveedores"


class ComprasEnc(ModeloEdit):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    fecha = models.DateField(null=False,blank=False)

    def __str__(self):
        return str(self.id)

    
    class Meta:
        verbose_name_plural= "Encabezados de Compras"


class ComprasDet(ModeloEdit):
    cabecera = models.ForeignKey(ComprasEnc,related_name='detalle',on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0)

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    descuento = models.FloatField(default=0)

    @property
    def total(self):
        return self.subtotal - self.descuento
    
    def __str__(self):
        return '{}-{}-{}'.format(self.id,self.cabecera,self.producto)

    class Meta:
        verbose_name_plural= "Detalles de Compras"


class Cliente(models.Model):
    nombre = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True
    )
    telefono = models.CharField(max_length=20,null=True,blank=True)
    email = models.TextField(null=True,blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural= "Clientes"



class FacturaEnc(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha = models.DateField()

    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural= "Encabezados de Factura"


class FacturaDet(models.Model):
    cabecera = models.ForeignKey(FacturaEnc,related_name='detalle',on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=0)
    precio = models.FloatField(default=0)

    @property
    def subtotal(self):
        return self.cantidad * self.precio

    descuento = models.FloatField(default=0)

    @property
    def total(self):
        return self.subtotal - self.descuento

    def __str__(self):
        return '{}-{}'.format(self.cabecera,self.producto)

    class Meta:
        verbose_name_plural = "Detalles de Factura"


# Signals de Compra
@receiver(post_save,sender=ComprasDet)
def vigila_guardar_detalle_compra(sender,instance,**kwargs):
    id_producto = instance.producto.id

    # print(id_producto,instance.cantidad)
    prod = Producto.objects.get(id = id_producto)
    if prod:
        prod.existencia = int(prod.existencia) + int(instance.cantidad)
        prod.save()


@receiver(post_delete,sender=ComprasDet)
def vigila_eliminar_detalle_compra(sender,instance,**kwargs):
    id_producto = instance.producto.id
    
    prod = Producto.objects.filter(id = id_producto).first()
    if prod:
        prod.existencia -= int(instance.cantidad)
        prod.save()