import requests
import json
from backend.gameclass import Game


class CheckGameisNSFW:
        
    def isNSFWGame(steamappid):
        nsfw_tag_list_steam = ["nudity", "sexual", "sexual content", "nsfw", "hentai"]
        steamspyResponseJSON = requests.get("https://steamspy.com/api.php?request=appdetails&appid=2246340&appid={}".format(str(steamappid))).json()
        if len(steamspyResponseJSON["tags"]) != 0:
            list_of_game_tags = steamspyResponseJSON["tags"].items()
            for tag in list_of_game_tags:
                currtag = str(tag[0]).lower()
                if currtag in nsfw_tag_list_steam:
                    return True
        else:
            return False
        