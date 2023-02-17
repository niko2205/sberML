import pandas as pd
import sqlite3
import time
from datetime import date

#method insert data credit
def insert_data_credit(x):
    # Insert data to credit table
    cursor.execute("""
                        INSERT INTO credit (id, summ)
                        VALUES ({}, {})
                """.format(x['Deal ID'],x['Summ of credit']))
    return

#method convert date from MM.yyyy in unix format
def get_timestamp(x):
    # Calc date in unix format
    date_arr = x.split(".")
    d = date(int(date_arr[1]), int(date_arr[0]), 1)
    unixtime = time.mktime(d.timetuple())
    return unixtime
    
#method insert data credit
def insert_data_payment(x):
    k = x.keys()
    i = 2
    while i < len(x):
        # Insert data to payment table
        cursor.execute("""
                        INSERT INTO payment (pdate, summ, deal_id)
                        VALUES ({}, {}, {})
                """.format(get_timestamp(k[i]),x[i],x['Deal ID']))
        i = i+1
    return

def create_db(cursor):
    # Create table credit
    cursor.execute("""CREATE TABLE credit
                (
                    id INTEGER PRIMARY KEY, 
                    summ REAL NOT NULL
                )
                """)
               
    # Create table payment
    cursor.execute("""CREATE TABLE payment
                (
                    id INTEGER PRIMARY KEY, 
                    pdate INTEGER NOT NULL,
                    summ REAL NOT NULL, 
                    deal_id INTEGER NOT NULL, 
                    FOREIGN KEY (deal_id) REFERENCES credit(id)
                )
                """)
    
    data = pd.read_csv('data.csv',';')
    data.apply(insert_data_credit, axis=1)
    data.apply(insert_data_payment, axis=1)

    
conn = sqlite3.connect("mydatabase.db") # or :memory: to save in RAM
cursor = conn.cursor()

create_db(cursor)
conn.commit()

sql = "SELECT * FROM payment WHERE deal_id=?"
cursor.execute(sql, [("4")])
print(cursor.fetchall()) # or use fetchone()
