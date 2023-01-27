from django.shortcuts import render, redirect
from habitacion.forms import HabitacionForm

# Create your views here.
def habitacion(request):
    return render(request, 'habitacion/habitacion.html')

def crearHabitacion(request):
    if request.method == 'POST':
        habitacion_form =  HabitacionForm(request.POST)
        if habitacion_form.is_valid():
            habitacion_form.save()
            return redirect()
    else:
        habitacion_form = HabitacionForm()
    return redirect(request, 'habitacion/crear_habitacion.html', {'habitacion_form':habitacion_form})