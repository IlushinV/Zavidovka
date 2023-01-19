# Generated by Django 3.2 on 2021-04-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restasite', '0002_remove_menuitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]