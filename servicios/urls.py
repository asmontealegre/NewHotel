from django.urls import path
from .views import servicios, contacto

urlpatterns = [
    path('servicios/',servicios, name ='servicios'),
    path('contacto/',contacto, name ='contacto'),

]