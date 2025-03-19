import requests
import json
from backend.checkNSFW import CheckGameisNSFW

class GameType:
    def lowPriceGame():
        gameAcquired = False
        i = 0
        gameDetails = requests.get("https://www.cheapshark.com/api/1.0/deals?upperprice=14&storeID=1&onSale=1&maxAge=168").json()
        while not gameAcquired:
            if CheckGameisNSFW.isNSFWGame(gameDetails[i]["steamAppID"]):
                i = i + 1
                continue
            else:
                gameID = gameDetails[i]["gameID"]
                gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameDetails[i]["gameID"])).json()
                gameAcquired = True
        return gameDetails, str(gameID)

    def midPriceGame():
        gameAcquired = False
        gameDetails = requests.get("https://www.cheapshark.com/api/1.0/deals?upperprice=28&lowerPrice=14&storeID=1&onSale=1&maxAge=168").json()
        i = 0
        while not gameAcquired:
            if CheckGameisNSFW.isNSFWGame(gameDetails[i]["steamAppID"]):
                i = i + 1
                continue
            else:
                gameID = gameDetails[i]["gameID"]
                gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameDetails[i]["gameID"])).json()
                gameAcquired = True
        return gameDetails, str(gameID)
    
    def highPriceGame():
        gameAcquired = False
        gameDetails = requests.get("https://www.cheapshark.com/api/1.0/deals?lowerPrice=28&storeID=1&onSale=1&maxAge=168").json()
        i = 0
        while not gameAcquired:
            if CheckGameisNSFW.isNSFWGame(gameDetails[i]["steamAppID"]):
                i = i + 1
                continue
            else:
                gameID = gameDetails[i]["gameID"]
                gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameDetails[i]["gameID"])).json()
                gameAcquired = True
        return gameDetails, str(gameID)
    
    def specificGame(gameID):
        gameDetails = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameID)).json()
        return gameDetails, str(gameID)