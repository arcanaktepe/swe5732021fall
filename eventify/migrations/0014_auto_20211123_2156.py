# Generated by Django 2.2.1 on 2021-11-23 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0013_auto_20211123_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerevent',
            old_name='approved_register',
            new_name='approved_comment',
        ),
        migrations.RenameField(
            model_name='registerservice',
            old_name='approved_register',
            new_name='approved_comment',
        ),
        migrations.RenameField(
            model_name='servicecomment',
            old_name='approved_register',
            new_name='approved_comment',
        ),
    ]
