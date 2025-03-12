import requests
import json
import re
from gameclass import Game
from GetSteamPriceCadForGame import get_inital_price
from ConvertPrice import ConvertUSDToCad

class DealForGameSimpleFactory:
        
    def GetGameDealsAcrossStores(cheapsharkgameID):
        gameObj = Game(cheapsharkgameID)
        cheapsharkdealsRequest = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameObj.cheapSharkGameId()))
        cheapsharkJSON = cheapsharkdealsRequest.json()
        gameObj.setGameName(cheapsharkJSON["info"]["title"])
        gameObj.setGameSteamappid(cheapsharkJSON["info"]["steamAppID"])
        gameObj.setGamePriceCAD(get_inital_price(gameObj.gameSteamAppId()))
        for deal in cheapsharkJSON["deals"]:
            gameObj.addToListOfPrices(deal["price"])
            gameObj.addToListOfStores(deal["storeID"])
            gameObj.addStoreAndPrice(deal["storeID"], deal["price"])
            gameObj.addStoreAndSavings(deal["storeID"], deal["savings"])
        ConvertUSDToCad.convertListOfPricesFromGame(gameObj)
        return gameObj