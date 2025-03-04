import requests
import json
import re

fileout = open("storelist.json", mode="w")

cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/stores"
cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
json.dump(cheapsharkGameIDResponseJSON, fileout)

fileout.close()
