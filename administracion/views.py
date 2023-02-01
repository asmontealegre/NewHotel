from django.shortcuts import render
from django.contrib.auth import logout
from habitacion.models import Habitacion
from reserva.models import Reserva
from usuarios.models import Usuario
from pqrs.models import PQRS

# Create your views here.


def login(request):
    context={   
    }
    return render(request,'registration/login.html',context)

def ayuda(request):
    context={   
    }
    return render(request,'administracion/ayuda.html',context)

def usuarios(request):
    titulo="Usuarios"
    context={
        'titulo':titulo
    }
    return render(request,'usuarios/usuarios.html',context)


def error_404(request,exception):
    return page_not_found(request,'404.html')


def loggedIn(request):
    if request.user.is_authenticated:
        respuesta:"Ingresado como "+ request.user.username
    else:
        respuesta:"No estas autenticado."
    return HttpResponse(respuesta)


def logout_user(request):
    logout(request)
    return redirect("registration/login.html")


def administracion(request):
    titulo="Tablero Principal"
    
   
    context={
        'titulo': titulo,
       
       
    }
    return render(request,'administracion/index-admin.html',context)
