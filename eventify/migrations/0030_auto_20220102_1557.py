# Generated by Django 2.2.1 on 2022-01-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventify', '0029_auto_20220102_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Conference', 'Conference'), ('Workshop', 'Workshop'), ('Themed_parties', 'Themed party'), ('Webinar', 'Webinar'), ('Summit', 'Summit'), ('Music festival', 'Music festival')], default='Seminar', max_length=20),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('Seminar', 'Seminar'), ('Conference', 'Conference'), ('Workshop', 'Workshop'), ('Themed_parties', 'Themed party'), ('Webinar', 'Webinar'), ('Summit', 'Summit'), ('Music festival', 'Music festival')], default='Seminar', max_length=20),
        ),
    ]
