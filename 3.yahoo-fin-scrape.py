import requests
from bs4 import BeautifulSoup

MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"
res = requests.get(MARA)
resText = res.text
soup = BeautifulSoup(resText, 'html.parser')

#Take turns commenting out/uncommenting the different solutions to get a better understanding of what each does

''' My answer for challenge problem'''
trs = soup.find_all('tr')
importantData = trs[:16]

for x in range(len(importantData)):
    print(importantData[x].span.text + ':', importantData[x].contents[1].text)

'''Given solution for challenge problem'''
# finalName = "1y Target Est"
# trs = soup.find_all('tr')

# names = []
# values = []

# namVal = {}

# for i in range(len(trs)):
#     for j in range(len(trs[i].contents)):
#         if j == 0:
#             name = trs[i].contents[j].text
#             names.append(name)
#         if j == 1:
#             value = trs[i].contents[j].text
#             values.append(value)
#     namVal[name] = [value]
#     if name == finalName:
#         break

# print(namVal)

"""____________________________________________________________________________
| |   !!Flash task!! What is the major difference between these two solutions? |
| |____________________________________________________________________________|
| |
| |
| |
| |
"""