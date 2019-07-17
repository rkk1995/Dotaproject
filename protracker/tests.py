
import requests, json

r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=BDAECC2049E139D32D5D7AEDEFC23304&partner=0")
b = json.loads(r.text)['game_list']
for i in b:
    print(i['game_time'],i['radiant_score'],i['dire_score'])

#https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1/?key=BDAECC2049E139D32D5D7AEDEFC23304&partner=0&server_steam_id=90127541958132739
# to get live match data ^

