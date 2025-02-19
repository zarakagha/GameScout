import requests
import json


steamResponse = requests.get("")
print(steamResponse)
steamGame = steamResponse.json()
print(json.dumps(steamGame))