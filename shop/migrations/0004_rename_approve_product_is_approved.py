# Generated by Django 3.2.3 on 2021-06-23 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_approve'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='approve',
            new_name='is_approved',
        ),
    ]