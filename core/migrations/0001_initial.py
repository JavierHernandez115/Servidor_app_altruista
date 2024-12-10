# Generated by Django 5.1.4 on 2024-12-09 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adulto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('foto', models.ImageField(upload_to='fotos_adultos/')),
                ('fecha_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='core.adulto')),
            ],
        ),
        migrations.CreateModel(
            name='Dirección',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cp', models.CharField(max_length=10)),
                ('referencia', models.TextField()),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='core.adulto')),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vivienda', models.CharField(max_length=255)),
                ('techo', models.CharField(max_length=255)),
                ('piso', models.CharField(max_length=255)),
                ('combustible_cocina', models.CharField(max_length=255)),
                ('num_habitantes', models.IntegerField()),
                ('trabajadores', models.IntegerField()),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudios', to='core.adulto')),
            ],
        ),
        migrations.CreateModel(
            name='Necesidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('necesidad', models.TextField()),
                ('fecha_solicitada', models.DateField()),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='necesidades', to='core.adulto')),
            ],
        ),
        migrations.CreateModel(
            name='Niño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('padres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='core.adulto')),
            ],
        ),
        migrations.CreateModel(
            name='Deseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deseo', models.TextField()),
                ('fecha', models.DateField()),
                ('niño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deseos', to='core.niño')),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('unidad', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('dador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recursos_donados', to='core.adulto')),
            ],
        ),
    ]
