# Generated by Django 4.2.2 on 2023-07-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_catalogitem_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitemimage',
            name='image',
            field=models.ImageField(default=None, upload_to='images'),
            preserve_default=False,
        ),
    ]
