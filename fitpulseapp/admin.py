from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display= ('rut', 'nombre', 'apellido', 'email', 'telefono', 'fecha_registro')
    search_fields = ('rut','nomnbre', 'apellido')
    list_filter = ('fecha_registro',)


# Register your models here.
admin.site.register(Cliente, ClienteAdmin)