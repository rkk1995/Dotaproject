# Generated by Django 2.2 on 2019-08-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protracker', '0015_matchestoget_match_mmr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchestoget',
            name='match_mmr',
            field=models.IntegerField(default=1),
        ),
    ]
