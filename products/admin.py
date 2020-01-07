from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Product, Offer


class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(ImportExportModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
