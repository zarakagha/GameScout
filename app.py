import os
from flask import Flask, request, render_template, session, redirect, flash 
from flask_session import Session
from datetime import timedelta
import requests
import urllib.parse
import json
from backend.gameclass import Game
from backend.DealFactory import DealForGameSimpleFactory
from backend.StoreNameAndPrice import StoreIDAction
from backend.checkNSFW import CheckGameisNSFW
from backend.GetSteamPriceCadForGame import get_inital_price
from backend.ConvertPrice import ConvertUSDToCad
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import re



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='SECRETKEY'
app.secret_key="GameScout"
db = SQLAlchemy(app)
SECRET_KEY = "GameScout"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.permanent_session_lifetime = timedelta(minutes=10)

Session(app)

class user(db.Model):
      __tablename__ = 'user'
      id=db.Column(db.Integer, primary_key=True)
      firstname= db.Column(db.String(100), nullable=False)
      lastname= db.Column(db.String(100), nullable=False)
      username= db.Column(db.String(100),unique=True, nullable=False)
      email= db.Column(db.String(100),unique=True, nullable=False)
      password=db.Column(db.String(100),nullable=False)
      isadmin = db.Column(db.Boolean, default=False, nullable=False)
      
class games(db.Model):
      __tablename__ = 'games'
      id=db.Column(db.Integer, primary_key=True)
      gameID= db.Column(db.String(100), nullable=False)
      user_id =db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

firstnameRegex=r'^[a-zA-Z]+$'
lastnameRegex=r'^[a-zA-Z]+$'
usernameRegex=r'^[a-zA-Z0-9]+$'
emailRegex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
passwordRegex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

@app.route('/',methods=["GET","POST"])
def serve_form():
    steamgamesDict = {}
    epicgamesDict = {}
    goggamesDict = {}
    fanaticalgamesDict = {}
    steamgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=1")
    steamgamesjson=steamgames.json()
    steamgamesjson=steamgamesjson[:9]
    for currentdeal in steamgamesjson:
          try:
                OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                savings = int(round(float(currentdeal["savings"]), 0))
                steamgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"]]
          except:
                print("Error in creating dictionary for game for Steam, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                continue
    epicgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=25")
    epicgamesjson=epicgames.json()
    epicgamesjson=epicgamesjson[:9]
    for currentdeal in epicgamesjson:
          try:
                OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                savings = int(round(float(currentdeal["savings"]), 0))
                epicgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"]]
          except:
                print("Error in creating dictionary for game for Epic, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                continue
    goggames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=7")
    goggamesjson=goggames.json()
    goggamesjson=goggamesjson[:9]
    for currentdeal in goggamesjson:
          try:
                OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                savings = int(round(float(currentdeal["savings"]), 0))
                goggamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"]]
          except:
                print("Error in creating dictionary for game for GOG, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                continue
    fanaticalgames=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=15")
    fanaticalgamesjson=fanaticalgames.json()
    fanaticalgamesjson=fanaticalgamesjson[:9]
    for currentdeal in fanaticalgamesjson:
          try:
                OriginalPriceOfGame = get_inital_price(currentdeal["steamAppID"])
                discounted_price = round(ConvertUSDToCad.convertPriceForGame(float(OriginalPriceOfGame), int(currentdeal["storeID"]), float(currentdeal["savings"])), 2)
                savings = int(round(float(currentdeal["savings"]), 0))
                fanaticalgamesDict[str(currentdeal["steamAppID"])] = [str(OriginalPriceOfGame), discounted_price, savings, currentdeal["title"]]
          except:
                print("Error in creating dictionary for game for Fanatical, Game name: " + currentdeal["title"] + " Steam App ID value: " + str(currentdeal["steamAppID"]))
                continue
    print(steamgamesDict)
    print(epicgamesDict)
    print(goggamesDict)
    print(fanaticalgamesjson)
    print(fanaticalgamesDict)
    return render_template("mainpage.html", steamgamesjson=steamgamesDict.items(),epicgamesjson=epicgamesDict.items(),goggamesjson=goggamesDict.items(),fanaticalgamesjson=fanaticalgamesDict.items()) 
@app.route('/accounts')
def accounts():
        return render_template("accounts.html")
@app.route('/admin')
def admin():
        return render_template("admin.html")

@app.route('/adminUser')
def adminUser():
        return render_template("adminUser.html")
@app.route('/adminGamePage')
def adminGamePage():
        return render_template("adminGamePage.html")
@app.route('/adminGame')
def adminGame():
        return render_template("adminGame.html")
@app.route('/genre')
def genre():
        return render_template("genre.html")
@app.route('/login',methods=["GET","POST"])
def login():
        if request.method=="POST":
            username =request.form.get('username')
            password =request.form.get('password')
            checkusername = user.query.filter_by(username=username).first()
            

            if checkusername and user.password == password:
                  session.permant = True
                  session['userid']=user.id
                  session['username']=user.username
                  session['usertype'] = user.isadmin
                  if session['usertype'] == True:
                        return redirect ('/admin')
                  else:
                        return redirect ('/')
            
        return render_template("login.html")
@app.route('/signup', methods=["GET","POST"])
def signup():
        if request.method=="POST":
            firstname=request.form.get('firstname')
            lastname=request.form.get('lastname')
            username=request.form.get('username')
            email=request.form.get('email')
            password=request.form.get('password')
        
            if not firstname or not lastname or not username or not email or not password:
              return "please enter all data",400
            elif not re.match(firstnameRegex,firstname):
              return "please enter a first name with only letters",400
            elif not re.match(lastnameRegex,lastname):
              return "please enter a last name with only letters",400
            elif not re.match(usernameRegex,username):
              return "please enter a username with only letters and numbers",400
            elif not re.match(emailRegex,email):
              return "please enter a valid email",400
            elif not re.match(passwordRegex,password):
              return "please enter a valid password",400
            exists = user.query.filter((user.username== username)|(user.email == email)).first()
            if exists:
              return "user already exists",400
            new_user =user(firstname=firstname,lastname=lastname,username=username,password=password,email=email,isadmin=False)
            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
        else:
            return render_template("signup.html")

@app.route('/wishlist')
def wishlist():
        return render_template("wishlist.html")
@app.route('/gamesearch',methods =["GET","POST"])
def get_Game():
    if request.method == "POST":
        name= request.form.get("name")
        session["name"]=name 
        return redirect('/game') 
    else:
        return redirect('/') 

@app.route('/game', methods=["GET","POST"])

def game():
    
   gamename=session.get("name")
   game_name=str(gamename)
   game_name=game_name.replace(" ","+")
   gamelist=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=1&title={}".format(game_name))
   gamelistjson=gamelist.json()
   gamelistjson=gamelistjson[:15]
   print(gamelistjson)
   noNSFWGameList = []
   for game in gamelistjson:
         if CheckGameisNSFW.isNSFWGame(game["steamAppID"]):
               continue
         else:
               noNSFWGameList.append(game)
   if not gamename:
        return redirect("/",error="please enter game name")
   
   if len(noNSFWGameList) == 0:
         error="no games found"
         return render_template("explore.html",error=error)  
   if gamename:
        return render_template("explore.html",game_list=noNSFWGameList)
   else:
        return render_template("explore.html", error="Game details not found.")

@app.route('/gamedetail/<int:game_id>')

def gamedetail(game_id):
      print(game_id)
      currentgamedeals=DealForGameSimpleFactory.GetGameDealsAcrossStores(game_id)
      name=currentgamedeals.GetGamename()
      storedict=StoreIDAction.StoreIDToNameWithPrice(currentgamedeals.storeWithPriceSavingsDealURl())
      gameImg=currentgamedeals.gameImage()
      print(storedict)
      if game_id:
            return render_template("game.html",gamename=name,store_dict=storedict.items(), gameIMG=gameImg)
      else:
            return render_template("game.html",404,404)

with app.app_context():
    db.create_all() 

if __name__=='__main__':
   app.run(debug=True)

