from backend.gameclass import Game
from backend.ConvertPrice import ConvertUSDToCad
from backend.DealFactory import DealForGameSimpleFactory
from pprint import pprint

newobj = DealForGameSimpleFactory.GetGameDealsAcrossStores("236717")
pprint(vars(newobj))