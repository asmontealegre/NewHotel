
from django.shortcuts import render, redirect
from pqrs.forms import PQRSForms
from pqrs.models import PQRS
from django.contrib import messages

# Create your views here.
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
                request, f"Se creo la PQRS exitosamente!"
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
    pqrs= PQRS.objects.get(id=pk)
    pqrs.delete()

    return redirect('pqrs')