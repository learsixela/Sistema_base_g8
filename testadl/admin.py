from django.contrib import admin
from .models import Pelicula, Cliente, Direccion,Libro,Autor,AutorLibro
# Register your models here.
admin.site.register(Pelicula)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['cliente_id','nombre','apellido','edad','email','cliente_activo']


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Direccion)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(AutorLibro)