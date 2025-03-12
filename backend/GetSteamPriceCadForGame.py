import requests
import json


def get_inital_price(appid):
    SteamRetailPriceResponse = requests.get("http://store.steampowered.com/api/appdetails?appids={}&cc=CA&filters=price_overview".format(appid))
    SteamRetailPriceResponseJSON = SteamRetailPriceResponse.json()
    SteamRetailPriceString = json.dumps(SteamRetailPriceResponseJSON)
    SteamRetailPriceJSON = json.loads(SteamRetailPriceString)
    inital_price = SteamRetailPriceJSON[appid]["data"]["price_overview"]["initial"]
    inital_price = float(inital_price) / 100
    return inital_price