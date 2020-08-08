from django.db import models

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

