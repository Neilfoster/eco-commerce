from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


class OrderlineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderlineAdminInline, )


admin.site.register(Order, OrderAdmin)
