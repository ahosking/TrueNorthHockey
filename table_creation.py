#Database testing and learning

import sqlite3 as lite
import sys

con = None

con = lite.connect('new.db')

with con:
    cur = con.cursor()

    #Create the table for seasons
    try:
        cur.execute("CREATE TABLE Seasons(Id INT, Year_start INT, Season TEXT)")
    except:
        pass

    #Insert a season!
    cur.execute("INSERT INTO Seasons VALUES(1, 2014, 'Winter')")

    #Create the Games Table
    try:
        cur.execute("CREATE TABLE Games(Id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT, Time TEXT, Rink TEXT,\
         Home_Team TEXT, Home_Score INT, Away_Team TEXT, Away_Score INT, Season TEXT)")
    except:
        pass
