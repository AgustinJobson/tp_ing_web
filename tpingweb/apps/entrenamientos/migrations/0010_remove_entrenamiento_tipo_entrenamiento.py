# Generated by Django 3.1 on 2020-09-08 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamientos', '0009_auto_20200907_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenamiento',
            name='tipo_entrenamiento',
        ),
    ]
