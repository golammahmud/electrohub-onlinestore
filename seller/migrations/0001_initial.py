# Generated by Django 3.2.3 on 2021-06-20 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.IntegerField(default=0)),
                ('currency', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('del_price', models.CharField(blank=True, max_length=50, null=True)),
                ('offers_price', models.CharField(blank=True, max_length=60, null=True)),
                ('product_type', models.CharField(blank=True, choices=[('New', 'New'), ('Latest', 'Latest')], max_length=70, null=True)),
                ('stock', models.IntegerField(blank=True, default=1, null=True)),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, height_field='height', upload_to='shop/product/images', width_field='width')),
                ('num_visits', models.IntegerField(default=0)),
                ('last_visit', models.DateTimeField(blank=True, null=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sproducts', to='shop.subcategory')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='seller.sellerproduct')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(height_field='height', upload_to='shop/product/images', width_field='width')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seller.sellerproduct')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.TextField(blank=True, null=True, verbose_name='feature')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seller.sellerproduct')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.TextField(blank=True, null=True, verbose_name='facility')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='seller.sellerproduct')),
            ],
        ),
    ]
