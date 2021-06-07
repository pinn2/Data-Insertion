# Data_injection
A PoC for a data ingestion system to make incoming CSV data easy to use / query by end user and take Backups in Host server and finally it removes backup file from current directory or server.

## requirments:
1. Python 3 <br />
2. MySql Database <br />
3. pandas <br />

## Modules:
#### 1. [Main data Injection module](https://github.com/pinn2/Data_injection/blob/main/data_injection.py) : 
It reads all `csv` file present in current directory and store it into database as defined table scheme after successfully stored into DB it takes data backup of stored `csv` file.

#### 2. [Connect database Module](https://github.com/pinn2/Data_injection/blob/main/connect_db.py) :
This module provides connection between database server or other host server where we want to store the all `csv` data and current server.

#### 3. [Create Tables Module](https://github.com/pinn2/Data_injection/blob/main/create_table.py) :
This module will create table into given database for data storage.<br />
Note : I am using normal `MySql table scheme` to store incoming `csv` data.

#### 4. [Insert data Module](https://github.com/pinn2/Data_injection/blob/main/insert_data.py) :
This module will insert or upload `csv` data into given table.
