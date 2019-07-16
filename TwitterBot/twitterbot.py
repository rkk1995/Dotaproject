import tweepy
import time
import os
import pickle
import requests, json

#keys for throwaway account, feel free to use
CONSUMER_KEY = 'vCysD6IMgXRfRfVe9WxMT8HEK'
CONSUMER_SECRET = 'Srq3m9wvCfT5J3Qw5VbQUHHZ3OOpIPOVqgahf9FdSy5Jo7aB5h'
ACCESS_KEY = '1067739065737519104-cLHyB9kaFK3jaDPnBBL0z4xqGKsiqS'
ACCESS_SECRET = 'z221DyYYQznbvawmwAnC8GmNqY0vVikGDlr3lOaLguqCy'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

dirname = os.path.dirname(__file__)
lastseen = os.path.join(dirname, 'last_seen_id.txt')

with open(os.path.join(dirname, "PlayerFollowerData.txt"), "rb") as myFile:
    PlayerFollowerData = pickle.load(myFile)


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def UpdateDatabase():
    print('scanning tweets & updating database...', flush=True)
    # DEV NOTE: use 12345 as last_seen_id for testing.
    last_seen_id = retrieve_last_seen_id(lastseen)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        #id of tweeter/user
        user_id = mention.author.id
        bot_screen_name = mention.in_reply_to_screen_name
        #steamid of player user wants to track
        player = mention.full_text.lower()
        for r in (("@" + bot_screen_name.lower() + ' ',''), (' ', '')):
            player = player.replace(*r)
        player = ''.join(c for c in player if c.isnumeric())
        player = int(player)
        #now have user_id of tweeter, screen_name of host account, player steam id
        #print(user_id, screen_name, player)
        last_seen_id = mention.id

        #populating database

        r = requests.get("https://api.opendota.com/api/players/" + str(player) +"/matches/?limit=1")
        if len(json.loads(r.text))==1:
            lastmatch = json.loads(r.text)[0]['match_id']
            profile = json.loads(requests.get("https://api.opendota.com/api/players/" + str(player)).text)['profile']
            if profile['name'] is not None:
                playername = profile['name']
            else:
                playername = profile['personaname']

            if player not in PlayerFollowerData.keys():
                PlayerFollowerData[player] = {"LastMatch" : lastmatch, "Followers" : [user_id], "Name" : playername}
            else:
                PlayerFollowerData[player]['Followers'].append(user_id)
        #else:
            #tWEeTBackuserhas never played or invalid. Find steamid3 here : liNk
    store_last_seen_id(last_seen_id, lastseen)
    #print(PlayerFollowerData)

    with open(os.path.join(dirname, "PlayerFollowerData.txt"), "wb") as myFile:
        pickle.dump(PlayerFollowerData, myFile)

def ReportNewMatches():
    print('Discovering new matches...')
    for player in PlayerFollowerData:
        latestmatch = json.loads((requests.get("https://api.opendota.com/api/players/" + str(player) +"/matches/?limit=1").text))[0]['match_id']
        if PlayerFollowerData[player]["LastMatch"] != latestmatch:
            for follower in PlayerFollowerData[player]["Followers"]:
                api.update_status('@' + api.get_user(follower).screen_name + ' ' + PlayerFollowerData[player]['Name'] + ' just played a match! ' + 'https://www.dotabuff.com/matches/' + str(latestmatch))
            PlayerFollowerData[player]["LastMatch"] = latestmatch
            with open(os.path.join(dirname, "PlayerFollowerData.txt"), "wb") as myFile:
                pickle.dump(PlayerFollowerData, myFile)
            #print(PlayerFollowerData)
            print('database updated, tweet sent')




while True:
    UpdateDatabase()
    ReportNewMatches()
    time.sleep(15)