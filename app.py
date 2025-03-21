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


#create the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] ='SECRETKEY'
app.secret_key="GameScout"
SECRET_KEY = "GameScout"
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.permanent_session_lifetime = timedelta(minutes=10)

Session(app)



#creates a class for accessing the databases
#there are three data bases for the users, wishlist and the gamestores
users = database.UsersDatabase()
WishList = database.WishListDatabase()
Gamestores = database.Gamestores()

#checks is the user is logged on by seeing if the userid is in session
def loginchecker():
     return 'userid' in session

#regex used to check valididy of the names,email, and password using regex
firstnameRegex=r'^[a-zA-Z]+$'
lastnameRegex=r'^[a-zA-Z]+$'
usernameRegex=r'^[a-zA-Z0-9]+$'
emailRegex=r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
passwordRegex=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

#creates a variable to hold sessiondata and sends an address to the API call class
sessionData = SessionData()
api =API(sessionData)

'''
This is the main page for the website
It represents the interface that the user can use
If first runs the API function to gather to information on the games
The function checks to see if the user is logged on
If they are not then it loads the generic main page
If they are logged on then it sends there ID to the observer pattern

Input: None
Output render mainpage HTML
Uses: HTML, session variables, sessionData variables,observerpattern and wishlist game file, database classes,API
'''
@app.route('/',methods=["GET","POST"])
def serve_form():
    #runs API go put information in games into sessiondata
    api.runMainAPI()
    try:
      #user is not logged in 
      if session['userid']==None:
            #runs HTML for main page 
            #sends API details to the mainpage
            return render_template("mainpage.html", steamgamesjson=sessionData.steamgamesDict.items(),epicgamesjson=sessionData.epicgamesDict.items(),goggamesjson=sessionData.goggamesDict.items(),fanaticalgamesjson=sessionData.fanaticalgamesDict.items(),wishlistupdate=False, loginbutton=True)
      else:
         #user is logged in
         #this function checks to see if any games on their wishlist has gotten its price updated
         #with a reduced price
         needsupdate=WishlistGame.getState(session['userid'])
         #sets updateuser back to 0 to indicate the observer has been updated
         sql = "UPDATE Users SET updateuser=0 WHERE id = %s;"
         users.select(sql,session['userid'])
         return render_template("mainpage.html", steamgamesjson=sessionData.steamgamesDict.items(),epicgamesjson=sessionData.epicgamesDict.items(),goggamesjson=sessionData.goggamesDict.items(),fanaticalgamesjson=sessionData.fanaticalgamesDict.items(),wishlistupdate=needsupdate,loginbutton=False)   
    except:
            #user is not logged in 
            #runs HTML for main page
            return render_template("mainpage.html", steamgamesjson=sessionData.steamgamesDict.items(),epicgamesjson=sessionData.epicgamesDict.items(),goggamesjson=sessionData.goggamesDict.items(),fanaticalgamesjson=sessionData.fanaticalgamesDict.items(),wishlistupdate=False,loginbutton=True)


'''
This is the main admin page it only has two buttons for the user to press
Accounts button to deal with account and game button to deal with gamestores
It checks to make sure to user is logged in with an admin account

Input: None
Output redirect to login or render admin HTML
Uses: session variables,HTML
'''
@app.route('/admin')
def admin():
      #Makes sure that the user is logged in with an admin account
      if 'usertype' not in session.keys() or session["usertype"] == 0 :
            #if they are not logged in it sends them to the login page
            return redirect("/login")
      
      else:
            #if they are logged in it renders the admin page
            return render_template("admin.html")

'''
The admin accounts page renders all the the non admin accounts that exists
It lists off all of the users and lets to admin select which one to edit
The page also lets to admin search up the users by username and order the users 
based of username or email

Input: None
Output redirect to login or render account HTML
Uses: session variables, HTML, flask requests,POST,database class,
'''
@app.route('/accounts', methods = ["POST", "GET"])
def accounts():
      order = 0
      #Makes sure that the user is logged in with an admin account
      if 'usertype' not in session.keys() or session["usertype"] == 0 :
            #if they are not logged in it sends them to the login page
            return redirect("/login")
      #checks to see when the user presses the submit button for sort or search 
      
      if request.method=="POST":
            #gets search text
            username = request.form.get('usertextsearch')
            #gets sort selection
            select = request.form.get("order")
            
            #checks if anything was written in textbox
            if username != None:
                  #gets all users with exact username match
                  userList = users.select("SELECT * FROM Users WHERE username = %s AND isAdmin = 0;",username)
                  #looks for users with start match to what was typed in and sorts them based of select which is never None
                  if len(userList) == 0:
                        userList = users.select("SELECT * FROM Users WHERE username REGEXP %s AND isAdmin = 0 ORDER BY {s};".format(s=select),"^"+username)
            #if nothing was written in text box is sorts users based off of select box          
            else:
                 userList = users.select("SELECT * FROM Users WHERE isAdmin = 0 ORDER BY {s};".format(s=select))
            if select == "id":
                 order = 0
            if select == "username":
                 order = 1
            if select == "email":
                 order = 2
      #default just selects users from database and lists them       
      else:
           userList = users.select("SELECT * FROM Users WHERE isAdmin = 0")
      #sends the list of users to the account.html to render    
      return render_template("accounts.html",userlist = userList,order = order)

'''
This page looks at an individual user.
The admin can edit the information of the user or delete the user
entirely.

Input: id int for the current user,
Output: Redirect to login, or adminUser template
Uses: session dict,  database class
'''
@app.route('/adminUser/<id>',methods = ["POST","GET"])
def adminUser(id):
      #makes sure user is logged in
      if 'usertype' not in session.keys() or session["usertype"] == 0 :
            #if user not logged sends them to login page
            return redirect("/login")
      #checks if information is edited
      if request.method == "POST":
           #gets all the information that could be edited
           username = request.form.get("username")
           firstname = request.form.get("firstname")
           lastname = request.form.get("lastname")
           email = request.form.get("email")
           password = request.form.get("password")
           
           
           #checks is username is changed then updates the database if it is changed
           if username != None:
                sql = "UPDATE Users SET username = %s WHERE id =%s;"
                users.select(sql,username,id)

           #checks is firstname is changed then updates the database if it is changed
           if firstname != None:
                sql = "UPDATE Users SET firstname = %s WHERE id =%s;"
                users.select(sql,firstname,id)   
           #checks is lastname is changed then updates the database if it is changed
           if lastname != None:
                sql = "UPDATE Users SET lastname = %s WHERE id =%s;"
                users.select(sql,lastname,id)
           #checks is email is changed then updates the database if it is changed     
           if email != None:
                sql = "UPDATE Users SET email = %s WHERE id =%s;"
                users.select(sql,email,id)  
           
           #checks is password is changed then updates the database if it is changed
           if password != None:
                sql = "UPDATE Users SET password = %s WHERE id =%s;"
                users.select(sql,password,id) 
      #this will use the id the function is given and load the current user
      user = users.select("SELECT * FROM Users WHERE id = %s;",id)
      #renders the template and sends the user to the html 
      return render_template("adminUser.html",user = user[0])

'''
This is a special routing function for deleting a user
It calls the database and tells it to delete the user

Input: id  int to identify user
Output: redirect to accounts
Uses: database class
'''
@app.route('/adminDelete/<id>')
def adminDelete(id):
     #calls the data base and tells it to remove items from the users wishlist
     sql = "DELETE FROM WishList WHERE userID = %s;"
     WishList.remove(sql,id)
     #tells the database to remove the user
     sql = "DELETE FROM Users WHERE id = %s;"
     users.remove(sql,id)
     #goes back to accounts
     return redirect('/accounts')

'''
This is the admin game page which allows the admin to disable certian gamestores 
from being shown. The user can click to enable or disable certian gamestores and 
submit the changes.

Input: None
Output: redirect to login or renders accounts
Uses: database class for gamestores
'''
@app.route('/adminGamePage',methods = ["POST","GET"])
def adminGamePage():
      #checks if user is logged in and an admin user
      if 'usertype' not in session.keys() or session["usertype"] == 0 :
            #if not it redirects them to login
            return redirect("/login")
      #creats and built in dictionary with all the game stores
      gameStoreArray = {2:"GamersGate",3:"GreenManGaming",7:"GOG",8:"Orgin",
                        11:"Humble",13: "Uplay",15:"Fanatical",21:"WinGameStore",23:"GameBillet",
                        24:"Voidu",25:"Epic Games Store",27:"Gamesplanet",28:"Gamesload",29:"2Game",
                        30:"IndieGala",31:"BlizzardShop",33:"DLGamer",34:"Noctre",35:"DreamGame"}
      
      #gets the current stat of gamestores
      sql = "SELECT * FROM Gamestores;"
      games = Gamestores.select(sql)

      gameDict = {}
      #creates a new dictionary with key as id and value a list with game name and the enabled disabled state
      for i in range(len(games)):
           gameDict[games[i]["id"]] = [gameStoreArray[games[i]["id"]],games[i]["enabled"]]

      #checks if submit butten was pressed
      if request.method == "POST":
            sql = "UPDATE Gamestores SET enabled = %s WHERE id = %s;"
            #gets all of the values that the admin selected and puts them into the database
            for key,values in gameDict.items():
                en=request.form.get(values[0])
                Gamestores.update(sql,int(en),key)
            #redirects in order to refresh the page
            return redirect("/adminGamePage")
           
      #sends gameDict to the html template
      return render_template("adminGamePage.html",gameStoreArray = gameDict.items())

'''
A funtion to output the user. It sets and the login specific session variabes to 0 and 
if sends the user to the logout page.

Input: None
Output: redirect to login 
Uses: session variables,sessionData
'''
@app.route('/logout')
def logout():
     #sets session vars to None
     session['userid']=None
     session['username']=None
     session['usertype'] = None
     
     sessionData.gamedetailDict ={}
     #sends user back to logout page
     return redirect('/login')

     
'''
This is the main login function. It recieves the login input from the user and checks
to see if it is valid. It checks if the user exits. It updates the session variables
to say that the user has logged in. It checks wether the user is an admin user and 
directs them to the appropriate page. It calls the wishlist API to load the users wish
list while they login.

Inputs: None
Outputs: sends them to mainpage or admin page, or it renders login page
Uses: database class, session variables, API,sessionData
'''  
@app.route('/login',methods=["GET","POST"])
def login():
        #checks if user pressed submin
        if request.method=="POST":
            #gets data from login page
            username =request.form.get('username')
            password =request.form.get('password')
            #checks for user in database
            user = users.select("SELECT * FROM Users WHERE username = %s;",username)
            #checks if password maches
            if user and user[0]["password"]== password:
                  #changes session variables to indicate user has logged in
                  session.permanent = True
                  session['userid']=user[0]["id"]
                  session['username']=user[0]["username"]
                  session['usertype'] = user[0]["isAdmin"]
                  #checks is user account is admin then sends them to admin page if they are
                  if session['usertype'] == True:
                       
                        return redirect ('/admin')
                  else:
                        #Runs API to load the wishlist
                        api.runWishAPI(user[0]["id"])
                        #checks games in wishlist to see if there are better deals for them
                        for key, value in sessionData.gamedetailDict.items():
                             WishlistGame.setState(value[4])

                    
                        #sends user to mainpage
                        return redirect ('/')
            #sends user back to login
            return render_template("login.html")
        else: 
            return render_template("login.html")

'''
Main Sign-up page takes the users firstname,lastname,username,email, and password and puts it
into the database if it is valid. It also checks if the account already exists in which case it
will send them to the login page.

Input: None
Output: redirect to or login page, or render sign-up page
Uses: users database class,
'''  
@app.route('/signup', methods=["GET","POST"])
def signup():
        #checks if submit is pressed
        if request.method=="POST":
            #gets the data from sign-up page
            firstname=request.form.get('firstname')
            lastname=request.form.get('lastname')
            username=request.form.get('username')
            email=request.form.get('email')
            password=request.form.get('password')
        
            #checks to see if the data is valid
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
            #checks if user already exists by checking if the username is taken
            exists = users.select("SELECT * FROM Users WHERE username = %s;",username)
            if exists:
              return "user already exists",400
            #adds the new user to the database
            new_user =users.insert(firstname=firstname,lastname=lastname,username=username,password=password,email=email,isAdmin=False)
            
            #sends user to login
            return redirect("/login")
        else:
            #renders signup page
            return render_template("signup.html")
'''
This is a special function that will add a game to the wishlist. It will use the gameid
to find the game and add the game to the users wishlist if they are logged on.

Input: game   A list contianing gameID and gameprice 
Output: redirects to wishlist or login
Uses: wishlist observer, session vars, API call
'''    
@app.route('/addtowishlist/<game>',methods=['GET'])
def addtowishlist(game):
     #parses the game array which is passed as a string
     game =game.replace("'",'"')
     game = json.loads(game)
     #gets the id and the price of the game
     game_id = int(game[4])
     game_price = float(game[1])
     
     #checks if the user is logged on if not sends them to the login page
     if not loginchecker():
          return redirect('/login')
     #gets the user id of the user
     userid= session['userid']

     #tells the wishlist observer that the game was added
     #inserts the game into the wishlist database
     game_added = WishlistGame.AddObserver(userid, game_id, game_price)
     
     #game already exists redirects to wishlist
     if not game_added:
          return redirect('/wishlist')
     
     #calls API to load new game to the wishlist
     api.addToWishList(game_id)
  
     #redirects to wishlist
     return redirect('/wishlist')

'''
This is a special function that will remove a game to the wishlist. It will use the gameid
to find the game and remove the game to the users wishlist. It updates
the wishlist observer to remove the game from the wishlist.

Input: game   A list contianing gameID and gameprice 
Output: redirects to wishlist 
Uses: wishlist observer, session vars, API call
'''  

@app.route('/removefromwishlist/<game>',methods=['GET'])
def removefromwishlist(game):
     #parces the string that into an array
     game =game.replace("'",'"')
     game = json.loads(game)
     #gets the game id
     game_id = int(game[4])

     #gets the user id
     userid= session['userid']
     
     #removes the game from wishlist observer and database
     GameRemoved = WishlistGame.RemoveObserver(userid, game_id)
     
     #error case if the game was not in the wishlist
     if not GameRemoved:
          redirect('/wishlist')

     
     #loops through the wishlist session data
     for i,j in sessionData.gamedetailDict.items():
          #find the game that was removes
          if j[4] == game_id:
               #removes the game from the session wishlist
               sessionData.gamedetailDict.pop(i)
               break
    
     #sends user back to the wishlist
     return redirect('/wishlist')

'''
This is the wishlist page for the game. The user must be logged on to access the wish list.
It will list all of there games that they have in the wish list and the preices.

Input: None 
Output: renders wishlist.html
Uses: sessionData
'''  
@app.route('/wishlist')
def wishlist():
        #checks if user is logged on and redirects them to login if they are not
        if session['userid']==None:
             return redirect('/login')
        
        #renderes wishlist and sends the html the sessionData containing wishlist info
        return render_template('wishlist.html', gamedetailDict=sessionData.gamedetailDict.items())

'''
get_game is a special function for finding the game that the user puts into the search bar. When 
the user submits the game name the function updates the session variable to tell the game page what was 
searched.

Input: None 
Output: redirects to mainpage or game page
Uses:  session dict
'''  
@app.route('/gamesearch',methods =["GET","POST"])
def get_Game():
    #checks if user submitted
    if request.method == "POST":
        #gets what the user typed in
        name= request.form.get("name")
        #updates session name
        session["name"]=name 
        #sends user to game function
        return redirect('/game') 
    else:
        return redirect('/') 

'''
game is a function which will use the name of a game to search of the games from the api. It will lood
for games that closely match what the user typed in. When it gets all of the games from the API it will
append them to a list and send them to the explore.html page.

Input: None 
Output: redirects to explore page
Uses:  session dict, api call
'''  
@app.route('/game', methods=["GET","POST"])
def game():
   #gets the game name
   gamename=session.get("name")
   #parces the game name into proper format
   game_name=str(gamename)
   game_name=game_name.replace(" ","+")
   #looks for the game in the API
   gamelist=requests.get("https://www.cheapshark.com/api/1.0/deals?storeID=1&title={}".format(game_name))
   #gets a list of games and picks the first 15 elements
   gamelistjson=gamelist.json()
   gamelistjson=gamelistjson[:15]
   
   noNSFWGameList = []
   #iterates through the game list
   for game in gamelistjson:
         #checks if game is inappropriate for a university project
         if CheckGameisNSFW.isNSFWGame(game["steamAppID"]):
               continue
         else:
               #if it is appropriate then adds it the the list
               noNSFWGameList.append(game)
   #name was not typed in
   if not gamename:
        return redirect("/",error="please enter game name")
   #No games were found for the name
   if len(noNSFWGameList) == 0:
         error="no games found"
         return render_template("explore.html",error=error)  
   #Games were found and the games are sent to the explore.html to be displayed
   if gamename:
        return render_template("explore.html",game_list=noNSFWGameList)
   else:
        #No games are found and it informs the user of an error
        return render_template("explore.html", error="Game details not found.")

'''
gamedetail shows the user the details of a specific game. It searches up the price for
that game of different game stores and compares them. It orders the price from least to 
greatest.

Input: game_id
Output: game.html, gamename,details and image, and wishlist dict
Uses:  session dict'
'''

@app.route('/gamedetail/<int:game_id>')
def gamedetail(game_id):
      #gets the information about the game from the backend
      currentgamedeals=DealForGameSimpleFactory.GetGameDealsAcrossStores(game_id)
      name=currentgamedeals.GetGamename()
      storedict=StoreIDAction.StoreIDToNameWithPrice(currentgamedeals.storeWithPriceSavingsDealURl())
      gameImg=currentgamedeals.gameImage()
      wishlistdict = currentgamedeals.getWishListFormatDict()
      #checks if the game id exists and renders the game
      if game_id:
            return render_template("game.html",gamename=name,store_dict=storedict.items(), gameIMG=gameImg, wishlistdict=wishlistdict.items())
      else:
            #game_id does not exist error
            return render_template("game.html",404,404)


#RUN
if __name__=='__main__':
   app.run(debug=True)

