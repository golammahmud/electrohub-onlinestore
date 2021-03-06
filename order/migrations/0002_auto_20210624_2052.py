# Generated by Django 3.2.3 on 2021-06-24 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_suplier'),
        ('users', '0014_auto_20210620_1310'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ManyToManyField(related_name='orders', to='users.Seller'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_paid', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='users.seller')),
            ],
        ),
    ]
