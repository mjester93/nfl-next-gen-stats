from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    gsis_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.full_name} ({self.gsis_id})"


class PassingStats(models.Model):
    gsis = models.ForeignKey(Player, to_field='gsis_id', on_delete=models.CASCADE)
    season = models.IntegerField()
    season_type = models.CharField(max_length=50)
    week = models.IntegerField()
    position = models.CharField(max_length=10)
    team = models.CharField(max_length=10)
    avg_time_to_throw = models.FloatField(blank=True, null=True)
    avg_completed_air_yards = models.FloatField(blank=True, null=True)
    avg_intended_air_yards = models.FloatField(blank=True, null=True)
    avg_air_yards_differential = models.FloatField(blank=True, null=True)
    aggressiveness = models.FloatField(blank=True, null=True)
    max_completed_air_distance = models.FloatField(blank=True, null=True)
    avg_air_yards_to_sticks = models.FloatField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    pass_yards = models.IntegerField(blank=True, null=True)
    pass_touchdowns = models.IntegerField(blank=True, null=True)
    interceptions = models.IntegerField(blank=True, null=True)
    passer_rating = models.FloatField(blank=True, null=True)
    completions = models.IntegerField(blank=True, null=True)
    completion_percentage = models.FloatField(blank=True, null=True)
    expected_completion_percentage = models.FloatField(blank=True, null=True)
    completion_percentage_above_expectation = models.FloatField(blank=True, null=True)
    avg_air_distance = models.FloatField(blank=True, null=True)
    max_air_distance = models.FloatField(blank=True, null=True)
    player_jersey_number = models.IntegerField(blank=True, null=True)

