# Generated by Django 5.1.4 on 2024-12-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0004_delete_contact_supplier_house_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supplier",
            name="level",
        ),
    ]