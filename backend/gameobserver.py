from abc import ABC


#general class for subject of the Game
class Subject(ABC):
    #registers user as observer of the wishlisted game
    def AddObserverToWishlist(Observer):
        pass
    #removes user as an observer of the wishlisted game
    def RemoveObserverFromWishlist(Observer):
        pass
    #notifies the list of users for the wishlisted game that the state has changed
    def NotifyObservers():
        pass
    
#concrete class of a wishlisted game
#we are keeping track of the observers through ID's within a database
class WishlistGame(Subject):
    #list of observers exists in database, list of users = database call
    #add user as observer of game
    def AddObserverToWishlist(Observer):
        #add user to list in database
        pass
    def RemoveObserverFromWishlist(Observer):
        #remove user from list in database
        pass
    def NotifyObservers():
        #inform list of users that the state of the game has changed (cheaper price), update the value in the DB
        #{for each user in list from database call the Shopper.update() function}
        pass
    #set the state of the subject (set the price within the database)
    def setState():
        #set price into database
        pass
    #get current price of game function
    def getState():
        #gets state within the database
        pass
    

class Observer(ABC):
    lowest_stored_price_in_db = 0
    def update():
        pass

class Shopper(Observer):
    lowest_stored_price_in_db = 0
    #update the price of the game in the database for the gameid
    def update(WishlistGame, priceOfGame):
        #use the getState() from the WishlistGame class to get the datavalue of interest from Database
        #check if price is lower than stored value
        #if lower set lowest_stored_price_in_db = priceOfGame
        #probably update the value in the db afterwards
        #call updateview() function
        pass
    def updateview():
        #change the view of the user to indiciate a change has occurred
        pass