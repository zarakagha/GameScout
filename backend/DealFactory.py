import requests
import json
import re
from backend.gameclass import Game
from backend.GetSteamPriceCadForGame import get_inital_price
from backend.ConvertPrice import ConvertUSDToCad
from backend.GameTypeList import GameType

class GameSimpleFactory:
    def acquireGame(gameType):
        gameType = int(gameType)
        gameDetails = None
        if gameType == 10000000:
            gameDetails = GameType.lowPriceGame()
        elif gameType == 20000000:
            gameDetails = GameType.midPriceGame()
        elif gameType == 30000000:
            gameDetails = GameType.highPriceGame()
        else:
            gameDetails = GameType.specificGame(gameType)
        return gameDetails

class DealForGameSimpleFactory:        
    def GetGameDealsAcrossStores(cheapsharkgameID):
        gameObj = Game(cheapsharkgameID)
        cheapsharkJSON, gameID = GameSimpleFactory.acquireGame(cheapsharkgameID)
        #gameObj.setCheapSharkGameID(gameID)
        #gameObj.setGameName(cheapsharkJSON["info"]["title"])
        #gameObj.setGameSteamappid(cheapsharkJSON["info"]["steamAppID"])
        #gameObj.setGamePriceCAD(get_inital_price(gameObj.gameSteamAppId()))
        #gameObj.setGameImageURL("https://steamcdn-a.akamaihd.net/steam/apps/{}/library_600x900_2x.jpg".format(str(gameObj.gameSteamAppId())))
        #for deal in cheapsharkJSON["deals"]:
            #gameObj.addToListOfPrices(deal["price"])
            #gameObj.addToListOfStores(deal["storeID"])
            #gameObj.addStorePriceSavingsDealUrl(deal["storeID"], deal["price"], deal["savings"], gameObj.cheapSharkGeneralDealURL+deal["dealID"])
        gameObj.prepareGameObject(cheapsharkJSON, gameID)
        ConvertUSDToCad.convertListOfPricesFromGame(gameObj)
        return gameObj