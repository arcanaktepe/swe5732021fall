# Generated by Django 2.2.1 on 2021-11-22 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0004_auto_20211122_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicecomment',
            old_name='post',
            new_name='service',
        ),
    ]
