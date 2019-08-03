from django.shortcuts import render, redirect
from django.http import HttpResponse
from protracker.ProTrackerFunctions import converttime, time, display_time
import requests, json, os, pickle
from protracker.models import LiveMatch, MatchesToGet, Match, Hero, Player, Role
from django.db.models import Count
import time
dirname = os.path.dirname(__file__) + "/databases"

with open(os.path.join(dirname, "HeroImageDict.txt"), "rb") as myFile:
    HeroImageDict = pickle.load(myFile)

key = "BDAECC2049E139D32D5D7AEDEFC23304"


def index(request):
    a = LiveMatch.objects.get(counter=1).myList
    currentgames = json.decoder.JSONDecoder().decode(a)
    totalmatches = Match.objects.all().count()
    top16winrates = sorted(Hero.objects.all(), key=lambda m: m.winrate, reverse = True)[:16]
    top16gamesplayed = sorted(Hero.objects.all(), key=lambda m: m.totalgames, reverse = True)[:16]

    return render(request, 'protracker.jinja', {'livematches': currentgames, 'HeroImageDict': HeroImageDict, 'totalmatches' : totalmatches, 'mostgames' : top16gamesplayed, 'highestwinrate': top16winrates, 'all_players':Player.objects.all()} )

def player(request, player_name):
    a = LiveMatch.objects.get(counter=1).myList
    currentgames = json.decoder.JSONDecoder().decode(a)
    player = Player.objects.get(player_name__iexact = player_name)
    playermatches = Match.objects.filter(role__player = player, match_date__gte = time.time() - 604800)
    playerrecentmatches = []
    for match in playermatches:
        win = match.role_set.get(player=player).win
        a = match.role_set.all()
        teammates = a.exclude(player = player).filter(win = win)
        opponents = a.exclude(player = player).filter(win = not win)
        playerrecentmatches.append({'match_id':match.match_id, 'mmr': match.match_mmr, 'win': win , 'hero':match.role_set.get(player=player).hero.hero_id, 'gamedate': display_time(match.match_date), 'teammates': teammates if teammates.count() > 0 else False, 'opponents': opponents if opponents.count() > 0 else False} )   
    print(playerrecentmatches)
    return render(request, 'protrackerplayerpage.jinja', {'livematches': currentgames, 'HeroImageDict': HeroImageDict ,  'player': player, 'playermatches' : playerrecentmatches, 'all_players':Player.objects.all()} )
