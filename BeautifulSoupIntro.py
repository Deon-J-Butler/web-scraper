import requests
from bs4 import BeautifulSoup

MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"
res = requests.get(MARA)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

tables = soup.find_all('table')
trs = soup.find_all('tr')
importantData = trs[:16]

for x in range(len(importantData)):
    print(trs[x].span.text + ':', trs[x].contents[1].text)