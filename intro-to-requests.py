import requests

prop = "Previous Close"
MARA = "https://finance.yahoo.com/quote/MARA?p=MARA&.tsrc=fin-srch"
res = requests.get(MARA)
resText = res.text

i = resText.index(prop)

reduceText = resText.split("PREV_CLOSE-value\">")[1].split("<")[0]
print(reduceText)