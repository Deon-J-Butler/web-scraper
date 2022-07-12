import requests
from bs4 import BeautifulSoup

wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
res = requests.get(wikiLink)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

tickerSymbols = []
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