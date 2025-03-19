#Game object class

from backend.ConvertPrice import ConvertUSDToCad
from backend.GetSteamPriceCadForGame import get_inital_price

class Game:
    #initalization of game Object

    def __init__(self, cheapsharkID):
        self.inital_price = 0
        self.name = ""
        self.steamappid = 0
        self.cheapsharkgameid = cheapsharkID
        self.imageURL = ""
        self.NSFW = False
        self.cheapSharkGeneralDealURL = "https://www.cheapshark.com/redirect?dealID="
        self.list_of_prices = []
        self.list_of_game_stores = []
        self.StoreID_Price_Savings_Dealurl = {}
        self.store_and_price = {}
        self.store_and_savings = {}
        self.store_and_dealurl = {}
        

    #setters
    def setGameName(self, Game_name):
        self.name = str(Game_name)
    
    def setCheapSharkGameID(self, cheapsharkID):
        self.cheapsharkgameid = str(cheapsharkID)
    
    def setGamePriceCAD(self, Game_price):
        self.inital_price = float(Game_price)
    
    def setGameSteamappid(self, Game_steamappid):
        self.steamappid = int(Game_steamappid)
        
    def setGameImageURL(self, url_link):
        self.imageURL = str(url_link)
    
    def setNSFW(self, isNSFW):
        self.NSFW = bool(isNSFW)
    
    def addToListOfPrices(self, price):
        self.list_of_prices.append(float(price))
    
    def addToListOfStores(self, storeID):
        self.list_of_game_stores.append(int(storeID))
        
    def addStorePriceSavingsDealUrl(self, storeID, price, savings, dealurl):
        self.StoreID_Price_Savings_Dealurl[int(storeID)] = [float(price), float(savings), str(dealurl)]
        
    def prepareGameObject(self, gamedetails, gameid):
        #game id
        self.cheapsharkgameid = str(gameid)
        #game name
        self.name = str(gamedetails["info"]["title"])
        self.steamappid = int(gamedetails["info"]["steamAppID"])
        self.inital_price = float(get_inital_price(self.steamappid))
        self.imageURL = "https://steamcdn-a.akamaihd.net/steam/apps/{}/library_600x900_2x.jpg".format(str(self.steamappid))
        for deal in gamedetails["deals"]:
            self.addToListOfPrices(deal["price"])
            self.addToListOfStores(deal["storeID"])
            self.addStorePriceSavingsDealUrl(deal["storeID"], deal["price"], deal["savings"], self.cheapSharkGeneralDealURL+deal["dealID"])

    
    #def addStoreAndPrice(self, storeID, price):
    #    self.store_and_price[int(storeID)] = float(price)
        
    #def addStoreAndSavings(self, storeID, savings):
    #    self.store_and_savings[int(storeID)] = float(savings)
    
    #getters
    def GetGamename(self):
        return self.name
    
    def gamePrice(self):
        return self.inital_price
    
    def gameSteamAppId(self):
        return self.steamappid
    
    def cheapSharkGameId(self):
        return self.cheapsharkgameid
    
    def gameImage(self):
        return self.imageURL
    
    def NSFWstatus(self):
        return self.NSFW
    
    def gamePricesAcrossStores(self):
        return self.list_of_prices
    
    def gameStores(self):
        return self.list_of_game_stores
    
    #def storesWithPrice(self):
    #    return self.store_and_price
    
    #def storeWithSavings(self):
    #    return self.store_and_savings
    
    def storeWithPriceSavingsDealURl(self):
        return self.StoreID_Price_Savings_Dealurl
    
    #function to sort prices from cheapest to highest
    def sortPrice(self):
        return self.list_of_prices.sort()