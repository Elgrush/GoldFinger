# Generated by Django 4.2.2 on 2023-08-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_catalogitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogitem',
            name='price',
            field=models.CharField(max_length=64),
        ),
    ]
