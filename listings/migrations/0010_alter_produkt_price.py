# Generated by Django 4.1 on 2022-09-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_produkt_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='price',
            field=models.IntegerField(),
        ),
    ]