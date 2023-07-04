# Generated by Django 4.2.2 on 2023-07-03 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authorisation', '0006_alter_pickupaddress_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickupaddress',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authorisation.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]