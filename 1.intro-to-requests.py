import requests

prop = "Previous Close"
MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"

#The requests get function allow the client to GET data from the server
res = requests.get(MARA)
"""____________________________________________________________________________
| |  !!Flash task!! requests can also perform the post function, which creates |
| |                 data on the server. What are two other actions that        |
| |                 requests can perform? What are the function names?         |
| |____________________________________________________________________________|
| |
| |
| |
| |
"""

resText = res.text

i = resText.index(prop)

reduceText = resText.split("PREV_CLOSE-value\">")[1].split("<")[0]
print(reduceText)