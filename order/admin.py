from django.contrib import admin
from .models import Order, OrderStatus, AcceptOrder
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'created_at', 'update_at']
admin.site.register(Order, OrderAdmin)


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['status']
admin.site.register(OrderStatus, OrderStatusAdmin)

admin.site.register(AcceptOrder)