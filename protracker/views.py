from django.shortcuts import render, redirect
from django.http import HttpResponse
from protracker.ProTrackerFunctions import converttime
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

    return render(request, 'protracker.jinja', {'livematches': currentgames, 'HeroImageDict': HeroImageDict, 'totalmatches' : totalmatches, 'mostgames' : top16gamesplayed, 'highestwinrate': top16winrates} )

def player(request, player_name):
    a = LiveMatch.objects.get(counter=1).myList
    currentgames = json.decoder.JSONDecoder().decode(a)
    a = time.time()
    playermatches = Match.objects.filter(role__player = Player.objects.get(player_name__iexact = player_name), match_date__gte = time.time() - 604800)
    player = Player.objects.get(player_name__iexact = player_name)
    return render(request, 'protrackerplayerpage.jinja', {'livematches': currentgames, 'HeroImageDict': HeroImageDict , 'player_name' : player_name, 'player': player} )

