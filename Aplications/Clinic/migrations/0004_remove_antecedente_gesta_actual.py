# Generated by Django 2.0 on 2020-09-09 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0003_auto_20200908_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antecedente',
            name='GESTA_ACTUAL',
        ),
    ]