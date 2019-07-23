from celery.task.schedules import crontab
from celery.decorators import periodic_task
from protracker.models import Hero, Match, LiveMatch, MatchesToGet
import requests, json, pickle, os
from time import sleep

key = "BDAECC2049E139D32D5D7AEDEFC23304"
dirname = 'D:/coding/test/mysite/polls/databases'


@periodic_task(
  run_every=(crontab(minute='*/5')),
  name="update_livematch",
  ignore_result=True
)
def update_livematch():
  dirname = 'D:\Coding\Dotaproject\protracker\databases'
  from protracker.ProTrackerFunctions import converttime, GetProPlayersFromMatch
  r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=" + key + "&partner=0")
  if "game_list" in r.text:
    LiveMatch.objects.all().delete()
    currentlivematchids = []
    livematches = json.loads(r.text)['game_list']
    currentgames=[]
    for i in livematches:
      MatchesToGet.objects.get_or_create(match_id = i['match_id'])
      currentlivematchids.append(i['match_id'])
      total = GetProPlayersFromMatch(i)
      if total:
        currentgames.append(total)
    LiveMatch.objects.create(myList = json.dumps(currentgames))
    for matchtoget in MatchesToGet.objects.all():
      if matchtoget.match_id not in currentlivematchids:
        matchdata = requests.get("http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1?key=" + key + "&match_id=" + str(matchtoget.match_id))
        if str(matchtoget.match_id) in matchdata.text:
          if 'radiant_win' not in matchdata.text:
            matchtoget.delete()
            continue
          matchdata = json.loads(matchdata.text)['result']
          p, created = Match.objects.get_or_create(match_id = matchdata['match_id'], match_date = matchdata['start_time'])
          players = matchdata['players']
          if matchdata['radiant_win']:
            for i in range(0,5):
              p.heros_won.add(Hero.objects.get(hero_id=players[i]['hero_id']))
            for i in range(5,10):
              p.heros_lost.add(Hero.objects.get(hero_id=players[i]['hero_id']))
          if not matchdata['radiant_win']:
            for i in range(0,5):
              p.heros_lost.add(Hero.objects.get(hero_id=players[i]['hero_id']))
            for i in range(5,10):
              p.heros_won.add(Hero.objects.get(hero_id=players[i]['hero_id']))
        matchtoget.delete() 
