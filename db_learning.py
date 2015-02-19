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
        cur.execute("CREATE TABLE Games(Id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT, Time TEXT, Rink TEXT, Home_Team TEXT, Home_Score INT, Away_Team TEXT, Away_Score INT)")
    except:
        pass

    #Add a game
    # cur.execute("INSERT INTO Games VALUES(null, 'Sep 14', '21:00', 'Rinx 1', 'Toronto Ice Dogs', 4, 'Shock', 6)")
    # cur.execute("INSERT INTO Games VALUES(null, 'Sep 21', '17:15', 'Rinx 2', 'Lucky Pucks', 6, 'Toronto Ice Dogs', 6)")