# Generated by Django 4.2.4 on 2024-03-17 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_alter_orderdetail_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_boy_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=False, max_length=254)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Delivery Boy Profile',
            },
        ),
    ]
