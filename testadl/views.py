from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Pelicula, Cliente

# Create your views here.
def index(request):
    peli = Pelicula(titulo = 'Matrix',
                        descripcion='Pelicula de Neo', 
                        fecha_creacion='2020-01-01 12:00:00',
                        duracion='2',
                        )
    
    #peli.save()# insert into pelicula

    #select * from peliculas;
    lista_peliculas = Pelicula.objects.all()

    for pelicula in lista_peliculas:
        print(pelicula.titulo)

    #select * from peliculas WHERE titulo = 'Titanic';
    peli2 = Pelicula.objects.filter(titulo = 'Titanic')
    print("Pelicula con filter ",peli2)  

    #select * from peliculas WHERE id = 2;
    pelicula_unica = Pelicula.objects.get(id=2)
    #update o actualizacion de un registro
    pelicula_unica.duracion = 3
    #pelicula_unica.save()

    #exclude
    peli_exclude = Pelicula.objects.exclude(titulo = 'Titanic')


    messages.add_message(request,messages.SUCCESS,'esto es un mensaje de tipo INFO')

    messages.success(request,'esto es un mensaje de tipo SUCCESS',extra_tags='error 1')
    messages.error(request,'esto es un mensaje de tipo ERROR',extra_tags='alert-danger')
    
    # class={{message.tags}}

    return HttpResponse("Creacion correcta de Pelicula")


def cliente(request):
    lista_clientes  = Cliente.objects.all()

#get
#if request.method =='GET':
    context = {
        'lista_clientes': lista_clientes,
    }

    return render(request,"cliente.html",context)

def guardar_cliente(request):
#post
#if request.method =='POST':
    pnombre = request.POST['nombre']
    papellido = request.POST['apellido']
    pedad = request.POST['edad']
    pemail = request.POST['email']
    
    cliente = Cliente(nombre=request.POST['nombre'],apellido= papellido, edad= pedad, email= pemail )
    cliente.save()

    return redirect("cliente")

def editar_cliente(request):
    pass
#un metodo que despliegue el template 
#un metodo que capture el formulario(si existiese el formulario)

def eliminar_cliente(request):
    pass