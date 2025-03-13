import requests
from backend.gameclass import Game
import json

class ConvertUSDToCad:
    #takes float value price
    def Convert(price):
        if price is not type(float):
            price = float(price)
        currencyExchangeResponse = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
        currencyExchangeJSON = currencyExchangeResponse.json()
        newprice = price * float(currencyExchangeJSON["usd"]["cad"])
        return newprice
    
    def convertListOfPricesFromGame(Gameobj):
        CanadianStoreID = [1, 2, 3, 7, 8, 15, 25, 35]
        for storeID in Gameobj.gameStores():
            if int(storeID) in CanadianStoreID:
                original_price = Gameobj.gamePrice()
                savings = 1 - (Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][1] / 100)
                discounted_price = original_price * savings
                Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0] = discounted_price
            else:
                Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0] = ConvertUSDToCad.Convert(Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0])
