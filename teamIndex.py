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
            cur.execute("INSERT INTO Games VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?, ?)",\
                        (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            # cur.execute("INSERT INTO Games VALUES(null, 'Sep 14', '21:00', 'Rinx 1', 'Toronto Ice Dogs', 4, 'Shock', 6, "Winter2014", "Gamesheet")")

        print "\nSuccessfully added games!\n"

def add_players(new_players):
    #Make DB Connection
    con = lite.connect('new.db')

    with con:
        cur = con.cursor()
        for i in new_players:
            print i
            cur.execute("INSERT INTO Players VALUES(null, ?, ?, ?, ?, ?, ?, ?, ?)",\
                        (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            # "Player    GP    G    A    Pts    PIM   Season"
        print "\nSuccessfully added players.\n"

soup = BeautifulSoup(urllib2.urlopen("http://www.truenorthhockey.com/asp_pages/Team.aspx?team_id=17178").read())

# print soup.prettify()

#Table 8 seems to carry all player data
# print soup.find_all('table')[8]
# print soup.find_all('table')[8].findAll('tr')[1]
playerCount = range(1,len(soup.find_all('table')[8]) - 2)
players = []
#This will collect all player data for the current season
print "Number\tPlayer\t\t\t\tGP\t G\t A\t Pts\t PIM"
for i in playerCount:
    player = []
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[0].string)
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[1].string)
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[2].string)
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[3].string)
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[4].string)
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[5].string)
    player.append(soup.find_all('table')[8].findAll('tr')[i].findAll('td')[6].string)
    player.append("Winter2014")
    players.append(player)
    # print soup.find_all('table')[8].findAll('tr')[i].findAll('td')[1].string,"\t\t\t",\
    #     soup.find_all('table')[8].findAll('tr')[i].findAll('td')[2].string,"\t",\
    #     soup.find_all('table')[8].findAll('tr')[i].findAll('td')[3].string,"\t",\
    #     soup.find_all('table')[8].findAll('tr')[i].findAll('td')[4].string,"\t",\
    #     soup.find_all('table')[8].findAll('tr')[i].findAll('td')[5].string,"\t",\
    #     soup.find_all('table')[8].findAll('tr')[i].findAll('td')[6].string
#Add the players!
# add_players(players)


#Table 9 seems to carry all goalie data
goalieCount = range(1,len(soup.find_all('table')[9]) - 2)
goalies = []
print "Player\tGP\tGA\tGAA\tShO"
for i in goalieCount:
    goalie = []
    goalie.append(soup.find_all('table')[9].findAll('tr')[i].findAll('td')[0].string)
    goalie.append(soup.find_all('table')[9].findAll('tr')[i].findAll('td')[1].string)
    goalie.append(soup.find_all('table')[9].findAll('tr')[i].findAll('td')[2].string)
    goalie.append(soup.find_all('table')[9].findAll('tr')[i].findAll('td')[3].string)
    goalie.append(soup.find_all('table')[9].findAll('tr')[i].findAll('td')[4].string)
    goalie.append("Winter2014")
    # print soup.find_all('table')[9].findAll('tr')[i].findAll('td')[1].string,"\t",\
    # soup.find_all('table')[9].findAll('tr')[i].findAll('td')[2].string,"\t",\
    # soup.find_all('table')[9].findAll('tr')[i].findAll('td')[3].string,"\t",\
    # soup.find_all('table')[9].findAll('tr')[i].findAll('td')[4].string,"\t",\
    # soup.find_all('table')[9].findAll('tr')[i].findAll('td')[5].string
    print goalie
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
    game.append("Winter2014")
    #Get the score sheets
    game.append((soup.find_all('table')[10].findAll('tr')[i].findAll('a')[1]).get('href'))

    games.append(game)
    #add game sheet URL
    # gameSheets.append("http://www.truenorthhockey.com/asp_pages/" + (soup.find_all('table')[10].findAll('tr')[i].findAll('a')[1]).get('href'))
    # print soup.find_all('table')[10].findAll('tr')[i].findAll('td')[0].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[1].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[2].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[3].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[4].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[5].string,\
    #     soup.find_all('table')[10].findAll('tr')[i].findAll('td')[6].string
# add_games(games)

print "\n-------------------------------------------------------------------"
print "Game Sheet\n"
for i in games:
    print i[8]
print
testSheet = ("http://www.truenorthhockey.com/asp_pages/" + games[1][8])
print testSheet
# gameSoup = BeautifulSoup(urllib2.urlopen(testSheet).read())

# print gameSoup.prettify()

#We need to find links to the score sheets
print (soup.find_all('table')[10].findAll('tr')[6].findAll('a')[1]).get('href')

##################################
##Game Sheets
##################################
# Game Index Number Per	Time	Player#	PIM	Penalty   Season
