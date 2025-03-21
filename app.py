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
import re
import threading
from backend.sessionVariables import SessionData
from backend.API import API
from backend.gameobserver import WishlistGame,Shopper



app = Flask(__name__)
app.config['SECRET_KEY'] ='SECRETKEY'
app.secret_key="GameScout"
SECRET_KEY = "GameScout"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.permanent_session_lifetime = timedelta(minutes=10)

Session(app)




users = database.UsersDatabase()
WishList = database.WishListDatabase()
Gamestores = database.Gamestores()


def loginchecker():
     return 'userid' in session

firstnameRegex=r'^[a-zA-Z]+$'
lastnameRegex=r'^[a-zA-Z]+$'
usernameRegex=r'^[a-zA-Z0-9]+$'
emailRegex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
passwordRegex=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"


sessionData = SessionData()
api =API(sessionData)




@app.route('/',methods=["GET","POST"])
def serve_form():
    api.runMainAPI()
    try:
      if session['userid']==None:
            return render_template("mainpage.html", steamgamesjson=sessionData.steamgamesDict.items(),epicgamesjson=sessionData.epicgamesDict.items(),goggamesjson=sessionData.goggamesDict.items(),fanaticalgamesjson=sessionData.fanaticalgamesDict.items(),wishlistupdate=False, loginbutton=True)
      else:
         needsupdate=WishlistGame.getState(session['userid'])
         sql = "UPDATE Users SET updateuser=0 WHERE id = %s;"
         users.select(sql,session['userid'])
         return render_template("mainpage.html", steamgamesjson=sessionData.steamgamesDict.items(),epicgamesjson=sessionData.epicgamesDict.items(),goggamesjson=sessionData.goggamesDict.items(),fanaticalgamesjson=sessionData.fanaticalgamesDict.items(),wishlistupdate=needsupdate,loginbutton=False)   
    except:
            return render_template("mainpage.html", steamgamesjson=sessionData.steamgamesDict.items(),epicgamesjson=sessionData.epicgamesDict.items(),goggamesjson=sessionData.goggamesDict.items(),fanaticalgamesjson=sessionData.fanaticalgamesDict.items(),wishlistupdate=False,loginbutton=True)
         
@app.route('/accounts', methods = ["POST", "GET"])
def accounts():
      if 'usertype' not in session.keys() or session["usertype"] == 0 :
            
            return redirect("/login")
      if request.method=="POST":
            username = request.form.get('usertextsearch')
            select = request.form.get("order")
            print(select)

            if username != None:
                  userList = users.select("SELECT * FROM Users WHERE username = %s AND isAdmin = 0;",username)
            
                  if len(userList) == 0:
                        userList = users.select("SELECT * FROM Users WHERE username REGEXP %s AND isAdmin = 0 ORDER BY {s};".format(s=select),"^"+username)
                        print("el 1")
            else:
                 userList = users.select("SELECT * FROM Users WHERE isAdmin = 0 ORDER BY {s};".format(s=select))
                 print("el 2")
      else:
           userList = users.select("SELECT * FROM Users WHERE isAdmin = 0")
           print("el 3")
      print(userList)
      return render_template("accounts.html",userlist = userList)

@app.route('/admin')
def admin():
      
      if 'usertype' not in session.keys() or session["usertype"] == 0 :
            
            return redirect("/login")
      
      else:
           
            return render_template("admin.html")

@app.route('/adminUser/<id>')
def adminUser(id):
      user = users.select("SELECT * FROM Users WHERE id = %s;",id)
      print(user)
      return render_template("adminUser.html",user = user[0])

@app.route('/adminDelete/<id>')
def adminDelete(id):
     sql = "DELETE FROM WishList WHERE userID = %s;"
     WishList.remove(sql,id)
     sql = "DELETE FROM Users WHERE id = %s;"
     users.remove(sql,id)
     return redirect('/accounts')

@app.route('/adminGamePage',methods = ["POST","GET"])
def adminGamePage():
      gameStoreArray = {2:"GamersGate",3:"GreenManGaming",7:"GOG",8:"Orgin",
                        11:"Humble",13: "Uplay",15:"Fanatical",21:"WinGameStore",23:"GameBillet",
                        24:"Voidu",25:"Epic Games Store",27:"Gamesplanet",28:"Gamesload",29:"2Game",
                        30:"IndieGala",31:"BlizzardShop",33:"DLGamer",34:"Noctre",35:"DreamGame"}
      
      sql = "SELECT * FROM Gamestores;"
      games = Gamestores.select(sql)

      gameDict = {}
      for i in range(len(games)):
           gameDict[games[i]["id"]] = [gameStoreArray[games[i]["id"]],games[i]["enabled"]]

      if request.method == "POST":
            sql = "UPDATE Gamestores SET enabled = %s WHERE id = %s;"
            for key,values in gameDict.items():
                en=request.form.get(values[0])
                Gamestores.update(sql,int(en),key)

            return redirect("/adminGamePage")
           

      return render_template("adminGamePage.html",gameStoreArray = gameDict.items())


@app.route('/logout')
def logout():
     session['userid']=None
     session['username']=None
     session['usertype'] = None
     
     sessionData.gamedetailDict ={}
     return redirect('/login')

     
     
@app.route('/login',methods=["GET","POST"])
def login():
        if request.method=="POST":
            
            username =request.form.get('username')
            password =request.form.get('password')
            #checkusername = user.query.filter_by(username=username).first()
            user = users.select("SELECT * FROM Users WHERE username = %s;",username)
            
            if user and user[0]["password"]== password:
                  session.permanent = True
                  session['userid']=user[0]["id"]
                  session['username']=user[0]["username"]
                  session['usertype'] = user[0]["isAdmin"]
                  if session['usertype'] == True:
                        print("Redirecting to Admin Page")
                        return redirect ('/admin')
                  else:
                        api.runWishAPI(user[0]["id"])
                        for key, value in sessionData.gamedetailDict.items():
                             WishlistGame.setState(value[4])

                    
                        print("Redirecting to Main Page")
                        return redirect ('/')
                  
            return render_template("login.html")
        else: 
            return render_template("login.html")
        
@app.route('/signup', methods=["GET","POST"])
def signup():
        
        if request.method=="POST":
            
            firstname=request.form.get('firstname')
            lastname=request.form.get('lastname')
            username=request.form.get('username')
            email=request.form.get('email')
            password=request.form.get('password')
        
            print(f"Form Data Received: firstname={firstname}, lastname={lastname}, username={username}, email={email}, password={password}")
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
            
            exists = users.select("SELECT * FROM Users WHERE username = %s AND email = %s;",username,email)
            if exists:
              return "user already exists",400
            new_user =users.insert(firstname=firstname,lastname=lastname,username=username,password=password,email=email,isAdmin=False)
            
            return redirect("/login")
        else:
            return render_template("signup.html")
        
@app.route('/addtowishlist/<game>',methods=['GET'])
def addtowishlist(game):
     game =game.replace("'",'"')
     game = json.loads(game)
     print(game)
     game_id = int(game[4])
     game_price = float(game[1])
     
     if not loginchecker():
          return redirect('/login')
     
     userid= session['userid']

     
     game_added = WishlistGame.AddObserver(userid, game_id, game_price)
    
     if not game_added:
          return redirect('/wishlist')
     

     api.addToWishList(game_id)
  
    
     return redirect('/wishlist')

@app.route('/removefromwishlist/<game>',methods=['GET'])
def removefromwishlist(game):
     game =game.replace("'",'"')
     game = json.loads(game)
     game_id = int(game[4])

     
     
     
     userid= session['userid']

    
     
     GameRemoved = WishlistGame.RemoveObserver(userid, game_id)
     
     if not GameRemoved:
          redirect('/wishlist')

     

     for i,j in sessionData.gamedetailDict.items():
          if j[4] == game_id:
               
               sessionData.gamedetailDict.pop(i)
               break
    
     
     return redirect('/wishlist')

@app.route('/wishlist')
def wishlist():
        if not loginchecker():
             return redirect('/login')
        
             
        return render_template('wishlist.html', gamedetailDict=sessionData.gamedetailDict.items())

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
      wishlistdict = currentgamedeals.getWishListFormatDict()
      print(storedict)
      if game_id:
            return render_template("game.html",gamename=name,store_dict=storedict.items(), gameIMG=gameImg, wishlistdict=wishlistdict.items())
      else:
            return render_template("game.html",404,404)



if __name__=='__main__':
   app.run(debug=True)

