import requests
from bs4 import BeautifulSoup

wikiLink = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
res = requests.get(wikiLink)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

# Instantiating an empty list to store the different ticker symbols
tickerSymbols = []

trs = soup.find_all('tr')[1:504]

for x in range(len(trs)):
    tickerSymbols.append(trs[x].a.text)

for i in tickerSymbols:
    #Some stock tickers contain special characters such as "." that will cause the program to crash. To avoid that, we will wrap this portion in a try-except clause to skip tickerSymbols that may break the program.
    try:
        # Here, we use a template literal to let the string know that "i" will be formatted and represented by the stock ticker that "i" is for that loop iteration
        stockPage = 'https://finance.yahoo.com/quote/{i}?p={i}'.format(i=i)
        res = requests.get(stockPage)
        resText = res.text
        soup = BeautifulSoup(resText, 'html.parser')

        trs = soup.find_all('tr')
        importantData = trs[:16]

        print(i)
        for x in range(len(importantData)):
            print(trs[x].contents[0].text + ':', trs[x].contents[1].text)
    except:
        pass

    # The "\n" is an example of the escape command we spoke about before. \n means new line. Check out this link for more information: https://docs.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170
    print('\n')

"""____________________________________________________________________________
| |  !!Flash task!! There is a way to navigate to stock pages for stocks that  |
| |                 contain a period without breaking the program. Try to      |
| |                 figure out a way to do it. Brainstorm ideas, get creative! |
| |____________________________________________________________________________|
| |
| |
| |
| |
"""