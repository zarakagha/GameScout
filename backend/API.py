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


users = database.UsersDatabase()
WishList = database.WishListDatabase()


class API:
    def __init__(self,sessionData):
        self.sessionData = sessionData


    def runMainAPI(self):
         if not self.sessionData.Loaded:
              cheepsharkThread = threading.Thread(target = self.cheepsharkAPI)
              epicThread = threading.Thread(target = self.epicAPI)
              GOGThread = threading.Thread(target = self.GOGAPI)
              fanaticalThread = threading.Thread(target = self.fanaticalAPI)

              cheepsharkThread.start()
              epicThread.start()
              GOGThread.start()
              fanaticalThread.start()

              cheepsharkThread.join()
              epicThread.join()
              GOGThread.join()
              fanaticalThread.join()

              self.sessionData.Loaded = True

    
    def cheepsharkAPI(self):
        steamgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=1")
        steamgamesjson=steamgames.json()
        steamgamesjson=steamgamesjson[:9]
        for currentdeal in steamgamesjson:
            try:
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.steamgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  print("Error in creating dictionary for game for Steam, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
            
    def epicAPI(self):
        epicgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=25")
        epicgamesjson=epicgames.json()
        epicgamesjson=epicgamesjson[:9]
        for currentdeal in epicgamesjson:
            try:
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.epicgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  print("Error in creating dictionary for game for Epic, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
            
    def GOGAPI(self):
        goggames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=7")
        goggamesjson=goggames.json()
        goggamesjson=goggamesjson[:9]
        for currentdeal in goggamesjson:
            try:
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.goggamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  print("Error in creating dictionary for game for GOG, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
            
    def fanaticalAPI(self):
        fanaticalgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=15")
        fanaticalgamesjson=fanaticalgames.json()
        fanaticalgamesjson=fanaticalgamesjson[:9]
        for currentdeal in fanaticalgamesjson:
            try:
                  OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                  discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                  savings = int(round(float(currentdeal["savings"]), 0))
                  self.sessionData.fanaticalgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"], currentdeal["gameID"]]
            except:
                  print("Error in creating dictionary for game for Fanatical, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                  continue
            
            
    def runWishAPI(self, userID):
         
        sql = "SELECT * FROM WishList WHERE userID = %s;"
        usergameslist = WishList.select(sql,userID)
        #self.wishAPI(usergameslist)
        size = 5
        threads = [0]*((len(usergameslist)-1)//size + 1)
        mutex_lock = threading.Lock()
        for i in range((len(usergameslist)-1)//size + 1):
            
            if size*(i+1) >= len(usergameslist):
                threads[i] = threading.Thread(target = self.wishAPI, args = ( usergameslist[size*i:],mutex_lock))
            else:
                threads[i] = threading.Thread(target = self.wishAPI, args = (  usergameslist[size*i:size*i+size],mutex_lock))

        for i in range(len(threads)):
             threads[i].start()

        for i in range(len(threads)):
             threads[i].join()
        
             

    def wishAPI(self,usergameslist,lock):      
        
        for game in usergameslist:
            id=game["gameID"]
            gamedetails=requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(id))
            gamedetailsjson=gamedetails.json()
                         
                                                            
            OriginalPriceOfGame = get_inital_price(gamedetailsjson["info"]["steamAppID"])
            discounted_price,store = ConvertUSDToCad.getDiscountedPrice(gamedetailsjson["deals"])
            savings = int(round((1.0 - discounted_price/float(OriginalPriceOfGame))*100 ))
            lock.acquire()
            self.sessionData.gamedetailDict[str(gamedetailsjson["info"]["steamAppID"])] = [str(OriginalPriceOfGame), round(discounted_price,2), savings, gamedetailsjson["info"]["title"], id,store]
            lock.release()

    def addToWishList(self,id, original_price, discounted_price, savings):
        gamedetails=requests.get("https://www.cheapshark.com/api/1.0/games?id={}".format(id))
        gamedetailsjson=gamedetails.json()
        print(original_price)
        print(discounted_price)
        print(savings)
                                                            
        #discounted_price,store = ConvertUSDToCad.getDiscountedPrice(gamedetailsjson["deals"])
        #savings = int(round((1.0 - discounted_price/float(OriginalPriceOfGame))*100 ))
        self.sessionData.gamedetailDict[str(gamedetailsjson["info"]["steamAppID"])] = [str(original_price), discounted_price, savings, gamedetailsjson["info"]["title"], id,0]
        print(self.sessionData.gamedetailDict[str(gamedetailsjson["info"]["steamAppID"])])
        
    
      
        
    