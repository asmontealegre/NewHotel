from django.urls import path, include
from usuarios.views import usuarios
from django.contrib import admin
from administracion.views import administracion, ayuda, loggedIn,logout, logout_user
from django.contrib.auth.views import LoginView as login
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("",login.as_view(),name="inicio"),
    path('',usuarios,name="usuarios"),
    path('adm/', administracion,name='index-admin'),
    path('Ayuda',ayuda,name="ayuda"),


    path('loggedin/',loggedIn,name="inicio-sesion"),
    path('logout/',logout,name="fin-sesion"),
    path('logout/',logout_user,name="logout"),
    path('',auth_views.LoginView.as_view(),name='inicio'),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/enviar',auth_views.PasswordResetDoneView.as_view(),name='pass_reset_done'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='pass_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='pass_reset_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    

]