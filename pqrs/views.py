
from django.shortcuts import render, redirect
from pqrs.forms import PQRSForms
from django.contrib.auth.decorators import login_required, permission_required
from pqrs.models import PQRS


from django.contrib import messages
# Create your views here.
@login_required
def pqrs(request):
    titulo="Buzón de Pqrs"
    form= PQRSForms()
    pqrs=PQRS.objects.all()
    context={
        'titulo':titulo,
        'pqrs':pqrs,
        'form':form
    }
    return render(request,'pqrs/pqrs.html',context)
 


def pqrs_registrada(request):
    titulo="PQRS Registradas"
    if request.method == "POST":
        form= PQRSForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,f"Se Creo la PQRS exitosamente!"
            )
            return redirect("pqrs-registrada")
        else:
            form=PQRSForms(request.POST)
    else:
        form=PQRSForms()
    context={
        'titulo':titulo,
        'form': form
    }
    return render(request,'pqrs/pqrs-registrada.html',context)

def pqrs_eliminar(request, pk):
    titulo="Pqrs - Eliminar"
    pqrs= PQRS.objects.all()

    PQRS.objects.filter(id=pk).update(
            estado='0'
        )
    messages.success(
                request,f"Se elimino la PQRS exitosamente!"
            )
    return redirect('pqrs')
        
   
    context={
        'pqrs':pqrs,
        'titulo':titulo,
     
    }
    return render(request,'pqrs/pqrs.html',context)





   
