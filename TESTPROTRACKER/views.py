from django.shortcuts import render, redirect
from django.http import HttpResponse
from TESTPROTRACKER.timeconverter import converttime
import requests, json, os, pickle
from django.template.defaulttags import register


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, "HeroImageDict.txt"), "rb") as myFile:
    HeroImageDict = pickle.load(myFile)

with open(os.path.join(dirname, "currentgames.txt"), "rb") as myFile:
    currentgames = pickle.load(myFile)

def protrackertest(request):
    return render(request, 'protracker.jinja', {'livematches': currentgames, 'HeroImageDict': HeroImageDict} )
