# Generated by Django 2.2.1 on 2022-01-01 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0028_auto_20220102_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='address',
        ),
        migrations.RemoveField(
            model_name='service',
            name='address',
        ),
    ]
