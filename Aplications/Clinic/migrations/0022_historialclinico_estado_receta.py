# Generated by Django 2.1 on 2020-11-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0021_receta_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialclinico',
            name='estado_receta',
            field=models.BooleanField(default=False),
        ),
    ]