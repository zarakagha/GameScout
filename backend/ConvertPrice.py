import requests
import json

class ConvertUSDToCad:
    #takes float value price
    def Convert(price): #function to convert usd prices to cad
        if price is not type(float): #checks if prices are floats
            price = float(price)
        currencyExchangeResponse = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json") #stores conversion prices from api
        currencyExchangeJSON = currencyExchangeResponse.json() #parses conversion json data and stores it into a dictionary
        newprice = price * float(currencyExchangeJSON["usd"]["cad"]) #calculates the converted price by multiplying then USD price with the canadian conversion rate
        return newprice
    
    def convertListOfPricesFromGame(Gameobj): #function to convert the different store prices to CAD
        from backend.gameclass import Game
        CanadianStoreID = [1, 2, 3, 7, 8, 15, 25, 35] #stores various storefront ids into an array
        for storeID in Gameobj.gameStores(): #for loop to iterate through all game stores
            if int(storeID) in CanadianStoreID: #checks if store id is in the array
                original_price = Gameobj.gamePrice() 
                savings = 1 - (Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][1] / 100) #calculates total savings
                discounted_price = original_price * savings #calculates the discounted price
                Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0] = discounted_price #stores the discount price back into the gameobj
            else:
                Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0] = ConvertUSDToCad.Convert(Gameobj.storeWithPriceSavingsDealURl()[int(storeID)][0]) #converts the saving price into cad and storing it in gameobj



    def convertPriceForGame(original_price, storeID, savings): #function to convert the prices for each game
        CanadianStoreID = [1, 2, 3, 7, 8, 15, 25, 35] #stores various storefront ids into an array
        if int(storeID) in CanadianStoreID: #checks if store id is in the array
            savings = 1 - (savings / 100) #calculates savings
            discounted_price = original_price * savings #calculates discounted price
            return discounted_price #returns discounted price
        else:
            return ConvertUSDToCad.Convert(original_price) #returns the Canadian original price