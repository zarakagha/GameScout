from backend.gameclass import Game
from backend.ConvertPrice import ConvertUSDToCad
from backend.DealFactory import DealForGameSimpleFactory
from pprint import pprint
import backend.database as database

Gamestores = database.Gamestores()
users = database.UsersDatabase()
WishList = database.WishListDatabase()


sql = "UPDATE WishList SET price = %s WHERE gameID = %s;"
sqlsel = "SELECT * FROM WishList;"
price = WishList.select(sql,1000,236717)
game = WishList.select(sqlsel)
print(game)

#sql = "SELECT enabled FROM Gamestores WHERE id = %s;"
#game = Gamestores.select(sql, 2)
#print(game[0]["enabled"])


#newobj = DealForGameSimpleFactory.GetGameDealsAcrossStores("236717")
#pprint(vars(newobj))
#hi