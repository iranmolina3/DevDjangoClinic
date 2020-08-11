# Generated by Django 2.0 on 2020-08-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0008_historialcsat_tipocita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('PK_CITA', models.AutoField(primary_key=True, serialize=False)),
                ('NUMERO', models.IntegerField(null=True)),
                ('FECHA_CREACION', models.DateTimeField(auto_now_add=True)),
                ('FECHA_FINALIZACION', models.DateTimeField(auto_now=True)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'ordering': ['NUMERO'],
            },
        ),
    ]
