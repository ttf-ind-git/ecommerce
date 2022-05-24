from django.contrib import admin

# Register your models here.
from .models import *

admin.site.site_header = 'Ecom Admin'

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('static/admin/css/admin/base.css',)
        }

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
