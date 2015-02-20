import urllib2
from bs4 import BeautifulSoup
import sqlite3 as lite
import sys

soup = BeautifulSoup(urllib2.urlopen("http://www.truenorthhockey.com/asp_pages/Team.aspx?team_id=17178").read())

schedCount = range(1,len(soup.find_all('table')[10]) - 2)
gameSheets = []
# for i in schedCount:
#     #Get the score sheets
#     # print ("www.truenorthhockey.com/asp_pages/" + (soup.find_all('table')[10].findAll('tr')[i].findAll('a')[1]).get('href'))
#     gameSheets.append(("http://www.truenorthhockey.com/asp_pages/" + (soup.find_all('table')[10].findAll('tr')[i].findAll('a')[1]).get('href')))
#
# print gameSheets[0]

#Lets study the gamesheet
# soup = BeautifulSoup(urllib2.urlopen(gameSheets[0]))
soup = BeautifulSoup(urllib2.urlopen("http://www.truenorthhockey.com/asp_pages/tnhcGameSheetPrint.aspx?gameid=163334").read())
# print soup.prettify()
# print soup.find_all('table')
#This finds the Game information including scores and referee numbers
# print (soup.find_all('table')[1].findAll('tr')[3].findAll('span'))

#Finds home and away teams
# print (soup.find_all('table')[9].findAll('tr')[0].findAll('td'))

#Player/Game Summary
# print (soup.find_all('table')[10].findAll('tr'))

#Scoring Details
print (soup.find_all('table')[20].findAll('tr'))