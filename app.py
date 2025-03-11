import os
from steam_web_api import Steam
KEY = os.environ.get()
steam = Steam(KEY)
from flask import Flask, request, render_template, session, redirect 
from flask_session import Session
from datetime import timedelta
import requests
import urllib.parse


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

@app.route('/gamesearch',methods =["GET","POST"])
def get_Game():
    if request.method == "POST":
        name= request.form.get("name")
        session["name"]=name 
        print(name)
        return redirect("/game") 
    else:
        return redirect("/") 

@app.route("/game", methods=["GET","POST"])

def game():
    
   gamename=session.get("name")

   if not gamename:
        return redirect("/")
   results = steam.apps.search_games(gamename)
   if results:
      firstresult = results["items"][0]
      gameid = firstresult.get("appid")
      gamename = firstresult.get("name")
      
      if gameid and gamename:
            return render_template("game.html", gamename=gamename, gameid=gameid)
      else:
            return render_template("game.html", error="Game details not found.")
   else:
        return render_template("game.html", error="No games found.")

#print(json.dumps(steamGame))
#isFound = re.search(str(regexForGame), Gamefilecontent)
#if isFound:
   # UserGame = isFound.group()
    #appid = UserGame.split(',')[0]
    #appid = appid[10:]
    
   # if name is not None: 
        
        #name=
        #price=
       # storefront=

    #return render_template("game.php",name=name,price=price,storefront=storefront) 

       
if __name__=='__main__':
   app.run(debug=True)

#steamResponse = requests.get("")
#print(steamResponse)
#steamGame = steamResponse.json()
#print(json.dumps(steamGame))
#isFound = re.search(str(regexForGame), Gamefilecontent)
#if isFound:
   # UserGame = isFound.group()
    #appid = UserGame.split(',')[0]
    #appid = appid[10:]
    
    #cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/games?steamAppID={}".format(appid)
    #cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
    #cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
    #cheapsharkGameIDString = json.dumps(cheapsharkGameIDResponseJSON)
    #cheapsharkGameIDJSON = json.loads(cheapsharkGameIDString)
    #cheapsharkGameIDJSONFound = cheapsharkGameIDJSON[0]["gameID"]
    #if cheapsharkGameIDJSONFound:
        #cheapsharkGameDealsRequestString = "https://www.cheapshark.com/api/1.0/games?id={}".format(cheapsharkGameIDJSONFound)
        #cheapsharkGameDealsResponse = requests.get(cheapsharkGameDealsRequestString)
        #cheapsharkGameDealsResponseJSON = cheapsharkGameDealsResponse.json()
        #cheapsharkGameDeals = json.dumps(cheapsharkGameDealsResponseJSON)
        #cheapsharkJSON = json.loads(cheapsharkGameDeals)
        #print(cheapsharkJSON["deals"])
    #else:
       # print("Failed to find Cheapshark game id")
    
#else:
    #print("Sorry the game: " + userRequest + " Could not be found")
    



    

#cheapSharkResponse = requests.get("https://www.cheapshark.com/api/1.0/games?id=236717")
#print(cheapSharkResponse)
#Result = cheapSharkResponse.json()
#print(json.dumps(Result)

#Gamefile.close()
