import pickle
import os

#Reinitialize playerdata file in format
#PlayerFollowerData = { "Player" : {"LastMatch" : 12345 , "Followers" : ["User_Id1", "User_Id2"]}}

# mentions[i]
# id gives tweet id 
# text gives tweet text
# author gives user info # user id for dict
# author.id
# author.screen_name 
# text.replace("@" + username + ' ','') = playerid , add this to dictionary

dirname = os.path.dirname(__file__)


#PlayerFollowerData = {}

# Saves PlayerFollowerData
# with open(os.path.join(dirname, "PlayerFollowerData.txt"), "wb") as myFile:
#     pickle.dump(PlayerFollowerData, myFile)

# # #Loads PlayerFollowerData
# with open(os.path.join(dirname, "PlayerFollowerData.txt"), "rb") as myFile:
#     PlayerFollowerData = pickle.load(myFile)

# PlayerFollowerData[86745912]['LastMatch'] = 2323123

# with open(os.path.join(dirname, "PlayerFollowerData.txt"), "wb") as myFile:
#     pickle.dump(PlayerFollowerData, myFile)

print(PlayerFollowerData)

