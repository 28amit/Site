# Generated by Django 3.1 on 2020-10-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0011_course_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='module',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='course',
            name='points',
            field=models.TextField(default=None),
        ),
    ]