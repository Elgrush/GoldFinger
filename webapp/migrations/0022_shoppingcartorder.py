# Generated by Django 4.2.2 on 2023-08-08 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorisation', '0011_delete_shoppingcart'),
        ('webapp', '0021_catalogitem_created_at_catalogitem_factory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatalogItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.catalogitem')),
                ('UserProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authorisation.userprofile')),
            ],
        ),
    ]