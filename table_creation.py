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
    # cur.execute("INSERT INTO Seasons VALUES(1, 2014, 'Winter')")

    #Create the Games Table
    try:
        cur.execute("CREATE TABLE Games(Id INTEGER PRIMARY KEY AUTOINCREMENT, Date TEXT, Time TEXT, Rink TEXT,\
         Home_Team TEXT, Home_Score INT, Away_Team TEXT, Away_Score INT, Season TEXT, game_sheet TEXT)")
    except:
        pass

    #Create the Players Table
    try:
        # print "Player\t\t\t\tGP\t G\t A\t Pts\t PIM"
        cur.execute("CREATE TABLE Players(Id INTEGER PRIMARY KEY AUTOINCREMENT,player_number TEXT, player_name TEXT,\
         games_played INT, goals INT, assists INT, points INT, penalty_minutes INT, Season TEXT)")
        print "Player table created!"
    except:
        print "Player table creation failed."

def createGameSheets():
    # Game Index Number Per	Time	Player#	PIM	Penalty   Season
    cur.execute("CREATE TABLE gameSheets(GameIndex INT, roster_number TEXT, roster_name TEXT, roster_goals INT,\
     roster_assists INT, roster_points INT, roster_pim INT, goals_period INT, goals_time TEXT, goals_assist1 TEXT,\
     goals_assist2 TEXT, penalty_period INT, penalty_time TEXT, penalty_player INT, penalty_pim INT,\
     penalty_call TEXT)")
    print "Game sheet creation succeeded?!"

createGameSheets()