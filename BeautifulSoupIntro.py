import requests
from bs4 import BeautifulSoup

MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"
res = requests.get(MARA)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

trs = soup.find_all('tr')
importantData = trs[:16]

for x in range(len(importantData)):
    print(trs[x].span.text + ':', trs[x].contents[1].text)


wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
response = requests.get(wikiLink)
responseText = response.text
soup2 = BeautifulSoup(responseText, 'html.parser')

trs2 = soup2.find_all('tr')
stockTickers = trs2[:504]

for x in range(len(stockTickers)):
    print(trs2[x].a.text)