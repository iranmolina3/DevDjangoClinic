# Generated by Django 2.1 on 2020-11-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0007_auto_20201102_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='motivo_consulta',
            field=models.TextField(max_length=200),
        ),
    ]