# Generated by Django 3.1 on 2020-10-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='points',
            field=models.TextField(default=''),
        ),
    ]
