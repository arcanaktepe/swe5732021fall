# Generated by Django 2.2.1 on 2021-11-22 11:02

import eventify.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0002_post_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=eventify.models.upload_post_to),
        ),
    ]
