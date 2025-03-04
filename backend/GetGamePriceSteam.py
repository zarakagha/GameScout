import requests
import json
import re


userRequest = input("Enter game name: ")
userRequest = userRequest.lower()

Gamefile = open("Gameslistwithappidandname.txt", mode="r")
Gamefilecontent = Gamefile.read().lower()
regexForGame = '{{"appid".*?"name": "{}"}}'.format(userRequest)
regexForCheapSharkGameID = '"gameID".*?,'


isFound = re.search(str(regexForGame), Gamefilecontent)
if isFound:
    UserGame = isFound.group()
    appid = UserGame.split(',')[0]
    appid = appid[10:]
    
    cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/games?steamAppID={}".format(appid)
    cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
    cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
    cheapsharkGameIDString = json.dumps(cheapsharkGameIDResponseJSON)
    cheapsharkGameIDJSON = json.loads(cheapsharkGameIDString)
    cheapsharkGameIDJSONFound = cheapsharkGameIDJSON[0]["gameID"]
    if cheapsharkGameIDJSONFound:
        cheapsharkGameDealsRequestString = "https://www.cheapshark.com/api/1.0/games?id={}".format(cheapsharkGameIDJSONFound)
        cheapsharkGameDealsResponse = requests.get(cheapsharkGameDealsRequestString)
        cheapsharkGameDealsResponseJSON = cheapsharkGameDealsResponse.json()
        cheapsharkGameDeals = json.dumps(cheapsharkGameDealsResponseJSON)
        cheapsharkJSON = json.loads(cheapsharkGameDeals)
        print(cheapsharkJSON["deals"])
    else:
        print("Failed to find Cheapshark game id")
    
else:
    print("Sorry the game: " + userRequest + " Could not be found")
    



    

#cheapSharkResponse = requests.get("https://www.cheapshark.com/api/1.0/games?id=236717")
#print(cheapSharkResponse)
#Result = cheapSharkResponse.json()
#print(json.dumps(Result)

Gamefile.close()
