import pymysql


'''
Base class for the database classes. It is used to connect to the database and open it.
'''
class Database:
    #initalizer picks up the name of the database
    def __init__(self):
          self.dbname = "GameScout"

    '''
    Function to open the database
    
    Input: None
    Output: database connection variable
    Uses: Database
    '''
    def DBOpen(self):
        timeout = 10
        #call to open database
        connection = pymysql.connect(
         charset="utf8mb4",
         connect_timeout=timeout,
         cursorclass=pymysql.cursors.DictCursor,
         db="defaultdb",
         host="mysql-3483d28-gamescout.k.aivencloud.com",
         password="AVNS_84_-W4vXr2O0cZwE5xm",#put in password here
         read_timeout=timeout,
         port=11029,
         user="avnadmin",
         write_timeout=timeout,
        )
        return connection
    


'''
Class for the user database
'''
class UsersDatabase(Database):
    def __init__(self):
        super().__init__()
    
    '''
    Inserts an elements into the users database. 

    Input: firstname string, lastname string, username string, email string, password string isAdmin bool
    Output:None
    Uses: database
    '''
    def insert(self,firstname,lastname, username, email,password,isAdmin = False ):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            sql = "INSERT INTO Users (firstname,lastname,username,email,password,isadmin) VALUES (%s, %s,%s,%s,%s,%s)"
            #exicutes Sql
            cursor.execute(sql,(firstname,lastname,username,email,password,isAdmin))
        finally:
            #commits changes and closes
            connection.commit()
            connection.close()
    '''
    Pushes sql into the database

    Input: SQL command,arguments given for the s1l
    Output:values
    Uses: database
    '''  
    def select(self,SQL,*args):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            #exicutes Code
            cursor.execute(SQL,args)
            value = cursor.fetchall()
        finally:
            connection.commit()
            connection.close()

        return value
    '''
    Pushes sql into the database

    Input: SQL command,arguments given for the s1l
    Output:values
    Uses: database
    '''
    def remove(self,SQL,*args):
        connection = self.DBOpen()

        try:
            cursor = connection.cursor()
            cursor.execute("USE GameScout;")
            cursor.execute(SQL,args)
            value = cursor.fetchall()
        finally:
            connection.commit()
            connection.close()

        return value

'''
Class for wishlist database
'''

class WishListDatabase(Database):
    def __init__(self):
        super().__init__()

    def insert(self,userId,gameId, price):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            sql = "INSERT INTO WishList (userID,gameID,price) VALUES (%s, %s,%s)"
            cursor.execute(sql,(userId,gameId,price))
        finally:
            connection.commit()
            connection.close()
    '''
    Pushes sql into the database

    Input: SQL command,arguments given for the s1l
    Output:values
    Uses: database
    '''
    def select(self,SQL,*args):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            #exicutes sql and gets values
            cursor.execute(SQL,args)
            value = cursor.fetchall()
        finally:
            #commits connection and closes
            connection.commit()
            connection.close()

        return value
    
    '''
    Pushes sql into the database

    Input: SQL command,arguments given for the s1l
    Output:values
    Uses: database
    '''
    def remove(self,SQL,*args):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            #exicute sql
            cursor.execute(SQL,args)
            value = cursor.fetchall()
        finally:
            #commits and closes database
            connection.commit()
            connection.close()

        return value

'''
Class for gamestore database
'''
class Gamestores(Database):
    def __init__(self):
        super().__init__()

   
    '''
    Pushes sql into the database

    Input: SQL command,arguments given for the s1l
    Output:values
    Uses: database
    '''
    def select(self,SQL,*args):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            #exicutes code
            cursor.execute(SQL,args)
            value = cursor.fetchall()
        finally:
            #commits and closes database
            connection.commit()
            connection.close()

        return value
    '''
    Pushes sql into the database

    Input: SQL command,arguments given for the s1l
    Output:values
    Uses: database
    '''
    def update(self,SQL,*args):
        #opens the database using parent class
        connection = self.DBOpen()
        #try to handle errors
        try:
            #connects a cursor to send calls
            cursor = connection.cursor()
            #uses database
            cursor.execute("USE GameScout;")
            #exi
            cursor.execute(SQL,args)
            value = cursor.fetchall()
        finally:
            connection.commit()
            connection.close()

        