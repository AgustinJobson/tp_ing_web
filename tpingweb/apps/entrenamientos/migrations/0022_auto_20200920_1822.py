# Generated by Django 3.1.1 on 2020-09-20 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamientos', '0021_entrenamiento_tipo_entrenamiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrenamiento',
            name='tipo_entrenamiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='entrenamientos.tipoentrenamiento'),
        ),
    ]