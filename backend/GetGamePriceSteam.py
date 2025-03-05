import requests
import json
from flask import Flask, request, render_template, session, redirect 
from flask_session import Session
import re

#store 1 = steam
#store 7 = GOG
#store 8 = origin
#store 11 = Humble
#store 25 = epic games
#store 31 = blizzard

userRequest = input("Enter game name: ")
userRequest = userRequest.lower()

Gamefile = open("Gameslistwithappidandname.txt", mode="r")
Gamefilecontent = Gamefile.read().lower()
regexForGame = '{{"appid".*?"name": "{}"}}'.format(userRequest)
regexForCheapSharkGameID = '"gameID".*?,'

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
        session["name"]=uni 
        
        return redirect("/game") 
    else:
        return redirect("/") 

def game():
    
    name=session.get("name") 
    name = 
    
    if name is not None: 
        
        name=
        price=
        storefront=

    return render_template("game.php",name=name,price=price,storefront=storefront) 

       
if __name__=='__main__':
   app.run(debug=True)

#steamResponse = requests.get("")
#print(steamResponse)
#steamGame = steamResponse.json()
#print(json.dumps(steamGame))
isFound = re.search(str(regexForGame), Gamefilecontent)
if isFound:
    UserGame = isFound.group()
    appid = UserGame.split(',')[0]
    appid = appid[10:]
    
    cheapsharkRequestString = "https://www.cheapshark.com/api/1.0/games?steamAppID={}".format(appid)
    cheapsharkGameIDResponse = requests.get(cheapsharkRequestString)
    cheapsharkGameIDResponseJSON = cheapsharkGameIDResponse.json()
    cheapsharkGameIDString = json.dumps(cheapsharkGameIDResponseJSON)
    cheapsharkGameIDJSON = json.loads(cheapsharkGameIDString)
    cheapsharkGameIDJSONFound = cheapsharkGameIDJSON[0]["gameID"]
    if cheapsharkGameIDJSONFound:
        cheapsharkGameDealsRequestString = "https://www.cheapshark.com/api/1.0/games?id={}".format(cheapsharkGameIDJSONFound)
        cheapsharkGameDealsResponse = requests.get(cheapsharkGameDealsRequestString)
        cheapsharkGameDealsResponseJSON = cheapsharkGameDealsResponse.json()
        cheapsharkGameDeals = json.dumps(cheapsharkGameDealsResponseJSON)
        cheapsharkJSON = json.loads(cheapsharkGameDeals)
        print(cheapsharkJSON["deals"])
    else:
        print("Failed to find Cheapshark game id")
    
else:
    print("Sorry the game: " + userRequest + " Could not be found")
    



    

#cheapSharkResponse = requests.get("https://www.cheapshark.com/api/1.0/games?id=236717")
#print(cheapSharkResponse)
#Result = cheapSharkResponse.json()
#print(json.dumps(Result)

Gamefile.close()
