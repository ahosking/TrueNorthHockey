import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen("http://www.truenorthhockey.com/asp_pages/Team.aspx?team_id=17178").read())

# print soup.prettify()
print len(soup.find_all('table')[8].findAll('tr'))

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


#Table 9 seems to carry all goalie data
print soup.find_all('table')[9]