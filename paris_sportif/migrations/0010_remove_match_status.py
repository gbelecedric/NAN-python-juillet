# Generated by Django 2.2.3 on 2019-08-02 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paris_sportif', '0009_auto_20190802_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='status',
        ),
    ]