# Generated by Django 4.2.2 on 2023-07-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_jewelerytype_articlerequest_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=32)),
                ('size', models.CharField(max_length=32)),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
    ]
