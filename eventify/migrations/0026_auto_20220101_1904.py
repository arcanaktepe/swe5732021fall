# Generated by Django 2.2.1 on 2022-01-01 16:04

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0025_auto_20220101_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='41.088165, 29.043431', max_length=63),
        ),
        migrations.AlterField(
            model_name='service',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='41.088165, 29.043431', max_length=63),
        ),
    ]
