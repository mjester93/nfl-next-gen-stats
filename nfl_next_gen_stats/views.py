from django.shortcuts import render
from .models import *


def player_page(request, gsis_id=None):

    player = get_object_or_404(Player, gsis_id=gsis_id)

    context = {
        'player': player,
        'title': player.full_name
    }

    return render(request, 'nfl_next_gen_stats/player.html', context)
