# Generated by Django 3.1 on 2020-10-07 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0007_course_slug'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='course',
            index_together={('id', 'slug')},
        ),
    ]