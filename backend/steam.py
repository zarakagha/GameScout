import requests
import json
import re

#https://api.steampowered.com/{interface}/{method}/{version}/?key={your_api_key}&{parameters}


#files that will contain game names
fileout = open("Gameslist.txt", mode="w")
fileoutappidandname = open("Gameslistwithappidandname.txt", mode="w")
fileoutraw = open("RawGameList.json", mode="w")
fileoutappid = open("gamelistappid.txt", mode="w")

#initalize dictionary for no duplicates
gamedict = {}

#Getting the list of games from steam
steamResponse = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=STEAMKEYHERE")
steamGamesList = steamResponse.json()
gameString = json.dumps(steamGamesList)
json.dump(steamGamesList, fileoutraw)


list_of_games_with_appid_and_name = re.findall(r'({"appid".*?})', gameString)

#Games with unique app ids and names
for gameappidandname in list_of_games_with_appid_and_name:
    #match game app id, and game name in string
    currgameappidmatch = re.search(r'("appid".*?,)', gameappidandname)
    currgamenamematch = re.search(r'("name".+?})', gameappidandname)
    #retreive values for game name and app id
    currgameappid = currgameappidmatch.group()
    currgamename = currgamenamematch.group()
    #clean up game name string
    currgamename = currgamename.replace("}", "")
    #add to dictionary so no duplicated values are added
    if currgameappid not in gamedict:
        gamedict[currgameappid] = currgamename
        #print out to files
        #Appid + gamename file
        print(gameappidandname, file=fileoutappidandname)
        #app id only file
        print(currgameappid, file=fileoutappid)
        #game name only file
        print(currgamename, file=fileout)


fileoutappidandname.close()
fileout.close()
fileoutraw.close()
fileoutappid.close()