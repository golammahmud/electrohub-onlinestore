# Generated by Django 3.2.3 on 2021-06-06 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 18, 54, 11, 335737, tzinfo=utc)),
        ),
    ]