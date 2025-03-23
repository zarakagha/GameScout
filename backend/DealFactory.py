import requests
import json
import re
from backend.gameclass import Game, lowPriceGame, midPriceGame, highPriceGame, specificGame
from backend.GetSteamPriceCadForGame import get_inital_price
from backend.ConvertPrice import ConvertUSDToCad

#SIMPLE FACTORY CLASS HERE, depending on the input it will generate a game
class GameSimpleFactory:
    #method determining which game to generate depending on the gameType
    def acquireGame(gameType):
        #ensure the gameType is in INT
        gameType = int(gameType)
        #initalize a gamedetails variable, this will be the information of the game
        gameObj = None
        #This will generate a low priced game
        if gameType == 10000000:
            gameObj = lowPriceGame(gameType)
            gameObj.setGameDetails()
        #this will generate a medium priced game
        elif gameType == 20000000:
            gameObj = midPriceGame(gameType)
            gameObj.setGameDetails()
        #this will generate a game that is higher priced
        elif gameType == 30000000:
            gameObj = highPriceGame(gameType)
            gameObj.setGameDetails()
        #this will generate a specific game
        else:
            gameObj = specificGame(gameType)
            gameObj.setGameDetails()
        #Return the game details
        return gameObj

# Class to generate a game
class DealForGameSimpleFactory:
    #Method to get the deals across stores for a game
    def GetGameDealsAcrossStores(cheapsharkgameID):
        #RUN THE SIMPLE FACTORY, DEPENDING ON INPUT (cheapsharkgameID) IT WILL GENERATE A GAME
        gameObj = GameSimpleFactory.acquireGame(cheapsharkgameID)
        #Getting the information from the simple factory prepare the game object
        gameObj.prepareGameObject(gameObj.getGameDetails(), gameObj.cheapSharkGameId())
        #Convert the prices across all the stores into its CAD equivalent
        ConvertUSDToCad.convertListOfPricesFromGame(gameObj)
        #return game obj
        return gameObj