# Generated by Django 4.2.2 on 2023-09-20 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0003_ventasdet_venta_ventasenc_fecha_venta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventasdet',
            old_name='precio_prv',
            new_name='valor_prv',
        ),
    ]