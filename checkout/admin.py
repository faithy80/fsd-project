from django.contrib import admin
from .models import Order, OrderItem


# class to enable non-editable fields to display
# for content upload model
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_number',
        'order_total',
        'order_date',
    )

class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_reference',
        'product_name',
        'price',
        'quantity',
    )

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
