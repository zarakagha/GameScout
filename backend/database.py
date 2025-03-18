import pymysql

class Database:
    def __init__(self):
          self.dbname = "GameScout"

    def DBOpen(self):
        timeout = 10
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
    



class UsersDatabase(Database):
    def __init__(self):
        super().__init__()
    

    def insert(self,firstname,lastname, username, email,password,isAdmin = False ):
        connection = self.DBOpen()

        try:
            cursor = connection.cursor()
            cursor.execute("USE GameScout;")
            sql = "INSERT INTO Users (firstname,lastname,username,email,password,isadmin) VALUES (%s, %s,%s,%s,%s,%s)"
            cursor.execute(sql,(firstname,lastname,username,email,password,isAdmin))
        finally:
            connection.commit()
            connection.close()
    def select(self,SQL,*args):
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


class WishListDatabase(Database):
    def __init__(self):
        super().__init__()

    def insert(self,userId,gameId, price):
        connection = self.DBOpen()

        try:
            cursor = connection.cursor()
            cursor.execute("USE GameScout;")
            sql = "INSERT INTO WishList (userID,gameID,price) VALUES (%s, %s,%s)"
            cursor.execute(sql,(userId,gameId,price))
        finally:
            connection.commit()
            connection.close()
      
    def select(self,SQL,*args):
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
