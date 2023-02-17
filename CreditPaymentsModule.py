import sqlite3
import time
from datetime import date
import pandas as pd

class CreditPayments:

    def __init__(self):
        # connect to DB
        self.conn = sqlite3.connect('mydatabase.db')
        # save cursor object to self property
        self.cursor = self.conn.cursor()
        
    #method convert date from MM.yyyy in unix format
    def get_timestamp(self, x):
        # Calc date in unix format
        date_arr = x.split(".")
        d = date(int(date_arr[1]), int(date_arr[0]), 1)
        unixtime = time.mktime(d.timetuple())
        return unixtime
    
    #method getRestOfCredit
    def getRestOfCredit(self, id, date):
        # get summ of credit
        self.summ = self.getSummOfCredit(id)
        # query payments from DB where deal_id=id AND pdate<=date
        sql = 'SELECT sum(summ) FROM payment WHERE deal_id=? AND pdate<=?'
        self.cursor.execute(sql, [(id), (self.get_timestamp(date))])
        payed = self.cursor.fetchone()[0]
        # calculate rest of credit and return it
        self.res = self.summ - payed
        return self.res

    #method getSummOfCredit
    def getSummOfCredit(self, id):
        # query summ of credit from DB where id=id
        sql = 'SELECT summ FROM credit WHERE id=?'
        self.cursor.execute(sql, (id,))
        self.res = self.cursor.fetchone()[0]
        # return it
        return self.res
    
    def deleteID(self, id):
        sql = 'DELETE FROM payment WHERE deal_id=?'
        self.cursor.execute(sql, (id,))
        self.conn.commit()
   
    def show_payment(self):
        sql = 'SELECT * FROM payment'
        self.cursor.execute(sql)
        self.res = pd.DataFrame(self.cursor.fetchall())
        return self.res