from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json

def index(request):
    key = "BDAECC2049E139D32D5D7AEDEFC23304"
    
    with open(os.path.join(dirname, "ProPlayerDict.txt"), "rb") as myFile:
        ProPlayerDict = pickle.load(myFile)

    
    r =  requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=" + key + "&partner=0")
    livematches = json.loads(r.text)['game_list']
    
    return render(request, 'protracker.jinja', {'livematches': livematches})
