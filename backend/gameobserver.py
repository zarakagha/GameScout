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
class WishlistGame(Subject):
    #list of observers that have wishlisted the game
    listOfObservers = []
    def __init__(self):
        self.PriceOfGame = 0
    #add user as observer of game
    def AddObserverToWishlist(Observer):
        #add user to list in database
        pass
    def RemoveObserverFromWishlist(Observer):
        #remove user from list in database
        pass
    def NotifyObservers():
        #inform list of users that the state of the game has changed (cheaper price), update the value in the DB
        pass
    #get current price of game function
    def getState():
        #gets the current price
        pass
    

class Observer(ABC):
    lowest_stored_price_in_db = 0
    def update():
        pass

class Shopper(Observer):
    lowest_stored_price_in_db = 0
    #update the price of the game in the database for the gameid
    def update(currentsubject, priceOfGame):
        #check if price is lower than stored value
        # if lower set lowest_stored_price_in_db = priceOfGame
        #probably update the value in the db afterwards
        pass
    def updateview():
        #change the view of the user to indiciate a change has occurred
        pass