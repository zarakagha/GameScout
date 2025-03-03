import requests
import json
import re


userRequest = input("Enter EXACT game name: ")

Gamefile = open("Gameslistwithappidandname.txt", mode="r")

for line in Gamefile:
    
    

#cheapSharkResponse = requests.get("https://www.cheapshark.com/api/1.0/games?id=236717")
#print(cheapSharkResponse)
#Result = cheapSharkResponse.json()
#print(json.dumps(Result))