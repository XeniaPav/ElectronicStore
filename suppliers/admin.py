from django.contrib import admin

from suppliers.models import Supplier


@admin.action(description="Обнулить задолженность перед поставщиком")
def reset_debts(modeladmin, request, queryset):
    """Добавление admin action для обнуления задолженности выбранных поставщиков"""
    queryset.update(debts=0.00)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Отображение поставщиков в админке"""

    list_display = (
        "id",
        "name",
        "parent_supplier",
        "debts",
        "level",
        "email",
        "city",
    )
    search_fields = ("name",)
    list_filter = ("city",)
    actions = [reset_debts]
    list_display_links = ["parent_supplier"]
