# Generated by Django 4.2.4 on 2024-03-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_delivery_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_order',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
