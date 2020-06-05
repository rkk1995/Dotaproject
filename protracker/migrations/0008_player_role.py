# Generated by Django 2.2 on 2019-07-27 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protracker', '0007_auto_20190723_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField()),
                ('player_name', models.CharField(default='Dota 2 Player', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.BooleanField()),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protracker.Hero')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protracker.Match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protracker.Player')),
            ],
        ),
    ]