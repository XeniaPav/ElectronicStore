# Generated by Django 5.1.4 on 2024-12-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0003_contact"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.AddField(
            model_name="supplier",
            name="house_number",
            field=models.CharField(
                blank=True,
                help_text="Введите номер дома",
                null=True,
                verbose_name="Номер дома",
            ),
        ),
    ]
