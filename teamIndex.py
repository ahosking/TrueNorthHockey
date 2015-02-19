import urllib2
from bs4 import BeautifulSoup
import sqlite3 as lite
import sys

con = None

def add_games(new_games):
    #Make DB Connection
    con = lite.connect('new.db')

    with con:
        cur = con.cursor()
        for i in new_games:
            cur.execute("INSERT INTO Games VALUES(null, ?, ?, ?, ?, ?, ?, ?)", (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
            # cur.execute("INSERT INTO Games VALUES(null, 'Sep 14', '21:00', 'Rinx 1', 'Toronto Ice Dogs', 4, 'Shock', 6)")



soup = BeautifulSoup(urllib2.urlopen("http://www.truenorthhockey.com/asp_pages/Team.aspx?team_id=17178").read())

# print soup.prettify()

#Table 8 seems to carry all player data
# print soup.find_all('table')[8]
# print soup.find_all('table')[8].findAll('tr')[1]
playerCount = range(1,len(soup.find_all('table')[8]) - 2)

#This will collect all player data for the current season
print "Player\t\t\t\tGP\t G\t A\t Pts\t PIM"
for i in playerCount:
    print soup.find_all('table')[8].findAll('tr')[i].findAll('td')[1].string,"\t\t\t",\
        soup.find_all('table')[8].findAll('tr')[i].findAll('td')[2].string,"\t",\
        soup.find_all('table')[8].findAll('tr')[i].findAll('td')[3].string,"\t",\
        soup.find_all('table')[8].findAll('tr')[i].findAll('td')[4].string,"\t",\
        soup.find_all('table')[8].findAll('tr')[i].findAll('td')[5].string,"\t",\
        soup.find_all('table')[8].findAll('tr')[i].findAll('td')[6].string
print

#Table 9 seems to carry all goalie data
goalieCount = range(1,len(soup.find_all('table')[9]) - 2)
print "Player\tGP\tGA\tGAA\tShO"
for i in goalieCount:
    print soup.find_all('table')[9].findAll('tr')[i].findAll('td')[1].string,"\t",\
    soup.find_all('table')[9].findAll('tr')[i].findAll('td')[2].string,"\t",\
    soup.find_all('table')[9].findAll('tr')[i].findAll('td')[3].string,"\t",\
    soup.find_all('table')[9].findAll('tr')[i].findAll('td')[4].string,"\t",\
    soup.find_all('table')[9].findAll('tr')[i].findAll('td')[5].string
print


#Table 10 is schedules and scores
##We'll need to capture the urls here to parse for scoring data
schedCount = range(1,len(soup.find_all('table')[10]) - 2)
games = []
for i in schedCount:
    game = []
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[0].string)
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[1].string)
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[2].string)
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[3].string)
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[4].string)
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[5].string)
    game.append(soup.find_all('table')[10].findAll('tr')[i].findAll('td')[6].string)
    games.append(game)
    # print soup.find_all('table')[10].findAll('tr')[i].findAll('td')[0].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[1].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[2].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[3].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[4].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[5].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[6].string
add_games(games)



#We need to find links to the score sheets
print (soup.find_all('table')[10].findAll('tr')[6].findAll('a')[1]).get('href')