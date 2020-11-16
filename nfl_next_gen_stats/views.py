from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import *


def home(request):
    return render(request, 'nfl_next_gen_stats/home.html')


def player_page(request, gsis_id=None, season=None):

    player = get_object_or_404(Player, gsis_id=gsis_id)
    passing_stats = player.passing_stats().order_by('season', 'week')
    rushing_stats = player.rushing_stats().order_by('season', 'week')
    receiving_stats = player.receiving_stats().order_by('season', 'week')

    context = {
        'player': player,
    }

    if season:
        context.update({
            'title': f"{player.full_name} -- {season}",
            'season': season,
            'passing_stats': passing_stats.filter(~Q(week=0), season=season),
            'rushing_stats': rushing_stats.filter(~Q(week=0), season=season),
            'receiving_stats': receiving_stats.filter(~Q(week=0), season=season),
        })

    else:
        context.update({
            'title': player.full_name,
            'passing_stats': passing_stats.filter(week=0),
            'rushing_stats': rushing_stats.filter(week=0),
            'receiving_stats': receiving_stats.filter(week=0),
        })

    return render(request, 'nfl_next_gen_stats/player.html', context)
