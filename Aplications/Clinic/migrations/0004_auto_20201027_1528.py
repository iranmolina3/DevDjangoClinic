# Generated by Django 2.1 on 2020-10-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0003_auto_20201025_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='municipio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='estado_civil',
            field=models.CharField(blank=True, default='Soltero(a)', max_length=10, null=True),
        ),
    ]