from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    gsis_id = models.CharField(max_length=20)


class PassingStats(models.Model):
    player = models.ForeignKey('Player', to_field='gsis_id', on_delete=models.CASCADE)
    season = models.IntegerField()
    season_type = models.CharField(max_length=50)
    week = models.IntegerField()
    position = models.CharField(max_length=10)
    team = models.CharField(max_length=10)
    avg_time_to_throw = models.FloatField()
    avg_completed_air_yards = models.FloatField()
    avg_intended_air_yards = models.FloatField()
    avg_air_yards_differential = models.FloatField()
    aggressiveness = models.FloatField()
    max_completed_air_distance = models.FloatField()
    avg_air_yards_to_sticks = models.FloatField()
    attempts = models.IntegerField()
    pass_yards = models.IntegerField()
    pass_touchdowns = models.IntegerField()
    interceptions = models.IntegerField()
    passer_rating = models.FloatField()
    completions = models.IntegerField()
    completion_percentage = models.FloatField()
    expected_completion_percentage = models.FloatField()
    completion_percentage_above_expectation = models.FloatField()
    avg_air_distance = models.FloatField()
    max_air_distance = models.FloatField()
    player_jersey_number = models.IntegerField()

