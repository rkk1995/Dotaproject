
import requests, json

r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=BDAECC2049E139D32D5D7AEDEFC23304&partner=0")
b = json.loads(r.text)['game_list']
for i in b:
    print(i['game_time'],i['radiant_score'],i['dire_score'])

