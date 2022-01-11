from django.contrib import admin
from .models import Client

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number']
admin.site.register(Client, ClientAdmin)