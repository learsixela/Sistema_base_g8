from django.db import models

# Create your models here.
#https://docs.djangoproject.com/en/5.0/topics/db/models/

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion= models.DateTimeField()
    duracion = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    cliente_activo = models.BooleanField(default=True)


class Direccion(models.Model):
    cliente = models.OneToOneField(Cliente,blank=False,null=False,on_delete=models.CASCADE)

    calle = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)

''' ManyToMany'''

class Libro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    libros = models.ManyToManyField(Libro, related_name="autores")
#tabla relacionar para agregar campos extras
class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    creado_por = models.CharField(max_length=50, null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)