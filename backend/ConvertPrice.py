import requests
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
        from backend.gameclass import Game
        CanadianStoreID = [1, 2, 3, 7, 8, 15, 25, 35]
        for storeID in Gameobj.gameStores():
            if int(storeID) in CanadianStoreID:
                original_price = Gameobj.gamePrice()
                savings = 1 - (Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][1] / 100)
                discounted_price = original_price * savings
                Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0] = discounted_price
            else:
                Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0] = ConvertUSDToCad.Convert(Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0])

    def getDiscountedPrice(Gameobj):
        from backend.gameclass import Game
        CanadianStoreID = [1, 2, 3, 7, 8, 15, 25, 35]
        price = 10000.0
        store = 0
        for deal in Gameobj:
            if int(deal["storeID"]) in CanadianStoreID:
                val = float(deal["price"])
                if val < price:
                    price = val
                    store = int(deal["storeID"])

        return ConvertUSDToCad.Convert(price),store

    def convertPriceForGame(original_price, storeID, savings):
        CanadianStoreID = [1, 2, 3, 7, 8, 15, 25, 35]
        if int(storeID) in CanadianStoreID:
            savings = 1 - (savings / 100)
            discounted_price = original_price * savings
            return discounted_price
        else:
            return ConvertUSDToCad.Convert(original_price)