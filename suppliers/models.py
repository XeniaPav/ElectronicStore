from django.db import models

NULLABLE = {"blank": True, "null": True}


class Supplier(models.Model):
    """Модель поставшика"""

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование",
    )
    parent_supplier = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        **NULLABLE,
        help_text="Выберете поставщика",
    )
    debts = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=None,
        verbose_name="Задолженность перед поставщиком",
        **NULLABLE,
        help_text="Введите сумму задолженности",
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        **NULLABLE,
        verbose_name="Время создания",
    )
    LEVEL_ZERO = 0
    LEVEL_FIRST = 1
    LEVEL_SECOND = 2
    LEVEL = [
        (LEVEL_ZERO, "завод"),
        (LEVEL_FIRST, "розничная сеть"),
        (LEVEL_SECOND, "индивидуальный предприниматель"),
    ]
    level = models.IntegerField(
        choices=LEVEL,
        verbose_name="Уровень сети",
        default=0,
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="Введите e-mail",
    )
    country = models.CharField(
        verbose_name="Страна",
        default="Россия",
        help_text="Введите страну",
    )
    city = models.CharField(
        verbose_name="Город",
        **NULLABLE,
        help_text="Введите Город",
    )
    street = models.CharField(
        verbose_name="Улица",
        **NULLABLE,
        help_text="Введите улицу",
    )
    house_number = models.CharField(
        verbose_name="Номер дома",
        **NULLABLE,
        help_text="Введите номер дома",
    )

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name
