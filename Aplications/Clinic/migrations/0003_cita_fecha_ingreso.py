# Generated by Django 2.0 on 2020-09-10 02:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0002_auto_20200909_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='FECHA_INGRESO',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
