# Generated by Django 4.2.2 on 2023-07-04 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorisation', '0008_userprofile_middle_name_userprofile_name_and_more'),
        ('webapp', '0003_factory_alter_articleorder_size'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleOrder',
            new_name='ArticleRequest',
        ),
    ]