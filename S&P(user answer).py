import requests
from bs4 import BeautifulSoup

""" ___________________________________________________________
   This is my solution, it prints the S&P in the log/terminal. |
   ____________________________________________________________|
| |
| |
| |
| |
"""

#This link leads to a list of all the S&P500 stocks, we can use the ticker symbols as input to route to yahoo finance pages
wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
res = requests.get(wikiLink)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

#Instantiating an empty list to store the different ticker symbols
tickerSymbols = []

#BS4 is a html parser, this command looks through the html and finds all occurances of "tbody"
tbody = soup.find_all('tbody')

for i in range(len(tbody[0].contents)):
    if i<2:
        continue
    if i%2 != 0:
        continue

    symbol = tbody[0].contents[i].contents[1].text
    tickerSymbols.append(symbol.strip('\n'))
    if len(tickerSymbols) == 505:
        break

for i in tickerSymbols:
    stockPage = 'https://finance.yahoo.com/quote/{i}?p={i}'.format(i=i)
    res = requests.get(stockPage)
    resText = res.text
    soup = BeautifulSoup(resText, 'html.parser')

    trs = soup.find_all('tr')
    importantData = trs[:16]

    print(i)
    for x in range(len(importantData)):
        print(trs[x].span.text + ':', trs[x].contents[1].text)

    print('\n')