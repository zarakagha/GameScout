import requests

#https://api.steampowered.com/{interface}/{method}/{version}/?key={your_api_key}&{parameters}

steamResponse = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/?key=SETKEYHERE")
steamGamesList = steamResponse.json()
print(steamGamesList)