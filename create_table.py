'''
Create Table scheme into given DataBase, Python code by Pints [pin2sharma248@gmail.com]

'''

import mysql.connector
from mysql.connector import errorcode

# check if table already exist or not
def checkTableExists(db_con, tablename):
    try:
        db_cur = db_con.cursor()
        db_cur.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_name = {}".format(tablename))
        if db_cur.fetchone()[0] == 1:
            db_cur.close()
            return(True,1)

        db_cur.close()
        return(False,1)
    except Exception as err:
        print("ERROR : {}".format(err))
        return(None,0)

# creating new table in given database
def createTable(db_con, tablename):
    try:
        table_exists = checkTableExists(db_con, tablename)
        if not table_exists[1]:
            raise("ERROR : Something went wrong while checking Table in data base")
        else:
            if table_exists[0]:
                print("INFO : Table already exist in Data Base ")
                return True
            else:
                db_cur = db_con.cursor()
                query = "CREATE TABLE {} ( id INT , SeriousDlqin2yrs BOOL, RevolvingUtilizationOfUnsecuredLines FLOAT, age INT, 'NumberOfTime30-59DaysPastDueNotWorse' INT, DebtRatio FLOAT, MonthlyIncome MONEY, NumberOfOpenCreditLinesAndLoans INT, NumberOfTimes90DaysLate INT, NumberRealEstateLoansOrLines INT, 'NumberOfTime60-89DaysPastDueNotWorse' INT, NumberOfDependents INT)".format(tablename)
                db_cur.execute(query)

                return True

    except Exception as err:
        print("ERROR : {} ".format(err))
        return False
