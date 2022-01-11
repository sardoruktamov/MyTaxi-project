from django.contrib import admin
from driver.models import Driver

class DriveAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'car_number', 'phone_number']
admin.site.register(Driver, DriveAdmin)
