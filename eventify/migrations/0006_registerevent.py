# Generated by Django 2.2.1 on 2021-11-22 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventify', '0005_auto_20211122_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postregister', to='eventify.Post')),
            ],
        ),
    ]
