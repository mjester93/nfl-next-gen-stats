# Generated by Django 3.1.3 on 2020-11-15 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nfl_next_gen_stats', '0003_auto_20201114_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='RushingStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('season_type', models.CharField(max_length=50)),
                ('week', models.IntegerField()),
                ('position', models.CharField(max_length=10)),
                ('team', models.CharField(max_length=10)),
                ('efficiency', models.FloatField(blank=True, null=True)),
                ('percent_attempts_gte_eight_defenders', models.FloatField(blank=True, null=True)),
                ('avg_time_to_los', models.FloatField(blank=True, null=True)),
                ('rush_attempts', models.IntegerField(blank=True, null=True)),
                ('rush_yards', models.IntegerField(blank=True, null=True)),
                ('expected_rush_yards', models.FloatField(blank=True, null=True)),
                ('rush_yards_over_expected', models.FloatField(blank=True, null=True)),
                ('avg_rush_yards', models.FloatField(blank=True, null=True)),
                ('rush_yards_over_expected_per_att', models.FloatField(blank=True, null=True)),
                ('rush_pct_over_expected', models.FloatField(blank=True, null=True)),
                ('rush_touchdowns', models.IntegerField(blank=True, null=True)),
                ('player_jersey_number', models.IntegerField(blank=True, null=True)),
                ('gsis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfl_next_gen_stats.player', to_field='gsis_id')),
            ],
        ),
    ]
