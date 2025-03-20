from abc import ABC
import requests
import backend.database as database
from backend.gameclass import Game
from backend.DealFactory import DealForGameSimpleFactory
#The setState() will check if there is an update to the DB that needs to occur if the price is lower, 
#if there is a change in price that is lower we will update the observer and the display, indicating a change in price for a specific subject (game)

users = database.UsersDatabase()
WishList = database.WishListDatabase()


#general class for subject of the Game
class Subject(ABC):
    #registers user as observer of the wishlisted game
    def AddObserver(Observer):  
        pass
    #removes user as an observer of the wishlisted game
    def RemoveObserver(Observer):
        pass
    #notifies the list of users for the wishlisted game that the state has changed
    def NotifyObservers():
        pass
    
#concrete class of a wishlisted game
#we are keeping track of the observers through ID's within a database
class WishlistGame(Subject):
    #list of observers exists in database, list of users = database call
    #add user as observer of game
    def AddObserver(Observer, gameid, gameprice):
        #add user to list in database
        sql = "SELECT * FROM WishList WHERE userID = %s AND gameID = %s;"
        gameexists = WishList.select(sql,Observer,gameid)
        if gameexists:
            return False
        else:
            WishList.insert(Observer,gameid,gameprice)
            return True
    def RemoveObserver(Observer, game_id):
        #remove user from list in database
        sqlsel = "SELECT * FROM WishList WHERE userID = %s AND gameID = %s;"
        usergameslist = WishList.select(sqlsel,Observer,game_id)
        if not usergameslist:
            return False
        else:
            sqldel = "DELETE FROM WishList WHERE userID = %s AND gameID = %s;"
            WishList.remove(sqldel,Observer,game_id)
            return True
    def NotifyObservers(gameid):
        #inform list of users that the state of the game has changed (cheaper price), update the value in the DB
        #{for each user in list from database call the Shopper.update() function}
        sqlsel = "SELECT userID FROM WishList WHERE gameID = %s;"
        userList = WishList.select(sqlsel, gameid)
        for i in userList:
            userid = i["userID"]
            Shopper.update(userid)
    #set the state of the subject (set the price within the database)
    def setState(game_id):
        #set new price into database if it is lower (use the getState() function to possibly retreive from database)
        #call notifyObservers() if it is lower
        CurrGameObj = DealForGameSimpleFactory.GetGameDealsAcrossStores(game_id)
        wishlist=CurrGameObj.getWishListFormatDict()
        AcquiredWishlistList = wishlist[str(CurrGameObj.gameSteamAppId())]
        lowest_price = AcquiredWishlistList[1]
        sqlsel = "SELECT price FROM WishList Where gameID = %s;"
        databaseprice = WishList.select(sqlsel,game_id)
        if(lowest_price<databaseprice[0]["price"]):
            sqludp = "UPDATE WishList SET price = %s WHERE gameID = %s;"
            WishList.select(sqludp,lowest_price,game_id)
            WishlistGame.NotifyObservers(game_id)
    #get current price of game function
    def getState(observer):
        sql ="SELECT updateuser FROM Users WHERE id = %s;"
        user = users.select(sql,observer)
        if user[0]["updateuser"]==1:
            return Shopper.updateview()
        else:
            return False

class Observer(ABC):
    
    #general update function that takes in the game and the new price
    def update(WishlistGame, priceOfGame):
        
        pass

class Shopper(Observer):
    #update the price of the game in the database for the gameid
    def update(user_id):
        #update the screen with the new price of the game
        #use the updateview function to update the screen
        sql = "UPDATE Users SET updateuser=1 WHERE id = %s;"
        users.select(sql,user_id)

            #updateview()
    def updateview():
        #change the view of the user to indiciate a change has occurred
        return True