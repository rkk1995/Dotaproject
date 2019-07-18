import requests
import json, os, pickle

#Creates Hero Image Dictionary

key = "BDAECC2049E139D32D5D7AEDEFC23304"
r = requests.get("https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/?key=BDAECC2049E139D32D5D7AEDEFC23304&language=en")
b = json.loads(r.text)['result']['heroes']
dirname = os.path.dirname(__file__)

# HeroImageDict = {}
# for hero in b:
#     HeroImageDict[hero['id']] = {'hero': hero['localized_name'] , 
#                                 'vert':  "http://cdn.dota2.com/apps/dota2/images/heroes/" + hero['name'][14::] + "_vert.jpg",
#                                 'large': "http://cdn.dota2.com/apps/dota2/images/heroes/" + hero['name'][14::]  + "_lg.png" ,
#                                 'icon' : "/static/images/miniheroes/" + hero['name'][14::]  + ".png" }

# # Saves PlayerFollowerData
# with open(os.path.join(dirname, "HeroImageDict.txt"), "wb") as myFile:
#     pickle.dump(HeroImageDict, myFile)

with open(os.path.join(dirname, "HeroImageDict.txt"), "rb") as myFile:
    HeroImageDict = pickle.load(myFile)

print(HeroImageDict.keys())
