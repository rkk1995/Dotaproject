import os, pickle, json, requests

dirname = "d:/Coding/test/mysite/polls/databases"
key = "BDAECC2049E139D32D5D7AEDEFC23304"

def converttime(seconds):
    minutes, seconds = divmod(seconds, 60)
    if minutes <= 10:
        return str("%02d"%minutes) + ":" + str("%02d"%seconds)
    else:
        return str(minutes) + ":" + str("%02d"%seconds)

with open(os.path.join(dirname, "ProPlayerDict.txt"), "rb") as myFile:
    ProPlayerDict = pickle.load(myFile)

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
    return gameinfo