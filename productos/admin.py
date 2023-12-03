from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'price', 'stock')
    list_display = ['id', '__str__', 'price', 'stock', 'created_at']

admin.site.register(models.Product, ProductAdmin)