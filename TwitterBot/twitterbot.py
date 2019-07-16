import tweepy
import time
import os
import pickle

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


def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 12345 as last_seen_id for testing.
    last_seen_id = retrieve_last_seen_id(lastseen)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        #id of tweeter/user
        user_id = mention.author.id
        screen_name = mention.author.screen_name
        #steamid of player user wants to track
        player = mention.full_text.lower()
        for r in (("@" + screen_name.lower() + ' ',''), (' ', '')):
            player = player.replace(*r)
        #now have user+id, screen_name, player
        print(user_id, screen_name, player)
        last_seen_id = mention.id

        if player not in PlayerFollowerData.keys():
            PlayerFollowerData[player] = {"LastMatch" : 'test', "Followers" : [user_id]}
        else:
            PlayerFollowerData[player]['Followers'].append(user_id)


    store_last_seen_id(last_seen_id, lastseen)
    print(PlayerFollowerData)

    with open(os.path.join(dirname, "PlayerFollowerData.txt"), "wb") as myFile:
        pickle.dump(PlayerFollowerData, myFile)



# def checktweets():
#     # function adds players to database and associates player with tweeter
#     # SteamID3s have 9 numbers, ie 177648913
#     print('retrieving and replying to tweets...', flush=True)
#     # DEV NOTE: use 12345 as last_seen_id for testing.
#     last_seen_id = retrieve_last_seen_id(lastseen)
#     mentions = api.mentions_timeline(
#                         last_seen_id,
#                         tweet_mode='extended')
#     for mention in reversed(mentions):
#         print(str(mention.id) + ' - ' + mention.full_text, flush=True)
#         user_id = mention.author.id
#         screen_name = mention.author.screen_name

#         print(user_id,screen_name)
#         last_seen_id = mention.id
#         store_last_seen_id(last_seen_id, lastseen)
#         if '#helloworld' in mention.full_text.lower():
#             print('found #helloworld!', flush=True)
#             print('responding back...', flush=True)
#             api.update_status('@' + mention.user.screen_name +
#                     ' #dog back to you!', mention.id)



while True:
    reply_to_tweets()
    time.sleep(15)