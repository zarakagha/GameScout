import requests
import json
import re
from gameclass import Game

class DealForGameSimpleFactory:
    
    def __init__(self, cheapsharkID):
        self.current_game = Game(cheapsharkID)
        
    def GetGameDealsAcrossStores(appid):
        cheapshark