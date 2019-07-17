import pickle
import os
import xlrd

#initialize dict
# ProPlayerDict = {}
# wb = xlrd.open_workbook(r"D:\Coding\Dotaproject\protracker\BaseProdatabase.xlsx")
# sh = wb.sheet_by_index(0)
# for i in range(142):
#     c1 = int(sh.cell(i,0).value)
#     c2 = str(sh.cell(i,1).value)
#     ProPlayerDict[c1] = c2

dirname = os.path.dirname(__file__)

# # Saves 
# with open(os.path.join(dirname, "ProPlayerDict.txt"), "wb") as myFile:
#     pickle.dump(ProPlayerDict, myFile)

# # #Loads PlayerFollowerData
with open(os.path.join(dirname, "ProPlayerDict.txt"), "rb") as myFile:
    ProPlayerDict = pickle.load(myFile)


print(ProPlayerDict)

