# Generated by Django 2.2.1 on 2021-11-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0010_remove_post_eventdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='eventdate',
            field=models.DateField(null=True),
        ),
    ]
