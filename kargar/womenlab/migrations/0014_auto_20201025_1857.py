# Generated by Django 3.1 on 2020-10-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0013_auto_20201025_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='module',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='course',
            name='points',
            field=models.TextField(blank=True, default=''),
        ),
    ]
