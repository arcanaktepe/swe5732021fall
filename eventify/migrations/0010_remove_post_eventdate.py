# Generated by Django 2.2.1 on 2021-11-22 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0009_auto_20211122_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='eventdate',
        ),
    ]