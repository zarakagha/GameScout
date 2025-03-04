import requests
import json
import re


cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/games?steamAppID=1245620"
cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
data = json.loads(cheapsharkGameIDResponseJSON)

print(data)