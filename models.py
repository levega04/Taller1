from django.db import models

# Create your models here.
class CentroComercial(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Centros Comerciales"

class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    centro_comercial = models.ForeignKey(CentroComercial, related_name='tiendas', on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - {self.centro_comercial.nombre}"

    class Meta:
        verbose_name_plural = "Locales"

class Archivo(models.Model):
    nombre = models.CharField(max_length=100)
    upload = models.FileField(upload_to="uploads/")

    def __str__(self):
         return self.nombre
    