# Generated by Django 5.0.4 on 2024-04-12 08:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoProcessor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processedvideo',
            name='time_stamp',
        ),
        migrations.RemoveField(
            model_name='processedvideo',
            name='video_file',
        ),
        migrations.AddField(
            model_name='processedvideo',
            name='axvspan',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processedvideo',
            name='pareto',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
