from abc import ABC

#The setState() will check if there is an update to the DB that needs to occur if the price is lower, 
#if there is a change in price that is lower we will update the observer and the display, indicating a change in price for a specific subject (game)


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
    def AddObserver(Observer):
        #add user to list in database
        pass
    def RemoveObserver(Observer):
        #remove user from list in database
        pass
    def NotifyObservers():
        #inform list of users that the state of the game has changed (cheaper price), update the value in the DB
        #{for each user in list from database call the Shopper.update() function}
        pass
    #set the state of the subject (set the price within the database)
    def setState():
        #set new price into database if it is lower (use the getState() function to possibly retreive from database)
        #call notifyObservers() if it is lower
        pass
    #get current price of game function
    def getState():
        #gets state within the database
        pass
    

class Observer(ABC):
    #general update function that takes in the game and the new price
    def update(WishlistGame, priceOfGame):
        pass

class Shopper(Observer):
    lowest_stored_price_in_db = 0
    #update the price of the game in the database for the gameid
    def update(WishlistGame, priceOfGame):
        #update the screen with the new price of the game
        #use the updateview function to update the screen
        pass
    def updateview():
        #change the view of the user to indiciate a change has occurred
        pass