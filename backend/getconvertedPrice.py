

import requests
import json
import re




"""
def get_inital_price(appid):
    SteamRetailPriceResponse = requests.get("http://store.steampowered.com/api/appdetails?appids={}&cc=CA&filters=price_overview".format(appid))
    SteamRetailPriceResponseJSON = SteamRetailPriceResponse.json()
    SteamRetailPriceString = json.dumps(SteamRetailPriceResponseJSON)
    SteamRetailPriceJSON = json.loads(SteamRetailPriceString)
    inital_price = SteamRetailPriceJSON[appid]["data"]["price_overview"]["initial"]
    inital_price = float(inital_price) / 100
    inital_price = str(inital_price)
    return inital_price
"""

def get_currency_exchange_rate():
    currencyexchangeResponse = requests.get("")
    currencyexchangeResponseJSON = currencyexchangeResponse.json()
    currencyexchangeResponseString = json.dumps(currencyexchangeResponseJSON)
    currencyexchangeJSON = json.loads(currencyexchangeResponseString)
    print(currencyexchangeJSON["conversion_rates"]["CAD"])
    return currencyexchangeJSON["conversion_rates"]["CAD"]


TestcheapSharkResponse = requests.get("https://www.cheapshark.com/api/1.0/games?id=236717")
TestcheapSharkResponseJSON = TestcheapSharkResponse.json()
TestcheapsharkResponseString = json.dumps(TestcheapSharkResponseJSON)
TestcheapsharkDealsJSON = json.loads(TestcheapsharkResponseString)

def get_discount(appid):
    currency_exchange_rate = float(get_currency_exchange_rate())
    for store in TestcheapsharkDealsJSON["deals"]:
        discount_cad_price = float(store["price"]) * currency_exchange_rate
        print("for store id: " + store["storeID"] + " the value is $" + format(discount_cad_price, '.2f') + "CAD")
        

get_discount("1245620")


"""

#store 1 = steam
#store 7 = GOG
#store 8 = origin
#store 11 = Humble
#store 25 = epic games
#store 31 = blizzard

userRequest = input("Enter game name: ")
userRequest = userRequest.lower()

Gamefile = open("Gameslistwithappidandname.txt", mode="r")
Gamefilecontent = Gamefile.read().lower()
regexForGame = '{{"appid".*?"name": "{}"}}'.format(userRequest)
regexForCheapSharkGameID = '"gameID".*?,'


isFound = re.search(str(regexForGame), Gamefilecontent)
if isFound:
    UserGame = isFound.group()
    appid = UserGame.split(',')[0]
    appid = appid[10:]
    
    cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/games?steamAppID={}".format(appid)
    cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
    cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
    cheapsharkGameIDString = json.dumps(cheapsharkGameIDResponseJSON)
    cheapsharkGameIDJSON = json.loads(cheapsharkGameIDString)
    cheapsharkGameIDJSONFound = cheapsharkGameIDJSON[0]["gameID"]
    if cheapsharkGameIDJSONFound:
        cheapsharkGameDealsRequestString = "https://www.cheapshark.com/api/1.0/games?id={}".format(cheapsharkGameIDJSONFound)
        cheapsharkGameDealsResponse = requests.get(cheapsharkGameDealsRequestString)
        cheapsharkGameDealsResponseJSON = cheapsharkGameDealsResponse.json()
        cheapsharkGameDeals = json.dumps(cheapsharkGameDealsResponseJSON)
        cheapsharkJSON = json.loads(cheapsharkGameDeals)
        print(cheapsharkJSON["deals"])
    else:
        print("Failed to find Cheapshark game id")
    
else:
    print("Sorry the game: " + userRequest + " Could not be found")
    



    

#cheapSharkResponse = requests.get("https://www.cheapshark.com/api/1.0/games?id=236717")
#print(cheapSharkResponse)
#Result = cheapSharkResponse.json()
#print(json.dumps(Result)

Gamefile.close()

"""