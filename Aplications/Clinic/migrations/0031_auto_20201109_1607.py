# Generated by Django 2.1 on 2020-11-09 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0030_auto_20201109_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['pk_servicio'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
