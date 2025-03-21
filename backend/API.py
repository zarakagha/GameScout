import os
from flask import Flask, request, render_template, session, redirect, flash 
from flask_session import Session
from datetime import timedelta
import requests
import urllib.parse
import json
import pymysql
import backend.database as database
from backend.gameclass import Game
from backend.DealFactory import DealForGameSimpleFactory
from backend.StoreNameAndPrice import StoreIDAction
from backend.checkNSFW import CheckGameisNSFW
from backend.GetSteamPriceCadForGame import get_inital_price
from backend.ConvertPrice import ConvertUSDToCad
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, text
import re
import threading
import concurrent.futures
from backend.sessionVariables import SessionData

#loads access to users and wishlist tables in the database
users = database.UsersDatabase()
WishList = database.WishListDatabase()

'''
This is the main API class which is used to load the games in the main page.
'''
class API:
    #In the constructor the class API is passed the memory address to the session variables and 
    #stores then as a variable inside the class
    def __init__(self,sessionData):
        self.sessionData = sessionData

    '''
    This is the main function which calls the API for the main page. The function
    firs checks if the API's have already been loaded. The function works by 
    multithreading and calling functions which call multiple APIs at the same time.
    The function creates four thread for the four gamestore APIs that is must call.
    It then starts the threads which call the function. It joins the threads then 
    ends the function.

    Inputs: None
    Outputs: None
    Uses: session data,self.cheapsharkAPI,self.epicAPI,self.GOGAPI,self.fanaticalAPI
    '''
    def runMainAPI(self):
         # checks if the API has been loaded already
         if not self.sessionData.Loaded:
              #Uses python threading to create four threads. It sets the target to a function
              #loading the API
              cheapsharkThread = threading.Thread(target = self.cheapsharkAPI)
              epicThread = threading.Thread(target = self.epicAPI)
              GOGThread = threading.Thread(target = self.GOGAPI)
              fanaticalThread = threading.Thread(target = self.fanaticalAPI)

              #This will start the tread
              cheapsharkThread.start()
              epicThread.start()
              GOGThread.start()
              fanaticalThread.start()
              
              #This will join all of the threads which means waiting for 
              #all the treads to end before the parent can proceed
              cheapsharkThread.join()
              epicThread.join()
              GOGThread.join()
              fanaticalThread.join()
              
              #sets Loaded to True to indicate that the API's are loaded
              self.sessionData.Loaded = True

    '''
    Loads the games from Cheapshark. It sends a request to cheapshark.com for games from
    that store to be displayed on the main page. The functions stores that values to these calls
    in a sessiondata dict called steamgamesDict.
    Input: None
    Output: None
    Uses: session vars,api calls
    '''
    def cheapsharkAPI(self):
        #request the api
        steamgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=1")
        #converts it into a json
        steamgamesjson=steamgames.json()
        #picks the first 9 games
        steamgamesjson=steamgamesjson[:9]
        #loops through the games
        for currentdeal in steamgamesjson:
            try:
                  #gets the price of the game,the discounted price, savings and puts it
                  #into the sessiondata dictionary
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.steamgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  #error
                  print("Error in creating dictionary for game for Steam, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
    '''
    Loads the games from epic. It sends a request to cheapshark for epic games for games from
    that store to be displayed on the main page. The functions stores that values to these calls
    in a sessiondata dict called steamgamesDict.
    Input: None
    Output: None
    Uses: session vars,api calls
    '''    
    def epicAPI(self):
        #request the api
        epicgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=25")
        #converts it into a json
        epicgamesjson=epicgames.json()
        #picks the first 9 games
        epicgamesjson=epicgamesjson[:9]
        #loops through the games
        for currentdeal in epicgamesjson:
            try:
                  #gets the price of the game,the discounted price, savings and puts it
                  #into the sessiondata dictionary
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.epicgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  #error
                  print("Error in creating dictionary for game for Epic, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
    '''
    Loads the games from GOG. It sends a request to cheapshark.com for games from
    that store to be displayed on the main page. The functions stores that values to these calls
    in a sessiondata dict called steamgamesDict.
    Input: None
    Output: None
    Uses: session vars,api calls
    '''
    def GOGAPI(self):
        #request the api
        goggames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=7")
        #converts it into a json
        goggamesjson=goggames.json()
        #picks the first 9 games
        goggamesjson=goggamesjson[:9]
        #loops through the games
        for currentdeal in goggamesjson:
            try:
                  #gets the price of the game,the discounted price, savings and puts it
                  #into the sessiondata dictionary
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.goggamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  #error
                  print("Error in creating dictionary for game for GOG, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
    
    '''
    Loads the games from fanatical. It sends a request to cheapshark.com for games from
    that store to be displayed on the main page. The functions stores that values to these calls
    in a sessiondata dict called steamgamesDict.
    Input: None
    Output: None
    Uses: session vars,api calls
    '''
    def fanaticalAPI(self):
        #request the api
        fanaticalgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=15")
        #converts it into a json
        fanaticalgamesjson=fanaticalgames.json()
        #picks the first 9 games
        fanaticalgamesjson=fanaticalgamesjson[:9]
        #loops through the games
        for currentdeal in fanaticalgamesjson:
            try:
                  #gets the price of the game,the discounted price, savings and puts it
                  #into the sessiondata dictionary
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.fanaticalgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  #Error
                  print("Error in creating dictionary for game for Fanatical, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
            
    '''
    RunWishAPI: This function calls the API to load the game details for the wishlist.
    It also uses multithreading and it does this by breaking the wishlist into groups of 
    5 and sending each thread to do one of these groups.

    Input: UserID
    Output: None
    Uses: sessionData,api calls,database
    '''
    def runWishAPI(self, userID):
        #gets the wishlist from the database class using the userid
        sql = "SELECT * FROM WishList WHERE userID = %s;"
        usergameslist = WishList.select(sql,userID)
        
        #sets thread size
        size = 5
        #creates a list with threads
        threads = [0]*((len(usergameslist)-1)//size + 1)
        #creates a mutex lock for the sessiondata dictionary
        mutex_lock = threading.Lock()
        #loops through all the threads
        for i in range((len(usergameslist)-1)//size + 1):
            #checks if it is the last thread
            if size*(i+1) >= len(usergameslist):
                #makes thread contain remaining items
                threads[i] = threading.Thread(target = self.wishAPI, args = ( usergameslist[size*i:],mutex_lock))
            else:
                #puts 5 items from the wishlist into a thread and calls wishAPI function
                threads[i] = threading.Thread(target = self.wishAPI, args = (  usergameslist[size*i:size*i+size],mutex_lock))#

        #starts all the threads
        for i in range(len(threads)):
             threads[i].start()
        #joins all the threads
        for i in range(len(threads)):
             threads[i].join()
        
             
    '''
    wishAPI: the main API function that actually calls the API to load the wishlist. it loops through the usergameslist
    calls the API and updates the session data

    Inputs: wishlist for this thread, mutex lock to protect the wishlist
    Outputs: None
    Uses: sessionData,api calls,database
    '''
    def wishAPI(self,usergameslist,lock):      
        #loops through the games
        for game in usergameslist:
            #gets gameid
            id=game["gameID"]
            #looks accross stores for game price
            CurrGameObj = DealForGameSimpleFactory.GetGameDealsAcrossStores(id)
            #turns into a proper dictionary 
            wishlist=CurrGameObj.getWishListFormatDict()
            AcquiredWishlistList = wishlist[str(CurrGameObj.gameSteamAppId())]
            #finds initial price, lowest price, savings, title
            inital_price = str(AcquiredWishlistList[0])
            lowest_price = AcquiredWishlistList[1]
            savings = AcquiredWishlistList[2]
            title = AcquiredWishlistList[3]
            #locks sessionData.gamedetailDict which is a shared resource
            lock.acquire()
            #updates sessionData
            self.sessionData.gamedetailDict[CurrGameObj.gameSteamAppId()] = [inital_price, lowest_price, savings, title, id, 0]
            #releases lock
            lock.release()

    '''
    addToWishList: used to add a single element to a wishlist

    Inputs: id for the user
    Outputs: None
    Uses: sessionData,api calls,database
    '''
    def addToWishList(self,id):
        #finds prices of game accross stores
        CurrGameObj = DealForGameSimpleFactory.GetGameDealsAcrossStores(id)
        #formats the object
        wishlist=CurrGameObj.getWishListFormatDict()
        AcquiredWishlistList = wishlist[str(CurrGameObj.gameSteamAppId())]
        #finds initial price, lowest price, savings, title
        inital_price = str(AcquiredWishlistList[0])
        lowest_price = AcquiredWishlistList[1]
        savings = AcquiredWishlistList[2]
        title = AcquiredWishlistList[3]
        #puts data in session variable
        self.sessionData.gamedetailDict[CurrGameObj.gameSteamAppId()] = [inital_price, lowest_price, savings, title, id,0]
        
    
      
        
    