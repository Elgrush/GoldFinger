# Generated by Django 4.2.2 on 2023-07-31 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_remove_catalogitem_photo_catalogitemimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitem',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
