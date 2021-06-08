'''
Connecting to Given DataBase Python code by Pints [pin2sharma248@gmail.com]

'''

import mysql.connector
from mysql.connector import errorcode

# create new Database
def createDatabase(HOSTNAME,
                   USERNAME,
                   PASSWORD,
                   DATABASE_NAME
                        ):
    try:
        mydb = mysql.connector.connect(
        host=HOSTNAME,
        user=USERNAME,
        password=PASSWORD,
        )

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE {}".format(DATABASE_NAME))
        print("INFO : Created DataBase {}".format(DATABASE_NAME))

        return(True,mydb)

    except mysql.connector.Error as err:
        print("ERROR INFO : {}".format(err))

        return(False,None)

# connect to given or already existed database
def connect_to_database(HOSTNAME,
                        USERNAME,
                        PASSWORD,
                        DATABASE_NAME
                        ):
    try:
        mydb = mysql.connector.connect(
          host=HOSTNAME,
          user=USERNAME,
          password=PASSWORD,
          database=DATABASE_NAME
        )

        if mydb.is_connected():
            print("INFO : Connected to Host Data Machine")
            return(True,mydb)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
          print("ERROR INFO : {} Something went wrong in Database Authentication ".format(errorcode.ER_ACCESS_DENIED_ERROR))
          return(False,None)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
          print("ERROR INFO : Database does not exist, creating a new one with DB_NAME : {}".format(DATABASE_NAME))

          # if database is not exist then creating a new database
          # and then connecting with new Database
          if createDatabase(HOSTNAME,
                            USERNAME,
                            PASSWORD,
                            DATABASE_NAME
                                  )[0]:
              connect_to_database(HOSTNAME,
                                  USERNAME,
                                  PASSWORD,
                                  DATABASE_NAME
                                      ):
          else:
              return(False,None)

        else:
          print("ERROR INFO : {}".format(err))
          return(False,None)
