import requests
from bs4 import BeautifulSoup
import pandas as pd
import time, os, datetime


def getFinancialInformation(symbol):
    url = 'https://finance.yahoo.com/quote/'+symbol+'?p='+symbol

    res = requests.get(url)
    resText = res.text
    soup = BeautifulSoup(resText, 'html.parser')

    finalName = "1y Target Est"
    trs = soup.find_all('tr')

    names = []
    values = []

    namVal = {}

    for i in range(len(trs)):
        for j in range(len(trs[i].contents)):
            if j == 0:
                name = trs[i].contents[j].text
                names.append(name)
            if j == 1:
                value = trs[i].contents[j].text
                values.append(value)
        namVal[name] = [value]
        if name == finalName:
            break

    return names, values


def getCompanyList():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    res = requests.get(url)
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

    return tickerSymbols


while True:
    # Check current time
    start = time.time()
    waitTime = 15

    # Extract and Save Data
    data = {"symbol": [],
            "metric": [],
            "value": [],
            "time": []}
    try:
        tickerSymbols = getCompanyList()
    except Exception as e:
        print(str(e))
        break

    for symbol in tickerSymbols:
        try:
            names, values = getFinancialInformation(symbol)
        except Exception as e:
            continue

        collectedTime = datetime.datetime.now().timestamp()

        for i in range(len(names)):
            data["symbol"].append(symbol)
            data["metric"].append(names[i])
            data["value"].append(values[i])
            data["time"].append(collectedTime)

            # '''Alternate Method Instead of List Appending'''
            # '''List Concatenation Technique'''
            # data["symbol"] += [symbol] * len(names)
            # data["metric"] += names
            # data["value"] += values

    currentDate = datetime.date.today()
    df = pd.DataFrame(data)
    savePath = str(currentDate) + "financialData.csv"
    if os.path.isfile(savePath):
        # Dont overwrite existing file
        df.to_csv(savePath, mode="a", header=False, columns=["symbol", "metric", "value", "time"])
    else:
        # Create new file
        df.to_csv(savePath, columns=["symbol", "metric", "value", "time"])

    # waitTime duration until loop runs again
    timeDiff = time.time() - start
    if waitTime - timeDiff > 0:
        time.sleep(waitTime - timeDiff)