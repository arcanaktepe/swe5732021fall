# Generated by Django 2.2.1 on 2022-01-02 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0033_auto_20220102_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='eventtime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='service',
            name='eventtime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
