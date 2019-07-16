import pickle
import os

#initialize playerdata file

# mentions[i]
# id gives tweet id 
# text gives tweet text
# author gives user info # user id for dict
# author.id
# author.screen_name 
# text.replace("@" + username + ' ','') = playerid , add this to dictionary

dirname = os.path.dirname(__file__)


# PlayerFollowerData = { "Player" : {"LastMatch" : 12345 , "Followers" : ["User_Id1", "User_Id2"]}}

# with open(os.path.join(dirname, "PlayerFollowerData.txt"), "wb") as myFile:
#     pickle.dump(PlayerFollowerData, myFile)

with open(os.path.join(dirname, "PlayerFollowerData.txt"), "rb") as myFile:
    PlayerFollowerData = pickle.load(myFile)



print(PlayerFollowerData)
