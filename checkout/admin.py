from django.contrib import admin
from .models import Order, OrderItem


# class to enable non-editable fields to display
# for content upload model
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'order_number',
        'order_date',
    )

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
