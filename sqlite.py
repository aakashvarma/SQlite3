import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145123542, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",(unix, datestamp, keyword, value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot WHERE value=4')
    data = c.fetchall()
    print(data)

def update():
    c.execute('SELECT * FROM stuffToPlot')
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 4')
    
def delete():
    c.execute('DELETE FROM stuffToPlot WHERE value = 1')
    conn.commit()


#delete()
#read_from_db()
#create_table()
#data_entry()
#update()


#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)


c.close()
conn.close()