from treecePythonDjango.models import Usuario
from django import forms


class RecuperarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'email'
        ]
