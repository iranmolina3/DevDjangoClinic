# Generated by Django 2.1 on 2020-10-25 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0002_auto_20201024_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='fk_municipio',
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
    ]
