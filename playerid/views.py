from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
def myView(request):
     
    return render(request, 'getplayerid.html')

def playerData(request, player_id):
    r = requests.get("https://api.opendota.com/api/players/" + str(player_id) +"/matches/?limit=20")
    last20matches = json.loads(r.text)

    return render (request, "playerstats.jinja", {'last20' : last20matches,'playerid' : player_id})

def getplayerid(request):
    content = request.POST.get('content')
    return redirect('/players2/{}/'.format(content))