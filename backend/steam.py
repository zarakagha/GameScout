import requests
import json
import re

#https://api.steampowered.com/{interface}/{method}/{version}/?key={your_api_key}&{parameters}


#files that will contain game names
fileout = open("Gameslist.txt", mode="w")
fileoutappid = open("Gameslistwithappid.txt", mode="w")

#Getting the list of games from steam
steamResponse = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=STEAMKEYHERE")
steamGamesList = steamResponse.json()
gameString = json.dumps(steamGamesList)

#acquire the names and appid's of the game in question
list_of_games = re.findall(r'("name".+?})', gameString)
list_of_games_with_appid = re.findall(r'({"appid".*?})', gameString)

#for games with the name only, remove the bracket and print toi its respective file
for game in list_of_games:
    game = game.replace("}", "")
    print(game, file=fileout)

#Games with app ids
for gameappid in list_of_games_with_appid:
    print(gameappid, file=fileoutappid)


fileoutappid.close()
fileout.close()