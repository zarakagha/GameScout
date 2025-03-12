import os
from flask import Flask, request, render_template, session, redirect 
from flask_session import Session
from datetime import timedelta
import requests
import urllib.parse
import json
from backend.gameclass import Game
from backend.DealFactory import DealForGameSimpleFactory


#store 1 = steam
#store 7 = GOG
#store 8 = origin

#userRequest = input("Enter game name: ")
#userRequest = userRequest.lower()

#Gamefile = open("Gameslistwithappidandname.txt", mode="r")
#Gamefilecontent = Gamefile.read().lower()
#regexForGame = '{{"appid".*?"name": "{}"}}'.format(userRequest)
#regexForCheapSharkGameID = '"gameID".*?,'

app = Flask(__name__)
app.secret_key="GameScout"

SECRET_KEY = "GameScout"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.permanent_session_lifetime = timedelta(minutes=10)
Session(app)


@app.route('/',methods=["GET","POST"])
def serve_form():
    return render_template("mainpage.html") 
@app.route('/accounts')
def accounts():
        return render_template("account.html")
@app.route('/admin')
def admin():
        return render_template("admin.html")
@app.route('/genre')
def genre():
        return render_template("genre.html")
@app.route('/login')
def login():
        return render_template("login.html")
@app.route('/signup')
def signup():
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
   gamelistjson=gamelistjson[:5]
   print(gamelistjson[0])
   if not gamename:
        return redirect("/")
   if gamename:
        return render_template("explore.html",game_list=gamelistjson)
   else:
        return render_template("explore.html", error="Game details not found.")

@app.route('/gamedetail/<int:game_id>')

def gamedetail(game_id):
      print(game_id)
      currentgamedeals=DealForGameSimpleFactory.GetGameDealsAcrossStores(game_id)
      print(currentgamedeals.storesWithPrice())
      name=currentgamedeals.GetGamename()
      storeswithprice=currentgamedeals.storesWithPrice()
      if game_id:
            return render_template("game.html",gamename=name,stores_with_price=storeswithprice)
      else:
            return render_template("game.html",404,404)
       
if __name__=='__main__':
   app.run(debug=True)

