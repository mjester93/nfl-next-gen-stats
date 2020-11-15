from bulk_sync import bulk_sync
from django.core.management.base import BaseCommand, CommandError
from ...models import Player, PassingStats
import pandas as pd
import requests
import time

NAME_COLUMNS = ['player_first_name', 'player_last_name', 'player_display_name', 'player_short_name', 'player_gsis_id']

class Command(BaseCommand):
    help = 'Imports NGS from the github data page'
    
    def handle(self, *args, **options):
        years = [2016, 2017, 2018, 2019, 2020]

        for year in years:
            current_passing_data = pd.read_csv(
                "https://github.com/mrcaseb/nfl-data/blob/master/data/ngs/ngs_" + year +"_passing.csv.gz?raw=True",
                compression='gzip', 
                low_memory=False,
            )

            final_passing_data = final_passing_data.append(current_passing_data, sort=True)
            
            # TODO ADD RUSHING AND RECEIVER URLS

        #Give each row a unique index
        final_passing_data.reset_index(drop=True, inplace=True)

        passing_players = final_passing_data[NAME_COLUMNS]
        print(passing_players)

