# Generated by Django 2.2.3 on 2019-08-02 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paris_sportif', '0010_remove_match_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mise',
            name='author',
        ),
        migrations.RemoveField(
            model_name='mise',
            name='is_bet',
        ),
        migrations.RemoveField(
            model_name='bet',
            name='team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='cote',
        ),
        migrations.AddField(
            model_name='bet',
            name='match',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bet',
            name='somme',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='coteone',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='cotetwo',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='scoreone',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='scoretwo',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='finish',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='is_win',
        ),
        migrations.DeleteModel(
            name='mise',
        ),
    ]
