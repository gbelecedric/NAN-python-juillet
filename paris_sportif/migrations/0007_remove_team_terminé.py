# Generated by Django 2.2.3 on 2019-08-02 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paris_sportif', '0006_remove_bet_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='terminé',
        ),
    ]
