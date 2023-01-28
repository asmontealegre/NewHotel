from django.urls import path
from .views import crearHabitacion, habitacion

urlpatterns = [

    path('habitacion/',habitacion, name = 'habitacion'),
    path('crear_habitacion/',crearHabitacion, name='crear_habitacion'),
]