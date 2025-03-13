import requests
import json
import re
from backend.gameclass import Game
from backend.GetSteamPriceCadForGame import get_inital_price
from backend.ConvertPrice import ConvertUSDToCad

class DealForGameSimpleFactory:
        
    def GetGameDealsAcrossStores(cheapsharkgameID):
        gameObj = Game(cheapsharkgameID)
        cheapsharkdealsRequest = requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(gameObj.cheapSharkGameId()))
        cheapsharkJSON = cheapsharkdealsRequest.json()
        gameObj.setGameName(cheapsharkJSON["info"]["title"])
        gameObj.setGameSteamappid(cheapsharkJSON["info"]["steamAppID"])
        gameObj.setGamePriceCAD(get_inital_price(gameObj.gameSteamAppId()))
        gameObj.setGameImageURL(cheapsharkJSON["info"]["thumb"])
        for deal in cheapsharkJSON["deals"]:
            gameObj.addToListOfPrices(deal["price"])
            gameObj.addToListOfStores(deal["storeID"])
            gameObj.addStorePriceSavingsDealUrl(deal["storeID"], deal["price"], deal["savings"], gameObj.cheapSharkGeneralDealURL+deal["dealID"])
        ConvertUSDToCad.convertListOfPricesFromGame(gameObj)
        return gameObj