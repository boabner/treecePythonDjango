from django.contrib import admin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from treecePythonDjango.models import Usuario


# Register your models here.
@admin.register(Usuario)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Usuario
    list_display = ('email', 'name', 'is_active')
