from django.shortcuts import get_object_or_404, render
from .models import *


def player_page(request, gsis_id=None):

    player = get_object_or_404(Player, gsis_id=gsis_id)

    context = {
        'player': player,
        'title': player.full_name,
        'passing_stats': player.passing_stats().order_by('season', 'week')
    }

    return render(request, 'nfl_next_gen_stats/player.html', context)
