# Generated by Django 4.2.2 on 2023-07-09 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_articlerequestanswer_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlerequestanswer',
            name='size',
        ),
        migrations.AlterField(
            model_name='articlerequestanswer',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.articlerequest'),
        ),
    ]
