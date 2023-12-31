# Generated by Django 4.2.2 on 2023-07-03 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authorisation', '0008_userprofile_middle_name_userprofile_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorisation.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=31)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('amount', models.IntegerField(blank=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorisation.userprofile')),
            ],
        ),
    ]
