# Generated by Django 4.2.4 on 2024-03-18 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delivery_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery_order',
            name='address',
        ),
    ]
