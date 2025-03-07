import requests
import json
import re

#note: one time run functions per day should be "get_currency_exchange_rate", also the file steam.py (get latest game titles)


storelistfile = open("storelist.json", mode="r")
storelist = json.load(storelistfile) 



def get_inital_price(appid):
    SteamRetailPriceResponse = requests.get("http://store.steampowered.com/api/appdetails?appids={}&cc=CA&filters=price_overview".format(appid))
    SteamRetailPriceResponseJSON = SteamRetailPriceResponse.json()
    SteamRetailPriceString = json.dumps(SteamRetailPriceResponseJSON)
    SteamRetailPriceJSON = json.loads(SteamRetailPriceString)
    inital_price = SteamRetailPriceJSON[appid]["data"]["price_overview"]["initial"]
    inital_price = float(inital_price) / 100
    return inital_price


def get_currency_exchange_rate():
    currencyexchangeResponse = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
    currencyexchangeResponseJSON = currencyexchangeResponse.json()
    currencyexchangeResponseString = json.dumps(currencyexchangeResponseJSON)
    currencyexchangeJSON = json.loads(currencyexchangeResponseString)
    return currencyexchangeJSON["usd"]["cad"]


def get_discount(cheapsharkDealsJSON, appid):
    currency_exchange_rate = float(get_currency_exchange_rate())
    stores_operating_in_CAD = [1, 2, 3, 7, 8, 15, 25, 35]
    for store in cheapsharkDealsJSON["deals"]:
        #for the case of using original pricing in cad
        if int(store["storeID"]) in stores_operating_in_CAD:
            original_price = get_inital_price(appid)
            savings = float(store["savings"]) / 100
            discount_percentage_of_orignal = 1 - savings
            discount_cad_price = original_price * discount_percentage_of_orignal
        #for the case where currency conversion is needed
        else:
            discount_cad_price = float(store["price"]) * currency_exchange_rate
        print("for store id: " + store["storeID"] + " the name of the store being: " + storelist[int(store["storeID"])-1]["storeName"] + " the value is $" + format(discount_cad_price, '.0f') + "CAD")
        

#get game name
userRequest = input("Enter game name: ")
userRequest = userRequest.lower()

#open file and regex for searching for game inside txt file
Gamefile = open("Gameslistwithappidandname.txt", mode="r")
Gamefilecontent = Gamefile.read()
Gamefilecontent = Gamefilecontent.lower()
regexForGame = '{{"appid".*?"name": "{}"}}'.format(userRequest)
regexForCheapSharkGameID = '"gameID".*?,'

#search for game that the user inputted
isFound = re.search(str(regexForGame), Gamefilecontent)
#if game is found
if isFound:
    #get appid of game
    UserGame = isFound.group()
    appid = UserGame.split(',')[0]
    appid = appid[10:]
    
    #get game id for cheapshark using the steamappid
    cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/games?steamAppID={}".format(appid)
    cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
    cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
    cheapsharkGameIDString = json.dumps(cheapsharkGameIDResponseJSON)
    cheapsharkGameIDJSON = json.loads(cheapsharkGameIDString)
    cheapsharkGameIDJSONFound = cheapsharkGameIDJSON[0]["gameID"]
    
    #if the gameid for cheapshark was found
    if cheapsharkGameIDJSONFound:
        #get deals from cheapshark for the game
        cheapsharkGameDealsRequestString = "https://www.cheapshark.com/api/1.0/games?id={}".format(cheapsharkGameIDJSONFound)
        cheapsharkGameDealsResponse = requests.get(cheapsharkGameDealsRequestString)
        cheapsharkGameDealsResponseJSON = cheapsharkGameDealsResponse.json()
        cheapsharkGameDeals = json.dumps(cheapsharkGameDealsResponseJSON)
        cheapsharkGameDealsJSON = json.loads(cheapsharkGameDeals)
        print(cheapsharkGameDealsJSON)
        #discount function to get the discounts across the stores for the game
        get_discount(cheapsharkGameDealsJSON, appid)
    else:
        print("Failed to find Cheapshark game id")
    
else:
    print("Sorry the game: " + userRequest + " Could not be found")
    

Gamefile.close()

