# Generated by Django 5.1.4 on 2024-12-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="create_time",
            field=models.DateTimeField(
                auto_created=True, blank=True, null=True, verbose_name="Время создания"
            ),
        ),
    ]