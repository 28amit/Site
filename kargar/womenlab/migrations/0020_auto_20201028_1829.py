# Generated by Django 3.1 on 2020-10-28 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0019_remove_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]