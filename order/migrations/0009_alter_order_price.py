# Generated by Django 3.2.3 on 2021-06-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
    ]
