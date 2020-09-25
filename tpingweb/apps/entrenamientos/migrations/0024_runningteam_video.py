# Generated by Django 3.1 on 2020-09-25 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrenamientos', '0023_runningteam_youtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='runningteam_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos_runningteams')),
                ('runningteam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrenamientos.runningteam')),
            ],
        ),
    ]
