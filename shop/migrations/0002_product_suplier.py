# Generated by Django 3.2.3 on 2021-06-21 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210620_1310'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='suplier',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='suplier', to='users.seller'),
        ),
    ]