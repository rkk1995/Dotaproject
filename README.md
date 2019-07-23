#DotaProject - created with django

This app has 3 subapps.

### 1)ProTracker ###
### 2)playerid - stats ###
### 3)player tracker via twitterbot ###

# ProTracker #

Frontend is not mine. Backend is entirely my own.

![Homepage](http://puu.sh/DWx1Z/b7622ca6e2.jpg)

# playerid - stats #

This is an app where you can get the last 20 matches of any player by searching their steamid32. If you dont know yours or another players, it can be found here https://steamid.xyz/ .

## Homepage: ## 
![Homepage](http://puu.sh/DNCtR/2f3061ef6b.png)


Stats page of a player:

![Your Stats Page](http://puu.sh/DNCuI/688c22ae15.png)

## How to run ##

To run clone repository and run following in terminal. To run ProTracker, additional steps described below.

1) Pipenv Shell
2) python manage.py runserver


# twitterbot #

This is a twitterbot for Dota 2 Stats. It lets you track your favorite pro player or anyone else (maybe your friend to see if he loses)

Host the script, tweet at @Dota2Bot_Test (temporary) with a players steamID32ID (can be found here https://steamid.xyz/) Feel free to use 121769650 for testing. I have the twitter API key for @Dota2Bot_Test on there. Throwaway account, so feel free to try.

So @Dota2Bot_test  121769650

Whenever said player plays a match from the time you tweeted, you'll be notified via tweet.
 

![Alt text](http://puu.sh/DTr9l/c78861a7db.png "Example")



