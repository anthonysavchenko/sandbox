# Generated by Django 2.1.5 on 2020-04-21 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200421_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='stars',
        ),
    ]