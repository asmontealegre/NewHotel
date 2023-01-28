
from django.shortcuts import render

# Create your views here.
def reserva(request):
    return render(request, 'reserva/reserva.html')
