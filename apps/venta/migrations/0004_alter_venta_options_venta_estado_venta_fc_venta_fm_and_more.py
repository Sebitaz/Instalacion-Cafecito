# Generated by Django 4.2.2 on 2023-09-15 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venta', '0003_alter_venta_cliente_delete_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name_plural': 'Ventas'},
        ),
        migrations.AddField(
            model_name='venta',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]