import requests
from bs4 import BeautifulSoup

MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"
res = requests.get(MARA)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

trs = soup.find_all('tr')
print(trs[0].span.text + ':', trs[0].contents[1].text)