# Generated by Django 4.2.2 on 2023-08-17 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_alter_catalogitem_size'),
        ('authorisation', '0013_shoppingcartorder_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCartRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('ArticleRequestAnswer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.articlerequestanswer')),
                ('UserProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorisation.userprofile')),
            ],
        ),
    ]
