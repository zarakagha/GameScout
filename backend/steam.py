import requests
import json
import re

#https://api.steampowered.com/{interface}/{method}/{version}/?key={your_api_key}&{parameters}


#files that will contain game names
fileout = open("Gameslist.txt", mode="w")
fileoutappidandname = open("Gameslistwithappidandname.txt", mode="w")
fileoutraw = open("RawGameList.json", mode="w")
fileoutappid = open("gamelistappid.txt", mode="w")

#Getting the list of games from steam
steamResponse = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=STEAMKEYHERE")
steamGamesList = steamResponse.json()
gameString = json.dumps(steamGamesList)
json.dump(steamGamesList, fileoutraw)

#acquire the names and appid's of the game in question
list_of_games = re.findall(r'("name".+?})', gameString)
list_of_games_with_appid_and_name = re.findall(r'({"appid".*?})', gameString)
list_of_games_appid = re.findall(r'("appid".*?,)', gameString)

#for games with the name only, remove the bracket and print toi its respective file
for game in list_of_games:
    game = game.replace("}", "")
    print(game, file=fileout)

#Games with app ids
for gameappidandname in list_of_games_with_appid_and_name:
    print(gameappidandname, file=fileoutappidandname)
    
for gameappid in list_of_games_appid:
    gameappid = gameappid.replace(",", "")
    print(gameappid, file=fileoutappid)


fileoutappidandname.close()
fileout.close()
fileoutraw.close()
fileoutappid.close()