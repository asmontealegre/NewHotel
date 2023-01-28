from django.urls import path
from .views import reserva

urlpatterns = [
    path('reserva/',reserva, name ='reserva'),

]