# Generated by Django 3.1 on 2020-09-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamientos', '0016_auto_20200908_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenamiento',
            name='tipo_entrenamiento',
        ),
    ]