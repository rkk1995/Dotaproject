# Generated by Django 2.2 on 2019-07-20 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='heros_lost',
        ),
        migrations.RemoveField(
            model_name='match',
            name='heros_won',
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
