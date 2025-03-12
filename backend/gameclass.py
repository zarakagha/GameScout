#Game object class

class Game:
    #initalization of game Object
    __inital_price = 0
    def __init__(self):
        self.__name = ""
        self.__steamappid = 0
        self.__cheapsharkgameid = 0
        self.__list_of_prices = []
        self.__game_stores = []
        self.__store_and_price = {}
        self.__store_and_savings = {}
        

    #setters
    def setGameName(self, Game_name):
        self.__name = str(Game_name)
    
    def setGamePrice(self, Game_price):
        self.__inital_price = float(Game_price)
    
    def setGameSteamappid(self, Game_steamappid):
        self.setGameSteamappid = int(Game_steamappid)
    
    def setToListOfPrices(self, price):
        self.__list_of_prices.append(float(price))
    
    def setToListOfStores(self, storeID):
        self.__game_stores.append(int(storeID))
        
    def setStoreAndPrice(self, storeID, price):
        self.__store_and_price[int(storeID)] = float(price)
        
    def setStoreAndSavings(self, storeID, savings):
        self.__store_and_savings[int(storeID)] = float(savings)
    
    #getters
    def name(self):
        return self.__name
    
    def gamePrice(self):
        return self.__inital_price
    
    def gameSteamAppId(self):
        return self.__steamappid
    
    def cheapSharkGameId(self):
        return self.__cheapsharkgameid
    
    def gamePricesAcrossStores(self):
        return self.__list_of_prices
    
    def gameStores(self):
        return self.__game_stores
    
    def storesWithPrice(self):
        return self.__store_and_price
    
    def storeWithSavings(self):
        return self.__store_and_savings
    
    #function to sort prices from cheapest to highest
    def sortPrice(self):
        return self.__list_of_prices.sort()