# Generated by Django 3.1 on 2020-09-27 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0005_comentario_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]