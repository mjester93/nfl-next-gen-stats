from bulk_sync import bulk_sync
from django.core.management.base import BaseCommand, CommandError
from ...models import Player, PassingStats
import pandas as pd
import requests
import time

pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)

NAME_COLUMNS = ['first_name', 'last_name', 'full_name', 'short_name', 'gsis_id']
PASS_STATS_TO_REMOVE = ['first_name', 'last_name', 'full_name', 'short_name']

class Command(BaseCommand):
    help = 'Imports NGS from the github data page'
    
    def handle(self, *args, **options):
        years = [2016, 2017, 2018, 2019, 2020]
        final_passing_data = pd.DataFrame()
        final_rushing_data = pd.DataFrame()
        final_receiving_data = pd.DataFrame()

        for year in years:
            current_passing_data = pd.read_csv(
                f"https://github.com/mrcaseb/nfl-data/blob/master/data/ngs/ngs_{year}_passing.csv.gz?raw=True",
                compression='gzip', 
                low_memory=False,
            )

            final_passing_data = final_passing_data.append(current_passing_data, sort=True)
            
            # TODO ADD RUSHING AND RECEIVER URLS

        #Give each row a unique index
        final_passing_data.reset_index(drop=True, inplace=True)
        # Changing the column names
        final_passing_data = final_passing_data.rename(
            columns = {
                "player_first_name": "first_name",
                "player_last_name": "last_name",
                "player_display_name": "full_name", 
                "player_short_name": "short_name",
                "player_gsis_id": "gsis_id",
                "player_position": "position",
                "team_abbr": "team",
            }
        )

        # Getting all players
        passing_players = final_passing_data[NAME_COLUMNS].drop_duplicates(subset=['gsis_id'], keep='last')
        
        # TODO COMBINE RUSHING AND RECEIVING PLAYERS 
        # TO GET A UNIQUE PLAYERS ACROSS ALL THREE
        players = passing_players

        # Adding players to database; if they exist, update them
        new_players = [Player(**vals) for vals in players.to_dict('records')]
        key_fields = ('gsis_id', )
        ret = bulk_sync(new_models=new_players, filters=None, key_fields=key_fields, skip_deletes=True)

        # Adding passing stats to database; if they exist, update them
        final_passing_data = final_passing_data.drop(columns=PASS_STATS_TO_REMOVE)
        new_passing_data = [PassingStats(**vals) for vals in final_passing_data.to_dict('records')]
        key_fields = ('gsis_id', 'season', 'week')
        ret = bulk_sync(new_models=new_passing_data, filters=None, key_fields=key_fields, skip_deletes=True)
