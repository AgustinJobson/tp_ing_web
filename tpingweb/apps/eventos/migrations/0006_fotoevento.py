# Generated by Django 3.1 on 2020-09-07 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_evento_categoria_evento'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='fotos_eventos')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
            ],
        ),
    ]
