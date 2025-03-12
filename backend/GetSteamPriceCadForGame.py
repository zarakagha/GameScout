import requests
import json


def get_inital_price(appid):
    SteamRetailPriceResponse = requests.get("http://store.steampowered.com/api/appdetails?appids={}&cc=CA&filters=price_overview".format(appid))
    SteamRetailPriceJSON = SteamRetailPriceResponse.json()
    inital_price = SteamRetailPriceJSON[str(appid)]["data"]["price_overview"]["initial"]
    inital_price = float(inital_price) / 100
    return inital_price