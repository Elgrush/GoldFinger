# Generated by Django 4.2.2 on 2023-08-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_alter_catalogitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerequestanswer',
            name='price',
            field=models.CharField(default=9999999999999999999, max_length=64),
            preserve_default=False,
        ),
    ]
