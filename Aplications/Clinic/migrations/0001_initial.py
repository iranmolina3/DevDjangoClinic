# Generated by Django 2.0 on 2020-09-09 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('PK_ANTECEDENTES', models.AutoField(primary_key=True, serialize=False)),
                ('ULTIMA_REGLA', models.DateTimeField(blank=True, null=True)),
                ('FECHA_PROBABLE_PARTO', models.DateTimeField(blank=True, null=True)),
                ('GESTA_INICIO', models.DateTimeField(blank=True, null=True)),
                ('ABORTO', models.DateTimeField(blank=True, null=True)),
                ('HIJOS_VIVOS', models.IntegerField(blank=True, null=True)),
                ('PESO', models.IntegerField(blank=True, null=True)),
                ('QUIRURGICO', models.TextField(blank=True, null=True)),
                ('MEDICO', models.TextField(blank=True, null=True)),
                ('ALERGIA', models.TextField(blank=True, null=True)),
                ('FAMILIAR', models.TextField(blank=True, null=True)),
                ('HABITO', models.TextField(blank=True, null=True)),
                ('CIGARRO', models.TextField(blank=True, null=True)),
                ('LICOR', models.TextField(blank=True, null=True)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Antecedente',
                'verbose_name_plural': 'Antecedentes',
            },
        ),
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
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('PK_CONSULTA', models.AutoField(primary_key=True, serialize=False)),
                ('MOTIVO_CONSULTA', models.CharField(max_length=200)),
                ('HISTORIA', models.TextField()),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ['MOTIVO_CONSULTA'],
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('PK_ESTADO_CIVIL', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=25)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'verbose_name_plural': 'Estados Civiles',
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='ExamenFisico',
            fields=[
                ('PK_EXAMEN_FISICO', models.AutoField(primary_key=True, serialize=False)),
                ('PRESION_ARTERIAL', models.IntegerField()),
                ('FRECUENCIA_CARDIACA', models.IntegerField()),
                ('FRECUENCIA_RESPIRATORIA', models.IntegerField()),
                ('TEMPERATURA', models.IntegerField()),
                ('FRECUENCIA_CARDIACA_FETAL', models.IntegerField()),
                ('IMPRESION_CLINCIA', models.TextField()),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Examene Fisico',
                'verbose_name_plural': 'Examenes Fisicos',
            },
        ),
        migrations.CreateModel(
            name='HistorialCsat',
            fields=[
                ('PK_HISTORIAL_CSAT', models.AutoField(primary_key=True, serialize=False)),
                ('RESPUESTA', models.IntegerField()),
                ('FECHA_CREACION', models.DateField(auto_now_add=True)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'HistorialCsat',
                'verbose_name_plural': 'HistorialCsat',
                'ordering': ['FECHA_CREACION'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('PK_MUNICIPIO', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=25)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('PK_PERSONA', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('APELLIDO', models.CharField(max_length=50)),
                ('DPI', models.CharField(default='Menor de edad', max_length=14)),
                ('EDAD', models.IntegerField()),
                ('FECHA_NACIMIENTO', models.DateField()),
                ('TELEFONO', models.CharField(blank=True, max_length=9, null=True)),
                ('GENERO', models.CharField(max_length=10)),
                ('DIRECCION', models.CharField(blank=True, max_length=200, null=True)),
                ('ESTADO', models.BooleanField(default=True)),
                ('FK_ESTADO_CIVIL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.EstadoCivil')),
                ('FK_MUNICIPIO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.Municipio')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['FECHA_NACIMIENTO'],
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('PK_PREGUNTA', models.AutoField(primary_key=True, serialize=False)),
                ('DESCRIPCION', models.CharField(max_length=200)),
                ('FECHA_CREACION', models.DateField(auto_now_add=True)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
                'ordering': ['FECHA_CREACION'],
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('PK_ROL', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del rol')),
                ('NOMBRE', models.CharField(max_length=25, verbose_name='Nombre del rol')),
                ('ESTADO', models.BooleanField(default=True, verbose_name='Estado activo/incativo')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='TipoCita',
            fields=[
                ('PK_TIPO_CITA', models.AutoField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo Cita',
                'verbose_name_plural': 'Tipos Citas',
                'ordering': ['NOMBRE'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('PK_USUARIO', models.AutoField(primary_key=True, serialize=False)),
                ('CARNET', models.CharField(max_length=60)),
                ('CONTRASENIA', models.CharField(max_length=25)),
                ('FECHA_CREACION', models.DateField(auto_now_add=True)),
                ('CORREO', models.EmailField(blank=True, default='nocorreo@dominio.com', max_length=254, null=True)),
                ('ESTADO', models.BooleanField(default=True)),
                ('FK_PERSONA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.Persona')),
                ('FK_ROL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.Rol')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['FECHA_CREACION'],
            },
        ),
        migrations.AddField(
            model_name='historialcsat',
            name='FK_PREGUNTA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.Pregunta'),
        ),
    ]
