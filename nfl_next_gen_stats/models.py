from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)
    gsis_id = models.CharField(max_length=20, unique=True)

    def passing_stats(self):
        return PassingStats.objects.filter(gsis_id=self.gsis_id)

    def rushing_stats(self):
        return RushingStats.objects.filter(gsis_id=self.gsis_id)

    def receiving_stats(self):
        return ReceivingStats.objects.filter(gsis_id=self.gsis_id)

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

class RushingStats(models.Model):
    gsis = models.ForeignKey(Player, to_field='gsis_id', on_delete=models.CASCADE)
    season = models.IntegerField()
    season_type = models.CharField(max_length=50)
    week = models.IntegerField()
    position = models.CharField(max_length=10)
    team = models.CharField(max_length=10)
    efficiency = models.FloatField(blank=True, null=True)
    percent_attempts_gte_eight_defenders = models.FloatField(blank=True, null=True)
    avg_time_to_los = models.FloatField(blank=True, null=True)
    rush_attempts = models.IntegerField(blank=True, null=True)
    rush_yards = models.IntegerField(blank=True, null=True)
    expected_rush_yards = models.FloatField(blank=True, null=True)
    rush_yards_over_expected = models.FloatField(blank=True, null=True)
    avg_rush_yards = models.FloatField(blank=True, null=True)
    rush_yards_over_expected_per_att = models.FloatField(blank=True, null=True)
    rush_pct_over_expected = models.FloatField(blank=True, null=True)
    rush_touchdowns = models.IntegerField(blank=True, null=True)
    player_jersey_number = models.IntegerField(blank=True, null=True)

class ReceivingStats(models.Model):
    gsis = models.ForeignKey(Player, to_field='gsis_id', on_delete=models.CASCADE)
    season = models.IntegerField()
    season_type = models.CharField(max_length=50)
    week = models.IntegerField()
    position = models.CharField(max_length=10)
    team = models.CharField(max_length=10)
    player_jersey_number = models.IntegerField(blank=True, null=True)
    avg_cushion = models.FloatField(blank=True, null=True)
    avg_separation = models.FloatField(blank=True, null=True)
    avg_intended_air_yards = models.FloatField(blank=True, null=True)
    percent_share_of_intended_air_yards = models.FloatField(blank=True, null=True)
    receptions = models.IntegerField(blank=True, null=True)
    targets = models.IntegerField(blank=True, null=True)
    catch_percentage = models.FloatField(blank=True, null=True)
    yards = models.IntegerField(blank=True, null=True)
    rec_touchdowns = models.IntegerField(blank=True, null=True)
    avg_yac = models.FloatField(blank=True, null=True)
    avg_expected_yac = models.FloatField(blank=True, null=True)
    avg_yac_above_expectation = models.FloatField(blank=True, null=True)
