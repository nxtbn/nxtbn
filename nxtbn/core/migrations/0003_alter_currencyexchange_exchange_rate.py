# Generated by Django 4.2.11 on 2024-05-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_currencyexchange_exchange_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyexchange',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]