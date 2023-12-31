# Generated by Django 4.2.2 on 2023-07-04 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_rename_articleorder_articlerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlerequest',
            name='factory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.factory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlerequest',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlerequest',
            name='size',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
