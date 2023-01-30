

from django.urls import path

from administracion.views import administracion

urlpatterns = [

    path('adm/', administracion,name='index-admin'),
]
    