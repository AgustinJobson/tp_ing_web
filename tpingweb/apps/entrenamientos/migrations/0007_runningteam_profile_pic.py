# Generated by Django 3.1 on 2020-09-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamientos', '0006_runningteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='runningteam',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_runningteams'),
        ),
    ]