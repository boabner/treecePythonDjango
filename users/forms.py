from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from treecePythonDjango.models import Usuario


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'telefone',
            'celular',
            'estadoCivil',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = '__all__'
