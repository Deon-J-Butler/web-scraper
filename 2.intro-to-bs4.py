import requests
from bs4 import BeautifulSoup

MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"
res = requests.get(MARA)
resText = res.text

#BeautifulSoup is an html parser, meaning it can look through the html of a webpage
#Here, the response text is being looked through
soup = BeautifulSoup(resText, 'html.parser')

#BeautifulSoup can find specific html tags, such as the table rows (tr) found below. It then stores the data in a list which you can name whatever you want.
trs = soup.find_all('tr')
"""____________________________________________________________________________
| |   !!Flash task!! tr is a subtag of the html table tag. What are two other  |
| |                 subtags of the table tag?                                  |
| |____________________________________________________________________________|
| |
| |
| |
| |
"""

#The list of data returned from the soup.find_all function can be extensive.Fortunately, our target data falls in the first two tables of the webpage. Therefore, we are going to splice the list into a new list called importantData, which only contains list items 1 through 16.
importantData = trs[:16]

#For the items in the length of the specified list
for x in range(len(importantData)):
    #Contents are the html content that you see on the webpage. This is found between the html tags. The first content which is index 0 of the list is the table row name (ex: "Previous Close"). The second content, index 1, is the table row data (ex: "$13.50").
    print(importantData[x].contents[0].text + ':', importantData[x].contents[1].text)


#Second trial at beautifulsoup html.parsing
wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
response = requests.get(wikiLink)
responseText = response.text
soup2 = BeautifulSoup(responseText, 'html.parser')

trs2 = soup2.find_all('tr')

#Although its called S&P500, there are actually 503. The splice below removes index[0], the column heading "Symbol," and ends the list after index[503], the last stock ticker.
stockTickers = trs2[1:504]
i = 1

for x in range(len(stockTickers)):
    print(i, stockTickers[x].a.text)
    i += 1

#The next two files will dive more deeply into pulling from these two sources