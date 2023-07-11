# Generated by Django 4.2.2 on 2023-07-10 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_alter_articlerequest_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='JeweleryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='articlerequest',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='webapp.jewelerytype'),
            preserve_default=False,
        ),
    ]
