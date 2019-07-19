from django.shortcuts import render, redirect
from django.http import HttpResponse
from protracker.services.ProTrackerFunctions import converttime
import requests, json, os, pickle

dirname = os.path.dirname(__file__) + "/databases"

with open(os.path.join(dirname, "HeroImageDict.txt"), "rb") as myFile:
    HeroImageDict = pickle.load(myFile)

with open(os.path.join(dirname, "ProPlayerDict.txt"), "rb") as myFile:
    ProPlayerDict = pickle.load(myFile)

key = "BDAECC2049E139D32D5D7AEDEFC23304"


def GetProPlayersFromMatch(data):
    game = data
    players = data['players']
    allplayers = []
    gameinfo = {}
    for index, player in enumerate(players):
        if player['account_id'] in ProPlayerDict.keys():
            allplayers.append({'playername': ProPlayerDict[player['account_id']], 'hero_id': player['hero_id'],'player_slot': index})
    if allplayers:
        server = game['server_steam_id']
        serverinfo = json.loads(requests.get("https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1/?key=" + key + "&partner=0&server_steam_id=" + str(server)).text)
        teams = serverinfo['teams']
        for player in allplayers:
            if player['player_slot'] <= 4:
                playerslot = player['player_slot']
                team = 0
            else:
                playerslot = player['player_slot'] - 5
                team = 1
            playerprofile = teams[team]['players'][playerslot]
            player.update([ ('kills', playerprofile['kill_count']), ('deaths', playerprofile['death_count']), ('assists', playerprofile['assists_count']), ('level', playerprofile['level'])])
        gameinfo.update([ ('server_steam_id', game['server_steam_id']) , ('average_mmr', game['average_mmr']) , ('game_time', converttime(game['game_time'])), ('radiant', game['radiant_score']), ('dire', game['dire_score']), ('Pro_Players', allplayers) ] )
    print(gameinfo)
    return gameinfo

def index(request):

    r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=" + key + "&partner=0")
    livematches = json.loads(r.text)['game_list']
    currentgames = []

    for i in livematches:
        total = GetProPlayersFromMatch(i)
        if total:
            currentgames.append(total)

    return render(request, 'protracker.jinja', {'livematches': currentgames, 'HeroImageDict': HeroImageDict} )
