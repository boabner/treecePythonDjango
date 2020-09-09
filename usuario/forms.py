from django.contrib.auth.forms import UserChangeForm

from treecePythonDjango.models import Usuario
from django import forms


class InsereUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'username',
            'first_name',
            'last_name',
            'celular',
            'telefone',
            'email',
            'password',
            'estadoCivil',
        ]

        def __init__(self, *args, **kwargs):
            super(InsereUsuarioForm, self).__init__(*args, **kwargs)


class UserChangeForm(UserChangeForm):
    # """Overriding visible fields."""
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'celular',
            'estadoCivil',
            'telefone',
            'email',
            'password',
        ]

        def __init__(self, *args, **kwargs):
            super(UserChangeForm, self).__init__(*args, **kwargs)
