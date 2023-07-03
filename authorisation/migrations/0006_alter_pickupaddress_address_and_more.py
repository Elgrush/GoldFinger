# Generated by Django 4.2.2 on 2023-07-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorisation', '0005_userprofile_address_pickupaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickupaddress',
            name='address',
            field=models.CharField(max_length=1023),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=1023, null=True),
        ),
    ]
