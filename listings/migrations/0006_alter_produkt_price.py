# Generated by Django 4.1 on 2022-09-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_produkt_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
    ]
