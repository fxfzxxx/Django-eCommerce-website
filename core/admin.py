from django.contrib import admin
from .models import Item, Order, OrderItems, Payment, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp']


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Coupon)
