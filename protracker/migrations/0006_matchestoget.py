# Generated by Django 2.2 on 2019-07-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protracker', '0005_livematch_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchesToGet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
            ],
        ),
    ]