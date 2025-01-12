from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserRegisterForm

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active']

admin.site.register(CustomUser, CustomUserAdmin)