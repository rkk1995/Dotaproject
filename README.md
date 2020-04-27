#DotaProject - created with django + python

To run

clone repository
enter your API keys where specified (below)
python manage.py runserver

This app has 3 subapps.

### 1)ProTracker ###
### 2)playerid - stats ###
### 3)player tracker via twitterbot ###

# ProTracker #

Frontend is not mine. Backend is mine.

![Homepage](https://user-images.githubusercontent.com/50536089/80338832-2e8cf500-8812-11ea-84fe-c2e000f82dc6.jpg) (click for better image)


## Live Games Section ##

Shows all live games with relevant pro players in my database.

## High MMR Pub Stats Section ##

Shows stats for high mmr pubs.

## Recent Matches & ## 

Eventually will show most recent matches of pro players.

## how to run ##


clone repository 


Requires Celery to run scheduled task of api calls.
Open two terminals

1st. `Celery -A dota2project worker -l info`

2nd. `Celery -A dota2project beat -l info`

Now that scheduled tasks are up and running

1) `Pipenv Shell`
2) `python manage.py runserver`

Requires STEAM API Key. (its free) Enter key in /protracker/tasks.py


## 

# playerid - stats #

This is an app where you can get the last 20 matches of any player by searching their steamid32. If you dont know yours or another players, it can be found here https://steamid.xyz/ .

## Homepage: ## 
![Homepage](https://user-images.githubusercontent.com/50536089/80339109-c985cf00-8812-11ea-90a8-64198b76a5f7.png)


Stats page of a player:

![Your Stats Page](https://user-images.githubusercontent.com/50536089/80339103-c7237500-8812-11ea-9327-e4e759dfc759.png)



# twitterbot #

This is a twitterbot for Dota 2 Stats. It lets you track your favorite pro player or anyone else (maybe your friend to see if he loses)

Host the script, tweet at @Dota2Bot_Test (temporary) with a players steamID32ID (can be found here https://steamid.xyz/) Feel free to use 121769650 for testing. I have the twitter API key for @Dota2Bot_Test on there. Throwaway account, so feel free to try.

So @Dota2Bot_test  121769650

Whenever said player plays a match from the time you tweeted, you'll be notified via tweet.
 

![Alt text](https://user-images.githubusercontent.com/50536089/80338933-76138100-8812-11ea-9f1c-53a623780bfd.png)



