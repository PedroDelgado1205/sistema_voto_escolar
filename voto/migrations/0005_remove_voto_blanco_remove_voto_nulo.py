# Generated by Django 5.0.6 on 2024-07-21 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0004_remove_voto_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voto',
            name='blanco',
        ),
        migrations.RemoveField(
            model_name='voto',
            name='nulo',
        ),
    ]
