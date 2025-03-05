import requests
import json
from flask import Flask, request, render_template, session, redirect 
from flask_session import Session

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