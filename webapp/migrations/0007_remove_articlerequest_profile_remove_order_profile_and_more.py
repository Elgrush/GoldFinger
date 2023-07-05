# Generated by Django 4.2.2 on 2023-07-05 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0006_articlerequest_created_at_articlerequest_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlerequest',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='order',
            name='profile',
        ),
        migrations.AddField(
            model_name='articlerequest',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
