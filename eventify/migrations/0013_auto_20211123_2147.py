# Generated by Django 2.2.1 on 2021-11-23 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventify', '0012_auto_20211122_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerevent',
            old_name='approved_comment',
            new_name='approved_register',
        ),
        migrations.RenameField(
            model_name='servicecomment',
            old_name='approved_comment',
            new_name='approved_register',
        ),
        migrations.CreateModel(
            name='RegisterService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_register', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceregister', to='eventify.Service')),
            ],
        ),
    ]
