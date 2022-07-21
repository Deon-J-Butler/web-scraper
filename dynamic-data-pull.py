#requests pulls data from server, time provides methods to manipulate time in code
import requests, time

#webdriver is a web framework that permits the execution of cross-browser testing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

"""____________________________________________________________________________
   !!Flash task!! Research what services the webdriver_manager library provide |
   ____________________________________________________________________________|
| |
| |
| |
| |
"""

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

url = "https://finance.yahoo.com/chart/AAL#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjgsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQifX19LCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkFBTCIsImNoYXJ0TmFtZSI6ImNoYXJ0IiwiaW5kZXgiOjAsInlBeGlzIjp7Im5hbWUiOiJjaGFydCIsInBvc2l0aW9uIjpudWxsfSwieWF4aXNMSFMiOltdLCJ5YXhpc1JIUyI6WyJjaGFydCIsIuKAjHZvbCB1bmRy4oCMIl19fSwic2V0U3BhbiI6e30sImxpbmVXaWR0aCI6Miwic3RyaXBlZEJhY2tncm91bmQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwic3RyaXBlZEJhY2tncm91ZCI6dHJ1ZSwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJBQUwiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiQUFMIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnt9fV19"

req = requests.get(url)
text = req.text

#Uncomment the line for the browser you have installed (31, 34, or 37)
#Opens Firefox browser
firefoxDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#Opens Chrome browser
# chromeDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Opens Edge browser
# edgeDriver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

#Choose your correct driver
firefoxDriver.get(url)

#Set sleep timer so page can load and data can pull before the webdriver closes
time.sleep(1)

for i in range(1, 6):
    #Can be retreived by using browser devtools, selecting element in question, and choosing "Copy XPath"
    xPath = '//section[@data-yaft-module="tdv2-applet-trending_tickers_title"]/table/tbody/tr['+str(i)+']'
    # /html/body/div[1]/div/div/div[1]/div/div[3]/div/div/section/section/aside/div/div[2]/section/div/section[2]
    #Change to your driver name
    elem = firefoxDriver.find_elements(By.XPATH, xPath)
    print(elem[0].text.split("\n"))

#Close your driver
firefoxDriver.close()