from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import CentroComercial, Tienda, Archivo

@admin.register(CentroComercial)
class CentroComercialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'telefono')
    search_fields = ('nombre', 'direccion') 

@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'centro_comercial')
    search_fields = ('nombre', 'direccion')
    list_filter = ('centro_comercial',)
    raw_id_fields = ('centro_comercial',)

@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
