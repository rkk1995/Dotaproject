from celery.task.schedules import crontab
from celery.decorators import periodic_task
from protracker.models import Hero, Match, LiveMatch
import requests, json, pickle, os

key = "BDAECC2049E139D32D5D7AEDEFC23304"
dirname = 'D:/coding/test/mysite/polls/databases'


@periodic_task(
  run_every=(crontab(minute='*/1')),
  name="update_livematch",
  ignore_result=True
)
def update_livematch():
  dirname = 'D:/coding/test/mysite/polls/databases'
  from protracker.ProTrackerFunctions import converttime, GetProPlayersFromMatch
  r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=" + key + "&partner=0")
  if "game_list" in r.text:
    LiveMatch.objects.all().delete()
    livematches = json.loads(r.text)['game_list']
    currentgames=[]
    for i in livematches:
          total = GetProPlayersFromMatch(i)
          if total:
              currentgames.append(total)     
    LiveMatch.objects.create(myList = json.dumps(currentgames))