import requests
from bs4 import BeautifulSoup

wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
res = requests.get(wikiLink)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

#Take turns commenting out/uncommenting the different solutions to get a better understanding of what each does

'''My Solution'''
trs = soup.find_all('tr')[1:504]
tickerSymbols = []

for x in range(len(trs)):
    tickerSymbols.append(trs[x].a.text)

print(tickerSymbols)

'''Given Solution'''
# tickerSymbols = []
# tbody = soup.find_all('tbody')

# for i in range(len(tbody[0].contents)):
#     if i<2:
#         continue
#     if i%2 != 0:
#         continue
#     symbol = tbody[0].contents[i].contents[1].text
#     tickerSymbols.append(symbol.strip('\n'))
#     if len(tickerSymbols) == 505:
#         break

# print(tickerSymbols)