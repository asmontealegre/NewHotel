from django.shortcuts import render

# Create your views here.
def administracion(request):
    titulo="Tablero Principal"
    context={
        'titulo': titulo,
    }
    return render(request,'administracion/index-admin.html',context)