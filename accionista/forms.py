from models import Accionista
from django import forms

class FormularioCrear(forms.ModelForm):
    class Meta:
        model = Accionista
        fields = [
            'nombres',
            'apellidos',
            'run',
            'totalAcciones',
            'nacionalidad',
            'direccion',
            'telefono',
            'email',
            'accionistas']
