# Generated by Django 3.1 on 2020-10-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0012_auto_20201025_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='module',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='points',
            field=models.TextField(blank=True, null=True),
        ),
    ]
