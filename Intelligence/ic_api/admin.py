from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ReceivedData

# Register your models here.
# class DataReceivedAdmin(UserAdmin):
#     model = ReceivedData
#     list_display = ["data"]

admin.site.register(ReceivedData)