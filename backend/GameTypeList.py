import requests
import json
from backend.checkNSFW import CheckGameisNSFW

#This will generate a game for when it is called
class GameType:
    #method to generate the details for a low priced game
    def lowPriceGame():
        #initalize game acquired variable and iterator variable
        gameAcquired = False
        i = 0
        gameDetails = None
        #while we have not got a game
        while not gameAcquired:
            #request getting the game
            gameDetails = requests.get("https://www.cheapshark.com/api/1.0/deals?upperprice=14&storeID=1&onSale=1&maxAge=300").json()
            #check if the game acquired is NSFW, skip this game if it is the case
            if CheckGameisNSFW.isNSFWGame(gameDetails[i]["steamAppID"]):
                i = i + 1
                continue
            #if it is not NSFW, we have successfully got a game and return the game deals information along with the game id.
            else:
                gameID = gameDetails[i]["gameID"]
                gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameDetails[i]["gameID"])).json()
                gameAcquired = True
        return gameDetails, str(gameID)
    #method to get a fairly mid priced game
    def midPriceGame():
        #initalize game acquired variable and iterator variable
        gameAcquired = False
        i = 0
        gameDetails = None
        #while we have not got a game
        while not gameAcquired:
            #request getting the game
            gameDetails = requests.get("https://www.cheapshark.com/api/1.0/deals?upperprice=28&lowerPrice=14&storeID=1&onSale=1&maxAge=300").json()
            #check if the game acquired is NSFW, skip this game if it is the case
            if CheckGameisNSFW.isNSFWGame(gameDetails[i]["steamAppID"]):
                i = i + 1
                continue
            #if it is not NSFW, we have successfully got a game and return the game deals information along with the game id.
            else:
                gameID = gameDetails[i]["gameID"]
                gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameDetails[i]["gameID"])).json()
                gameAcquired = True
        return gameDetails, str(gameID)
    #method to get a fairly high priced game
    def highPriceGame():
        #initalize game acquired variable and iterator variable
        gameAcquired = False
        i = 0
        gameDetails = None
        #while we have not got a game
        while not gameAcquired:
            #request getting the game
            gameDetails = requests.get("https://www.cheapshark.com/api/1.0/deals?lowerPrice=33&storeID=1&onSale=1&maxAge=300").json()
            #check if the game acquired is NSFW, skip this game if it is the case
            if CheckGameisNSFW.isNSFWGame(gameDetails[i]["steamAppID"]):
                i = i + 1
                continue
            #if it is not NSFW, we have successfully got a game and return the game deals information along with the game id.
            else:
                gameID = gameDetails[i]["gameID"]
                gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameDetails[i]["gameID"])).json()
                gameAcquired = True
        return gameDetails, str(gameID)
    #method to get a specific game based on the ID that was sent in
    def specificGame(gameID):
        #get the game details
        gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameID)).json()
        #return the game deals information and the gameID
        return gameDetails, str(gameID)