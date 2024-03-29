# Generated by Django 4.1 on 2022-08-31 21:06

from django.db import migrations, models
import django.db.models.deletion
import listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=1, max_digits=8)),
                ('short_description', models.TextField(max_length=600)),
                ('long_description', models.TextField(max_length=600)),
                ('primary_img', models.ImageField(upload_to=listings.models.img_path)),
                ('primary_alt', models.CharField(max_length=200)),
                ('img1', models.ImageField(blank=True, null=True, upload_to=listings.models.img_path)),
                ('img1_alt', models.CharField(blank=True, max_length=200, null=True)),
                ('img2', models.ImageField(blank=True, null=True, upload_to=listings.models.img_path)),
                ('img2_alt', models.CharField(blank=True, max_length=200, null=True)),
                ('img3', models.ImageField(blank=True, null=True, upload_to=listings.models.img_path)),
                ('img3_alt', models.CharField(blank=True, max_length=200, null=True)),
                ('img4', models.ImageField(blank=True, null=True, upload_to=listings.models.img_path)),
                ('img4_alt', models.CharField(blank=True, max_length=200, null=True)),
                ('stock', models.IntegerField()),
                ('eta', models.IntegerField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brand', to='listings.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to=listings.models.img_path_sub_category)),
                ('img_alt', models.CharField(max_length=200)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_category', to='listings.main_category')),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rozmery_sirka', models.IntegerField()),
                ('rozmery_delka', models.IntegerField()),
                ('varianta_img', models.ImageField(blank=True, null=True, upload_to=listings.models.img_path_varianta)),
                ('barva', models.CharField(max_length=200)),
                ('barva_img', models.ImageField(blank=True, null=True, upload_to=listings.models.img_path_barva)),
                ('eanv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='eanv', to='listings.produkt')),
                ('product_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_name', to='listings.produkt')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
                ('img', models.ImageField(upload_to=listings.models.img_path_sub_sub_category)),
                ('img_alt', models.CharField(max_length=200)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_category_to_sub', to='listings.main_category')),
                ('sub_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategory', to='listings.sub_category')),
            ],
        ),
        migrations.AddField(
            model_name='produkt',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='listings.sub_category'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='ean',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ean', to='listings.brand'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mistnosti', to='listings.main_category'),
        ),
        migrations.AddField(
            model_name='produkt',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategory', to='listings.sub_sub_category'),
        ),
    ]
