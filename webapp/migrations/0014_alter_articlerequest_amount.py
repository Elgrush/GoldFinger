# Generated by Django 4.2.2 on 2023-07-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_remove_articlerequestanswer_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlerequest',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
