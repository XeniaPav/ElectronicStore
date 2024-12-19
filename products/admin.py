from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "version", "supplier")
    list_filter = ("supplier",)
    search_fields = ("name",)
    list_display_links = ["supplier"]
