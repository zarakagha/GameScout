#Game object class

class Game:
    #initalization of game Object

    def __init__(self):
        self.inital_price = 0
        self.name = ""
        self.steamappid = 0
        self.cheapsharkgameid = 0
        self.list_of_prices = []
        self.list_of_game_stores = []
        self.store_and_price = {}
        self.store_and_savings = {}
        

    #setters
    def setGameName(self, Game_name):
        self.name = str(Game_name)
    
    def setGamePrice(self, Game_price):
        self.inital_price = float(Game_price)
    
    def setGameSteamappid(self, Game_steamappid):
        self.steamappid = int(Game_steamappid)
    
    def setToListOfPrices(self, price):
        self.list_of_prices.append(float(price))
    
    def setToListOfStores(self, storeID):
        self.list_of_game_stores.append(int(storeID))
        
    def setStoreAndPrice(self, storeID, price):
        self.store_and_price[int(storeID)] = float(price)
        
    def setStoreAndSavings(self, storeID, savings):
        self.store_and_savings[int(storeID)] = float(savings)
    
    #getters
    def GetGamename(self):
        return self.name
    
    def gamePrice(self):
        return self.inital_price
    
    def gameSteamAppId(self):
        return self.steamappid
    
    def cheapSharkGameId(self):
        return self.cheapsharkgameid
    
    def gamePricesAcrossStores(self):
        return self.list_of_prices
    
    def gameStores(self):
        return self.list_of_game_stores
    
    def storesWithPrice(self):
        return self.store_and_price
    
    def storeWithSavings(self):
        return self.store_and_savings
    
    #function to sort prices from cheapest to highest
    def sortPrice(self):
        return self.list_of_prices.sort()