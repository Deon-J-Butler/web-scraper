#webdriver is a web framework that permits the execution of cross-browser testing
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


"""____________________________________________________________________________
| |!!Flash task!! Research what services the webdriver_manager library provide |
| |____________________________________________________________________________|
| |
| |
| |
| |
"""
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


url = "https://finance.yahoo.com/chart/AAL#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjgsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQifX19LCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkFBTCIsImNoYXJ0TmFtZSI6ImNoYXJ0IiwiaW5kZXgiOjAsInlBeGlzIjp7Im5hbWUiOiJjaGFydCIsInBvc2l0aW9uIjpudWxsfSwieWF4aXNMSFMiOltdLCJ5YXhpc1JIUyI6WyJjaGFydCIsIuKAjHZvbCB1bmRy4oCMIl19fSwic2V0U3BhbiI6e30sImxpbmVXaWR0aCI6Miwic3RyaXBlZEJhY2tncm91bmQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwic3RyaXBlZEJhY2tncm91ZCI6dHJ1ZSwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJBQUwiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiQUFMIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnt9fV19"


#GOOGLE CHROME WEBDRIVER:
#By invoking the webdriver.BrowserOptions function, you can set rules for the webdriver to follow when ran
cOptions = webdriver.ChromeOptions()
#The --headless option makes it so that the browser window does not open.
cOptions.add_argument("--headless")
#The option is then declared in the initialization of the webdriver to make use of it. If you want to see how a webdriver works behind the scenes, remove
# ", options = cOptions"
chromeDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = cOptions)

#FIREFOX WEBDRIVER:
#Same as the chrome options setup, but a one-liner
fOptions = webdriver.FirefoxOptions().add_argument("--headless")
firefoxDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options = fOptions)

#Change the name to that of the driver you will be using "chromeDriver" or "firefoxDriver" in all instances that it appears in below (line 40, 43, 55, 63)
firefoxDriver.get(url)

#Setting the max wait threshold for targeted contents to load, this program will wait up to 5secs to get the information it wants before continuing
wait = WebDriverWait(firefoxDriver, 5)

#From the information I am targetting, this element takes the longest to load. If we don't wait for this element to load, the response will come back empty.
lastLoadedElementXPath = '//*[@id="data-util-col"]/section[2]/table/tbody/tr[1]/td[2]/p'

#If you compare this path to the previous one, you can see that they point in the same direction. The major difference is that the target of my search is the complete table row, while the previous path points to the paragraph in the table data in the table row.
xPath = '//*[@id="data-util-col"]/section[2]/table/tbody/tr[1]'

try:
    #At this point, we're specifying that we want to wait until that last loaded element is loaded before grabbing data.
    wait.until(ec.visibility_of_element_located((By.XPATH, lastLoadedElementXPath)))
    #The next step is the step that grabs the data from the table row
    elem = firefoxDriver.find_elements(By.XPATH, xPath)
    print(elem[0].text.split("\n"))

except Exception as e:
    print(str(e))
    print("Element not visible.")

#Close your driver
firefoxDriver.close()