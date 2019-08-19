import os, pickle, json, requests
from protracker.models import MatchesToGet, Player, RoleToGet
import time
dirname = "D:\Coding\Dotaproject\protracker\databases"
key = ""

def converttime(seconds):
    minutes, seconds = divmod(seconds, 60)
    if minutes <= 10:
        return str("%02d"%minutes) + ":" + str("%02d"%seconds)
    else:
        return str(minutes) + ":" + str("%02d"%seconds)

with open(os.path.join(dirname, "ProPlayerDict.txt"), "rb") as myFile:
    ProPlayerDict = pickle.load(myFile)

def GetProPlayersFromMatch(game):
    players = game['players']
    matchid = game['match_id']
    allplayers = []
    gameinfo = {}
    for index, player in enumerate(players):
        if player['account_id'] in ProPlayerDict.keys():
            allplayers.append({'playername': ProPlayerDict[player['account_id']], 'hero_id': player['hero_id'],'player_slot': index})
            RoleToGet.objects.create(matchtoget = MatchesToGet.objects.get(match_id = matchid), player = Player.objects.get(player_id = player['account_id']), slot = index )
    if allplayers:
        server = game['server_steam_id']
        serverinfo = requests.get("https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1/?key=" + key + "&partner=0&server_steam_id=" + str(server)).text
        if str(server) in serverinfo:
            serverinfo = json.loads(serverinfo)
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
    return gameinfo

intervals = (
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )

def display_time(seconds, granularity=1):
    seconds = time.time() - seconds
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(int(value), name))
    return ', '.join(result[:granularity])