import requests

prop = "Previous Close"
MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"

"""____________________________________________________________________________
   !!Flash task!! requests can also perform the post function, which creates   |
                  data on the server. What are two other actions that requests |
                  can do? What are the function names?                         |
   ____________________________________________________________________________|
| |
| |
| |
| |
"""

res = requests.get(MARA)
resText = res.text

i = resText.index(prop)

reduceText = resText.split("PREV_CLOSE-value\">")[1].split("<")[0]
print(reduceText)