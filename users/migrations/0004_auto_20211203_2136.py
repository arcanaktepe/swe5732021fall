# Generated by Django 2.2.1 on 2021-12-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211203_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='credits',
            field=models.IntegerField(default=6),
        ),
    ]
