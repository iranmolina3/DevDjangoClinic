# Generated by Django 2.1 on 2020-11-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0008_auto_20201102_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedente',
            name='cigarro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='antecedente',
            name='licor',
            field=models.TextField(blank=True, null=True),
        ),
    ]
