'''
Data Insertion into given DataBase, Python code by Pints [pin2sharma248@gmail.com]

'''

import os
import mysql.connector
from mysql.connector import errorcode

# bulk uploading csv file in given table
def insert_data(db_con,table_name,file_name):
    try:
        path = os.path.abspath(os.getcwd())

        db_cur = db_con.cursor()
        query = "LOAD DATA INFILE '{}/{}' INTO TABLE {} FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES (id, SeriousDlqin2yrs, RevolvingUtilizationOfUnsecuredLines, age, 'NumberOfTime30-59DaysPastDueNotWorse', DebtRatio, MonthlyIncome, NumberOfOpenCreditLinesAndLoans, NumberOfTimes90DaysLate, NumberRealEstateLoansOrLines, 'NumberOfTime60-89DaysPastDueNotWorse', NumberOfDependents)".format(path, file_name, table_name)

        db_cur.execute(query)
        return True
    except Exception as err:
        print("ERROR : {}".format(err))
        return False
