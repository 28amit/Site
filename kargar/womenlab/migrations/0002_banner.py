# Generated by Django 3.1 on 2020-10-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('womenlab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('banner', models.ImageField(upload_to='banner/')),
            ],
        ),
    ]
