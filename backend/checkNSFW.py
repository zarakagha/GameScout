import requests
import json
from backend.gameclass import Game

# class used for checking if a particular game is NSFW using tags
class CheckGameisNSFW:
    
    #method to check is a game is NSFW based on its steam app id
    def isNSFWGame(steamappid):
        #list of NSFW tags for games
        nsfw_tag_list_steam = ["nudity", "sexual", "sexual content", "nsfw", "hentai"]
        #using steam spy api, we will get the JSON file that has information about the game, most importantly its tags
        steamspyResponseJSON = requests.get("https://steamspy.com/api.php?request=appdetails&appid=2246340&appid={}".format(str(steamappid))).json()
        #check to make sure tags exist on the game
        if len(steamspyResponseJSON["tags"]) != 0:
            #get the tags for the game
            list_of_game_tags = steamspyResponseJSON["tags"].items()
            #for each tag, compare it to the list of nsfw tags, if it is in the nsfw tag list then return TRUE as it is NSFW otherwise return False.
            for tag in list_of_game_tags:
                currtag = str(tag[0]).lower()
                if currtag in nsfw_tag_list_steam:
                    return True
        else:
            return False
        