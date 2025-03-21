# Generated by Django 5.0.6 on 2024-07-04 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dignidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('funciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('lema', models.TextField()),
                ('logo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estudiante.estudiante')),
                ('dignidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.dignidad')),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidato.lista')),
            ],
        ),
    ]
