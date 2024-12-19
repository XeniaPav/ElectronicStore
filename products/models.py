from django.db import models

from suppliers.models import Supplier

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(
            max_length=100,
            verbose_name="Наименование",
            help_text="Введите наименование",)

    version = models.CharField(
            max_length=100,
            verbose_name="Укажите модель",
            **NULLABLE,
            help_text="Укажите модель",)

    release_date = models.DateField(
            verbose_name="дата релиза продукта",
            **NULLABLE,
            help_text="Укажите дату релиза",)

    supplier = models.ForeignKey(
        Supplier,
        verbose_name="Поставщик",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
