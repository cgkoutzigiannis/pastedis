from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUerCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUerCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
