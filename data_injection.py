'''
Data Injection Python code by Pints [pin2sharma248@gmail.com]

'''
import sys
import connect_db
import create_table
import insert_data
import csv
import pandas as pd
import glob

# following details are taken by command line arguments
HOSTNAME = sys.argv[1] # database host machine
USERNAME = sys.argv[2] # DB host machine username
PASSWORD = sys.argv[3] # DB host machine password
DATABASE_NAME = sys.argv[4] # DB Name
TABLE_NAME = sys.argv[5] # Table name to store data


# get all csv files from current directory [where this main file is present]
def getAll_csv():
    '''
    return : ( Boolean, csv file list )

    '''
    try:
        path = os.getcwd()
        csv_files = glob.glob(os.path.join(path, "*.csv"))
        return(True , csv_files)

    except Exception as err:
        print("ERROR : {}".format(err))
        return(False, [])


# after reading and storing into DataBase
# push csv file to backup folder
# please make sure that 'backup' folder is present in current directory
def moveToBackup(file_name):
    '''
    return : Boolean
    '''
    try:
        cmd = "mv {} backup/{}".format(file_name,file_name))
        os.system(cmd)
        print("INFO : successfully Backup done")
        return True
    except Exception as err:
        print("ERROR : {}".format(err))
        return False



# main method
def main():
    try:
        success, csv_file_list = getAll_csv()

        # if successfully get all csv files without any error
        if success:
            for file in csv_file_list:
                # connect to database
                success,db_connection = connect_db.connect_to_database(HOSTNAME,
                                                                       USERNAME,
                                                                       PASSWORD,
                                                                       DATABASE_NAME
                                                                       )

                # if connected to database
                if success:

                    # if table has created into DataBase
                    if create_table.createTable(db_connection,TABLE_NAME):

                        # if csv data has inserted into table
                        if insert_data.insert_data(db_connection,TABLE_NAME,file):
                            print("INFO : successfully csv data has inserted into database ")

                            # if backup is unsuccessfull
                            if not moveToBackup(file):
                                print("INFO : There is possibilities of data rendendency because backup of file: {} was not successfull".format(file))
                        else:
                            print("INFO : Unable to insert csv data into database ")
                    else:
                        print("INFO : Unable to create table into database ")
                else:
                    print("INFO : Unable to connect Database")

    except Exception as err:
        print("ERROR : Error in main, {}".format(err))

if __name__ == '__main__':
    main()
