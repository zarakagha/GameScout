import requests
import json

#function to get inital price of for a game in CAD
def get_inital_price(appid):
    #get the api response from steam that contains information about a game
    SteamRetailPriceResponse = requests.get("http://store.steampowered.com/api/appdetails?appids={}&cc=CA&filters=price_overview".format(appid))
    #get json file
    SteamRetailPriceJSON = SteamRetailPriceResponse.json()
    #get the inital price
    inital_price = SteamRetailPriceJSON[str(appid)]["data"]["price_overview"]["initial"]
    #convert to float
    inital_price = float(inital_price) / 100
    #Return the initial price
    return inital_price