# Generated by Django 4.1 on 2022-11-13 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_produkt_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]