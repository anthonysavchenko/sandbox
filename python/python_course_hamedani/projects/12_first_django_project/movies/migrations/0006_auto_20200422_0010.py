# Generated by Django 2.1.5 on 2020-04-21 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20200422_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='a',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='b',
        ),
    ]