from django import forms
from .models import Habitacion
from .models import TipoHabitacion

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['sede', 'numeroHabitacion','disponibilidad','TipoHabitacion_id' ]

class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = ['nombreHabitacion', 'capacidad', 'cantidad', 'valor', 'descripcion']